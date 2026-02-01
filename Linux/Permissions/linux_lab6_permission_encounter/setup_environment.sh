#!/bin/bash
################################################################################
# Lab 6: Permission Encounter - Unified Setup Script
#
# Creates the full lab structure (if missing), creates lab users and groups,
# sets all file/directory permissions, and assigns ownership so students see
# different users and groups in ls -l (alice, bob, charlie; developers,
# team_dev, shared_group). Students run as their own user and encounter
# permission denied on files owned by others or with restricted permissions.
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
echo -e "${BLUE}║  Lab 6: Permission Encounter - Setup                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}This script must be run with sudo.${NC}"
    echo "  sudo ./setup_environment.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${GREEN}[1/5] Creating lab users and groups...${NC}"
# Groups: developers (alice, bob), team_dev (alice, bob), shared_group (alice, bob, charlie)
for grp in developers team_dev shared_group; do
    getent group "$grp" >/dev/null 2>&1 || groupadd "$grp"
done
# Users: alice (developers, team_dev, shared_group), bob (same), charlie (shared_group only)
for user in alice bob charlie; do
    if ! getent passwd "$user" >/dev/null 2>&1; then
        case "$user" in
            charlie) useradd -m -s /bin/bash -G shared_group "$user" ;;
            *)       useradd -m -s /bin/bash -G developers,team_dev,shared_group "$user" ;;
        esac
        passwd -l "$user" >/dev/null 2>&1 || true
    else
        case "$user" in
            charlie) usermod -aG shared_group charlie 2>/dev/null || true ;;
            *)       usermod -aG developers,team_dev,shared_group "$user" 2>/dev/null || true ;;
        esac
    fi
done

echo -e "${GREEN}[2/5] Creating directory structure...${NC}"
mkdir -p data/files data/logs data/secrets
mkdir -p clues/level1 clues/level2 clues/level3
mkdir -p projects/personal_project projects/shared_project projects/team_project
mkdir -p restricted
mkdir -p .answers

echo -e "${GREEN}[3/5] Ensuring all lab files exist (touch if missing)...${NC}"
# data/
touch data/files/public_data.txt data/files/team_notes.txt data/files/private_log.txt
touch data/files/shared_report.txt data/files/readonly_archive.txt data/files/private_notes.txt
touch data/files/report.sh
touch data/logs/system.log
touch data/secrets/tips.txt
# clues
touch clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
touch clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
touch clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt
# projects
touch projects/personal_project/my_notes.txt projects/personal_project/my_script.sh
touch projects/personal_project/README.md
touch projects/shared_project/shared_doc.txt
touch projects/team_project/config.json projects/team_project/logs.txt projects/team_project/team_script.sh
# restricted
touch restricted/admin_config.txt restricted/secret_file.txt restricted/backup.tar.gz
# root
touch README.md start_here.txt
touch .answers/solutions.txt 2>/dev/null || true

echo -e "${GREEN}[4/5] Setting directory permissions and ownership...${NC}"
chmod 755 data data/files data/logs data/secrets
chmod 755 clues clues/level1 clues/level2 clues/level3
chmod 755 projects projects/personal_project projects/shared_project projects/team_project
chmod 755 restricted
chmod 755 .answers 2>/dev/null || true

echo -e "${GREEN}[5/5] Setting file permissions and ownership for all lab parts...${NC}"

# --- Ownership on key dirs so ls -l shows different owners/groups ---
chown alice:developers data/files
chown alice:developers data/logs
chown bob:shared_group data/secrets

# --- data/files/ (Level 1 & 2: mixed owners/groups so ls -l shows variety) ---
chmod 644 data/files/public_data.txt      # rw-r--r--
chown alice:developers data/files/public_data.txt
chmod 664 data/files/team_notes.txt       # rw-rw-r--
chown alice:team_dev data/files/team_notes.txt
chmod 600 data/files/private_log.txt     # rw-------
chown alice:alice data/files/private_log.txt
chmod 666 data/files/shared_report.txt   # rw-rw-rw-
chown bob:shared_group data/files/shared_report.txt
chmod 444 data/files/readonly_archive.txt # r--r--r--
chown root:root data/files/readonly_archive.txt
chmod 600 data/files/private_notes.txt   # rw-------
chown bob:bob data/files/private_notes.txt
chmod 755 data/files/report.sh           # rwxr-xr-x
chown alice:developers data/files/report.sh

# --- data/logs/ and data/secrets/ (Level 3) ---
chmod 644 data/logs/system.log
chown alice:developers data/logs/system.log
chmod 644 data/secrets/tips.txt
chown bob:shared_group data/secrets/tips.txt

# --- projects/personal_project/ (alice's; Level 2) ---
chmod 700 projects/personal_project/my_script.sh
chmod 600 projects/personal_project/my_notes.txt
chmod 644 projects/personal_project/README.md
chown -R alice:developers projects/personal_project

# --- projects/team_project/ (bob's, group developers) ---
chmod 770 projects/team_project/team_script.sh
chmod 660 projects/team_project/config.json
chmod 664 projects/team_project/logs.txt
chown -R bob:developers projects/team_project

# --- projects/shared_project/ (shared_group) ---
chmod 664 projects/shared_project/shared_doc.txt
chown charlie:shared_group projects/shared_project/shared_doc.txt
chown root:root projects projects/shared_project

# --- restricted/ (root-only; Level 2 & 3) ---
chmod 600 restricted/admin_config.txt
chmod 400 restricted/secret_file.txt
chmod 600 restricted/backup.tar.gz
chown -R root:root restricted

# --- clues (all readable) ---
chmod 644 clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
chmod 644 clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
chmod 644 clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt

# --- documentation ---
chmod 644 README.md start_here.txt

# --- instructor answers (readable by instructor) ---
[ -f .answers/solutions.txt ] && chmod 644 .answers/solutions.txt

echo ""
echo -e "${GREEN}✓ Setup complete.${NC}"
echo ""
echo -e "${BLUE}Summary:${NC}"
echo "  - Users created: alice, bob, charlie (passwords locked; for ownership only)"
echo "  - Groups created: developers, team_dev, shared_group"
echo "  - data/files and projects show mixed owners (alice, bob, charlie, root) and groups"
echo "  - restricted/ owned by root so students get 'Permission denied'"
echo "  - Students run as their own user and see different users/groups in ls -l"
echo ""
