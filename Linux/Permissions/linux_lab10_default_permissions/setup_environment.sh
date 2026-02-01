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
# Step 0: Create directory structure and ensure lab files exist (if missing)
################################################################################

echo -e "${GREEN}[STEP 0]${NC} Creating directory structure and ensuring lab files exist..."

mkdir -p data/examples/umask_022 data/examples/umask_027 data/examples/umask_077
mkdir -p data/logs data/secrets
mkdir -p clues/level1 clues/level2 clues/level3
mkdir -p projects/default_app projects/secure_files projects/shared_team
mkdir -p .answers

touch data/examples/umask_022/example_file.txt data/examples/umask_027/example_file.txt data/examples/umask_077/example_file.txt
touch data/logs/permissions_history.log data/secrets/tips.txt
touch clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
touch clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
touch clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt
touch projects/default_app/index.html projects/default_app/README.md
touch projects/secure_files/config.txt projects/secure_files/README.md
touch projects/shared_team/project_plan.md projects/shared_team/README.md
touch README.md start_here.txt
touch .answers/solutions.txt 2>/dev/null || true

echo -e "  ${GREEN}✓${NC} Directories and files ready"

################################################################################
# Set permissions for other files (do this FIRST so we don't overwrite examples)
################################################################################

echo -e "${GREEN}[STEP]${NC} Setting permissions for other files..."

# Clue files (all readable)
find clues -type f -name "*.txt" -exec chmod 644 {} \; 2>/dev/null || true

# Documentation
chmod 644 README.md 2>/dev/null || true
chmod 644 start_here.txt 2>/dev/null || true

# Data files (logs, secrets) - do NOT include data/examples yet
find data/logs -type f -name "*.log" -exec chmod 644 {} \; 2>/dev/null || true
find data/secrets -type f -name "*.txt" -exec chmod 644 {} \; 2>/dev/null || true

# Projects directories
find projects -type f -exec chmod 644 {} \; 2>/dev/null || true

# Answers
if [ -f ".answers/solutions.txt" ]; then
    chmod 644 .answers/solutions.txt
fi

################################################################################
# Set up example files with permissions matching different umask values
# (Must run AFTER other data chmods so these values are not overwritten)
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