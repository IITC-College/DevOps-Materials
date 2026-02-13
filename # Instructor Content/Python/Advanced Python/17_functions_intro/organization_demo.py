#!/usr/bin/env python3
# Functions help organize code logically

def validate_user(username):
    if len(username) < 3:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    return True

def login(username, password):
    if not validate_user(username):
        print("Invalid username")
        return False
    if not validate_password(password):
        print("Invalid password")
        return False
    print("Login successful")
    return True

# Clear structure: separate concerns into functions
login("alice", "password123")
login("ab", "short")
