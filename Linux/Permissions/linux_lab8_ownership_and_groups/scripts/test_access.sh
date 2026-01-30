#!/bin/bash

# Script to test file access based on ownership
# This script helps understand ownership and access

echo "Testing file access..."
echo ""

# Check identity
echo "You are: $(whoami)"
echo "Your groups: $(groups)"
echo ""

# Test access to different files
echo "Testing access to data/files/user_file.txt:"
if [ -r "data/files/user_file.txt" ]; then
    echo "  ✓ Can read user_file.txt"
else
    echo "  ✗ Cannot read user_file.txt"
fi

echo ""
echo "Use 'ls -l' to see ownership details!"
