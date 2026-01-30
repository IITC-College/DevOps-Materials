#!/usr/bin/env python3
# Using dict.values()

config = {
    "host": "localhost",
    "port": 8080,
    "timeout": 30,
    "secure": True
}

# Get all values
values = config.values()
print(f"Values: {values}")

# Convert to list
values_list = list(config.values())
print(f"Values as list: {values_list}")

# Iterate over values
print("All values:")
for value in config.values():
    print(f"  - {value}")
