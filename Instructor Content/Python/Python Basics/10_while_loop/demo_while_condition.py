#!/usr/bin/env python3
# Demonstrating while with condition

running = True
count = 0

while running:
    print(count)
    count = count + 1
    if count >= 3:
        running = False
