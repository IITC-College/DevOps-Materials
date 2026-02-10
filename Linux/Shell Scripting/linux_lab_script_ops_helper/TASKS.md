# Shell Scripting Lab: Ops Helper Tool

## Goal

Build a practical operations helper tool by combining all the concepts you've learned. You'll create a script that handles deployment, health checks, and backups with proper input validation and confirmation prompts.

## Prerequisites

- All previous labs (Basics through Exit Codes)
- Understanding of: variables, input, conditionals, exit codes
- Linux system with bash
- A text editor

## Tasks

### Task 1: Create Basic Action Reader

**Objective:** Start building the ops helper by reading user action choice

**Instructions:**
1. Look at the ops environment: `ls src/data/ops_env/`
2. Create a script called `ops_helper.sh`
3. Add the basic structure:
   ```bash
   #!/bin/bash
   
   echo "=== Ops Helper Tool ==="
   read -p "Action (deploy/check/backup): " ACTION
   echo "You chose: $ACTION"
   ```
4. Make it executable and run it
5. Test with different inputs: deploy, check, restart

**Expected Output:**
```
=== Ops Helper Tool ===
Action (deploy/check/backup): deploy
You chose: deploy
```

**Script Name:** `ops_helper.sh`

---

### Task 2: Handle Each Action with If/Elif

**Objective:** Implement different behavior for each action

**Instructions:**
1. Open `ops_helper.sh`
2. Replace the simple echo with if/elif/else logic:
   ```bash
   #!/bin/bash
   
   echo "=== Ops Helper Tool ==="
   read -p "Action (deploy/check/backup): " ACTION
   
   if [ "$ACTION" = "deploy" ]; then
       echo "Deploying application..."
       echo "✓ App deployed."
   elif [ "$ACTION" = "check" ]; then
       echo "Checking services..."
       echo "✓ Status: OK"
   elif [ "$ACTION" = "backup" ]; then
       echo "Backing up..."
       echo "✓ Backup finished."
   else
       echo "Unknown action. Use deploy, check, or backup."
   fi
   ```
3. Test all actions: deploy, check, backup, and an invalid one (like "restart")

**Expected Output:**
- deploy → "Deploying application..." and "✓ App deployed."
- check → "Checking services..." and "✓ Status: OK"
- backup → "Backing up..." and "✓ Backup finished."
- restart → "Unknown action..."

**Script Name:** `ops_helper.sh` (modified)

---

### Task 3: Add Input Validation

**Objective:** Handle empty input properly

**Instructions:**
1. Add validation for empty input at the start of your if/elif chain:
   ```bash
   if [ -z "$ACTION" ]; then
       echo "Error: action cannot be empty."
       exit 1
   elif [ "$ACTION" = "deploy" ]; then
       # ... rest of deploy logic
   # ... rest of branches
   fi
   
   echo ""
   echo "Done."
   ```
2. Test with empty input (press Enter without typing)
3. Test with valid actions to ensure they still work

**Expected Output (empty input):**
```
=== Ops Helper Tool ===
Action (deploy/check/backup): 
Error: action cannot be empty.
```

**Script Name:** `ops_helper.sh` (modified)

---

### Task 4: Add Variables for App and Paths

**Objective:** Make the script configurable with variables

**Instructions:**
1. Add variables at the top of the script (after shebang):
   ```bash
   #!/bin/bash
   
   # Configuration
   APP_NAME="webapp"
   LOG_DIR="src/data/ops_env/logs"
   CONFIG_DIR="src/data/ops_env/configs"
   
   echo "=== Ops Helper Tool ==="
   # ... rest of script
   ```
2. Update messages to use these variables:
   ```bash
   if [ "$ACTION" = "deploy" ]; then
       echo "Deploying $APP_NAME..."
       echo "✓ $APP_NAME deployed."
   elif [ "$ACTION" = "check" ]; then
       echo "Checking $APP_NAME services..."
       echo "✓ Status: OK"
   elif [ "$ACTION" = "backup" ]; then
       echo "Backing up logs from $LOG_DIR..."
       echo "✓ Backup finished."
   # ... else ...
   ```
3. Run and test

**Expected Output:**
```
=== Ops Helper Tool ===
Action (deploy/check/backup): deploy
Deploying webapp...
✓ webapp deployed.
```

**Script Name:** `ops_helper.sh` (modified)

---

### Task 5: Add Confirmation for Deploy

**Objective:** Require confirmation before dangerous operations

**Instructions:**
1. Add a confirmation prompt inside the deploy branch:
   ```bash
   if [ "$ACTION" = "deploy" ]; then
       read -p "Are you sure you want to deploy $APP_NAME? (yes/no): " CONFIRM
       
       if [ "$CONFIRM" != "yes" ]; then
           echo "Deploy cancelled."
       else
           echo "Deploying $APP_NAME..."
           echo "✓ $APP_NAME deployed."
       fi
   # ... rest of branches ...
   ```
2. Test deploy with "yes" confirmation
3. Test deploy with "no" or empty confirmation

**Expected Output (with "no"):**
```
=== Ops Helper Tool ===
Action (deploy/check/backup): deploy
Are you sure you want to deploy webapp? (yes/no): no
Deploy cancelled.

Done.
```

**Expected Output (with "yes"):**
```
=== Ops Helper Tool ===
Action (deploy/check/backup): deploy
Are you sure you want to deploy webapp? (yes/no): yes
Deploying webapp...
✓ webapp deployed.

Done.
```

**Script Name:** `ops_helper.sh` (modified)

---

### Task 6: Complete and Polish the Ops Helper

**Objective:** Final integration with all features working together

**Instructions:**
1. Review your complete `ops_helper.sh` - it should have:
   - Configuration variables (APP_NAME, LOG_DIR, CONFIG_DIR)
   - User prompt for action
   - Empty input validation
   - Deploy action with confirmation
   - Check action
   - Backup action
   - Unknown action handler
   - "Done." message at the end
2. Add a comment header describing what the script does
3. Test all scenarios:
   - Empty input → error
   - deploy + no → cancelled
   - deploy + yes → deployed
   - check → status OK
   - backup → backup finished
   - invalid action → unknown action

**Complete Script Structure:**
```bash
#!/bin/bash
# Ops Helper Tool - Handle deployment, health checks, and backups

# Configuration
APP_NAME="webapp"
LOG_DIR="src/data/ops_env/logs"
CONFIG_DIR="src/data/ops_env/configs"

echo "=== Ops Helper Tool ==="
read -p "Action (deploy/check/backup): " ACTION

# Validate input
if [ -z "$ACTION" ]; then
    echo "Error: action cannot be empty."
    exit 1
fi

# Handle actions
if [ "$ACTION" = "deploy" ]; then
    read -p "Are you sure you want to deploy $APP_NAME? (yes/no): " CONFIRM
    if [ "$CONFIRM" != "yes" ]; then
        echo "Deploy cancelled."
    else
        echo "Deploying $APP_NAME..."
        echo "✓ $APP_NAME deployed."
    fi
elif [ "$ACTION" = "check" ]; then
    echo "Checking $APP_NAME services..."
    echo "✓ Status: OK"
elif [ "$ACTION" = "backup" ]; then
    echo "Backing up logs from $LOG_DIR..."
    echo "✓ Backup finished."
else
    echo "Unknown action. Use deploy, check, or backup."
    exit 1
fi

echo ""
echo "Done."
```

**Script Name:** `ops_helper.sh` (final version)

---

## Completion

You've successfully built a practical operations helper tool! You've applied:
- Variables for configuration
- User input with `read`
- Input validation
- Conditional logic with if/elif/else
- Confirmation prompts for dangerous operations
- Exit codes for errors
- Clear user feedback

## Potential Enhancements (v2)

Consider these improvements for a more advanced version:
- Add a loop to keep the tool running until user types "exit"
- Use functions to organize code (deploy_app, check_services, backup_logs)
- Actually check if logs exist before backing up
- Add more actions (restart, rollback, logs)
- Use case statement instead of if/elif for cleaner code
- Add timestamps to output messages
- Implement actual file operations (copy logs, check services)
- Add error handling (what if deployment fails?)
- Support command-line arguments: `./ops_helper.sh deploy`

This is a foundation for real DevOps automation tools!
