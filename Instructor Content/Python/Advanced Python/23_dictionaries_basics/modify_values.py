#!/usr/bin/env python3
# Modifying dictionary values

config = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

print(f"Original: {config}")

# Modify values
config["host"] = "server1"
config["port"] = 9000
config["debug"] = True

print(f"Modified: {config}")

# Modify based on current value
config["port"] = config["port"] + 100
print(f"Port updated: {config}")
