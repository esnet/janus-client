import pytest


def test_nodes_list_all(node_fixture):
    print("Nodes:", node_fixture)
    assert isinstance(node_fixture, list)

def test_nodes_add(janus_client, node_fixture):
    print(f"Node available: {node_fixture}")
    assert node_fixture is not None

def test_nodes_delete(janus_client, node_fixture):
    if isinstance(node_fixture, list):
        pytest.skip("Skipping delete — fixture returned a list of nodes (exploration mode)")
    resp = janus_client.delete_node(node=node_fixture)
    print(resp.json())

def test_sessions_list_all(session_fixture):
    print("Sessions:", session_fixture)
    assert isinstance(session_fixture, list)

def test_sessions_create(janus_client):
    service = {"instances": 1, "image": "ubuntu:20.04", "profile": "default", "kwargs": {}}
    resp = janus_client.create([service])
    print(resp.json())

def test_sessions_start(janus_client, session_fixture):
    if isinstance(session_fixture, list):
        pytest.skip("Skipping start — fixture returned list of sessions")
    resp = janus_client.start(session_fixture)
    print(resp.json())

def test_sessions_stop(janus_client, session_fixture):
    if isinstance(session_fixture, list):
        pytest.skip("Skipping stop — fixture returned list of sessions")
    resp = janus_client.stop(session_fixture)
    print(resp.json())

def test_sessions_delete(janus_client, session_fixture):
    if isinstance(session_fixture, list):
        pytest.skip("Skipping delete — fixture returned list of sessions")
    resp = janus_client.delete(session_fixture)
    print(resp.json())

def test_profiles_list_all(profile_fixture):
    resource, profiles = profile_fixture
    print(f"Profiles for resource '{resource}':")
    for p in profiles:
        print(f"- {p['name']}")
    assert isinstance(profiles, list)

# @pytest.mark.profiles
def test_profiles_create(janus_client):
    resource = "host"
    name = "pytest-profile"
    resp = janus_client.create_profile(resource, name, {"cpu": 2, "memory": "4g"})
    print(resp.json())
    janus_client.delete_profile(resource, name)

# @pytest.mark.profiles
def test_profiles_get(janus_client, profile_fixture):
    resource, profiles = profile_fixture
    if not profiles:
        pytest.skip("No profiles available")
    profile_name = profiles[0]['name']
    resp = janus_client.profiles(resource=resource, name=profile_name)
    print(resp.json())

# @pytest.mark.profiles
def test_profiles_update(janus_client, profile_fixture):
    resource, profiles = profile_fixture
    if not profiles:
        pytest.skip("No profiles available")
    profile_name = profiles[0]['name']
    resp = janus_client.update_profile(resource, profile_name, {"cpu": 4, "memory": "8g"})
    print(resp.json())

# @pytest.mark.profiles
def test_profiles_delete(janus_client):
    resource = "host"
    name = "pytest-delete-profile"
    janus_client.create_profile(resource, name, {"cpu": 2, "memory": "4g"})
    resp = janus_client.delete_profile(resource, name)
    print(resp.json())


def test_images_list_all(image_fixture):
    print("Images:", image_fixture)
    assert isinstance(image_fixture, list)

def test_images_get(janus_client, image_fixture):
    if not image_fixture:
        pytest.skip("No images available")
    first_image = image_fixture[0].get("name")
    resp = janus_client.images(name=first_image)
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


def test_active_logs(janus_client, session_fixture):
    if isinstance(session_fixture, list):
        pytest.skip("Skipping logs — fixture returned list of sessions")
    start_resp = janus_client.start(session_fixture).json()
    node_name = list(start_resp[session_fixture]['services'].keys())[0]
    resp = janus_client.active_logs(aid=session_fixture, nname=node_name, stdout=1, stderr=1, tail=10)
    print(resp.json())