#!/usr/bin/env python3
# Reading text files

"""
READING TEXT FILES:

Common use cases:
- Configuration files
- Log files
- Data files
- CSV files
- Reports
"""

# Create sample log file
with open('app.log', 'w') as f:
    f.write("[2024-01-15 10:30:00] INFO: Application started\n")
    f.write("[2024-01-15 10:30:05] INFO: Connected to database\n")
    f.write("[2024-01-15 10:30:10] WARNING: High memory usage\n")
    f.write("[2024-01-15 10:30:15] ERROR: Failed to connect to API\n")
    f.write("[2024-01-15 10:30:20] INFO: Retrying connection\n")
    f.write("[2024-01-15 10:30:25] INFO: Connection successful\n")

# Example 1: Read entire log file
print("Example 1: Read entire log file")
print("-" * 40)
with open('app.log', 'r') as f:
    log_content = f.read()
    print(log_content)

# Example 2: Read and process line by line
print("\nExample 2: Find ERROR lines")
print("-" * 40)
with open('app.log', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(line.strip())

# Example 3: Count occurrences
print("\nExample 3: Count log levels")
print("-" * 40)
info_count = 0
warning_count = 0
error_count = 0

with open('app.log', 'r') as f:
    for line in f:
        if 'INFO' in line:
            info_count += 1
        elif 'WARNING' in line:
            warning_count += 1
        elif 'ERROR' in line:
            error_count += 1

print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")

# Example 4: Read config file
print("\nExample 4: Read configuration file")
print("-" * 40)

# Create config file
with open('config.txt', 'w') as f:
    f.write("host=localhost\n")
    f.write("port=8080\n")
    f.write("debug=true\n")
    f.write("max_connections=100\n")

# Parse config file
config = {}
with open('config.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=')
            config[key] = value

print("Configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Example 5: Read file with encoding
print("\nExample 5: Specify encoding")
print("-" * 40)

with open('app.log', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Read {len(content)} characters")

print("\nBest practices:")
print("  ✓ Use 'with' statement")
print("  ✓ Specify encoding for text files")
print("  ✓ Process line by line for large files")
print("  ✓ Handle errors with try/except")
