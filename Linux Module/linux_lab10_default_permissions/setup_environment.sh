#!/bin/bash
################################################################################
# Setup Environment Script for Lab 10: Default Permissions (umask)
#
# This script prepares the lab environment by setting up example files
# with permissions that match different umask values.
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
echo -e "${BLUE}║  Setting up Lab 10: Default Permissions (umask)     ║${NC}"
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

echo -e "${GREEN}[INFO]${NC} Setting up permissions for Default Permissions Lab..."
echo ""

################################################################################
# Set up example files with permissions matching different umask values
################################################################################

echo -e "${GREEN}[STEP]${NC} Setting up example files with different umask permissions..."

# umask 022: Files get 644 (666 - 022 = 644), Directories get 755 (777 - 022 = 755)
if [ -f "data/examples/umask_022/example_file.txt" ]; then
    chmod 644 data/examples/umask_022/example_file.txt
    echo -e "  ${GREEN}✓${NC} umask_022/example_file.txt → 644 (rw-r--r--)"
fi

# umask 027: Files get 640 (666 - 027 = 640), Directories get 750 (777 - 027 = 750)
if [ -f "data/examples/umask_027/example_file.txt" ]; then
    chmod 640 data/examples/umask_027/example_file.txt
    echo -e "  ${GREEN}✓${NC} umask_027/example_file.txt → 640 (rw-r-----)"
fi

# umask 077: Files get 600 (666 - 077 = 600), Directories get 700 (777 - 077 = 700)
if [ -f "data/examples/umask_077/example_file.txt" ]; then
    chmod 600 data/examples/umask_077/example_file.txt
    echo -e "  ${GREEN}✓${NC} umask_077/example_file.txt → 600 (rw-------)"
fi

# Set permissions for directories to match umask values
if [ -d "data/examples/umask_022" ]; then
    chmod 755 data/examples/umask_022
fi
if [ -d "data/examples/umask_027" ]; then
    chmod 750 data/examples/umask_027
fi
if [ -d "data/examples/umask_077" ]; then
    chmod 700 data/examples/umask_077
fi

################################################################################
# Set permissions for other files
################################################################################

echo -e "${GREEN}[STEP]${NC} Setting permissions for other files..."

# Clue files (all readable)
find clues -type f -name "*.txt" -exec chmod 644 {} \; 2>/dev/null || true

# Documentation
chmod 644 README.md 2>/dev/null || true
chmod 644 start_here.txt 2>/dev/null || true

# Data files
find data -type f -name "*.log" -exec chmod 644 {} \; 2>/dev/null || true
find data -type f -name "*.txt" -exec chmod 644 {} \; 2>/dev/null || true

# Projects directories
find projects -type f -exec chmod 644 {} \; 2>/dev/null || true

# Secrets
if [ -f "data/secrets/tips.txt" ]; then
    chmod 644 data/secrets/tips.txt
fi

# Answers
if [ -f ".answers/solutions.txt" ]; then
    chmod 644 .answers/solutions.txt
fi

echo ""
echo -e "${GREEN}✓${NC} Environment setup complete!"
echo ""
echo -e "${BLUE}Note:${NC} Example files have been set with permissions that match"
echo "what would be created with different umask values:"
echo "  • umask 022 → 644 (rw-r--r--)"
echo "  • umask 027 → 640 (rw-r-----)"
echo "  • umask 077 → 600 (rw-------)"
echo ""
echo "Students will learn to understand and modify umask values."
echo ""