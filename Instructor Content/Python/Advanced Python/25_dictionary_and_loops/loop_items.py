#!/usr/bin/env python3
# Looping over dictionary items (key-value pairs)

config = {
    "host": "localhost",
    "port": 8080,
    "secure": True,
    "timeout": 30
}

# Loop over items - most common pattern
print("Configuration settings:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Use both key and value
print("\nDetailed view:")
for setting, value in config.items():
    print(f"Setting '{setting}' is set to '{value}'")
