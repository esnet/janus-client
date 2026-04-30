import os
import json
import subprocess
import sys
import urllib.request
import argparse

# Paths
DEFAULT_URL = "http://localhost:5001/openapi/openapi.json"
OUTPUT_DIR = "janus-py-client"

def get_spec(url):
    print(f"Fetching OpenAPI spec from {url}...")
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
            else:
                print(f"Error: Received status code {response.status}")
                sys.exit(1)
    except Exception as e:
        print(f"Error fetching spec: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate Janus Python Client")
    parser.add_argument("--url", default=DEFAULT_URL, help=f"URL to Janus OpenAPI spec (default: {DEFAULT_URL})")
    args = parser.parse_args()

    spec = get_spec(args.url)
    version = spec.get("info", {}).get("version", "1.0.0")
    print(f"Detected Janus API version: {version}")
    
    spec_path = "openapi.json"
    with open(spec_path, "w") as f:
        json.dump(spec, f, indent=2)
    
    print(f"Generating client in {OUTPUT_DIR}...")
    
    cmd = [
        "openapi-generator", "generate",
        "-i", spec_path,
        "-g", "python",
        "-o", OUTPUT_DIR,
        "--package-name", "janus_py_client",
        f"--additional-properties=packageVersion={version},projectName=janus-py-client"
    ]
    
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print(f"Successfully generated janus-py-client (version {version})")
    else:
        print("Failed to generate client")
    
    if os.path.exists(spec_path):
        os.remove(spec_path)

if __name__ == "__main__":
    main()
