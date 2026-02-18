from unittest import result
import requests
import json

GITHUB_ENDPOINT = "https://api.github.com"

response = requests.get(GITHUB_ENDPOINT, timeout=10)

print(f"HTTP status code: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")

search_url = f"{GITHUB_ENDPOINT}/search/repositories"

# https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
query_params = {
    "q": "python devops",
    "sort": "stars",
    "order": "desc",
    "per_page": 5,
}

response = requests.get(search_url, params=query_params, timeout=10)
response.raise_for_status() # raise an exception if the request is4xx or 5xx

print(f"Requested URL: {response.url}")
results = response.json()

print(f"Found {results.get('total_count')} repositories")

for repo in results.get('items', []):
    print(f"  - {repo.get('name')} (Stars: {repo.get('stargazers_count')})")

# This line will print the first repository in the list, this is useful for debugging
print(json.dumps(results.get('items', [])[0], indent=2))