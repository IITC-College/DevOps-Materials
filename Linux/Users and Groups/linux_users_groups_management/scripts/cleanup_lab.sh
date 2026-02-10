#!/bin/bash

################################################################################
# Users and Groups Management Lab - Cleanup Script
################################################################################
# This script cleans up all test users and groups created during the lab.
# It must be run with sudo privileges.
#
# Usage: sudo ./cleanup_lab.sh
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
echo -e "${BLUE}       Users and Groups Management Lab - Cleanup${NC}"
echo -e "${BLUE}================================================================================${NC}"
echo ""

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}ERROR: This script must be run with sudo!${NC}"
    echo "Usage: sudo ./cleanup_lab.sh"
    exit 1
fi

echo -e "${YELLOW}This will remove all test users and groups created during the lab.${NC}"
echo -e "${YELLOW}Press Ctrl+C to cancel, or Enter to continue...${NC}"
read

echo ""
echo -e "${YELLOW}Cleaning up test users...${NC}"

# Remove test users if they exist
USERS_REMOVED=0
for testuser in testuser1 testuser2 testuser3; do
    if id "$testuser" &>/dev/null; then
        echo -e "  ${GREEN}Removing user:${NC} $testuser"
        deluser --remove-home "$testuser" 2>/dev/null || true
        USERS_REMOVED=$((USERS_REMOVED + 1))
    fi
done

if [ $USERS_REMOVED -eq 0 ]; then
    echo -e "  ${BLUE}No test users found${NC}"
else
    echo -e "  ${GREEN}✓ Removed $USERS_REMOVED test user(s)${NC}"
fi

echo ""
echo -e "${YELLOW}Cleaning up test groups...${NC}"

# Remove test groups if they exist
GROUPS_REMOVED=0
for testgroup in developers testers admins; do
    if getent group "$testgroup" &>/dev/null; then
        echo -e "  ${GREEN}Removing group:${NC} $testgroup"
        groupdel "$testgroup" 2>/dev/null || true
        GROUPS_REMOVED=$((GROUPS_REMOVED + 1))
    fi
done

if [ $GROUPS_REMOVED -eq 0 ]; then
    echo -e "  ${BLUE}No test groups found${NC}"
else
    echo -e "  ${GREEN}✓ Removed $GROUPS_REMOVED test group(s)${NC}"
fi

echo ""
echo -e "${YELLOW}Verifying cleanup...${NC}"

# Verify users are gone
REMAINING_USERS=$(getent passwd | grep -E 'testuser' | wc -l)
if [ $REMAINING_USERS -eq 0 ]; then
    echo -e "  ${GREEN}✓ No test users remaining${NC}"
else
    echo -e "  ${YELLOW}⚠ Warning: Some test users still exist${NC}"
    getent passwd | grep -E 'testuser'
fi

# Verify groups are gone
REMAINING_GROUPS=$(getent group | grep -E 'developers|testers|admins' | wc -l)
if [ $REMAINING_GROUPS -eq 0 ]; then
    echo -e "  ${GREEN}✓ No test groups remaining${NC}"
else
    echo -e "  ${YELLOW}⚠ Warning: Some test groups still exist${NC}"
    getent group | grep -E 'developers|testers|admins'
fi

echo ""
echo -e "${BLUE}================================================================================${NC}"
echo -e "${GREEN}✓ Cleanup complete!${NC}"
echo -e "${BLUE}================================================================================${NC}"
echo ""
