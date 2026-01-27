#!/bin/bash
# Set up permissions for sudo lab
# This script sets up the initial file permissions to create the learning scenarios

echo "Setting up permissions for Understanding sudo Lab..."
echo "This script requires sudo to set up the lab environment correctly."
echo ""

# Set protected system files (owned by root, restrictive permissions)
echo "Setting up protected system files..."
sudo chown root:root data/system_files/protected.txt
sudo chmod 600 data/system_files/protected.txt

sudo chown root:root data/system_files/system_config.txt
sudo chmod 644 data/system_files/system_config.txt

# Set readable file (user-owned, normal permissions)
echo "Setting up readable file..."
# This file should be readable by the user, so we'll leave it as is
# or set it to current user if needed
chmod 644 data/system_files/readable.txt

# Set user_app files to root ownership (simulating the problem)
echo "Setting up user_app files (simulating ownership problem)..."
sudo chown root:root projects/user_app/config.txt
sudo chmod 644 projects/user_app/config.txt

sudo chown root:root projects/user_app/install.sh
sudo chmod 644 projects/user_app/install.sh

# System service files should be readable (they demonstrate legitimate sudo use)
echo "Setting up system_service files..."
chmod 644 projects/system_service/install.sh
chmod 644 projects/system_service/service.conf

# Log files should be readable
echo "Setting up log files..."
chmod 644 data/logs/app.log
chmod 644 data/logs/sudo_example.log

# Secrets directory
echo "Setting up secrets..."
chmod 644 data/secrets/tips.txt

echo ""
echo "Permissions setup complete!"
echo ""
echo "Lab structure:"
echo "  - Protected files (root-owned): data/system_files/protected.txt, system_config.txt"
echo "  - Readable file (user-owned): data/system_files/readable.txt"
echo "  - User app files (root-owned, simulating problem): projects/user_app/*"
echo "  - System service files (readable): projects/system_service/*"
echo ""
echo "Students will learn to:"
echo "  1. Analyze 'Permission denied' errors"
echo "  2. Understand when sudo is needed"
echo "  3. Fix ownership instead of using sudo repeatedly"
echo "  4. Understand sudo logging"
echo "  5. Think critically about sudo usage"
echo ""
