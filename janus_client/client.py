import json
import uuid
import logging
import requests
from enum import Enum


class State(Enum):
    INITIALIZED = 1
    STARTED = 2
    STOPPED = 3
    MIXED = 4
    CREATED = 5
    DESTROYED = 6

log = logging.getLogger(__name__)
API_PREFIX="/api/janus/controller"

class SessionResponse(object):
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data

class SessEndpointResponse(SessionResponse):
    def __str__(self):
        return '\n'.join([ "{}: {}".format(k,v) for k,v in self._data.items() ])

class SessStatusResponse(SessionResponse):
    def __str__(self):
        ret = ""
        for item in self._data:
            k = item['id']
            for l,w in item['services'].items():
                for s in w:
                    ret += "id: {}, service: {}, errors: {}\n".format(k, l, s['errors'])
        return ret

class Service(object):
    def __init__(self, instances=None, image=None, profile=None,
                 username=None, public_key=None, manifest=None, **kwargs):
        self._instances = instances
        self._image = image
        self._profile = profile
        self._username = username
        self._public_key = public_key
        self._kwargs = kwargs
        self._manifest = manifest

    def json(self):
        kwargs = self._kwargs
        if self._username:
            kwargs["USER_NAME"] = self._username
        if self._public_key:
            kwargs["PUBLIC_KEY"] = self._public_key
        ret = {"instances": self._instances,
               "image": self._image,
               "profile": self._profile,
               "kwargs": kwargs}
        return ret

    def endpoints(self):
        if not self._manifest:
            return None
        eps = dict()
        for k,v in self._manifest['services'].items():
            for s in v:
                if s['errors']:
                    eps.update({"{} (Errors)".format(k): "{}".format(s['errors'])})
                else:
                    eps.update({k: "{}:{}".format(s['ctrl_host'], s['ctrl_port'])})
        return SessEndpointResponse(eps)

class Response(object):
    def __init__(self, res):
        self._data = res

    def __str__(self):
        return "{} {}".format(self._data.status_code,
                              self._data.json())

    def json(self):
        if not self._data.content:
            return None
        return self._data.json()

    def error(self):
        if self._data.status_code > 400:
            return True
        else:
            return False
    @property
    def status_code(self):
        return self._data.status_code

class StartResponse(Response):
    pass

class NodeResponse(Response):
    def __str__(self):
        if self.error():
            return super().__str__()
        return '\n'.join([ n['name'] for n in self.json() ])

class ProfileResponse(Response):
    def __str__(self):
        if self.error():
            return super().__str__()
        return '\n'.join([ n['name'] for n in self.json() ])

class ActiveResponse(Response):
    def __str__(self):
        if self.error():
            return super().__str__()
        return '\n'.join([ f"{n['id']}" for n in self.json() ])

    @property
    def services(self):
        ret = list()
        for item in self.json():
            ret.append({item['id']: Service(manifest=item)})
        return ret

class Client(object):
    def __init__(self, url=None, auth=None, verify=False, timeout=None):
        self.url = "{}{}".format(url, API_PREFIX)
        self.auth = auth
        self.verify = verify
        if not self.verify:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.timeout = timeout

    def setURL(self, url):
        self.url = url

    def getSession(self, clone=None):
        return Session(self, clone)

    def config(self):
        print("URL: {}".format(self.url))

    def active(self, Id=None, user=None, name=None):
        url = "{}{}".format(self.url, '/active')
        if Id:
            url = "{}/{}".format(url, Id)
        elif user:
            url = "{}/{}".format(url, user)
        elif name:
            url = "{}/{}".format(url, name)
        return ActiveResponse(self._call("GET", url))

    def active_logs(self, Id, nname, **kwargs):
        params = "&".join([f"{k}={v}" for k, v in kwargs.items()])
        url = f"{self.url}/active/{Id}/logs/{nname}"
        if params:
            url = f"{url}?{params}"
        return Response(self._call("GET", url))

    def delete(self, Id, force=False):
        ep = f'/active/{Id}'
        if force:
            ep = f"{ep}?force=true"
        url = f"{self.url}{ep}"
        return Response(self._call("DELETE", url))

    def nodes(self, node=None, node_id=None, refresh=False):
        if node and node_id:
            raise ValueError("Specify either node or node_id, not both")
        ep = '/nodes'
        if node:
            ep = f"{ep}/{node}"
        elif node_id:
            ep = f"{ep}/{node_id}"
        elif refresh:
            ep = f"{ep}?refresh=true"
        url = f"{self.url}{ep}"
        return NodeResponse(self._call("GET", url))

    def add_node(self, node_data):
        hdr = {"Content-type": "application/json"}
        payload = json.dumps(node_data)
        url = f"{self.url}/nodes"
        return Response(self._call("POST", url, hdr, payload))

    def delete_node(self, node=None, node_id=None):
        if node:
            url = f"{self.url}/nodes/{node}"
        elif node_id:
            url = f"{self.url}/nodes/{node_id}"
        else:
            raise ValueError("Must specify either node name or node_id")
        return Response(self._call("DELETE", url))

    def create(self, req, name=None):
        hdr = {"Content-type": "application/json"}
        payload = json.dumps(req)
        url = f"{self.url}/create"

        if name:
            url = f"{url}/{name}"

        return Response(self._call("POST", url, hdr, payload))

    def start(self, id):
        url = f"{self.url}/start/{id}"
        return Response(self._call("PUT", url))

    def stop(self, id):
        url = f"{self.url}/stop/{id}"
        return Response(self._call("PUT", url))

    def exec_create(self, exec_request):
        hdr = {"Content-type": "application/json"}
        payload = json.dumps(exec_request)
        url = f"{self.url}/exec"
        return Response(self._call("POST", url, hdr, payload))

    def exec_status(self, node, exec_id):
        url = f"{self.url}/exec?node={node}&exec_id={exec_id}"
        return Response(self._call("GET", url))

    def images(self, name=None):
        url = f"{self.url}/images"
        if name:
            url = f"{url}/{name}"
        return Response(self._call("GET", url))

    def profiles(self, resource=None, name=None, refresh=False):
        if resource and name:
            url = f"{self.url}/profiles/{resource}/{name}"
        elif resource:
            url = f"{self.url}/profiles/{resource}"
        else:
            url = f"{self.url}/profiles"
        if refresh:
            url += "?refresh=true"
        return ProfileResponse(self._call("GET", url))

    def create_profile(self, resource, name, settings):
        hdr = {"Content-type": "application/json"}
        payload = json.dumps({"settings": settings})
        url = f"{self.url}/profiles/{resource}/{name}"
        return Response(self._call("POST", url, hdr, payload))

    def update_profile(self, resource, name, settings):
        hdr = {"Content-type": "application/json"}
        payload = json.dumps({"settings": settings})
        url = f"{self.url}/profiles/{resource}/{name}"
        return Response(self._call("PUT", url, hdr, payload))

    def delete_profile(self, resource, name):
        url = f"{self.url}/profiles/{resource}/{name}"
        return Response(self._call("DELETE", url))

    def update_users(self, resource_type, resource, users=None, groups=None):
        hdr = {"Content-type": "application/json"}
        url = f"{self.url}/auth/{resource_type}/{resource}"
        users = users or []
        groups = groups or []
        payload = json.dumps({"users": users, "groups": groups})
        return Response(self._call("POST", url, hdr, payload))

    def _call(self, op, url, hdrs=None, data=None, auth=None):
        if not auth:
            auth = self.auth
        kwargs = {"auth": auth, "verify": self.verify, "headers": hdrs, "data": data}
        if op == "POST":
            return requests.post(url, **kwargs)
        elif op == "GET":
            kwargs.pop("data", None)
            return requests.get(url, timeout=self.timeout, **kwargs)
        elif op == "DELETE":
            kwargs.pop("data", None)
            return requests.delete(url, **kwargs)
        elif op == "PUT":
            # kwargs.pop("data", None)
            return requests.put(url, **kwargs)

class Session(object):
    TMPL="id: {}\nallocated: {}\nrequests: {}\nmanifest: {}\nstate: {}"

    def __init__(self, client, clone=None, json=None):
        self._id = uuid.uuid4()
        self._client = client
        self._allocated = False
        self._requests = list()
        self._manifest = dict()
        self._state = State.CREATED.name

        if clone:
            ret = self._client.active(Id=clone).json()
            for s in ret:
                for k,v in s.items():
                    self._manifest.update(s)
                    self._requests.extend(v['request'])
        if json:
            for k,v in json.items():
                self._manifest.update(json)
                self._requests.extend(v['request'])

    def __str__(self):
        return self.__class__.TMPL.format(self._id,
                                          self._allocated,
                                          self._requests,
                                          self._manifest,
                                          self._state)

    def addService(self, srv):
        if type(srv) == Service:
            self._requests.append(srv.json())
        else:
            raise Exception("Not a valid Service object: {}".format(srv))

    def initialize(self):
        ret = self._client.create(self._requests)
        if not ret.error():
            self._manifest.update(ret.json())
        else:
            raise Exception("Error initializing service: {}".format(ret))
        return ret

    def destroy(self):
        for k,v in self._manifest.items():
            self._client.delete(k)
            self._state = State.DESTROYED.name

    def start(self):
        if self._state is not State.INITIALIZED.name:
            self.initialize()
        ret = dict()
        for k,v in self._manifest.items():
            ret = self._client.start(k)
            if not ret.error():
                self._manifest.update(ret.json())
            else:
                raise Exception("Error starting service: {}".format(ret))
            self._state = ret.json()[k]['state']
        return ret

    def status(self):
        ret = list()
        for k in self._manifest.keys():
            ret.append(self._client.active(Id=k).json())
        return SessStatusResponse(ret)

    def stop(self):
        for k,v in self._manifest.items():
            ret = self._client.stop(k)
            if ret.error():
                raise Exception("Error stopping service: {}".format(ret))
            self._state = ret.json()[k]['state']

    def endpoints(self):
        eps = dict()
        for k,v in self._manifest.items():
            for l,w in v['services'].items():
                for s in w:
                    if s['errors']:
                        eps.update({"{} (Errors)".format(l): "{}".format(s['errors'])})
                    else:
                        eps.update({l: "{}:{}".format(s['ctrl_host'], s['ctrl_port'])})
        return SessEndpointResponse(eps)
