# Janus Python Client

A strictly-typed Python client for the Janus Controller API.

This client is automatically generated from the Janus Controller's OpenAPI 3.1 specifications and provides a robust, strongly-typed SDK for interacting with the various API components.

## Features

- **Auto-Generated SDK**: Built automatically using OpenAPI Generator (`generate_client.py`).
- **Strict Typing**: Utilizes Pydantic v2 models for comprehensive request and response validation.
- **Categorized APIs**: Logical separation of endpoints into dedicated API classes:
  - `SessionsApi`: Manage active container sessions
  - `NodesApi`: Manage Janus endpoints
  - `ProfilesApi`: Manage configuration profiles
  - `ImagesApi`: Browse available Docker images
  - `AuthApi`: Manage authentication and authorization
- **CLI Tool included**: Comes with an interactive command-line interface (`januscli`) to easily interact with the controller.

## Installation

```bash
git clone https://github.com/esnet/janus-client.git
cd janus-client
pip install -e .
```

## Usage

### Using the Python SDK

The core Python client is available in the `janus_client` module.

```python
from janus_client.client import Client

# Initialize the client with Basic Auth
# (A JWT is automatically acquired and used for subsequent requests)
client = Client("http://localhost:5000", auth=("admin", "admin_password"))

# Fetch active sessions
active_sessions = client.status()
print(active_sessions)

# Retrieve endpoints/nodes
nodes = client.nodes()
print(nodes)
```

### Using the CLI (`januscli`)

You can launch the interactive shell environment to quickly query the controller:

```bash
# janus <url> <user> <password>
janus http://localhost:5000 admin admin_password
```

Once inside the interactive prompt, type `help` to see the available commands.

```text
janus> help

Documented commands (type help <topic>):
========================================
active  auth  cd  create  destroy  images  nodes  profiles  sync

Undocumented commands:
======================
EOF  clear  exit  help  quit  refresh
```

## Development

If you've updated the Janus Controller API (e.g. `controller.py` or `models_api.py`), you should regenerate the core `janus-py-client` bindings. 

Make sure your Janus Controller is running locally on port `5000`, and then execute:

```bash
python generate_client.py
```

This script will fetch the latest `openapi.json` from the controller and use `openapi-generator` to update the `janus-py-client` bindings folder.

## Testing

To run the functional and unit tests:

```bash
pytest
```
