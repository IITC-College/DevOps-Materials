import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

GITHUB_ENDPOINT = "https://api.github.com"
token = os.environ.get("GH_TOKEN")
print(f"Token loaded (first 10 chars): {token[:10]}...")

urls = {
    "public": f"{GITHUB_ENDPOINT}/zen",
    "protected": f"{GITHUB_ENDPOINT}/user",
}

for description, url in urls.items():
    print(f"Requesting {description} ({url})")
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=10)
        response.raise_for_status()
        print(f"  Status: {response.status_code}")
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            print(f"  Body: {response.json()}")
        else:
            print(f"  Body: {response.text}")
    except requests.exceptions.HTTPError as error:
        print(f"  HTTP error: {error}")
