#!/usr/bin/env python3
# Using dict.get() with default values

config = {
    "host": "localhost",
    "port": 8080
}

# Get existing key
host = config.get("host")
print(f"Host: {host}")

# Get non-existing key (returns None)
timeout = config.get("timeout")
print(f"Timeout: {timeout}")

# Get non-existing key with default
timeout = config.get("timeout", 30)
print(f"Timeout with default: {timeout}")

debug = config.get("debug", False)
print(f"Debug with default: {debug}")

# Safer than direct access (no KeyError)
# config["missing"]  # This would raise KeyError
missing = config.get("missing", "N/A")
print(f"Missing with default: {missing}")
