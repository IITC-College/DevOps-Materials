#!/bin/bash
################################################################################
# Setup Environment Script for Lab 11: Debug Mindset
#
# This script prepares the lab environment by:
# - Setting up broken scenarios with wrong permissions
# - Setting root ownership for scenario4 (ownership mismatch)
# - Creating deliberately broken situations for students to debug
#
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
echo -e "${BLUE}║  Setting up Lab 11: Debug Mindset                    ║${NC}"
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

echo -e "${GREEN}[INFO]${NC} Setting up broken scenarios for Debug Mindset Lab..."
echo ""

# Run the existing set_permissions.sh script
if [ -f "set_permissions.sh" ]; then
    echo -e "${GREEN}[STEP]${NC} Running set_permissions.sh..."
    bash set_permissions.sh
else
    echo -e "${YELLOW}[WARN]${NC} set_permissions.sh not found, setting permissions manually..."
    
    # Scenario 1: Remove read permission
    echo "Setting up Scenario 1: Read failure..."
    chmod 000 broken_scenarios/scenario1_read_failure/secret.txt 2>/dev/null || true
    
    # Scenario 2: Remove execute permission from script
    echo "Setting up Scenario 2: Script won't execute..."
    chmod -x broken_scenarios/scenario2_script_broken/deploy.sh 2>/dev/null || true
    
    # Scenario 3: Remove write permission from directory
    echo "Setting up Scenario 3: Can't write to directory..."
    chmod 555 broken_scenarios/scenario3_cant_write/ 2>/dev/null || true
    
    # Scenario 4: Change ownership to root (ownership mismatch)
    echo "Setting up Scenario 4: Ownership mismatch..."
    chown root:root broken_scenarios/scenario4_ownership_mess/important.txt 2>/dev/null || true
    chmod 600 broken_scenarios/scenario4_ownership_mess/important.txt 2>/dev/null || true
    
    # Scenario 5: Hidden file with wrong permissions
    echo "Setting up Scenario 5: Hidden file access..."
    chmod 000 broken_scenarios/scenario5_lost_path/.config 2>/dev/null || true
    
    # Scenario 6: Multiple issues
    echo "Setting up Scenario 6: Mixed issues..."
    chmod -x broken_scenarios/scenario6_mixed_issues/run_backup.sh 2>/dev/null || true
    chmod 600 broken_scenarios/scenario6_mixed_issues/data.txt 2>/dev/null || true
    chmod 444 broken_scenarios/scenario6_mixed_issues/ 2>/dev/null || true
    chmod 644 broken_scenarios/scenario6_mixed_issues/deep/ 2>/dev/null || true
    chmod 644 broken_scenarios/scenario6_mixed_issues/deep/nested/ 2>/dev/null || true
    chmod 644 broken_scenarios/scenario6_mixed_issues/deep/nested/path/ 2>/dev/null || true
    chmod 000 broken_scenarios/scenario6_mixed_issues/README.md 2>/dev/null || true
fi

# Additional setup: Ensure scenario4 has root ownership (critical for ownership mismatch exercise)
echo ""
echo -e "${GREEN}[STEP]${NC} Setting root ownership for Scenario 4 (ownership mismatch)..."
if [ -f "broken_scenarios/scenario4_ownership_mess/important.txt" ]; then
    chown root:root broken_scenarios/scenario4_ownership_mess/important.txt
    chmod 600 broken_scenarios/scenario4_ownership_mess/important.txt
    echo -e "  ${GREEN}✓${NC} scenario4_ownership_mess/important.txt → root:root (600)"
else
    echo -e "  ${YELLOW}[WARN]${NC} scenario4_ownership_mess/important.txt not found"
fi

# Set permissions for clue files and documentation
echo -e "${GREEN}[STEP]${NC} Setting permissions for clue files and documentation..."
find clues -type f -name "*.txt" -exec chmod 644 {} \; 2>/dev/null || true
chmod 644 README.md 2>/dev/null || true
chmod 644 start_here.txt 2>/dev/null || true

# Set permissions for data files
if [ -f "data/logs/debug_methodology.txt" ]; then
    chmod 644 data/logs/debug_methodology.txt
fi
if [ -f "data/secrets/tips.txt" ]; then
    chmod 644 data/secrets/tips.txt
fi

# Set permissions for set_permissions.sh if it exists
if [ -f "set_permissions.sh" ]; then
    chmod 755 set_permissions.sh
fi

echo ""
echo -e "${GREEN}✓${NC} Environment setup complete!"
echo ""
echo -e "${BLUE}Note:${NC} All scenarios have been deliberately broken for students to debug:"
echo "  • Scenario 1: Read permission removed"
echo "  • Scenario 2: Execute permission missing"
echo "  • Scenario 3: Write permission removed from directory"
echo "  • Scenario 4: File owned by root (ownership mismatch)"
echo "  • Scenario 5: Hidden file with no access"
echo "  • Scenario 6: Multiple combined issues"
echo ""
echo "Students will use the 4-step debug methodology to fix these issues."
echo ""