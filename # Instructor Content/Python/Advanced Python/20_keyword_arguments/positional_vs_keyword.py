#!/usr/bin/env python3
# Positional vs keyword arguments

def create_user(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments (order matters)
create_user("Alice", 25, "Boston")

# Keyword arguments (order doesn't matter)
create_user(name="Bob", age=30, city="Seattle")
create_user(city="Chicago", name="Charlie", age=28)

# Mixed (positional first, then keyword)
create_user("David", age=35, city="Portland")
