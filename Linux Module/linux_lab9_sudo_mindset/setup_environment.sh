#!/bin/bash
################################################################################
# Setup Environment Script for Lab 9: Sudo Mindset
#
# This script prepares the lab environment by setting up file permissions
# and ownership (including root ownership for protected files).
# It should be run by the instructor with sudo before students start the lab.
#
# Usage: sudo ./setup_environment.sh
################################################################################

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Setting up Lab 9: Sudo Mindset                      ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then 
    echo -e "${YELLOW}Please run this script with sudo:${NC}"
    echo "  sudo ./setup_environment.sh"
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${GREEN}[INFO]${NC} Setting up permissions for Sudo Mindset Lab..."
echo ""

# Run the existing set_permissions.sh script
if [ -f "set_permissions.sh" ]; then
    echo -e "${GREEN}[STEP]${NC} Running set_permissions.sh..."
    bash set_permissions.sh
else
    echo -e "${YELLOW}[WARN]${NC} set_permissions.sh not found, setting permissions manually..."
    
    # Set protected system files (owned by root, restrictive permissions)
    echo "Setting up protected system files..."
    chown root:root data/system_files/protected.txt 2>/dev/null || true
    chmod 600 data/system_files/protected.txt 2>/dev/null || true
    
    chown root:root data/system_files/system_config.txt 2>/dev/null || true
    chmod 644 data/system_files/system_config.txt 2>/dev/null || true
    
    # Set readable file (user-owned, normal permissions)
    echo "Setting up readable file..."
    chmod 644 data/system_files/readable.txt 2>/dev/null || true
    
    # Set user_app files to root ownership (simulating the problem)
    echo "Setting up user_app files (simulating ownership problem)..."
    chown root:root projects/user_app/config.txt 2>/dev/null || true
    chmod 644 projects/user_app/config.txt 2>/dev/null || true
    
    chown root:root projects/user_app/install.sh 2>/dev/null || true
    chmod 644 projects/user_app/install.sh 2>/dev/null || true
    
    # System service files should be readable
    echo "Setting up system_service files..."
    chmod 644 projects/system_service/install.sh 2>/dev/null || true
    chmod 644 projects/system_service/service.conf 2>/dev/null || true
    
    # Clue files
    chmod 644 clues/level1/*.txt 2>/dev/null || true
    chmod 644 clues/level2/*.txt 2>/dev/null || true
    chmod 644 clues/level3/*.txt 2>/dev/null || true
    
    # Documentation
    chmod 644 README.md 2>/dev/null || true
    chmod 644 start_here.txt 2>/dev/null || true
    
    # Secrets
    chmod 644 data/secrets/tips.txt 2>/dev/null || true
fi

echo ""
echo -e "${GREEN}✓${NC} Environment setup complete!"
echo ""
echo -e "${BLUE}Note:${NC} Protected files are owned by root to demonstrate"
echo "when sudo is needed. User app files are also root-owned to simulate"
echo "common ownership problems students will learn to fix."
echo ""