#!/usr/bin/env python3
# Using datetime module

import datetime

# Get current date and time
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Get just the date
today = datetime.date.today()
print(f"Today's date: {today}")

# Format datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")

# Get individual components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

# Create specific date
specific = datetime.date(2026, 1, 30)
print(f"Specific date: {specific}")
