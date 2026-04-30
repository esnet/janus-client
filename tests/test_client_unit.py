import pytest
from unittest.mock import MagicMock, patch
from janus_client.client import Client, Session, Service

@pytest.fixture
def mock_controller():
    with patch('janus_client.client.JanusControllerApi') as mock:
        yield mock.return_value

@pytest.fixture
def mock_client(mock_controller):
    client = Client("http://test", auth=("user", "pass"))
    client.controller = mock_controller
    return client

def test_client_login(mock_client, mock_controller):
    mock_response = MagicMock()
    mock_response.access_token = "fake-token"
    mock_controller.controller_get_token_token_post.return_value = mock_response
    
    assert mock_client.login() is True
    assert mock_client.configuration.access_token == "fake-token"

def test_client_active_all(mock_client, mock_controller):
    mock_controller.controller_get_active_active_get.return_value = {"1": {"state": "RUNNING"}}
    res = mock_client.active()
    assert res == {"1": {"state": "RUNNING"}}
    mock_controller.controller_get_active_active_get.assert_called_once()

def test_client_create(mock_client, mock_controller):
    reqs = [{"instances": ["local"], "image": "img", "profile": "prof"}]
    mock_controller.controller_create_sessions_create_post.return_value = {"1": {}}
    
    res = mock_client.create(reqs)
    assert res == {"1": {}}
    args, _ = mock_controller.controller_create_sessions_create_post.call_args
    # SessionRequestList stores it in actual_instance
    assert args[0].actual_instance[0].image == "img"

def test_session_initialize(mock_client, mock_controller):
    mock_controller.controller_create_sessions_create_post.return_value = {"123": {"state": "CREATED"}}
    
    sess = Session(mock_client)
    srv = Service(instances=["local"], image="img", profile="prof")
    sess.addService(srv)
    
    res = sess.initialize()
    assert res == {"123": {"state": "CREATED"}}
    assert sess.manifest == {"123": {"state": "CREATED"}}
