#!/bin/bash

# Script to check file ownership
# This script demonstrates ownership checking

echo "Current user: $(whoami)"
echo "User ID: $(id -u)"
echo "Group ID: $(id -g)"
echo ""
echo "Groups you belong to:"
groups
echo ""
echo "Files in current directory:"
ls -l
