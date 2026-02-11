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

**Requirements:**
- Create a script called `check_step1.sh`
- Add the shebang line
- Define a function called `greet`
- Inside the function, print "Hello from the function!"
- Call the function twice
- Make it executable and run it

**Technical Hints:**
- Function syntax: `function_name() { commands; }`
- Or: `function function_name { commands; }`
- Functions must be defined BEFORE they're called
- Call a function by just using its name (no parentheses needed)
- Functions can be called multiple times

**Expected Output:**
```
Hello from the function!
Hello from the function!
```

**Testing:**
1. Run the script - should print message twice
2. Try calling the function 3 times - should print 3 times
3. Try calling before defining - should error (functions must be defined first)

**Script Name:** `check_step1.sh`

---

### Task 2: Function with Parameter ($1)

**Objective:** Learn to pass arguments to functions using positional parameters

**Requirements:**
- Modify `check_step1.sh` to create a new function
- Name the function `check_dir`
- The function should accept one parameter (a directory path)
- Inside the function, check if the directory exists
- If it exists, print "Directory [path] exists"
- If not, print "Directory [path] missing"
- Call the function three times with different paths:
  - "src/data/environments/project1"
  - "logs"
  - "src/data/environments/missing"

**Technical Hints:**
- Access first parameter with `$1`
- Second parameter would be `$2`, third `$3`, etc.
- Always quote parameters: `"$1"`
- Pass arguments when calling: `function_name argument1 argument2`
- The directory check uses `[ -d "$1" ]`

**Expected Output:**
```
Directory src/data/environments/project1 exists
Directory logs missing
Directory src/data/environments/missing missing
```
(Based on what actually exists)

**Testing:**
1. Run and observe which directories exist
2. Create the "logs" directory if missing
3. Run again - output should change
4. This shows parameters make functions reusable!

**Script Name:** `check_step1.sh` (modified)

---

### Task 3: Function Called Multiple Times

**Objective:** Understand how functions eliminate code duplication

**Requirements:**
- Create a script called `deploy_step2.sh`
- Add the shebang
- Define a function called `deploy_tier` that takes one parameter (tier name)
- Inside the function, print two messages:
  - "Deploying [tier]..."
  - "  [tier]: deployed"
- Call the function four times with different tier names:
  - "frontend"
  - "api"
  - "worker"
  - "cache"

**Technical Hints:**
- Use `$1` to reference the tier name parameter
- Each function call is independent
- The parameter `$1` gets a new value each time
- This is the DRY principle: Don't Repeat Yourself
- Without functions, you'd duplicate the echo statements 4 times

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

**Testing:**
1. Run the script - should deploy 4 tiers
2. Add another tier (e.g., "database") - just one function call needed
3. Modify the messages - only change the function, not 4 places
4. This shows the power of reusable functions!

**Script Name:** `deploy_step2.sh`

---

### Task 4: Function That Formats Output

**Objective:** Create a reusable function for consistent log formatting

**Requirements:**
- Create a script called `status_header.sh`
- Add the shebang
- Define a function called `log_header` that takes one parameter (message)
- Inside the function, print the message with a timestamp prefix
- The timestamp should show time in HH:MM:SS format
- Use command substitution to get the current time
- After defining the function, use it to log:
  - "Deploy started."
  - Then print regular echo messages for steps
  - "Deploy complete."

**Technical Hints:**
- Date with time format: `date '+%H:%M:%S'`
- Combine with message: `"[$(...)] $1"`
- The `$()` runs the date command and captures output
- `%H` = hour, `%M` = minute, `%S` = second
- This creates consistent timestamped logging

**Expected Output:**
```
[14:23:15] Deploy started.
  Stopping old services...
  Copying new files...
  Starting new services...
[14:23:15] Deploy complete.
```
(Times will be your current time)

**Testing:**
1. Run the script - timestamps should show current time
2. Add `sleep 2` between the log calls
3. Run again - should show 2-second difference
4. This is how professional scripts log operations!

**Script Name:** `status_header.sh`

---

### Task 5: Combine Functions with Loops

**Objective:** Call functions from inside loops for maximum efficiency

**Requirements:**
- Create a script called `deploy_loop.sh`
- Add the shebang
- Define a `deploy_tier` function (same as Task 3)
- The function should print deployment messages for the given tier
- Instead of calling the function multiple times manually, use a for loop
- Loop over: frontend, api, worker
- Call the function once per iteration
- After the loop, print "All tiers deployed!"

**Technical Hints:**
- Functions + loops = powerful automation
- Define function first, then use it in loop
- Pass loop variable to function: `function_name "$VARIABLE"`
- This is cleaner than duplicating function calls
- Easy to add more tiers - just update the list

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

**Testing:**
1. Run the script - should deploy 3 tiers
2. Add "database" to the loop list
3. Run again - should deploy 4 tiers (no code change in function!)
4. This combines loops + functions for clean automation

**Script Name:** `deploy_loop.sh`

---

### Task 6: Build a Complete Deployment Script

**Objective:** Combine multiple functions to build a realistic deployment tool

**Requirements:**
- Create a script called `deploy_tiers.sh`
- Define TWO functions:
  1. `log_header` - formats and prints header messages with timestamp
     - Add decorative lines (==========)
     - Include timestamp in YYYY-MM-DD HH:MM:SS format
     - Print the message parameter
  2. `deploy_tier` - simulates deploying one tier
     - Print "→ Stopping [tier]..."
     - Sleep 1 second (simulates work)
     - Print "→ Deploying [tier] from /opt/releases/[tier]..."
     - Sleep 1 second
     - Print "→ Starting [tier]..."
     - Print "✓ [tier]: deployed successfully"
     - Add blank line for spacing
- Main script flow:
  - Log header: "Starting Multi-Tier Deployment"
  - Print "Deploying application tiers..."
  - Loop over frontend, api, worker - call deploy_tier for each
  - Log header: "All tiers deployed. Running smoke tests..."
  - Print "✓ Smoke tests passed!"
  - Log header: "Deployment Complete"

**Technical Hints:**
- Multiple functions work together
- `sleep` command pauses execution (simulates actual work)
- Combine loops + functions for clean orchestration
- Use symbols for better UX: → ✓
- This is a realistic multi-tier deployment structure

**Expected Output:**
```
========================================
[2026-02-11 14:30:00] Starting Multi-Tier Deployment
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
[2026-02-11 14:30:06] All tiers deployed. Running smoke tests...
========================================
✓ Smoke tests passed!
========================================
[2026-02-11 14:30:06] Deployment Complete
========================================
```

**Testing:**
1. Run and watch the deployment progress
2. Notice the sleep delays (realistic timing)
3. Add another tier to the loop
4. This is how real deployment tools are structured!

**Script Name:** `deploy_tiers.sh`

---

### Task 7: Build a Menu with Functions (Case + Functions)

**Objective:** Combine case statements with functions for a clean, maintainable menu

**Requirements:**
- Create a script called `menu_full.sh`
- Define THREE functions at the top:
  1. `show_disk` - displays disk usage
     - Print header "=== Disk Usage (current directory) ==="
     - Run `df -h .` command
  2. `show_uptime` - displays system uptime
     - Print header "=== System Uptime ==="
     - Run `uptime` command
  3. `show_status` - displays system status
     - Print header "=== System Status ==="
     - Print hostname using `hostname` command
     - Print current date using `date` command
- Display a menu with 4 options
- Prompt user to enter choice (1-4)
- Use case statement to call appropriate function based on choice
- Handle invalid input with error message and exit code 1

**Technical Hints:**
- Define all functions BEFORE the menu/case
- Case branches should just call the function (one line each)
- This keeps the menu logic clean and functions reusable
- Functions can run any commands - very flexible
- Menu + functions = professional script structure

**Expected Output:**
- Option 1 → disk usage with header
- Option 2 → system uptime with header
- Option 3 → hostname and date with header
- Option 4 → "Exiting."
- Invalid → "Invalid option." (exit 1)

**Testing:**
1. Test each menu option 1-4
2. Test invalid option (5 or abc)
3. Notice how clean the case statement is (just function calls)
4. Try adding a 5th option - define function, add to menu, add case branch
5. This is the structure used in real ops tools!

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
