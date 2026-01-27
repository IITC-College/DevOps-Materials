#!/bin/bash
################################################################################
# Setup Environment Script for Lab 7: Why Script Doesn't Run
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
echo -e "${BLUE}║  Setting up Lab 7: Why Script Doesn't Run            ║${NC}"
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

echo -e "${GREEN}[INFO]${NC} Setting up permissions for Why Script Doesn't Run Lab..."
echo ""

# Run the existing set_permissions.sh script
if [ -f "set_permissions.sh" ]; then
    echo -e "${GREEN}[STEP]${NC} Running set_permissions.sh..."
    bash set_permissions.sh
else
    echo -e "${YELLOW}[WARN]${NC} set_permissions.sh not found, setting permissions manually..."
    
    # Set permissions for scripts/broken/ (NO execute - these are broken!)
    chmod 644 scripts/broken/hello.sh 2>/dev/null || true
    chmod 644 scripts/broken/backup.sh 2>/dev/null || true
    chmod 644 scripts/broken/deploy.sh 2>/dev/null || true
    chmod 600 scripts/broken/cleanup.sh 2>/dev/null || true
    chmod 600 scripts/broken/private_script.sh 2>/dev/null || true
    chmod 664 scripts/broken/team_script.sh 2>/dev/null || true
    chmod 664 scripts/broken/shared_tool.sh 2>/dev/null || true
    
    # Set permissions for scripts/fixed/ (WITH execute - these are examples)
    chmod 755 scripts/fixed/example.sh 2>/dev/null || true
    chmod 755 scripts/fixed/reference.sh 2>/dev/null || true
    
    # Set permissions for projects/web_app/ (NO execute - broken scripts)
    chmod 644 projects/web_app/start.sh 2>/dev/null || true
    chmod 644 projects/web_app/stop.sh 2>/dev/null || true
    chmod 664 projects/web_app/deploy.sh 2>/dev/null || true
    chmod 600 projects/web_app/config.sh 2>/dev/null || true
    
    # Set permissions for projects/automation/ (NO execute - broken scripts)
    chmod 644 projects/automation/daily_backup.sh 2>/dev/null || true
    chmod 644 projects/automation/weekly_report.sh 2>/dev/null || true
    chmod 600 projects/automation/cleanup_old_files.sh 2>/dev/null || true
    
    # Set permissions for data/configs/ and data/logs/
    chmod 644 data/configs/app.conf 2>/dev/null || true
    chmod 644 data/configs/settings.json 2>/dev/null || true
    chmod 644 data/logs/system.log 2>/dev/null || true
    
    # Set permissions for clue files
    chmod 644 clues/level1/*.txt 2>/dev/null || true
    chmod 644 clues/level2/*.txt 2>/dev/null || true
    chmod 644 clues/level3/*.txt 2>/dev/null || true
    
    # Set permissions for documentation
    chmod 644 README.md 2>/dev/null || true
    chmod 644 start_here.txt 2>/dev/null || true
fi

echo ""
echo -e "${GREEN}✓${NC} Environment setup complete!"
echo ""
echo -e "${BLUE}Note:${NC} Scripts in scripts/broken/ and projects/ do NOT have execute"
echo "permission - students will add it during the lab."
echo "Scripts in scripts/fixed/ have execute permission as examples."
echo ""