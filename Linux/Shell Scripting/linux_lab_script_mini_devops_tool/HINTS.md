# Hints

## Task 1 - Menu Structure
- Define all functions BEFORE the menu (at top of script)
- Stub functions = placeholder functions that just echo
- Case pattern matches exact strings
- `;;` ends each case branch
- `*)` is the catch-all for invalid input
- Test each branch individually

## Task 2 - show_status
- `$(command)` runs command and captures output
- `date '+FORMAT'` formats date/time
- `2>/dev/null` suppresses error messages
- `||` provides fallback if command fails
- `grep Mem` extracts memory line from free output
- Empty lines (`echo ""`) improve readability

## Task 3 - check_services
- `for SVC in list` loops over services
- Real check would use: `curl -f http://localhost/health` or `systemctl is-active $SVC`
- Loop keeps check_services clean and extensible
- Easy to add more services: just add to the list
- Timestamps show when check started/finished

## Task 4 - backup_now
- `$(date +%Y-%m-%d-%H%M)` creates timestamp for unique backup dirs
- Real backup: `tar -czf backup.tar.gz /path/to/data`
- Organize backups by date/time for easy restoration
- In production: backup to remote storage, verify integrity

## Task 5 - Exit Codes
- Add `exit 0` after EACH successful function call
- Add `exit 1` in the `*)` branch for invalid input
- Without explicit exit, script continues (not what we want)
- CI/CD tools check exit codes to determine success/failure
- Test: `./script.sh; echo $?` immediately after running

## Task 6 - run_pipeline
- Real pipeline would run actual commands and check their exit codes
- Each stage should validate before proceeding
- Use `set -e` to exit on any error (fail-fast)
- In production: stages might be separate scripts
- Consider: what happens if build fails? (don't deploy!)

## Task 7 - Testing
- Test happy path (all valid actions)
- Test error path (invalid action)
- Test exit codes for each action
- Verify output formatting
- Check that timestamps work correctly
- Ensure no syntax errors

## Task 8 - Polish
- Add header comment explaining purpose
- Comment each function
- Consistent indentation (2 or 4 spaces)
- Consistent naming (snake_case for functions)
- Consider adding `set -euo pipefail` for stricter error handling

## General Tips

### Function Organization
```bash
#!/bin/bash

# All functions at top
function1() { ... }
function2() { ... }
function3() { ... }

# Main logic at bottom
# (menu, case statement, etc.)
```

### Case Statement Best Practices
```bash
case "$VAR" in
    option1)
        do_something
        exit 0
        ;;
    option2)
        do_another_thing
        exit 0
        ;;
    *)
        echo "Error: invalid option"
        exit 1
        ;;
esac
```

### Function Calling
```bash
# Define function
my_function() {
    echo "Doing work..."
}

# Call function (no parentheses)
my_function

# NOT: my_function()  (that's definition, not call)
```

### Timestamp Formats
```bash
# Full datetime
date '+%Y-%m-%d %H:%M:%S'  # 2026-02-10 14:30:00

# Time only
date '+%H:%M:%S'  # 14:30:00

# Date only
date '+%Y-%m-%d'  # 2026-02-10

# For filenames (no spaces/colons)
date '+%Y%m%d-%H%M%S'  # 20260210-143000
```

### System Commands
```bash
# Date/time
date
date '+%Y-%m-%d'

# Uptime
uptime
uptime -p  # "pretty" format (if available)

# Disk space
df -h  # all filesystems
df -h .  # current directory's filesystem

# Memory
free -h  # human-readable
free -m  # megabytes
```

### Error Handling
```bash
# Suppress errors
command 2>/dev/null

# Provide fallback
command 2>/dev/null || echo "Not available"

# Check if command exists
if command -v free &>/dev/null; then
    free -h
else
    echo "free command not available"
fi
```

### Real vs Simulated Operations

**In this lab (simulated):**
```bash
backup_now() {
    echo "  Backing up logs..."
    echo "  Backing up configs..."
}
```

**In production (real):**
```bash
backup_now() {
    BACKUP_DIR="/backup/$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    echo "  Backing up logs..."
    tar -czf "$BACKUP_DIR/logs.tar.gz" /var/log/app/ || {
        echo "Error: log backup failed"
        return 1
    }
    
    echo "  Backing up configs..."
    tar -czf "$BACKUP_DIR/configs.tar.gz" /etc/app/ || {
        echo "Error: config backup failed"
        return 1
    }
    
    echo "  Backup saved to: $BACKUP_DIR"
}
```

### Debugging
```bash
# Trace execution
bash -x ops_tool.sh

# Check syntax
bash -n ops_tool.sh

# Add debug output
echo "DEBUG: ACTION=$ACTION"
echo "DEBUG: Calling function..."
```

### Common Mistakes
- Functions defined after they're called (put at top!)
- Missing `;;` at end of case branch
- Missing `esac` at end of case statement
- Forgetting `exit 0` after successful actions
- Not testing exit codes
- Inconsistent formatting

### Enhancement Patterns

**Loop menu until exit:**
```bash
while true; do
    # Show menu
    # Read action
    # Handle action
    # If action is exit, break
done
```

**Command-line arguments:**
```bash
ACTION="${1:-}"  # First argument or empty
if [ -z "$ACTION" ]; then
    # Show interactive menu
else
    # Run action directly
fi
```

**Configuration file:**
```bash
# Load config if exists
CONFIG_FILE="${HOME}/.ops_tool.conf"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Set defaults if not in config
BACKUP_DIR="${BACKUP_DIR:-/backup}"
LOG_DIR="${LOG_DIR:-/var/log/app}"
```

**Color output:**
```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'  # No Color

echo -e "${GREEN}✓ Success${NC}"
echo -e "${RED}✗ Failed${NC}"
```

**Actual health check:**
```bash
check_service() {
    local SERVICE=$1
    
    # Try systemctl
    if systemctl is-active --quiet "$SERVICE"; then
        echo "    $SERVICE: OK"
        return 0
    fi
    
    # Try curl health endpoint
    if curl -sf "http://localhost:8080/health/$SERVICE" >/dev/null; then
        echo "    $SERVICE: OK"
        return 0
    fi
    
    echo "    $SERVICE: FAILED"
    return 1
}
```

### Professional Script Template
```bash
#!/bin/bash
#
# Script Name: ops_tool.sh
# Description: Mini DevOps Tool for operations tasks
# Author: Your Name
# Version: 1.0
# Usage: ./ops_tool.sh
#

# Strict error handling
set -euo pipefail

# Configuration
readonly BACKUP_DIR="/backup"
readonly LOG_FILE="/var/log/ops_tool.log"

# Functions
function1() { ... }
function2() { ... }

# Main
main() {
    # Main logic here
}

# Run main
main "$@"
```
