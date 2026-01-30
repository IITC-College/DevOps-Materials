#!/usr/bin/env python3
# Multiple default parameters

def create_user(username, role="user", active=True, email=""):
    print(f"Username: {username}")
    print(f"Role: {role}")
    print(f"Active: {active}")
    print(f"Email: {email}")
    print("---")

# Use all defaults
create_user("alice")

# Override some defaults
create_user("bob", role="admin")

# Override multiple defaults
create_user("charlie", role="moderator", email="charlie@example.com")
