import pytest
from janus_client.client import Client

BASE_URL = "http://localhost:5001"
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
    c = Client(url=BASE_URL, auth=AUTH, verify=VERIFY_SSL)
    try:
        c.login()
    except Exception:
        pass
    return c

@pytest.fixture
def node_fixture(request, janus_client):
    node_name = request.config.getoption("--node")
    node_id = request.config.getoption("--node_id")
    if node_name:
        return node_name
    elif node_id:
        return node_id
    else:
        try:
            return janus_client.nodes()
        except Exception:
            return {}

@pytest.fixture
def session_fixture(request, janus_client):
    aid = request.config.getoption("--aid")
    if aid:
        try:
            return janus_client.active(aid)
        except Exception:
            return {}
    else:
        try:
            return janus_client.active()
        except Exception:
            return {}

@pytest.fixture
def profile_fixture(request, janus_client):
    resource = request.config.getoption("--resource") or "host"
    name = request.config.getoption("--name")
    if resource and name:
        return (resource, name)
    else:
        try:
            return (resource, janus_client.profiles(resource=resource))
        except Exception:
            return (resource, {})

@pytest.fixture
def image_fixture(request, janus_client):
    image_name = request.config.getoption("--name")
    if image_name:
        return image_name
    else:
        try:
            return janus_client.images()
        except Exception:
            return []
