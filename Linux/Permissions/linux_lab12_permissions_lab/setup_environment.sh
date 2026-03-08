#!/bin/bash
################################################################################
# Lab 12: Permissions Lab - Setup Script
#
# Creates users (intern, developer, manager), groups (engineering, marketing,
# devops), and sets INTENTIONALLY WRONG permissions and ownership on the
# existing lab files. Students must fix access issues using chmod, chown,
# and group management commands.
#
# The files and directory structure are already part of the lab.
# This script only creates system users/groups and applies broken permissions.
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
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Lab 12: Permissions Lab - Setup                      ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}This script must be run with sudo.${NC}"
    echo "  sudo ./setup_environment.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Detect the student user (whoever ran sudo)
STUDENT_USER="${SUDO_USER:-$(logname 2>/dev/null || echo '')}"
if [ -z "$STUDENT_USER" ] || [ "$STUDENT_USER" = "root" ]; then
    echo -e "${YELLOW}WARNING: Could not detect student user.${NC}"
    echo "  Please run with: sudo ./setup_environment.sh"
    echo "  (not as root directly)"
    exit 1
fi
echo -e "${GREEN}Detected student user: ${STUDENT_USER}${NC}"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[1/5] Creating lab groups...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
for grp in engineering marketing devops; do
    if getent group "$grp" >/dev/null 2>&1; then
        echo -e "  ${YELLOW}⚠${NC} Group '$grp' already exists - skipping"
    else
        groupadd "$grp"
        echo -e "  ${GREEN}✓${NC} Group '$grp' created"
    fi
done

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[2/5] Creating lab users...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
# intern    → engineering only
# developer → engineering + devops
# manager   → engineering + marketing + devops (multiple groups)
declare -A USER_GROUPS
USER_GROUPS[intern]="engineering"
USER_GROUPS[developer]="engineering,devops"
USER_GROUPS[manager]="engineering,marketing,devops"

for user in intern developer manager; do
    if getent passwd "$user" >/dev/null 2>&1; then
        echo -e "  ${YELLOW}⚠${NC} User '$user' already exists - updating groups"
        usermod -aG "${USER_GROUPS[$user]}" "$user" 2>/dev/null || true
    else
        useradd -m -s /bin/bash -G "${USER_GROUPS[$user]}" "$user"
        passwd -l "$user" >/dev/null 2>&1 || true
        echo -e "  ${GREEN}✓${NC} User '$user' created (groups: ${USER_GROUPS[$user]})"
    fi
done

# Add student to engineering group so they can practice group-based access
usermod -aG engineering "$STUDENT_USER" 2>/dev/null || true
echo -e "  ${GREEN}✓${NC} Student '$STUDENT_USER' added to 'engineering' group"

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[3/5] Verifying lab files exist...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
MISSING=0
for f in \
    company/hr/salaries.csv \
    company/hr/employee_reviews.txt \
    company/engineering/deploy_config.yaml \
    company/engineering/build.sh \
    company/engineering/api_keys.env \
    company/marketing/campaign_plan.txt \
    company/marketing/analytics_report.csv \
    company/shared_docs/company_handbook.txt \
    company/shared_docs/meeting_notes.txt \
    scripts/backup_database.sh \
    scripts/generate_report.sh \
    scripts/cleanup_logs.sh \
    data/reports/weekly_summary.txt \
    data/reports/security_audit.txt; do
    if [ ! -f "$f" ]; then
        echo -e "  ${RED}✗${NC} Missing: $f"
        MISSING=1
    fi
done

if [ "$MISSING" -eq 1 ]; then
    echo -e "${RED}ERROR: Some lab files are missing. Make sure you are running${NC}"
    echo -e "${RED}this script from the linux_lab12_permissions_lab directory.${NC}"
    exit 1
fi
echo -e "  ${GREEN}✓${NC} All lab files found"

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[4/5] Setting INTENTIONALLY WRONG permissions (for students to fix)...${NC}"
# ─────────────────────────────────────────────────────────────────────────────

# --- Directory permissions ---
chmod 755 company company/hr company/engineering company/marketing company/shared_docs
chmod 755 scripts data data/reports

# ============================================================================
# STEP 1 PROBLEM: HR salary file is world-readable (WRONG! should be 600)
# ============================================================================
chmod 644 company/hr/salaries.csv
chown manager:marketing company/hr/salaries.csv

# ============================================================================
# STEP 3 PROBLEM: Employee reviews readable by everyone (WRONG! should be 600)
# ============================================================================
chmod 644 company/hr/employee_reviews.txt
chown root:root company/hr/employee_reviews.txt

# ============================================================================
# STEP 2 PROBLEM: Build script missing execute permission
# ============================================================================
chmod 644 company/engineering/build.sh
chown developer:engineering company/engineering/build.sh

# ============================================================================
# STEP 3 PROBLEM: API keys file world-readable+writable (WRONG! should be 600)
# ============================================================================
chmod 666 company/engineering/api_keys.env
chown developer:engineering company/engineering/api_keys.env

# ============================================================================
# STEP 4 PROBLEM: Deploy config owned by wrong user and group
# ============================================================================
chmod 640 company/engineering/deploy_config.yaml
chown intern:marketing company/engineering/deploy_config.yaml

# ============================================================================
# STEP 5 PROBLEM: Marketing files owned by engineering users
# ============================================================================
chmod 664 company/marketing/campaign_plan.txt
chown developer:engineering company/marketing/campaign_plan.txt

chmod 644 company/marketing/analytics_report.csv
chown intern:engineering company/marketing/analytics_report.csv

# ============================================================================
# STEP 6 PROBLEM: Shared docs too restrictive and wrong ownership
# ============================================================================
chmod 600 company/shared_docs/company_handbook.txt
chown intern:intern company/shared_docs/company_handbook.txt

chmod 600 company/shared_docs/meeting_notes.txt
chown root:root company/shared_docs/meeting_notes.txt

# ============================================================================
# STEP 7 PROBLEM: Scripts wrong ownership and missing execute
# ============================================================================
chmod 644 scripts/backup_database.sh
chown root:root scripts/backup_database.sh

chmod 644 scripts/generate_report.sh
chown root:root scripts/generate_report.sh

chmod 644 scripts/cleanup_logs.sh
chown root:root scripts/cleanup_logs.sh

# ============================================================================
# STEP 8 PROBLEM: Reports with overly permissive access
# ============================================================================
chmod 666 data/reports/weekly_summary.txt
chown root:root data/reports/weekly_summary.txt

chmod 777 data/reports/security_audit.txt
chown root:root data/reports/security_audit.txt

echo -e "  ${GREEN}✓${NC} Intentionally wrong permissions applied"

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[5/5] Verification...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo -e "  Checking users:"
for user in intern developer manager; do
    if getent passwd "$user" >/dev/null 2>&1; then
        echo -e "    ${GREEN}✓${NC} $user exists (groups: $(groups "$user" 2>/dev/null | cut -d: -f2 | xargs))"
    else
        echo -e "    ${RED}✗${NC} $user NOT found"
    fi
done

echo -e "  Checking groups:"
for grp in engineering marketing devops; do
    if getent group "$grp" >/dev/null 2>&1; then
        echo -e "    ${GREEN}✓${NC} $grp exists (members: $(getent group "$grp" | cut -d: -f4))"
    else
        echo -e "    ${RED}✗${NC} $grp NOT found"
    fi
done

echo ""
echo -e "${GREEN}✓ Setup complete.${NC}"
echo ""
echo -e "${BLUE}Summary:${NC}"
echo "  - Users created: intern, developer, manager (passwords locked)"
echo "  - Groups created: engineering, marketing, devops"
echo "  - Student '$STUDENT_USER' added to 'engineering' group"
echo "  - Intentionally WRONG permissions applied to lab files"
echo "  - Students must fix permissions, ownership, and group access"
echo ""
echo -e "${YELLOW}NOTE: Student may need to log out and back in (or run 'newgrp engineering')${NC}"
echo -e "${YELLOW}      for the new group membership to take effect.${NC}"
echo ""
echo -e "${BLUE}Students should start with: cat start_here.txt${NC}"
echo ""
