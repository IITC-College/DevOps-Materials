#!/usr/bin/env python3
# Using dict.update()

config = {
    "host": "localhost",
    "port": 8080
}

print(f"Original: {config}")

# Update with another dictionary
new_settings = {
    "port": 9000,
    "timeout": 30,
    "secure": True
}

config.update(new_settings)
print(f"After update: {config}")

# Update with keyword arguments
config.update(host="server1", debug=True)
print(f"After keyword update: {config}")
