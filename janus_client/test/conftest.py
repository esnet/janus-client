import pytest
from janus_client.client import Client

BASE_URL = "https://localhost:5000"
AUTH = ("admin", "admin")
VERIFY_SSL = False

def pytest_addoption(parser):
    parser.addoption("--node", action="store", default=None)
    parser.addoption("--node_id", action="store", type=int, default=None)
    parser.addoption("--aid", action="store", type=int, default=None)
    parser.addoption("--exec_id", action="store", default=None)
    parser.addoption("--container_id", action="store", default=None)
    parser.addoption("--resource", action="store", default=None)
    parser.addoption("--name", action="store", default=None)

@pytest.fixture(scope="session")
def janus_client():
    return Client(url=BASE_URL, auth=AUTH, verify=VERIFY_SSL)

@pytest.fixture
def node_fixture(request, janus_client):
    node_name = request.config.getoption("--node")
    node_id = request.config.getoption("--node_id")
    if node_name:
        yield node_name
    elif node_id:
        yield node_id
    else:
        existing_nodes = janus_client.nodes().json()
        if existing_nodes:
            yield existing_nodes


@pytest.fixture
def new_node_fixture(janus_client):
    node_data = {
        "name": "pytest-node-temp",
        "url": "tcp://192.168.122.190:9001",
        "type": 1
    }
    janus_client.add_node(node_data)
    yield node_data
    # janus_client.delete_node(node=node_data["name"])  # cleanup


@pytest.fixture
def session_fixture(request, janus_client):
    aid = request.config.getoption("--aid")
    if aid:
        existing_session = janus_client.active(aid).json()
        yield existing_session
    else:
        existing_sessions = janus_client.active().json()
        if existing_sessions:
            yield existing_sessions

@pytest.fixture
def new_session_fixture(janus_client):
    service = {
        "instances": ["localhost"],
        "image": "ubuntu:latest",
        "profile": "default",
        "kwargs": {}
    }
    create_resp = janus_client.create([service]).json()
    aid = list(create_resp.keys())[0]
    yield aid
    # janus_client.delete(aid)  # Cleanup


@pytest.fixture
def profile_fixture(request, janus_client):
    resource = request.config.getoption("--resource") or "host"
    name = request.config.getoption("--name")
    if resource and name:
        yield (resource, name)
    else:
        existing_profiles = janus_client.profiles(resource=resource).json()
        if existing_profiles:
            yield (resource, existing_profiles)


@pytest.fixture
def new_profile_fixture(request, janus_client):
    resource = request.config.getoption("--resource") or "host"
    name = f"pytest-{resource}-profile-temp"
    if resource == "host":  # ContainerProfile
        settings = {
            "cpu": 2,
            "memory": 2048,
            "privileged": False,
            "systemd": False
        }
    elif resource == "network":  # NetworkProfile
        settings = {
            "driver": "bridge",
            "enable_ipv6": False
        }
    elif resource == "volume":  # VolumeProfile
        settings = {
            "type": "tmpfs"
            # driver/source/target are optional unless type="bind"
        }
    else:
        raise ValueError(f"Unsupported resource type: {resource}")

    janus_client.create_profile(resource, name, settings)
    yield (resource, name)
    # janus_client.delete_profile(resource, name) # Cleanup

@pytest.fixture
def update_profile_fixture(request, janus_client):
    resource = request.config.getoption("--resource")
    name = request.config.getoption("--name")
    if not resource or not name:
        pytest.skip("You must provide both --resource and --name to update a profile")

    # Default update settings
    if resource == "host":  # ContainerProfile
        update_settings = {
            "cpu": 4,
            "memory": 4294967296,
            "privileged": True
        }
    elif resource == "network":  # NetworkProfile
        update_settings = {
            "driver": "overlay",
            "enable_ipv6": True
        }
    elif resource == "volume":  # VolumeProfile
        update_settings = {
            "type": "tmpfs",
            "driver": "local"
        }
    else:
        raise ValueError(f"Unsupported resource type: {resource}")
    yield (resource, name, update_settings)


@pytest.fixture
def image_fixture(request, janus_client):
    image_name = request.config.getoption("--name")
    if image_name:
        yield image_name
    else:
        existing_images = janus_client.images().json()
        if existing_images:
            yield existing_images
        else:
            yield []


@pytest.fixture
def exec_fixture(request, janus_client):
    node = request.config.getoption("--node")
    exec_id = request.config.getoption("--exec_id")
    if node and exec_id:
        yield (node, exec_id)
    else:
        pytest.skip("You must provide both --node and --exec_id to get the status of exec instance")

@pytest.fixture
def new_exec_fixture(request, janus_client):
    node_name = request.config.getoption("--node")
    container_id = request.config.getoption("--container_id")

    if not node_name or not container_id:
        pytest.skip("You must provide both --node and --container_id to create a exec instance")
    else:
        exec_request = {
            "node": node_name,
            "container": container_id,
            "Cmd": ["echo", "hello from exec"],
            "start": False,
            "attach": False,
            "tty": False
        }
        exec_resp = janus_client.exec_create(exec_request).json()
        exec_id = exec_resp.get("Id") or exec_resp.get("id")
        yield (node_name, exec_id)