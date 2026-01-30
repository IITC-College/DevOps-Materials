#!/bin/bash
################################################################################
# Setup Script for Debug Mindset Lab
# 
# This script creates deliberately broken scenarios for students to debug.
# It sets up files and directories with wrong permissions, ownership, etc.
#
# Usage: Run this script from the lab root directory
#        ./set_permissions.sh
################################################################################

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up broken scenarios for Debug Mindset Lab...${NC}"
echo ""

# Get current user (for ownership fixes later)
CURRENT_USER=$(whoami)

# Scenario 1: Remove read permission
echo -e "${GREEN}Setting up Scenario 1: Read failure...${NC}"
chmod 000 broken_scenarios/scenario1_read_failure/secret.txt
echo "  - secret.txt: permissions set to 000 (no access)"

# Scenario 2: Remove execute permission from script
echo -e "${GREEN}Setting up Scenario 2: Script won't execute...${NC}"
chmod -x broken_scenarios/scenario2_script_broken/deploy.sh
echo "  - deploy.sh: execute permission removed"

# Scenario 3: Remove write permission from directory
echo -e "${GREEN}Setting up Scenario 3: Can't write to directory...${NC}"
chmod 555 broken_scenarios/scenario3_cant_write/
echo "  - directory: write permission removed (555 = r-xr-xr-x)"

# Scenario 4: Change ownership to root (if running as root, use a different approach)
echo -e "${GREEN}Setting up Scenario 4: Ownership mismatch...${NC}"
if [ "$CURRENT_USER" != "root" ]; then
    # Try to change ownership to root (requires sudo, but we'll note it)
    echo "  - important.txt: will be owned by root (requires sudo to fix)"
    # Note: Actual chown to root requires sudo, so we'll set restrictive permissions instead
    chmod 600 broken_scenarios/scenario4_ownership_mess/important.txt
    # In a real scenario, this would be: sudo chown root:root important.txt
    # For lab purposes, we'll use a different user or note it requires sudo
else
    chmod 600 broken_scenarios/scenario4_ownership_mess/important.txt
    echo "  - important.txt: restrictive permissions set"
fi

# Scenario 5: Hidden file with wrong permissions (already hidden, just need to break access)
echo -e "${GREEN}Setting up Scenario 5: Hidden file access...${NC}"
chmod 000 broken_scenarios/scenario5_lost_path/.config
echo "  - .config: permissions set to 000 (hidden file, no access)"

# Scenario 6: Multiple issues
echo -e "${GREEN}Setting up Scenario 6: Mixed issues...${NC}"

# Issue 1: Script missing execute permission
chmod -x broken_scenarios/scenario6_mixed_issues/run_backup.sh
echo "  - run_backup.sh: execute permission removed"

# Issue 2: File owned by root (simulated with restrictive permissions)
chmod 600 broken_scenarios/scenario6_mixed_issues/data.txt
if [ "$CURRENT_USER" != "root" ]; then
    echo "  - data.txt: restrictive permissions (simulates root ownership)"
fi

# Issue 3: Directory missing write permission
chmod 444 broken_scenarios/scenario6_mixed_issues/
echo "  - directory: write permission removed"

# Issue 4: Nested directories missing execute permission
chmod 644 broken_scenarios/scenario6_mixed_issues/deep/
chmod 644 broken_scenarios/scenario6_mixed_issues/deep/nested/
chmod 644 broken_scenarios/scenario6_mixed_issues/deep/nested/path/
echo "  - deep/, deep/nested/, deep/nested/path/: execute permission removed"

# Issue 5: README.md might have wrong permissions too
chmod 000 broken_scenarios/scenario6_mixed_issues/README.md
echo "  - README.md: permissions set to 000"

echo ""
echo -e "${BLUE}All broken scenarios have been set up!${NC}"
echo ""
echo "Students will need to use the 4-step methodology to fix:"
echo "  - Permission problems"
echo "  - Ownership problems"
echo "  - Path problems"
echo "  - Hidden file problems"
echo "  - Multiple combined issues"
echo ""
echo "Note: Some scenarios may require sudo to fix ownership issues."
echo "      This is intentional and part of the learning process."
