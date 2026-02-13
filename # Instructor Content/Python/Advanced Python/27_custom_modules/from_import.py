#!/usr/bin/env python3
# Different ways to import from modules

# Import specific items
from my_module import greet, add

# Use without module prefix
greeting = greet("Bob")
print(greeting)

result = add(5, 3)
print(f"5 + 3 = {result}")

# Import all (not recommended)
# from my_module import *

# Import with alias
from my_module import is_even as check_even

print(f"Is 10 even? {check_even(10)}")

# Import module with alias
import my_module as mm

print(mm.greet("Charlie"))
