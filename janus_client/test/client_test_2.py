import pytest


def test_nodes_get(janus_client, node_fixture):
    name = node_fixture
    resp = janus_client.nodes(name=name)
    print(resp.json())

def test_nodes_add(janus_client, node_fixture):
    print(f"Node available: {node_fixture}")
    assert node_fixture is not None

def test_nodes_delete(janus_client, node_fixture):
    resp = janus_client.delete_node(node=node_fixture)
    print(resp.json())


def test_active_logs(janus_client, session_fixture):
    # Start session to get logs
    start_resp = janus_client.start(session_fixture).json()
    node_name = list(start_resp[session_fixture]['services'].keys())[0]
    resp = janus_client.active_logs(aid=session_fixture, nname=node_name, stdout=1, stderr=1, tail=10)
    print(resp.json())


# @pytest.mark.exec
def test_exec_create(janus_client, exec_fixture):
    node, exec_id = exec_fixture
    assert node is not None
    assert exec_id is not None

# @pytest.mark.exec
def test_exec_status(janus_client, exec_fixture):
    node, exec_id = exec_fixture
    resp = janus_client.exec_status(node=node, exec_id=exec_id)
    print(resp.json())


def test_images_list(janus_client):
    resp = janus_client.images()
    print(resp.json())

def test_images_get(janus_client):
    all_images = janus_client.images().json()
    if all_images:
        first_image = all_images[0].get("name")
        resp = janus_client.images(name=first_image)
        print(resp.json())


# @pytest.mark.profiles
def test_profiles_create(janus_client, profile_fixture):
    resource, name = profile_fixture
    print(f"Profile: {resource}/{name}")
    assert resource is not None and name is not None

# @pytest.mark.profiles
def test_profiles_get(janus_client, profile_fixture):
    resource, name = profile_fixture
    resp = janus_client.profiles(resource=resource, name=name)
    print(resp.json())

def test_list_profiles(profile_fixture):
    resource, profiles = profile_fixture
    print(f"Profiles for resource '{resource}':")
    for p in profiles:
        print(f"- {p['name']}")
    assert isinstance(profiles, list)

# @pytest.mark.profiles
def test_profiles_update(janus_client, profile_fixture):
    resource, name = profile_fixture
    resp = janus_client.update_profile(resource, name, {"cpu": 4, "memory": "8g"})
    print(resp.json())

# @pytest.mark.profiles
def test_profiles_delete(janus_client, profile_fixture):
    resource, name = profile_fixture
    resp = janus_client.delete_profile(resource, name)
    print(resp.json())


def test_sessions_create(janus_client):
    service = {"instances": 1, "image": "ubuntu:20.04", "profile": "default", "kwargs": {}}
    resp = janus_client.create([service])
    print(resp.json())

def test_sessions_start(janus_client, session_fixture):
    resp = janus_client.start(session_fixture)
    print(resp.json())

def test_sessions_stop(janus_client, session_fixture):
    resp = janus_client.stop(session_fixture)
    print(resp.json())

def test_sessions_delete(janus_client, session_fixture):
    resp = janus_client.delete(session_fixture)
    print(resp.json())