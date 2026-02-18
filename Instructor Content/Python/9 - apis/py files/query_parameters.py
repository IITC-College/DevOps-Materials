import requests
import json

GITHUB_ENDPOINT = "https://api.github.com"

search_url = f"{GITHUB_ENDPOINT}/search/repositories"
query_params = {
    "q": "python devops",
    "sort": "stars",
    "order": "desc",
    "per_page": 5,
}

response = requests.get(search_url, params=query_params, timeout=10)
response.raise_for_status()

print(f"Requested URL: {response.url}")

print(f"HTTP status code: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")

data = response.json()
print(json.dumps(data, indent=2))