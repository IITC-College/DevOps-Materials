#!/usr/bin/env python3
# Looping over dictionary values

scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "David": 88
}

# Loop over values only
print("All scores:")
for score in scores.values():
    print(f"  Score: {score}")

# Calculate total using loop
total = 0
for score in scores.values():
    total += score

print(f"\nTotal: {total}")
print(f"Average: {total / len(scores)}")
