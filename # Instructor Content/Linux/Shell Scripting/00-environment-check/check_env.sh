#!/bin/bash

# Simple environment check script
# Demonstrates basic commands and output

echo "=== Environment Check ==="
echo ""

echo "Current User:"
whoami
echo ""

echo "Current Directory:"
pwd
echo ""

echo "Shell Type:"
echo $SHELL
echo ""

echo "OS Information:"
uname -a
echo ""

echo "Environment Ready!"
