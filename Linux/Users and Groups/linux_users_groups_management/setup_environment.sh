#!/bin/bash

################################################################################
# Users and Groups Management Lab - Setup Script
################################################################################
# This script prepares the lab environment for students.
# It must be run with sudo privileges.
#
# Usage: sudo ./setup_environment.sh
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Header
echo -e "${BLUE}================================================================================${NC}"
echo -e "${BLUE}       Users and Groups Management Lab - Environment Setup${NC}"
echo -e "${BLUE}================================================================================${NC}"
echo ""

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}ERROR: This script must be run with sudo!${NC}"
    echo "Usage: sudo ./setup_environment.sh"
    exit 1
fi

# Identify the student user (who ran sudo)
STUDENT_USER="${SUDO_USER:-$USER}"
if [ -z "$STUDENT_USER" ] || [ "$STUDENT_USER" = "root" ]; then
    echo -e "${RED}ERROR: Could not identify student user!${NC}"
    echo "Please run this script with: sudo ./setup_environment.sh"
    exit 1
fi

echo -e "${GREEN}✓ Running as root${NC}"
echo -e "${GREEN}✓ Student user identified: $STUDENT_USER${NC}"
echo ""

# Lab directory
LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo -e "Lab directory: ${BLUE}$LAB_DIR${NC}"
echo ""

################################################################################
# Create directory structure if missing
################################################################################
echo -e "${YELLOW}Setting up directory structure...${NC}"

mkdir -p "$LAB_DIR/clues/level1"
mkdir -p "$LAB_DIR/clues/level2"
mkdir -p "$LAB_DIR/clues/level3"
mkdir -p "$LAB_DIR/data/secrets"
mkdir -p "$LAB_DIR/scripts"
mkdir -p "$LAB_DIR/.answers"

echo -e "${GREEN}✓ Directory structure created${NC}"
echo ""

################################################################################
# Verify sudo permissions for student
################################################################################
echo -e "${YELLOW}Verifying sudo permissions for $STUDENT_USER...${NC}"

if sudo -u "$STUDENT_USER" sudo -n true 2>/dev/null; then
    echo -e "${GREEN}✓ Student has sudo permissions${NC}"
else
    echo -e "${YELLOW}⚠ Student may need to enter password for sudo commands${NC}"
    echo -e "${YELLOW}  This is normal and expected.${NC}"
fi
echo ""

################################################################################
# Clean up any existing test users and groups from previous runs
################################################################################
echo -e "${YELLOW}Cleaning up any previous test users and groups...${NC}"

# Remove test users if they exist
for testuser in testuser1 testuser2 testuser3; do
    if id "$testuser" &>/dev/null; then
        echo -e "  Removing existing user: $testuser"
        deluser --remove-home "$testuser" 2>/dev/null || true
    fi
done

# Remove test groups if they exist
for testgroup in developers testers admins; do
    if getent group "$testgroup" &>/dev/null; then
        echo -e "  Removing existing group: $testgroup"
        groupdel "$testgroup" 2>/dev/null || true
    fi
done

echo -e "${GREEN}✓ Cleanup complete${NC}"
echo ""

################################################################################
# Set permissions on lab files
################################################################################
echo -e "${YELLOW}Setting permissions on lab files...${NC}"

# Make student owner of lab directory
chown -R "$STUDENT_USER:$STUDENT_USER" "$LAB_DIR"

# Protect answers directory
if [ -d "$LAB_DIR/.answers" ]; then
    chmod 700 "$LAB_DIR/.answers"
    chmod 600 "$LAB_DIR/.answers"/* 2>/dev/null || true
fi

# Make scripts executable
if [ -d "$LAB_DIR/scripts" ]; then
    chmod +x "$LAB_DIR/scripts"/*.sh 2>/dev/null || true
fi

# Make setup script executable
chmod +x "$LAB_DIR/setup_environment.sh" 2>/dev/null || true

echo -e "${GREEN}✓ Permissions set${NC}"
echo ""

################################################################################
# Create tips file if missing
################################################################################
if [ ! -f "$LAB_DIR/data/secrets/tips.txt" ]; then
    echo -e "${YELLOW}Creating tips file...${NC}"
    cat > "$LAB_DIR/data/secrets/tips.txt" << 'EOF'
================================================================================
                        LAB TIPS AND HINTS
================================================================================

LEVEL 1 TIPS:
-------------
Tip 1.1: adduser is interactive and creates home directory automatically.
         useradd is basic and requires manual configuration.

Tip 1.2: Use 'id username' to see UID, GID, and all group memberships.
         Use 'groups username' to see just the group names.

Tip 1.3: getent passwd queries the user database.
         Format: username:x:UID:GID:comment:home:shell

LEVEL 2 TIPS:
-------------
Tip 2.1: Groups are created with 'groupadd groupname'.
         View with 'getent group groupname'.

Tip 2.2: CRITICAL: Always use -aG to add to groups, never -G alone!
         -aG appends (safe), -G replaces all groups (dangerous!)

Tip 2.3: Passwords are stored encrypted in /etc/shadow.
         Use 'passwd -S' to check password status.

LEVEL 3 TIPS:
-------------
Tip 3.1: usermod -G without -a replaces ALL secondary groups!
         This can break sudo access - very dangerous!

Tip 3.2: deluser removes user, --remove-home removes user AND files.
         Always verify before deleting: id username, ls -la /home/username

Tip 3.3: Cannot delete a group if it's a user's primary group.
         Delete the user first, or change their primary group.

COMMON MISTAKES:
----------------
- Using useradd and wondering where the home directory is
- Using -G instead of -aG and losing all groups
- Trying to delete a primary group while user still uses it
- Deleting users without checking their files first
- Forgetting to verify changes with id/groups/getent

VERIFICATION COMMANDS:
----------------------
After creating user:       id username, getent passwd username
After adding to group:     groups username, getent group groupname
After changing password:   sudo passwd -S username
After deleting user:       id username (should fail), ls -la /home
After deleting group:      getent group groupname (should be empty)

REMEMBER:
---------
- Always verify before deleting
- Use -aG not -G
- Back up before permanent deletion
- Test in lab before production!

Good luck!
EOF
    chown "$STUDENT_USER:$STUDENT_USER" "$LAB_DIR/data/secrets/tips.txt"
    echo -e "${GREEN}✓ Tips file created${NC}"
else
    echo -e "${GREEN}✓ Tips file already exists${NC}"
fi
echo ""

################################################################################
# Create .gitignore if missing
################################################################################
if [ ! -f "$LAB_DIR/.gitignore" ]; then
    echo -e "${YELLOW}Creating .gitignore...${NC}"
    cat > "$LAB_DIR/.gitignore" << 'EOF'
# Student answers - should not be committed
my_answers.txt

# Temporary files
*.tmp
*.swp
*~
.*.swp

# Backup files
*.bak
*_backup

# OS-specific files
.DS_Store
Thumbs.db
EOF
    chown "$STUDENT_USER:$STUDENT_USER" "$LAB_DIR/.gitignore"
    echo -e "${GREEN}✓ .gitignore created${NC}"
else
    echo -e "${GREEN}✓ .gitignore already exists${NC}"
fi
echo ""

################################################################################
# Final setup complete
################################################################################
echo -e "${BLUE}================================================================================${NC}"
echo -e "${GREEN}✓ Lab environment setup complete!${NC}"
echo -e "${BLUE}================================================================================${NC}"
echo ""
echo -e "${YELLOW}IMPORTANT INFORMATION FOR STUDENTS:${NC}"
echo ""
echo -e "1. ${GREEN}Start the lab${NC} by reading:"
echo -e "   ${BLUE}cat start_here.txt${NC}"
echo ""
echo -e "2. ${GREEN}Navigate to exercises${NC}:"
echo -e "   ${BLUE}cd clues/level1${NC}"
echo -e "   ${BLUE}cat clue1.txt${NC}"
echo ""
echo -e "3. ${GREEN}All user/group commands require sudo${NC}"
echo -e "   Example: ${BLUE}sudo adduser testuser1${NC}"
echo ""
echo -e "4. ${GREEN}Work only with test users${NC} (testuser1, testuser2, etc.)"
echo -e "   ${RED}Never modify system users!${NC}"
echo ""
echo -e "5. ${GREEN}Verify all changes${NC} using:"
echo -e "   ${BLUE}id username${NC}, ${BLUE}groups username${NC}, ${BLUE}getent passwd username${NC}"
echo ""
echo -e "6. ${GREEN}Save answers${NC} in: ${BLUE}my_answers.txt${NC}"
echo ""
echo -e "7. ${GREEN}Get hints${NC} if stuck: ${BLUE}cat data/secrets/tips.txt${NC}"
echo ""
echo -e "${YELLOW}KEY SAFETY REMINDER:${NC}"
echo -e "  ${RED}⚠  ALWAYS use -aG to add to groups, NOT -G alone!${NC}"
echo -e "  ${RED}⚠  Verify before deleting users or groups!${NC}"
echo -e "  ${RED}⚠  Only work with test users created in this lab!${NC}"
echo ""
echo -e "${GREEN}Good luck with the lab!${NC}"
echo ""
