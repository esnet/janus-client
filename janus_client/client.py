import logging
from typing import Optional, List, Dict, Any, Union

# Using the generated janus-py-client
from janus_py_client.api.janus_controller_api import JanusControllerApi
from janus_py_client.api.janus_agent_api import JanusAgentApi
from janus_py_client.api_client import ApiClient
from janus_py_client.configuration import Configuration
from janus_py_client.models.session_request import SessionRequest
from janus_py_client.models.session_request_list import SessionRequestList
from janus_py_client.models.add_endpoint_request import AddEndpointRequest
from janus_py_client.models.exec_request import ExecRequest
from janus_py_client.models.profile_request import ProfileRequest
from janus_py_client.models.auth_request import AuthRequest
from janus_py_client.models.instances_inner import InstancesInner

log = logging.getLogger(__name__)

class Client:
    def __init__(self, url: str, auth: Optional[tuple] = None, verify: bool = False, timeout: Optional[int] = None):
        self.configuration = Configuration(host=url)
        self.configuration.verify_ssl = verify
        
        if auth:
            self.configuration.username = auth[0]
            self.configuration.password = auth[1]

        self.api_client = ApiClient(self.configuration)
        self.controller = JanusControllerApi(self.api_client)
        self.agent = JanusAgentApi(self.api_client)
        self._token = None

    def login(self):
        """Get JWT token using basic auth and configure it for subsequent requests"""
        try:
            # We must ensure we're using basic auth for this specific call if configured
            res = self.controller.controller_get_token_token_post()
            if hasattr(res, 'access_token'):
                self._token = res.access_token
                self.configuration.access_token = self._token
                # Re-init API objects with updated config
                self.api_client = ApiClient(self.configuration)
                self.controller = JanusControllerApi(self.api_client)
                self.agent = JanusAgentApi(self.api_client)
                return True
            return False
        except Exception as e:
            log.error(f"Login failed: {e}")
            return False

    def active(self, aid: Optional[int] = None):
        if aid:
            return self.controller.controller_get_active_by_id_active_int_aid_get(aid)
        return self.controller.controller_get_active_active_get()

    def delete(self, aid: int, force: bool = False):
        return self.controller.controller_delete_active_active_int_aid_delete(aid, force=force)

    def nodes(self, node: Optional[Union[str, int]] = None, refresh: bool = False):
        if isinstance(node, int):
            return self.controller.controller_get_node_by_id_or_name_nodes_int_id_get(node)
        elif isinstance(node, str) and node.isdigit():
             return self.controller.controller_get_node_by_id_or_name_nodes_int_id_get(int(node))
        elif isinstance(node, str):
             return self.controller.controller_get_node_by_id_or_name_nodes_node_get(node)
        return self.controller.controller_get_nodes_nodes_get(refresh=refresh)

    def add_node(self, node_data: Dict[str, Any]):
        req = AddEndpointRequest(**node_data)
        return self.controller.controller_add_node_nodes_post(req)

    def delete_node(self, node: Union[str, int]):
        if isinstance(node, int) or (isinstance(node, str) and node.isdigit()):
            return self.controller.controller_delete_node_nodes_int_id_delete(int(node))
        return self.controller.controller_delete_node_nodes_node_delete(node)

    def create(self, requests: List[Dict[str, Any]], name: Optional[str] = None):
        if isinstance(requests, dict):
            requests = [requests]
        
        processed_reqs = []
        for r in requests:
            if 'instances' in r:
                r['instances'] = [InstancesInner(actual_instance=i) if not isinstance(i, InstancesInner) else i for i in r['instances']]
            processed_reqs.append(SessionRequest(**r))
            
        req_list = SessionRequestList(processed_reqs)
        return self.controller.controller_create_sessions_create_post(req_list)

    def start(self, aid: int):
        return self.controller.controller_start_session_endpoint_start_int_aid_put(aid)

    def stop(self, aid: int):
        return self.controller.controller_stop_session_endpoint_stop_int_aid_put(aid)

    def profiles(self, resource: Optional[str] = None, name: Optional[str] = None, refresh: bool = False):
        if resource and name:
            return self.controller.controller_get_profile_by_name_profiles_path_resource_path_rname_get(resource, name)
        elif resource:
            return self.controller.controller_get_profiles_by_resource_profiles_path_resource_get(resource)
        return self.controller.controller_get_profiles_default_profiles_get(refresh=refresh)

    def create_profile(self, resource: str, name: str, settings: Dict[str, Any]):
        req = ProfileRequest(settings=settings)
        return self.controller.controller_post_profile_profiles_path_resource_path_rname_post(resource, name, req)

    def update_profile(self, resource: str, name: str, settings: Dict[str, Any]):
        req = ProfileRequest(settings=settings)
        return self.controller.controller_put_profile_profiles_path_resource_path_rname_put(resource, name, req)

    def delete_profile(self, resource: str, name: str):
        return self.controller.controller_delete_profile_profiles_path_resource_path_rname_delete(resource, name)

    def images(self, name: Optional[str] = None):
        return self.controller.controller_get_images_images_get(name=name)

    def logs(self, aid: int, nname: str, **kwargs):
        return self.controller.controller_get_logs_active_int_aid_logs_path_nname_get(aid, nname, **kwargs)

    def exec(self, cmd: List[str], node: str, container: str, **kwargs):
        req = ExecRequest(Cmd=cmd, node=node, container=container, **kwargs)
        return self.controller.controller_exec_command_exec_post(req)

class Service:
    def __init__(self, instances=None, image=None, profile=None, **kwargs):
        self.instances = instances
        self.image = image
        self.profile = profile
        self.kwargs = kwargs

    def to_dict(self):
        return {
            "instances": self.instances,
            "image": self.image,
            "profile": self.profile,
            "kwargs": self.kwargs
        }

class Session:
    def __init__(self, client: Client):
        self.client = client
        self.requests = []
        self.manifest = {}

    def addService(self, srv: Service):
        self.requests.append(srv.to_dict())

    def initialize(self):
        res = self.client.create(self.requests)
        self.manifest = res
        return res

    def start(self):
        ret = {}
        for aid in self.manifest.keys():
            res = self.client.start(int(aid))
            self.manifest[aid].update(res.get(aid, {}))
            ret.update(res)
        return ret

    def stop(self):
        for aid in self.manifest.keys():
            self.client.stop(int(aid))

    def status(self):
        ret = []
        for aid in self.manifest.keys():
            ret.append(self.client.active(int(aid)))
        return ret

    def destroy(self):
        for aid in self.manifest.keys():
            self.client.delete(int(aid))
        self.manifest = {}
