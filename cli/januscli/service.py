from .util import col
from .ssh import get_pubkeys
from .util import CText

cout = CText()

SRV_ACTIONS = ['create', 'start', 'stop', 'del']
SRV_OPTIONS = {'-f': False}

def handle_service(client, args, cfg):
    if not args:
        cout.item(f"No argument, session options: {SRV_OPTIONS}")
        return
    parts = args.split(" ")
    if parts[0] not in SRV_ACTIONS:
        cout.error(f"Unknown service option \"{parts[0]}\"")
        return

    force = False
    if len(parts) > 2:
        for p in parts:
            if p in SRV_OPTIONS.keys():
                if p == '-f':
                    force = True

    if parts[0] == "create":
        try:
            instances = parts[1].split(",")
            image = parts[2]
            profile = parts[3]

            srv_req = {
                "instances": instances,
                "image": image,
                "profile": profile,
                "kwargs": {
                    "USER_NAME": "janus",
                    "PUBLIC_KEY": get_pubkeys()
                }
            }
            
            res = client.create([srv_req])
            cfg['active'].append(res)
            sid = next(iter(res))
            cout.warn(f"Initialized new session with id \"{sid}\"")
            return True
        except Exception as e:
            cout.error(f"Could not create session: {e}")
    elif parts[0] == "start":
        if len(parts) < 2:
            cout.error(f"No session specified")
            return False

        try:
            key = parts[1]
            active = cfg['active']
            found = None
            for a in active:
                if str(next(iter(a))) == str(key):
                    found = a
                    break
            
            if found:
                cout.warn(f"Starting session \"{key}\"")
            
            res = client.start(int(key))
            if found:
                found.update(res)
            return True
        except Exception as e:
            cout.error(f"Could not start session: {e}")
    elif parts[0] == "stop":
        if len(parts) < 2:
            cout.error(f"No session specified")
            return False

        try:
            key = parts[1]
            active = cfg['active']
            found = None
            for a in active:
                if str(next(iter(a))) == str(key):
                    found = a
                    break

            if found:
                cout.warn(f"Stopping session \"{key}\"")
            
            res = client.stop(int(key))
            if found:
                found.update(res)
            return True
        except Exception as e:
            cout.error(f"Could not stop session: {e}")
    elif parts[0] == "del":
        if len(parts) < 2:
            cout.error(f"No session specified")
            return False

        try:
            key = parts[1]
            active = cfg['active']
            found = None
            for a in active:
                if str(next(iter(a))) == str(key):
                    found = a
                    break

            if found:
                cout.warn(f"Deleting session \"{key}\"")
            
            client.delete(int(key), force=force)
            if found:
                active.remove(found)
            return True
        except Exception as e:
            cout.error(f"Could not delete session: {e}")
