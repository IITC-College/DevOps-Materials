#!/bin/bash
################################################################################
# Lab 12: Permissions Lab - Unified Setup Script
#
# Creates users (intern, developer, manager), groups (engineering, marketing,
# devops), and a company directory structure with intentionally WRONG
# permissions and ownership. Students must fix access issues using chmod,
# chown, and group management commands.
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
echo -e "${GREEN}[1/7] Creating lab groups...${NC}"
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
echo -e "${GREEN}[2/7] Creating lab users...${NC}"
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
echo -e "${GREEN}[3/7] Creating directory structure...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
mkdir -p company/hr company/engineering company/marketing company/shared_docs
mkdir -p scripts
mkdir -p data/reports
mkdir -p clues/level1 clues/level2 clues/level3
mkdir -p .answers

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[4/7] Creating lab files with content...${NC}"
# ─────────────────────────────────────────────────────────────────────────────

# company/hr/ - HR department files (should be private)
cat > company/hr/salaries.csv <<'CONTENT'
Employee,Department,Salary
Alice,Engineering,95000
Bob,Marketing,88000
Charlie,HR,92000
Dana,Engineering,97000
CONTENT

cat > company/hr/employee_reviews.txt <<'CONTENT'
=== CONFIDENTIAL: Employee Performance Reviews ===

Q4 Review Summary:
- Alice: Exceeds expectations - promote to Senior
- Bob: Meets expectations - standard raise
- Charlie: Needs improvement - schedule mentoring
- Dana: Exceeds expectations - bonus approved

This document is HR-CONFIDENTIAL.
CONTENT

# company/engineering/ - Engineering files
cat > company/engineering/deploy_config.yaml <<'CONTENT'
# Deployment Configuration
environment: production
replicas: 3
port: 8080
database:
  host: db.internal.company.com
  port: 5432
  name: app_production
CONTENT

cat > company/engineering/build.sh <<'CONTENT'
#!/bin/bash
# Build script for the main application
echo "Running tests..."
echo "Tests passed: 42/42"
echo "Building application..."
echo "Build successful! Ready to deploy."
CONTENT

cat > company/engineering/api_keys.env <<'CONTENT'
# WARNING: These are MOCK keys for lab purposes only
API_KEY=sk-lab-mock-12345-not-real
DB_PASSWORD=lab_password_mock_67890
SECRET_TOKEN=fake-token-for-learning
CONTENT

# company/marketing/ - Marketing files
cat > company/marketing/campaign_plan.txt <<'CONTENT'
=== Q1 Marketing Campaign ===

Target: Developer community
Budget: $50,000
Channels: Social media, tech blogs, conferences

Key Messages:
1. 10x faster deployment
2. Built-in security
3. Zero-downtime updates

Launch Date: March 15
CONTENT

cat > company/marketing/analytics_report.csv <<'CONTENT'
Month,Visitors,Signups,Conversion
January,45000,1200,2.7%
February,52000,1500,2.9%
March,61000,1900,3.1%
CONTENT

# company/shared_docs/ - Should be accessible to all departments
cat > company/shared_docs/company_handbook.txt <<'CONTENT'
=== Company Handbook ===

Welcome to TechCorp!

Core Values:
1. Collaboration across teams
2. Transparency in communication
3. Security-first mindset
4. Continuous learning

This document should be readable by ALL employees.
CONTENT

cat > company/shared_docs/meeting_notes.txt <<'CONTENT'
=== All-Hands Meeting Notes - March 2026 ===

Attendees: All departments
Topics:
1. Q1 Results - Revenue up 15%
2. New office opening - April
3. Team restructuring - Engineering + DevOps merger
4. Security audit results - 2 findings to address

Action Items:
- Engineering: Fix permission issues on shared resources
- Marketing: Prepare launch materials
- HR: Update onboarding docs

NEXT MEETING: April 5, 2026
CONTENT

# scripts/ - Automation scripts with intentional issues
cat > scripts/backup_database.sh <<'CONTENT'
#!/bin/bash
# Database backup script - should be executable by engineering team
echo "Connecting to database..."
echo "Creating backup: backup_$(date +%Y%m%d).sql"
echo "Backup completed successfully!"
echo "Stored in /backups/db/"
CONTENT

cat > scripts/generate_report.sh <<'CONTENT'
#!/bin/bash
# Weekly report generator - needs execute permission
echo "Generating weekly report..."
echo "Collecting metrics from all departments..."
echo "Report saved to data/reports/weekly_$(date +%Y%m%d).txt"
CONTENT

cat > scripts/cleanup_logs.sh <<'CONTENT'
#!/bin/bash
# Log cleanup utility - manager only
echo "Scanning for old log files..."
echo "Found 15 files older than 30 days"
echo "Cleaning up... Done!"
echo "Freed 2.3 GB of disk space"
CONTENT

# data/reports/ - Report files
cat > data/reports/weekly_summary.txt <<'CONTENT'
=== Weekly Summary Report ===
Generated: 2026-03-01

Deployments: 12 successful, 0 failed
Uptime: 99.97%
Active Users: 15,234
Support Tickets: 45 open, 128 closed

Status: All systems operational
CONTENT

cat > data/reports/security_audit.txt <<'CONTENT'
=== CONFIDENTIAL: Security Audit Report ===

Finding 1 (HIGH): Shared files have overly permissive access (777)
  - Risk: Any user can modify critical documents
  - Fix: Restrict to owner/group only

Finding 2 (MEDIUM): Scripts missing execute permission
  - Risk: Automation workflows broken
  - Fix: Add execute permission for appropriate users

Finding 3 (LOW): HR files accessible to all users
  - Risk: Salary data exposure
  - Fix: Restrict to HR group / owner only

Overall Score: 65/100 - NEEDS IMPROVEMENT
CONTENT

echo -e "  ${GREEN}✓${NC} All lab files created with content"

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[5/7] Setting INTENTIONALLY WRONG permissions (for students to fix)...${NC}"
# ─────────────────────────────────────────────────────────────────────────────

# --- Directory permissions ---
chmod 755 company company/hr company/engineering company/marketing company/shared_docs
chmod 755 scripts data data/reports
chmod 755 clues clues/level1 clues/level2 clues/level3
chmod 755 .answers 2>/dev/null || true

# ============================================================================
# LEVEL 1 PROBLEMS: chmod (Fixing file permissions)
# ============================================================================

# Problem 1A: HR salary file is world-readable (WRONG! should be 600)
chmod 644 company/hr/salaries.csv
chown manager:marketing company/hr/salaries.csv  # Wrong group too

# Problem 1B: Employee reviews readable by everyone (WRONG! should be 600)
chmod 644 company/hr/employee_reviews.txt
chown root:root company/hr/employee_reviews.txt  # Wrong owner

# Problem 1C: Build script missing execute permission
chmod 644 company/engineering/build.sh  # Missing +x
chown developer:engineering company/engineering/build.sh

# Problem 1D: API keys file world-readable (WRONG! should be 600)
chmod 666 company/engineering/api_keys.env  # Way too open
chown developer:engineering company/engineering/api_keys.env

# ============================================================================
# LEVEL 2 PROBLEMS: chown (Fixing ownership)
# ============================================================================

# Problem 2A: Deploy config owned by wrong user
chmod 640 company/engineering/deploy_config.yaml
chown intern:marketing company/engineering/deploy_config.yaml  # Wrong owner AND group

# Problem 2B: Marketing files owned by engineering user
chmod 664 company/marketing/campaign_plan.txt
chown developer:engineering company/marketing/campaign_plan.txt  # Wrong dept

chmod 644 company/marketing/analytics_report.csv
chown intern:engineering company/marketing/analytics_report.csv  # Wrong dept

# Problem 2C: Shared docs owned by single user instead of accessible
chmod 600 company/shared_docs/company_handbook.txt  # Too restrictive
chown intern:intern company/shared_docs/company_handbook.txt  # Wrong - needs group

chmod 600 company/shared_docs/meeting_notes.txt  # Too restrictive
chown root:root company/shared_docs/meeting_notes.txt  # Wrong owner

# ============================================================================
# LEVEL 3 PROBLEMS: Combined chmod + chown + group scenarios
# ============================================================================

# Problem 3A: Scripts need correct ownership AND execute permissions
chmod 644 scripts/backup_database.sh  # Missing execute
chown root:root scripts/backup_database.sh  # Wrong owner/group

chmod 644 scripts/generate_report.sh  # Missing execute
chown root:root scripts/generate_report.sh  # Wrong owner/group

chmod 644 scripts/cleanup_logs.sh  # Missing execute
chown root:root scripts/cleanup_logs.sh  # Wrong owner/group

# Problem 3B: Reports with mixed permission issues
chmod 666 data/reports/weekly_summary.txt  # Too open
chown root:root data/reports/weekly_summary.txt

chmod 777 data/reports/security_audit.txt  # Way too open for confidential
chown root:root data/reports/security_audit.txt

echo -e "  ${GREEN}✓${NC} Intentionally wrong permissions applied"

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[6/7] Setting clue and documentation permissions...${NC}"
# ─────────────────────────────────────────────────────────────────────────────
chmod 644 clues/level1/clue1.txt clues/level1/clue2.txt clues/level1/clue3.txt
chmod 644 clues/level2/clue1.txt clues/level2/clue2.txt clues/level2/clue3.txt
chmod 644 clues/level3/clue1.txt clues/level3/clue2.txt clues/level3/clue3.txt
chmod 644 README.md start_here.txt 2>/dev/null || true
[ -f .answers/solutions.txt ] && chmod 644 .answers/solutions.txt

# ─────────────────────────────────────────────────────────────────────────────
echo -e "${GREEN}[7/7] Verification...${NC}"
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
echo "  - Company directory structure created with INTENTIONALLY WRONG permissions"
echo "  - Students must fix permissions, ownership, and group access"
echo ""
echo -e "${YELLOW}NOTE: Student may need to log out and back in (or run 'newgrp engineering')${NC}"
echo -e "${YELLOW}      for the new group membership to take effect.${NC}"
echo ""
echo -e "${BLUE}Students should start with: cat start_here.txt${NC}"
echo ""
