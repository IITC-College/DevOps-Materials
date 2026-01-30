#!/usr/bin/env python3
# Importing multiple modules

import datetime
import random
import os

# Use datetime
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%H:%M:%S')}")

# Use random
lucky_number = random.randint(1, 100)
print(f"Lucky number: {lucky_number}")

# Use os
print(f"Current directory: {os.getcwd()}")

# Combine them
log_entry = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Random value: {lucky_number}"
print(log_entry)

# Import specific items
from math import pi, sqrt

print(f"Pi: {pi}")
print(f"Square root of 25: {sqrt(25)}")
