import requests
import json
print("Sending GET request to https://api.github.com with a 5 second timeout...")
response = requests.get("https://api.github.com", timeout=5)

print(f"HTTP status code of the response: {response.status_code}")
print(f"Content-Type header of the response: {response.headers.get('Content-Type')}")


""""
# Commenting out for clarity but keeping it here for reference
print("Entire response body as a decoded string:")
print(response.text)

print("Raw binary content of the response (first 60 bytes):")
print(response.content[:60])

print("This is an example of a GitHub personal access token—never share real tokens!")
print("github_pat_EXAMPLE1234567890_REPLACE_WITH_YOUR_ACTUAL_TOKEN_NEVER_COMMIT_REAL_TOKENS")
"""

data = response.json()
print("Available API endpoints:")
# for key in data.keys():
#     print(f"  - {key}")
print(json.dumps(data, indent=4))
