#!/usr/bin/env python3
# Building dictionaries with loops

# Build from list
names = ["Alice", "Bob", "Charlie"]
name_lengths = {}

for name in names:
    name_lengths[name] = len(name)

print(f"Name lengths: {name_lengths}")

# Build squares
numbers = [1, 2, 3, 4, 5]
squares = {}

for num in numbers:
    squares[num] = num ** 2

print(f"Squares: {squares}")

# Build from user input simulation
users = {}
user_data = [
    ("alice", 25),
    ("bob", 30),
    ("charlie", 28)
]

for username, age in user_data:
    users[username] = {"age": age, "active": True}

print(f"Users: {users}")
