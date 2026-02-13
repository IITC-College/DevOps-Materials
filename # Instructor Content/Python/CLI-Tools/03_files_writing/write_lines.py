#!/usr/bin/env python3
# Writing multiple lines

"""
WRITING MULTIPLE LINES:

Method 1: Multiple write() calls
Method 2: writelines() with list
Method 3: Loop over data
Method 4: Write multi-line string
"""

# Method 1: Multiple write() calls
print("Method 1: Multiple write() calls")
print("-" * 40)

with open('method1.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("✓ Wrote 3 lines with separate write() calls")

# Method 2: writelines() with list
print("\nMethod 2: writelines()")
print("-" * 40)

lines = [
    "First line\n",
    "Second line\n",
    "Third line\n",
    "Fourth line\n"
]

with open('method2.txt', 'w') as f:
    f.writelines(lines)

print("✓ Wrote list of lines with writelines()")

# Method 3: Loop over data
print("\nMethod 3: Loop over data")
print("-" * 40)

data = ["apple", "banana", "cherry", "date"]

with open('method3.txt', 'w') as f:
    for item in data:
        f.write(f"{item}\n")

print("✓ Wrote data in loop")

# Method 4: Multi-line string
print("\nMethod 4: Multi-line string")
print("-" * 40)

content = """This is line 1
This is line 2
This is line 3
This is line 4
"""

with open('method4.txt', 'w') as f:
    f.write(content)

print("✓ Wrote multi-line string")

# Example 5: Writing structured data
print("\nExample 5: Writing structured data")
print("-" * 40)

users = [
    {"name": "Alice", "age": 30, "role": "Admin"},
    {"name": "Bob", "age": 25, "role": "User"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]

with open('users.txt', 'w') as f:
    f.write("USER REPORT\n")
    f.write("=" * 40 + "\n")
    for user in users:
        f.write(f"Name: {user['name']}\n")
        f.write(f"Age: {user['age']}\n")
        f.write(f"Role: {user['role']}\n")
        f.write("-" * 40 + "\n")

print("✓ Wrote structured report")

# Example 6: Writing CSV-style data
print("\nExample 6: Writing CSV-style data")
print("-" * 40)

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "London"],
    ["Charlie", "35", "Tokyo"]
]

with open('data.csv', 'w') as f:
    for row in data:
        f.write(",".join(row) + "\n")

print("✓ Wrote CSV data")

# Example 7: Writing numbered lines
print("\nExample 7: Writing numbered lines")
print("-" * 40)

commands = ["deploy", "backup", "status", "help", "exit"]

with open('commands.txt', 'w') as f:
    f.write("Available Commands:\n")
    f.write("=" * 40 + "\n")
    for i, cmd in enumerate(commands, 1):
        f.write(f"{i}. {cmd}\n")

print("✓ Wrote numbered list")

# Verify
with open('commands.txt', 'r') as f:
    print("\nContent:")
    print(f.read())

print("Best practices:")
print("  ✓ Use writelines() for lists")
print("  ✓ Use loops for structured data")
print("  ✓ Add \\n explicitly (writelines doesn't)")
print("  ✓ Format data before writing")
