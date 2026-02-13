#!/usr/bin/env python3
# Different types as default values

def configure(host="localhost", port=8080, secure=True, tags=[]):
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Secure: {secure}")
    print(f"Tags: {tags}")
    print("---")

# Use all defaults
configure()

# Override with different types
configure(host="server1", port=9000)
configure(secure=False)

# Note: Be careful with mutable defaults like lists!
# Better practice: use None and create list inside function
