#!/usr/bin/env python3
# Using custom module

import my_module

# Use functions from module
greeting = my_module.greet("Alice")
print(greeting)

result = my_module.add(10, 20)
print(f"10 + 20 = {result}")

print(f"Is 10 even? {my_module.is_even(10)}")
print(f"Is 7 even? {my_module.is_even(7)}")
