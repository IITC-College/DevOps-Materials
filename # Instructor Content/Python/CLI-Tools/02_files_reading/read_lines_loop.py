#!/usr/bin/env python3
# Processing files line by line

"""
LINE-BY-LINE PROCESSING:

Best for:
- Large files (memory efficient)
- Log file analysis
- Data processing
- Filtering
- Transformations

Iterator approach - doesn't load entire file into memory!
"""

# Create sample log file
with open('server.log', 'w') as f:
    f.write("2024-01-15 10:00:01 INFO Server started\n")
    f.write("2024-01-15 10:00:05 INFO Listening on port 8080\n")
    f.write("2024-01-15 10:00:10 INFO Request: GET /api/users\n")
    f.write("2024-01-15 10:00:12 INFO Request: POST /api/login\n")
    f.write("2024-01-15 10:00:15 WARNING High memory usage: 85%\n")
    f.write("2024-01-15 10:00:20 INFO Request: GET /api/data\n")
    f.write("2024-01-15 10:00:25 ERROR Database connection failed\n")
    f.write("2024-01-15 10:00:30 ERROR Failed to process request\n")
    f.write("2024-01-15 10:00:35 INFO Retrying connection\n")
    f.write("2024-01-15 10:00:40 INFO Connection restored\n")

# Example 1: Simple line-by-line reading
print("Example 1: Read all lines")
print("-" * 40)

with open('server.log', 'r') as f:
    for line in f:
        print(line.strip())

# Example 2: Filter lines
print("\nExample 2: Filter ERROR lines")
print("-" * 40)

with open('server.log', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(line.strip())

# Example 3: Count and analyze
print("\nExample 3: Log analysis")
print("-" * 40)

log_stats = {
    'INFO': 0,
    'WARNING': 0,
    'ERROR': 0,
    'total_lines': 0
}

with open('server.log', 'r') as f:
    for line in f:
        log_stats['total_lines'] += 1
        if 'INFO' in line:
            log_stats['INFO'] += 1
        elif 'WARNING' in line:
            log_stats['WARNING'] += 1
        elif 'ERROR' in line:
            log_stats['ERROR'] += 1

print("Log statistics:")
for key, value in log_stats.items():
    print(f"  {key}: {value}")

# Example 4: Process and transform
print("\nExample 4: Extract timestamps")
print("-" * 40)

with open('server.log', 'r') as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 2:
            timestamp = f"{parts[0]} {parts[1]}"
            print(f"  {timestamp}")

# Example 5: Numbered lines
print("\nExample 5: Show line numbers")
print("-" * 40)

with open('server.log', 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"{line_num:3d}: {line.strip()}")

# Example 6: Skip empty lines
print("\nExample 6: Skip empty/whitespace lines")
print("-" * 40)

# Add some empty lines
with open('data.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("\n")
    f.write("Line 2\n")
    f.write("   \n")
    f.write("Line 3\n")

count = 0
with open('data.txt', 'r') as f:
    for line in f:
        if line.strip():  # Skip empty/whitespace
            count += 1
            print(f"  {count}: {line.strip()}")

# Example 7: Process in chunks
print("\nExample 7: Read first N lines")
print("-" * 40)

max_lines = 3
with open('server.log', 'r') as f:
    for i, line in enumerate(f, 1):
        if i > max_lines:
            break
        print(f"  {line.strip()}")

print("\nMemory efficiency:")
print("  ✓ for line in file: → Iterator, one line at a time")
print("  ✓ file.readlines() → List, all lines in memory")
print("  ✓ Use iterator for large files!")
