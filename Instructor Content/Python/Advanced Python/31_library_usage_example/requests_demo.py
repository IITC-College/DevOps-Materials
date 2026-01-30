#!/usr/bin/env python3
# Demonstrating requests library for HTTP requests

"""
requests - HTTP library for Python

INSTALLATION:
  pip install requests

USAGE:
  import requests
  response = requests.get('https://api.github.com')
"""

try:
    import requests
    
    # Simple GET request
    print("Making GET request...")
    response = requests.get('https://api.github.com')
    
    # Check response
    print(f"Status code: {response.status_code}")
    print(f"Content type: {response.headers.get('content-type')}")
    
    # Parse JSON
    if response.status_code == 200:
        data = response.json()
        print(f"API version: {data.get('current_user_url', 'N/A')}")
    
    # GET request with parameters
    print("\nSearching GitHub...")
    params = {'q': 'python', 'sort': 'stars'}
    search_response = requests.get(
        'https://api.github.com/search/repositories',
        params=params
    )
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        print(f"Found {search_data['total_count']} repositories")
        
        # Show first 3 results
        for repo in search_data['items'][:3]:
            print(f"  - {repo['name']}: {repo['stargazers_count']} stars")
    
    # POST request example (to httpbin.org test server)
    print("\nPOST request example...")
    post_data = {'name': 'Alice', 'age': 25}
    post_response = requests.post(
        'https://httpbin.org/post',
        json=post_data
    )
    
    if post_response.status_code == 200:
        result = post_response.json()
        print(f"Server received: {result['json']}")

except ImportError:
    print("requests is not installed")
    print("Install with: pip install requests")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
