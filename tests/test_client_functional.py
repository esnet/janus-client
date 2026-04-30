import pytest

def test_nodes_get(janus_client, node_fixture):
    if isinstance(node_fixture, str) or isinstance(node_fixture, int):
        # Specific node requested
        if isinstance(node_fixture, str):
            res = janus_client.nodes(node=node_fixture)
        else:
            res = janus_client.nodes(node_id=node_fixture)
        assert res is not None
    else:
        # List of nodes returned by fixture default
        assert isinstance(node_fixture, (list, dict))
        if isinstance(node_fixture, dict):
            print(f"Nodes: {list(node_fixture.keys())}")
        elif isinstance(node_fixture, list):
            print(f"Nodes: {[n.get('name') for n in node_fixture if isinstance(n, dict)]}")

def test_sessions_get(janus_client, session_fixture):
    assert session_fixture is not None
    if hasattr(session_fixture, 'items'):
         print(f"Active sessions: {list(session_fixture.keys())}")

def test_profiles_get(janus_client, profile_fixture):
    resource, data = profile_fixture
    assert data is not None
    if hasattr(data, 'items'):
         print(f"Profiles for {resource}: {list(data.keys())}")

def test_images_get(janus_client, image_fixture):
    assert image_fixture is not None
    if isinstance(image_fixture, list):
         print(f"Images: {image_fixture}")

def test_active_logs(janus_client, session_fixture):
    if not hasattr(session_fixture, 'items') or not session_fixture:
        pytest.skip("No active sessions to get logs from")
    
    aid = next(iter(session_fixture))
    manifest = session_fixture[aid]
    
    # Try to find a node name in the manifest
    services = manifest.get('services', {})
    if not services:
        pytest.skip("No services/nodes in session manifest")
        
    sname = next(iter(services))
    instances = services[sname]
    if not instances:
        pytest.skip("No instances in service")
    
    nname = instances[0].get('nname')
    if not nname:
        pytest.skip("No nname in instance")
        
    logs = janus_client.logs(int(aid), nname, tail=10)
    assert logs is not None
