# Shell Scripting Lab: Functions

## Goal

Master bash functions to write modular, reusable code. You'll learn to define functions, pass parameters, combine functions with loops, and build a multi-tier deployment script.

## Prerequisites

- Script Basics, Variables, Conditionals, Loops, and Case Statement labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Define a Simple Function

**Objective:** Learn basic function syntax and how to call functions

**Instructions:**
1. Create a script called `check_step1.sh`
2. Define a function and call it:
   ```bash
   #!/bin/bash
   
   greet() {
       echo "Hello from the function!"
   }
   
   # Call the function
   greet
   greet
   ```
3. Make it executable and run it

**Expected Output:**
```
Hello from the function!
Hello from the function!
```

**Script Name:** `check_step1.sh`

---

### Task 2: Function with Parameter ($1)

**Objective:** Learn to pass arguments to functions using positional parameters

**Instructions:**
1. Modify `check_step1.sh` to accept a parameter:
   ```bash
   #!/bin/bash
   
   check_dir() {
       if [ -d "$1" ]; then
           echo "Directory $1 exists"
       else
           echo "Directory $1 missing"
       fi
   }
   
   # Call with different arguments
   check_dir "src/data/environments/project1"
   check_dir "logs"
   check_dir "src/data/environments/missing"
   ```
2. Run the script

**Expected Output:**
```
Directory src/data/environments/project1 exists
Directory logs missing
Directory src/data/environments/missing missing
```

**Script Name:** `check_step1.sh` (modified)

---

### Task 3: Function Called Multiple Times

**Objective:** Understand how functions eliminate code duplication

**Instructions:**
1. Create a script called `deploy_step2.sh`
2. Define a function that simulates deploying a tier:
   ```bash
   #!/bin/bash
   
   deploy_tier() {
       echo "Deploying $1..."
       echo "  $1: deployed"
   }
   
   # Deploy multiple tiers
   deploy_tier "frontend"
   deploy_tier "api"
   deploy_tier "worker"
   deploy_tier "cache"
   ```
3. Run the script

**Expected Output:**
```
Deploying frontend...
  frontend: deployed
Deploying api...
  api: deployed
Deploying worker...
  worker: deployed
Deploying cache...
  cache: deployed
```

**Script Name:** `deploy_step2.sh`

---

### Task 4: Function That Formats Output

**Objective:** Create a reusable function for consistent log formatting

**Instructions:**
1. Create a script called `status_header.sh`
2. Define a function that adds timestamps to messages:
   ```bash
   #!/bin/bash
   
   log_header() {
       echo "[$(date '+%H:%M:%S')] $1"
   }
   
   # Use the function
   log_header "Deploy started."
   echo "  Stopping old services..."
   echo "  Copying new files..."
   echo "  Starting new services..."
   log_header "Deploy complete."
   ```
3. Run the script

**Expected Output:**
```
[14:23:15] Deploy started.
  Stopping old services...
  Copying new files...
  Starting new services...
[14:23:15] Deploy complete.
```
(Times will be your current time)

**Script Name:** `status_header.sh`

---

### Task 5: Combine Functions with Loops

**Objective:** Call functions from inside loops for maximum efficiency

**Instructions:**
1. Create a script called `deploy_loop.sh`
2. Combine a function with a for loop:
   ```bash
   #!/bin/bash
   
   deploy_tier() {
       echo "Deploying $1..."
       echo "  $1: deployed"
   }
   
   # Loop over tiers and deploy each
   for TIER in frontend api worker; do
       deploy_tier "$TIER"
   done
   
   echo "All tiers deployed!"
   ```
3. Run the script

**Expected Output:**
```
Deploying frontend...
  frontend: deployed
Deploying api...
  api: deployed
Deploying worker...
  worker: deployed
All tiers deployed!
```

**Script Name:** `deploy_loop.sh`

---

### Task 6: Build a Complete Deployment Script

**Objective:** Combine multiple functions to build a realistic deployment tool

**Instructions:**
1. Create a script called `deploy_tiers.sh`
2. Define multiple functions and orchestrate them:
   ```bash
   #!/bin/bash
   
   # Function for formatted log messages
   log_header() {
       echo "========================================"
       echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
       echo "========================================"
   }
   
   # Function to deploy a single tier
   deploy_tier() {
       echo "  → Stopping $1..."
       sleep 1
       echo "  → Deploying $1 from /opt/releases/$1..."
       sleep 1
       echo "  → Starting $1..."
       echo "  ✓ $1: deployed successfully"
       echo ""
   }
   
   # Main deployment flow
   log_header "Starting Multi-Tier Deployment"
   
   echo "Deploying application tiers..."
   echo ""
   
   for TIER in frontend api worker; do
       deploy_tier "$TIER"
   done
   
   log_header "All tiers deployed. Running smoke tests..."
   echo "✓ Smoke tests passed!"
   
   log_header "Deployment Complete"
   ```
3. Run the script and watch the deployment process

**Expected Output:**
```
========================================
[2026-02-10 14:30:00] Starting Multi-Tier Deployment
========================================
Deploying application tiers...

  → Stopping frontend...
  → Deploying frontend from /opt/releases/frontend...
  → Starting frontend...
  ✓ frontend: deployed successfully

  → Stopping api...
  → Deploying api from /opt/releases/api...
  → Starting api...
  ✓ api: deployed successfully

  → Stopping worker...
  → Deploying worker from /opt/releases/worker...
  → Starting worker...
  ✓ worker: deployed successfully

========================================
[2026-02-10 14:30:03] All tiers deployed. Running smoke tests...
========================================
✓ Smoke tests passed!
========================================
[2026-02-10 14:30:03] Deployment Complete
========================================
```

**Script Name:** `deploy_tiers.sh`

---

### Task 7: Build a Menu with Functions (Case + Functions)

**Objective:** Combine case statements with functions for a clean, maintainable menu

**Instructions:**
1. Create a script called `menu_full.sh`
2. Define functions at the top:
   ```bash
   #!/bin/bash
   
   show_disk() {
       echo "=== Disk Usage (current directory) ==="
       df -h .
   }
   
   show_uptime() {
       echo "=== System Uptime ==="
       uptime
   }
   
   show_status() {
       echo "=== System Status ==="
       echo "Hostname: $(hostname)"
       echo "Date: $(date)"
   }
   ```
3. Add a menu prompt:
   ```bash
   echo "Operations Menu:"
   echo "1) Check disk usage"
   echo "2) Show uptime"
   echo "3) Show system status"
   echo "4) Exit"
   read -p "Enter choice: " CHOICE
   ```
4. Add case statement calling functions:
   ```bash
   case "$CHOICE" in
       1)
           show_disk
           ;;
       2)
           show_uptime
           ;;
       3)
           show_status
           ;;
       4)
           echo "Exiting."
           exit 0
           ;;
       *)
           echo "Invalid option."
           exit 1
           ;;
   esac
   ```
5. Make executable and test all menu options

**Expected Output:**
- Option 1 → formatted disk usage
- Option 2 → system uptime
- Option 3 → hostname and date
- Option 4 → "Exiting."
- Invalid input → "Invalid option." and exit code 1

**Script Name:** `menu_full.sh`

---

## Completion

You've successfully learned:
- How to define functions in bash
- Calling functions multiple times
- Passing parameters to functions with `$1`, `$2`, etc.
- Using functions to eliminate code duplication
- Combining functions with loops
- Combining case statements with functions (menu with functions)
- Building modular, maintainable scripts
- Creating realistic deployment automation

Functions are fundamental to professional scripting! Benefits:
- **DRY Principle:** Don't Repeat Yourself
- **Maintainability:** Change logic in one place
- **Readability:** Clear, self-documenting code
- **Testability:** Test functions independently
- **Reusability:** Use functions across multiple scripts
