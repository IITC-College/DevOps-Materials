#!/usr/bin/env python3
# Using random module

import random

# Random integer
num = random.randint(1, 100)
print(f"Random number (1-100): {num}")

# Random float
rand_float = random.random()
print(f"Random float (0-1): {rand_float}")

# Random choice from list
colors = ["red", "green", "blue", "yellow"]
chosen = random.choice(colors)
print(f"Random color: {chosen}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")

# Random sample
items = ["a", "b", "c", "d", "e"]
sample = random.sample(items, 3)
print(f"Random sample of 3: {sample}")
