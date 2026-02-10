# Shell Scripting Lab: User Input

## Goal

Learn to capture user input in bash scripts using the `read` command. You'll build a service checking script that prompts for input and explores what happens with empty input (setting up for validation in future labs).

## Prerequisites

- Script Basics and Variables labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Read Basic User Input

**Objective:** Learn to capture user input with the `read` command

**Instructions:**
1. Create a script called `check_service.sh`
2. Add the shebang: `#!/bin/bash`
3. Add a read command with prompt:
   ```bash
   read -p "Enter service name: " SERVICE
   ```
4. Add an echo to display what was entered:
   ```bash
   echo "Checking service: $SERVICE"
   ```
5. Make it executable and run it
6. Type a service name (like "web" or "database") and press Enter

**Expected Output:**
```
Enter service name: web
Checking service: web
```

**Script Name:** `check_service.sh`

---

### Task 2: Understand `read -p` vs Plain `read`

**Objective:** Learn the difference between `read` with and without the `-p` option

**Instructions:**
1. Run your current script (`./check_service.sh`) and notice how the prompt works
2. Create a test script called `read_test.sh` with:
   ```bash
   #!/bin/bash
   read SERVICE
   echo "Service: $SERVICE"
   ```
3. Run both scripts and compare the user experience
4. Notice that `read -p` shows the prompt on the same line, while plain `read` just waits

**Expected Output:**
- `read -p`: Prompt appears, you type on the same line
- plain `read`: Cursor waits on next line, no visible prompt

**Script Name:** `read_test.sh` (new), `check_service.sh` (comparison)

---

### Task 3: Add Confirmation Messages

**Objective:** Build better user feedback with multiple echo statements

**Instructions:**
1. Open `check_service.sh`
2. After the existing echo, add another line:
   ```bash
   echo "Will check status of $SERVICE now."
   ```
3. Run the script and enter a service name
4. Notice how the variable is used in multiple places

**Expected Output:**
```
Enter service name: database
Checking service: database
Will check status of database now.
```

**Script Name:** `check_service.sh` (modified)

---

### Task 4: Test with Empty Input

**Objective:** Discover what happens when users don't enter anything

**Instructions:**
1. Run `./check_service.sh`
2. Press Enter without typing anything
3. Observe the output - notice the SERVICE variable is empty
4. The messages will show blank spaces where the service name should be
5. Run it again with actual input to confirm it still works normally

**Expected Output (empty input):**
```
Enter service name: 
Checking service: 
Will check status of  now.
```

**Script Name:** `check_service.sh` (testing only)

---

### Task 5: Understand the Problem with Empty Input

**Objective:** Recognize why input validation matters

**Instructions:**
1. Read the validation notes in `src/validation_note.txt`
2. Think about scenarios where empty input could cause problems:
   - Trying to check a service with no name
   - Deploying to an environment but the environment variable is empty
   - Backing up files but the filename is empty
3. Consider what might happen in a production DevOps script if validation is missing

**Expected Understanding:**
- Empty input can lead to unexpected behavior
- In production scripts, we should validate before using input
- You'll learn validation techniques (if statements, checking for empty strings) in the Conditionals lab

**Script Name:** None (reading and reflection)

---

## Completion

You've successfully learned:
- How to use `read` to capture user input
- The `-p` option for inline prompts
- Using input variables in multiple places
- What happens with empty input (security/reliability concern)
- Why input validation matters (preparation for conditionals lab)

**Note:** This script currently accepts empty input. In real-world DevOps scripts, you'd add validation to reject empty input and prompt again. You'll learn how to do this in the Conditionals lab using `if` statements and `[ -z "$VAR" ]` checks.
