# Shell Scripting Lab: Mini DevOps Tool (Capstone)

## Goal

Build a comprehensive Mini DevOps Tool that combines ALL concepts from previous labs. You'll create a menu-driven tool with functions for health checks, system status, backups, and CI/CD pipelines - a capstone project demonstrating professional bash scripting.

## Prerequisites

- **ALL previous labs completed**
- Understanding of: case statements, functions, loops, exit codes
- Linux system with bash
- A text editor

## Important Note

This lab builds ONE script (`ops_tool.sh`) incrementally across all tasks. Each task adds more functionality to the same script.

## Tasks

### Task 1: Create the Case Menu Structure

**Objective:** Build the menu framework with stub functions

**Instructions:**
1. Create a script called `ops_tool.sh`
2. Define stub functions (functions that just echo what they do):
   ```bash
   #!/bin/bash
   
   # Stub functions (will be implemented later)
   check_services() {
       echo "Running health check..."
   }
   
   show_status() {
       echo "Showing system status..."
   }
   
   backup_now() {
       echo "Running backup..."
   }
   
   run_pipeline() {
       echo "Running pipeline..."
   }
   
   # Main menu
   echo "=== Mini DevOps Tool ==="
   echo "  check | status | backup | pipeline | exit"
   read -p "Action: " ACTION
   
   case "$ACTION" in
       check)
           check_services
           ;;
       status)
           show_status
           ;;
       backup)
           backup_now
           ;;
       pipeline)
           run_pipeline
           ;;
       exit)
           echo "Exiting."
           exit 0
           ;;
       *)
           echo "Error: use check, status, backup, pipeline, or exit."
           exit 1
           ;;
   esac
   ```
3. Make it executable and test each menu option

**Expected Output:**
```
=== Mini DevOps Tool ===
  check | status | backup | pipeline | exit
Action: check
Running health check...
```

**Script Name:** `ops_tool.sh`

---

### Task 2: Implement show_status Function

**Objective:** Add real system commands to show status

**Instructions:**
1. Replace the `show_status()` stub with:
   ```bash
   show_status() {
       echo "[$(date '+%Y-%m-%d %H:%M:%S')] === System Status ==="
       echo ""
       echo "Date: $(date)"
       echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
       echo ""
       echo "Disk usage (current directory):"
       df -h . 2>/dev/null || echo "  (df not available)"
       echo ""
       echo "Memory:"
       free -h 2>/dev/null | grep Mem || echo "  (free not available)"
       echo ""
   }
   ```
2. Test with: `./ops_tool.sh` and choose "status"

**Expected Output:**
```
=== Mini DevOps Tool ===
  check | status | backup | pipeline | exit
Action: status
[2026-02-10 14:30:00] === System Status ===

Date: Tue Feb 10 14:30:00 EST 2026
Uptime: 2 hours, 15 minutes

Disk usage (current directory):
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   45G   55G  45% /

Memory:
Mem:            16G   8.2G   7.8G
```

**Script Name:** `ops_tool.sh` (modified)

---

### Task 3: Implement check_services Function

**Objective:** Add a health check function with a loop

**Instructions:**
1. Replace the `check_services()` stub with:
   ```bash
   check_services() {
       echo "[$(date '+%H:%M:%S')] Health check..."
       echo ""
       
       for SVC in nginx app db; do
           echo "  Checking $SVC..."
           # In real script: curl, systemctl, or actual check
           echo "    $SVC: OK"
       done
       
       echo ""
       echo "[$(date '+%H:%M:%S')] All services OK."
   }
   ```
2. Test with: choose "check"

**Expected Output:**
```
=== Mini DevOps Tool ===
  check | status | backup | pipeline | exit
Action: check
[14:30:00] Health check...

  Checking nginx...
    nginx: OK
  Checking app...
    app: OK
  Checking db...
    db: OK

[14:30:00] All services OK.
```

**Script Name:** `ops_tool.sh` (modified)

---

### Task 4: Implement backup_now Function

**Objective:** Add backup functionality with timestamps

**Instructions:**
1. Replace the `backup_now()` stub with:
   ```bash
   backup_now() {
       echo "[$(date '+%H:%M:%S')] Backup started..."
       echo ""
       
       BACKUP_DIR="/backup/$(date +%Y-%m-%d-%H%M)"
       echo "  Backup directory: $BACKUP_DIR"
       echo "  Backing up logs..."
       # In real script: tar -czf $BACKUP_DIR/logs.tar.gz /var/log/app/
       echo "  Backing up configs..."
       # In real script: tar -czf $BACKUP_DIR/configs.tar.gz /etc/app/
       
       echo ""
       echo "[$(date '+%H:%M:%S')] Backup complete."
   }
   ```
2. Test with: choose "backup"

**Expected Output:**
```
=== Mini DevOps Tool ===
  check | status | backup | pipeline | exit
Action: backup
[14:30:00] Backup started...

  Backup directory: /backup/2026-02-10-1430
  Backing up logs...
  Backing up configs...

[14:30:00] Backup complete.
```

**Script Name:** `ops_tool.sh` (modified)

---

### Task 5: Add Exit Codes to All Branches

**Objective:** Ensure proper exit codes for success and failure

**Instructions:**
1. Add `exit 0` after each successful action in the case statement:
   ```bash
   case "$ACTION" in
       check)
           check_services
           exit 0
           ;;
       status)
           show_status
           exit 0
           ;;
       backup)
           backup_now
           exit 0
           ;;
       pipeline)
           run_pipeline
           exit 0
           ;;
       exit)
           echo "Exiting."
           exit 0
           ;;
       *)
           echo "Error: use check, status, backup, pipeline, or exit."
           exit 1
           ;;
   esac
   ```
2. Test with valid action: `./ops_tool.sh` (choose "check"), then `echo $?` (should be 0)
3. Test with invalid action: `./ops_tool.sh` (choose "invalid"), then `echo $?` (should be 1)

**Expected Behavior:**
- Valid actions exit with code 0
- Invalid actions exit with code 1

**Script Name:** `ops_tool.sh` (modified)

---

### Task 6: Implement run_pipeline Function

**Objective:** Add a multi-stage CI/CD pipeline simulation

**Instructions:**
1. Replace the `run_pipeline()` stub with:
   ```bash
   run_pipeline() {
       echo "[$(date '+%H:%M:%S')] === Pipeline (validate → build → test → deploy) ==="
       echo ""
       
       echo "  [validate] Checking config..."
       echo "    ✓ Config OK"
       echo "    ✓ Disk space OK"
       echo ""
       
       echo "  [build] Building artifact..."
       echo "    ✓ Artifact built: app-v1.2.3.jar"
       echo ""
       
       echo "  [test] Running tests..."
       echo "    ✓ Unit tests passed (45/45)"
       echo "    ✓ Integration tests passed (12/12)"
       echo ""
       
       echo "  [deploy] Deploying to staging..."
       echo "    ✓ Deployed to staging"
       echo ""
       
       echo "[$(date '+%H:%M:%S')] Pipeline complete."
   }
   ```
2. Test with: choose "pipeline"

**Expected Output:**
```
=== Mini DevOps Tool ===
  check | status | backup | pipeline | exit
Action: pipeline
[14:30:00] === Pipeline (validate → build → test → deploy) ===

  [validate] Checking config...
    ✓ Config OK
    ✓ Disk space OK

  [build] Building artifact...
    ✓ Artifact built: app-v1.2.3.jar

  [test] Running tests...
    ✓ Unit tests passed (45/45)
    ✓ Integration tests passed (12/12)

  [deploy] Deploying to staging...
    ✓ Deployed to staging

[14:30:00] Pipeline complete.
```

**Script Name:** `ops_tool.sh` (modified)

---

### Task 7: Test All Functions Together

**Objective:** Verify the complete tool works properly

**Instructions:**
1. Test each menu option:
   - check → health check with loop
   - status → system info with real commands
   - backup → backup simulation
   - pipeline → CI/CD pipeline
   - exit → clean exit
   - invalid → error message
2. Check exit codes with `echo $?` after each run
3. Verify timestamps appear correctly
4. Ensure output is clean and readable

**Verification Checklist:**
- ✓ Case statement handles all options
- ✓ Functions are defined before being called
- ✓ Loop works in check_services
- ✓ Real system commands work (date, uptime, df, free)
- ✓ Exit codes are correct (0 for success, 1 for error)
- ✓ Output is well-formatted and professional

**Script Name:** `ops_tool.sh` (testing)

---

### Task 8: Final Polish and Documentation

**Objective:** Add comments and finalize the professional tool

**Instructions:**
1. Add a header comment to your script:
   ```bash
   #!/bin/bash
   #
   # Mini DevOps Tool - Capstone Project
   # Provides health checks, system status, backups, and CI/CD pipeline
   # 
   # Usage: ./ops_tool.sh
   # Actions: check, status, backup, pipeline, exit
   #
   ```
2. Add comments to each function explaining what it does
3. Review the complete script for consistency
4. Consider enhancements for v2 (see below)

**Complete Script Structure:**
```bash
#!/bin/bash
# Mini DevOps Tool - Capstone Project

# Health check function - checks all services
check_services() {
    # ... implementation ...
}

# System status function - shows date, uptime, disk, memory
show_status() {
    # ... implementation ...
}

# Backup function - simulates backing up logs and configs
backup_now() {
    # ... implementation ...
}

# Pipeline function - simulates CI/CD pipeline
run_pipeline() {
    # ... implementation ...
}

# Main menu
echo "=== Mini DevOps Tool ==="
echo "  check | status | backup | pipeline | exit"
read -p "Action: " ACTION

case "$ACTION" in
    check)
        check_services
        exit 0
        ;;
    # ... other branches ...
esac
```

**Script Name:** `ops_tool.sh` (final version)

---

## Completion

Congratulations! You've built a comprehensive Mini DevOps Tool that demonstrates:
- ✓ Case statements for menu systems
- ✓ Functions for code organization
- ✓ Loops for repetitive tasks
- ✓ Exit codes for success/failure signaling
- ✓ Real system commands (date, uptime, df, free)
- ✓ Professional output formatting
- ✓ Modular, maintainable code structure

## What You've Mastered

- **Case Statements:** Clean menu routing
- **Functions:** Modular code organization
- **Loops:** Automated service checks
- **Variables:** Consistent naming and usage
- **Exit Codes:** Proper error handling
- **System Commands:** Integration with Linux tools
- **Formatting:** Professional, readable output

## Enhancement Ideas (v2)

Take your tool to the next level:
- **Add a loop** to keep running until "exit" is chosen
- **Add actual health checks** using curl or systemctl
- **Implement real backup** with tar and file operations
- **Add error handling** (what if df fails?)
- **Add logging** to file with timestamps
- **Add configuration file** for customizable settings
- **Add command-line arguments:** `./ops_tool.sh check`
- **Add color output** (green for success, red for errors)
- **Add notifications** (send email/Slack on pipeline failure)
- **Add database backup** in addition to files
- **Add rollback capability** for deployments
- **Add dry-run mode** to preview without executing

This is the foundation for real DevOps automation tools used in production!
