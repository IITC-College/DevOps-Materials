#!/bin/bash
################################################################################
# Lab 7: Why Script Doesn't Run - Unified Setup Script
#
# Creates the full lab structure (if missing), sets all file/directory
# permissions so that:
# - scripts/broken/ and projects/* scripts have NO execute (students fix them)
# - scripts/fixed/ have execute as examples
# - data/configs and data/logs have no execute (config/data files)
#
# Run as root (sudo) before students start the lab.
#
# Usage: sudo ./setup_environment.sh
################################################################################

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Lab 7: Why Script Doesn't Run - Setup                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}This script must be run with sudo.${NC}"
    echo "  sudo ./setup_environment.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${GREEN}[1/4] Creating directory structure...${NC}"
mkdir -p scripts/broken scripts/fixed
mkdir -p projects/web_app projects/automation
mkdir -p data/configs data/logs
mkdir -p clues/level1 clues/level2 clues/level3
mkdir -p .answers

echo -e "${GREEN}[2/4] Ensuring all lab files exist (touch if missing)...${NC}"
# scripts/broken (Level 1 & 2)
touch scripts/broken/hello.sh scripts/broken/backup.sh scripts/broken/deploy.sh
touch scripts/broken/cleanup.sh scripts/broken/private_script.sh
touch scripts/broken/team_script.sh scripts/broken/shared_tool.sh
# scripts/fixed (Level 1 - same scripts as broken but with execute; private_script for clue 3 comparison)
touch scripts/fixed/private_script.sh scripts/fixed/hello.sh scripts/fixed/example.sh scripts/fixed/reference.sh
# projects/web_app (Level 3)
touch projects/web_app/start.sh projects/web_app/stop.sh
touch projects/web_app/deploy.sh projects/web_app/config.sh
# projects/automation (Level 3)
touch projects/automation/daily_backup.sh projects/automation/weekly_report.sh
touch projects/automation/cleanup_old_files.sh
# data (Level 3 - configs and logs, no execute)
touch data/configs/app.conf data/configs/settings.json
touch data/logs/system.log
# clues
touch clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
touch clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
touch clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt
# root
touch README.md start_here.txt
touch .answers/solutions.txt 2>/dev/null || true

echo -e "${GREEN}[3/4] Setting directory permissions (755)...${NC}"
chmod 755 scripts scripts/broken scripts/fixed
chmod 755 projects projects/web_app projects/automation
chmod 755 data data/configs data/logs
chmod 755 clues clues/level1 clues/level2 clues/level3
chmod 755 .answers 2>/dev/null || true

echo -e "${GREEN}[4/4] Setting file permissions for all lab parts...${NC}"

# --- scripts/broken/ (NO execute - students add x per clues) ---
# Level 1: hello.sh, backup.sh, deploy.sh, cleanup.sh
chmod 644 scripts/broken/hello.sh          # rw-r--r-- (no x)
chmod 644 scripts/broken/backup.sh        # rw-r--r-- (no x)
chmod 644 scripts/broken/deploy.sh        # rw-r--r-- (no x)
chmod 600 scripts/broken/cleanup.sh        # rw------- (no x)
# Level 2: private_script.sh (u+x), team_script.sh, shared_tool.sh (g+x)
chmod 600 scripts/broken/private_script.sh # rw------- (no x)
chmod 664 scripts/broken/team_script.sh   # rw-rw-r-- (no x)
chmod 664 scripts/broken/shared_tool.sh   # rw-rw-r-- (no x)

# --- scripts/fixed/ (WITH execute - same scripts as broken, correct permissions) ---
chmod 755 scripts/fixed/private_script.sh  # rwxr-xr-x (for clue 3: compare with broken - not fixed in clue 1/2)
chmod 755 scripts/fixed/hello.sh          # rwxr-xr-x
chmod 755 scripts/fixed/example.sh         # rwxr-xr-x
chmod 755 scripts/fixed/reference.sh       # rwxr-xr-x

# --- projects/web_app/ (Level 3 - NO execute, students fix) ---
chmod 644 projects/web_app/start.sh       # rw-r--r-- (no x)
chmod 644 projects/web_app/stop.sh        # rw-r--r-- (no x)
chmod 664 projects/web_app/deploy.sh      # rw-rw-r-- (no x)
chmod 600 projects/web_app/config.sh      # rw------- (config file, NOT executable)

# --- projects/automation/ (Level 3 - NO execute, students fix) ---
chmod 644 projects/automation/daily_backup.sh     # rw-r--r-- (no x)
chmod 644 projects/automation/weekly_report.sh   # rw-r--r-- (no x)
chmod 600 projects/automation/cleanup_old_files.sh # rw------- (no x)

# --- data/configs/ and data/logs/ (Level 3 - config/data, no x) ---
chmod 644 data/configs/app.conf            # rw-r--r--
chmod 644 data/configs/settings.json       # rw-r--r--
chmod 644 data/logs/system.log             # rw-r--r--

# --- clues (readable) ---
chmod 644 clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
chmod 644 clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
chmod 644 clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt

# --- documentation ---
chmod 644 README.md start_here.txt

# --- instructor answers ---
[ -f .answers/solutions.txt ] && chmod 644 .answers/solutions.txt

echo ""
echo -e "${GREEN}✓ Setup complete.${NC}"
echo ""
echo -e "${BLUE}Summary:${NC}"
echo "  - scripts/broken/ and projects/*: scripts have NO execute (students add with chmod)"
echo "  - scripts/fixed/: private_script.sh, hello.sh, example.sh, reference.sh have execute (for L1 clue 3 compare; private_script left unfixed in broken until L2 clue 1)"
echo "  - data/configs and data/logs: no execute (correct for config/data files)"
echo "  - All directories 755; all clue and doc files 644"
echo ""
