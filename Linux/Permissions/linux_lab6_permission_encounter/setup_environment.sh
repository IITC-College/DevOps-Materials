#!/bin/bash
################################################################################
# Setup Environment Script for Lab 6: Permission Encounter
#
# This script prepares the lab environment by setting up file permissions.
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
echo -e "${BLUE}║  Setting up Lab 6: Permission Encounter              ║${NC}"
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

echo -e "${GREEN}[INFO]${NC} Setting up permissions for Permission Encounter Lab..."
echo ""

# Run the existing set_permissions.sh script
if [ -f "set_permissions.sh" ]; then
    echo -e "${GREEN}[STEP]${NC} Running set_permissions.sh..."
    bash set_permissions.sh
else
    echo -e "${YELLOW}[WARN]${NC} set_permissions.sh not found, setting permissions manually..."
    
    # Set permissions for data/files/
    chmod 644 data/files/public_data.txt 2>/dev/null || true
    chmod 664 data/files/team_notes.txt 2>/dev/null || true
    chmod 600 data/files/private_log.txt 2>/dev/null || true
    chmod 666 data/files/shared_report.txt 2>/dev/null || true
    chmod 444 data/files/readonly_archive.txt 2>/dev/null || true
    chmod 600 data/files/private_notes.txt 2>/dev/null || true
    chmod 755 data/files/report.sh 2>/dev/null || true
    
    # Set permissions for other directories
    chmod 644 data/logs/system.log 2>/dev/null || true
    chmod 644 data/secrets/tips.txt 2>/dev/null || true
    chmod 644 clues/level1/*.txt 2>/dev/null || true
    chmod 644 clues/level2/*.txt 2>/dev/null || true
    chmod 644 clues/level3/*.txt 2>/dev/null || true
    chmod 644 README.md 2>/dev/null || true
    chmod 644 start_here.txt 2>/dev/null || true
fi

echo ""
echo -e "${GREEN}✓${NC} Environment setup complete!"
echo ""
echo -e "${BLUE}Note:${NC} This lab works with any user. File ownership will depend"
echo "on who extracts the archive, which is fine for this lab's objectives."
echo ""