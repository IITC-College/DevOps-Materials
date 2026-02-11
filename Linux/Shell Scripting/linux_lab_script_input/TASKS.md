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

**Requirements:**
- Create a script called `check_service.sh`
- Add the shebang line
- Use the `read` command to prompt the user with "Enter service name: "
- Store the user's input in a variable called SERVICE
- Display a message showing what was entered: "Checking service: [service name]"
- Make it executable and test it
- Try typing different service names (like "web" or "database")

**Technical Hints:**
- The `read` command with `-p` flag allows inline prompts
- Syntax: `read -p "prompt text" VARIABLE_NAME`
- When declaring with `read`, don't use `$` before the variable name
- To use the value later, reference it with `$VARIABLE_NAME`
- The prompt text should end with a space for better readability

**Expected Output:**
```
Enter service name: web
Checking service: web
```

**Testing:**
1. Run the script
2. Type "web" and press Enter
3. Run again and type "database"
4. The script should echo back whatever you enter

**Script Name:** `check_service.sh`

---

### Task 2: Understand `read -p` vs Plain `read`

**Objective:** Learn the difference between `read` with and without the `-p` option

**Requirements:**
- Run your current `check_service.sh` script and observe the prompt
- Create a new test script called `read_test.sh`
- In the test script, use plain `read` (without `-p`)
- Store input in a SERVICE variable
- Echo the service name
- Run both scripts and compare the user experience
- Identify which version provides better user experience

**Technical Hints:**
- `read -p "text"` = inline prompt (text appears, cursor waits on same line)
- `read` (no `-p`) = no visible prompt (cursor waits on blank line)
- Both work, but `-p` is more user-friendly
- The `-p` flag stands for "prompt"

**Expected Behavior:**
- `check_service.sh` with `-p`: Prompt appears, you type on the same line
- `read_test.sh` without `-p`: Cursor waits on next line, no visible prompt (confusing!)

**Testing:**
1. Run `check_service.sh` - notice the clear prompt
2. Run `read_test.sh` - notice no prompt appears
3. Conclude: Always use `-p` for better UX

**Script Name:** `read_test.sh` (new), `check_service.sh` (comparison)

---

### Task 3: Add Confirmation Messages

**Objective:** Build better user feedback with multiple echo statements

**Requirements:**
- Modify `check_service.sh`
- After the existing echo statement, add a second confirmation message
- The new message should say "Will check status of [service name] now."
- Use the SERVICE variable in both messages
- Run and test to verify the variable works in multiple places

**Technical Hints:**
- You can use the same variable as many times as needed
- Each `$SERVICE` reference will be replaced with the user's input
- Variables persist throughout the entire script execution
- Adding confirmation messages improves user experience

**Expected Output:**
```
Enter service name: database
Checking service: database
Will check status of database now.
```

**Testing:**
1. Run the script
2. Enter "database"
3. Both messages should show "database"
4. Try different service names to verify it works

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
