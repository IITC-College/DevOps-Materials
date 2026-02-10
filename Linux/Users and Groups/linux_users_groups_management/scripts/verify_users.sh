#!/bin/bash

################################################################################
# Users and Groups Management Lab - Verification Script
################################################################################
# This script helps verify the current state of test users and groups.
# It does NOT require sudo (read-only operations).
#
# Usage: ./verify_users.sh
################################################################################

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Header
echo -e "${BLUE}================================================================================${NC}"
echo -e "${BLUE}       Users and Groups Management Lab - Verification${NC}"
echo -e "${BLUE}================================================================================${NC}"
echo ""

################################################################################
# Check current user
################################################################################
echo -e "${CYAN}YOUR IDENTITY:${NC}"
echo -e "${YELLOW}Current user:${NC} $(whoami)"
echo -e "${YELLOW}User ID:${NC} $(id -u)"
echo -e "${YELLOW}Primary group:${NC} $(id -gn) (GID: $(id -g))"
echo -e "${YELLOW}All groups:${NC} $(groups | tr ' ' ', ')"
echo ""

################################################################################
# Check test users
################################################################################
echo -e "${CYAN}TEST USERS:${NC}"
FOUND_USERS=false
for testuser in testuser1 testuser2 testuser3; do
    if id "$testuser" &>/dev/null; then
        FOUND_USERS=true
        echo -e "${GREEN}✓ $testuser exists${NC}"
        echo -e "  UID: $(id -u $testuser)"
        echo -e "  Primary group: $(id -gn $testuser) (GID: $(id -g $testuser))"
        echo -e "  All groups: $(groups $testuser | cut -d: -f2)"
        echo -e "  Home directory: $(getent passwd $testuser | cut -d: -f6)"
        
        # Check if home directory exists
        HOME_DIR=$(getent passwd $testuser | cut -d: -f6)
        if [ -d "$HOME_DIR" ]; then
            echo -e "  Home status: ${GREEN}exists${NC}"
        else
            echo -e "  Home status: ${RED}does not exist${NC}"
        fi
        
        # Check password status (requires sudo, so skip if not available)
        if sudo -n passwd -S "$testuser" &>/dev/null; then
            PASS_STATUS=$(sudo passwd -S "$testuser" | awk '{print $2}')
            if [ "$PASS_STATUS" = "P" ]; then
                echo -e "  Password: ${GREEN}set${NC}"
            else
                echo -e "  Password: ${YELLOW}not set${NC}"
            fi
        fi
        echo ""
    fi
done

if [ "$FOUND_USERS" = false ]; then
    echo -e "${YELLOW}No test users found${NC}"
    echo -e "${BLUE}Hint: Create users with 'sudo adduser testuser1'${NC}"
fi
echo ""

################################################################################
# Check test groups
################################################################################
echo -e "${CYAN}TEST GROUPS:${NC}"
FOUND_GROUPS=false
for testgroup in developers testers admins; do
    if getent group "$testgroup" &>/dev/null; then
        FOUND_GROUPS=true
        GROUP_INFO=$(getent group "$testgroup")
        GID=$(echo "$GROUP_INFO" | cut -d: -f3)
        MEMBERS=$(echo "$GROUP_INFO" | cut -d: -f4)
        
        echo -e "${GREEN}✓ $testgroup exists${NC}"
        echo -e "  GID: $GID"
        if [ -n "$MEMBERS" ]; then
            echo -e "  Members: $MEMBERS"
        else
            echo -e "  Members: ${YELLOW}(none)${NC}"
        fi
        echo ""
    fi
done

if [ "$FOUND_GROUPS" = false ]; then
    echo -e "${YELLOW}No test groups found${NC}"
    echo -e "${BLUE}Hint: Create groups with 'sudo groupadd developers'${NC}"
fi
echo ""

################################################################################
# Summary
################################################################################
echo -e "${CYAN}SUMMARY:${NC}"
USER_COUNT=$(getent passwd | grep -c -E 'testuser' || true)
GROUP_COUNT=$(getent group | grep -c -E 'developers|testers|admins' || true)
echo -e "Test users: $USER_COUNT"
echo -e "Test groups: $GROUP_COUNT"
echo ""

################################################################################
# Quick reference
################################################################################
echo -e "${CYAN}QUICK REFERENCE:${NC}"
echo -e "Check user:        ${BLUE}id username${NC}"
echo -e "Check groups:      ${BLUE}groups username${NC}"
echo -e "View all users:    ${BLUE}getent passwd | grep testuser${NC}"
echo -e "View all groups:   ${BLUE}getent group | grep -E 'developers|testers|admins'${NC}"
echo -e "Password status:   ${BLUE}sudo passwd -S username${NC}"
echo ""
