"""
Pytest Test Suite for Janus Client
==================================

This file contains functional tests for the Janus Client API.
Tests cover nodes, sessions, profiles, images, exec commands, and logs.

Prerequisites
-------------
1. Ensure the Janus API server is running and accessible.
2. Update BASE_URL, AUTH, and VERIFY_SSL in `conftest.py` if needed.
3. Install dependencies:
    pip install pytest requests

Running All Tests
-----------------
Run the entire test suite:
    pytest -v client_test_2.py

Running Specific Tests
----------------------
Run a single test by name:
    pytest -v -k test_nodes_list_all client_test_2.py

Using CLI Options for Fixtures
------------------------------
Many fixtures in `conftest.py` accept command-line options to control behavior:

    --node <node_name>        Use a specific node name for node tests
    --node_id <node_id>       Use a specific node ID for node tests
    --aid <session_id>        Use a specific session ID for session tests
    --name <resource_name>    Use a specific profile or image name
    --resource <type>         Resource type for profiles ("host", "network", "volume")
    --exec_id <exec_id>       Use a specific exec ID for exec tests
    --container <container_id> Use a specific container ID for exec tests

Examples:
---------
List all nodes:
    pytest -v -k test_nodes_list_all

Get details for a specific node:
    pytest -v -k test_nodes_get --node my-node

List all profiles for a resource:
    pytest -v -k test_profiles_list_all --resource host

Update a specific profile:
    pytest -v -k test_profiles_update --resource host --name my-profile

Run exec create on an existing container:
    pytest -v -k test_exec_create --node my-node --container abcd1234

Notes
-----
- If no CLI option is provided, fixtures will try to use existing resources.
- If no resources exist, some fixtures will create temporary ones for testing.
- Tests that require a specific resource may skip if the fixture returns a list instead of a single ID/name.
"""

import pytest


def test_nodes_get(janus_client, node_fixture):
    if isinstance(node_fixture, list):
        #List all nodes
        print("Nodes:", node_fixture)
        assert isinstance(node_fixture, list)
    else:
        #Get a specific node
        if isinstance(node_fixture, str):
            resp = janus_client.nodes(node=node_fixture)
        else:
            resp = janus_client.nodes(node_id=node_fixture)
        data = resp.json()
        print("Node details:", data)
        assert data is not None

def test_nodes_add(janus_client, new_node_fixture):
    print(f"New node created: {new_node_fixture}")
    assert new_node_fixture is not None
    # Optional: Verify node exists
    # nodes = janus_client.nodes().json()
    # assert any(n["name"] == new_node_fixture["name"] for n in nodes)

def test_nodes_delete(janus_client, node_fixture):
    if isinstance(node_fixture, list):
        pytest.skip("Skipping delete — fixture returned a list of nodes (exploration mode)")
    resp = janus_client.delete_node(node=node_fixture)
    print(resp.json())


def test_sessions_get(janus_client, session_fixture):
    if isinstance(session_fixture, list):
        #List all sessions
        print("Sessions:", session_fixture)
        assert isinstance(session_fixture, list)
    else:
        #Get a specific session
        print("Session details:", session_fixture)
        assert session_fixture is not None

def test_sessions_create(janus_client, new_session_fixture):
    session_id= new_session_fixture
    print(f"Created session with Id: {session_id}")
    assert new_session_fixture is not None
    # Optional: Verify session exists
    # active_sessions = janus_client.active().json()
    # assert any(new_session_fixture in sess for sess in active_sessions)

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


def test_profiles_get(janus_client, profile_fixture):
    resource, data = profile_fixture
    if isinstance(data, list):
        #List all profiles
        print(f"Profiles for resource '{resource}': {data}")
        assert isinstance(data, list)
    else:
        #Get a specific profile
        profile_name = data
        resp = janus_client.profiles(resource=resource, name=profile_name)
        print(resp.json())
        assert resp.json() is not None

def test_profiles_create(janus_client, new_profile_fixture):
    resource, name = new_profile_fixture
    assert new_profile_fixture is not None
    # Optional: Verify profile exists
    # profiles_list = janus_client.profiles(resource=resource).json()
    # assert any(p["name"] == name for p in profiles_list)

# @pytest.mark.profiles
def test_profiles_update(janus_client, update_profile_fixture):
    resource, name, update_settings = update_profile_fixture
    resp = janus_client.update_profile(resource, name, update_settings)
    print(resp.json())
    # Optional: verify the update took effect
    # updated_profile = janus_client.profiles(resource=resource, name=name).json()
    # assert updated_profile["settings"] is not None
    # for key, value in update_settings.items():
    #     assert updated_profile["settings"].get(key) == value

# @pytest.mark.profiles
def test_profiles_delete(janus_client, profile_fixture):
    resource, name = profile_fixture
    if not name:
        pytest.skip(f"No profile with name {name} available")
    resp = janus_client.delete_profile(resource, name)
    print(resp.json())


def test_images_get(janus_client, image_fixture):
    if isinstance(image_fixture, list):
        #List all images
        print("Images:", image_fixture)
        assert isinstance(image_fixture, list)
        if not image_fixture:
            pytest.skip("No images available")
    else:
        #Get a specific image
        resp = janus_client.images(name=image_fixture)
        print(resp.json())
        assert resp.json() is not None


# @pytest.mark.exec
def test_exec_create(janus_client, new_exec_fixture):
    node, exec_id = new_exec_fixture
    assert node is not None
    assert exec_id is not None
    # Optional: Check exec status
    resp = janus_client.exec_status(node=node, exec_id=exec_id)
    print(resp.json())

# @pytest.mark.exec
def test_exec_status(janus_client, exec_fixture):
    node, exec_id = exec_fixture
    resp = janus_client.exec_status(node=node, exec_id=exec_id)
    print(resp.json())


def test_active_logs(janus_client, session_fixture):
    session_info = session_fixture
    session_id = session_info['id']
    node_name = session_info['request'][0]['instances'][0]
    if isinstance(session_fixture, list):
        pytest.skip("Skipping logs — provide session ID using --aid flag")
    else:
        resp = janus_client.active_logs(Id=session_id, nname=node_name, stdout=1, stderr=1, tail=100)
        print(resp.json())