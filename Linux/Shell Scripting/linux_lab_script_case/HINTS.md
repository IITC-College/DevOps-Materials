# Hints

## Task 1
- `case` syntax: `case "$VAR" in pattern) commands ;; esac`
- Each pattern ends with `)`
- Each branch ends with `;;` (double semicolon)
- Always quote the variable: `"$CHOICE"`
- `*)` is the catch-all/default pattern (matches anything)
- `esac` closes the case statement (it's "case" backwards!)

## Task 2
- Case patterns can be strings: `disk)` instead of `1)`
- Patterns are literal strings, not regular expressions (by default)
- You can match multiple patterns: `yes|y)` matches "yes" or "y"
- Case is case-sensitive: `disk)` won't match "DISK" or "Disk"
- For case-insensitive: use pattern like `[Dd]isk)` or convert input to lowercase first

## Task 3
- Exit codes: 0 = success, non-zero = error
- `exit 1` in default branch signals invalid input
- Check exit code of last command: `echo $?`
- Exit codes are important for scripting chains and automation
- Valid branches don't need explicit `exit 0` (script ends naturally with 0)

## Task 4
- You can run any command in a case branch
- Commands execute in order within a branch
- Multiple commands in one branch:
  ```bash
  1)
      echo "Starting disk check..."
      df -h .
      echo "Check complete."
      ;;
  ```
- Exit codes: if the branch command fails, the script continues unless you check `$?` or use `set -e`

## General Tips

### Case Pattern Matching
- Literal string: `prod)` matches "prod" exactly
- Multiple patterns: `prod|production)` matches either
- Wildcards: `*.txt)` matches anything ending in .txt
- Character classes: `[0-9])` matches any single digit
- Question mark: `?)` matches any single character

### Menu Best Practices
- Show clear menu options before prompting
- Number options for easy selection
- Always include exit option
- Handle invalid input gracefully

### When to Use Case vs If/Elif
- **Use case when:**
  - You have many discrete options (3+)
  - Matching against specific values
  - Building menu systems
  - Cleaner, more readable code

- **Use if/elif when:**
  - Complex conditions (greater than, less than)
  - Combining multiple tests
  - Fewer than 3 options
  - Need && or || logic

### Advanced Case Patterns
```bash
case "$VAR" in
    [Yy]es|[Yy])  # Match yes, Yes, y, Y
        ;;
    [0-9])        # Match any single digit
        ;;
    [0-9][0-9])   # Match any two digits
        ;;
    *.log)        # Match anything ending in .log
        ;;
esac
```

### Debugging Case Statements
- Add `echo "DEBUG: CHOICE=$CHOICE"` before case
- Check each branch individually
- Verify `esac` is present (missing esac = syntax error)
- Verify `;;` after each branch
- Use `set -x` to trace execution

---

## Solutions

### Task 1 Solution

```bash
#!/bin/bash
read -p "Enter option (1/2/3): " CHOICE

case "$CHOICE" in
    1)
        echo "You selected Option 1"
        ;;
    2)
        echo "You selected Option 2"
        ;;
    3)
        echo "You selected Option 3"
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

### Task 2 Solution

```bash
#!/bin/bash
read -p "Enter option (disk/uptime/exit): " CHOICE

case "$CHOICE" in
    disk)
        echo "Option: disk check"
        ;;
    uptime)
        echo "Option: uptime"
        ;;
    exit)
        echo "Exiting."
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

### Task 3 Solution

```bash
#!/bin/bash
read -p "Enter option (disk/uptime/exit): " CHOICE

case "$CHOICE" in
    disk)
        echo "Option: disk check"
        ;;
    uptime)
        echo "Option: uptime"
        ;;
    exit)
        echo "Exiting."
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac
```

### Task 4 Solution

```bash
#!/bin/bash
read -p "Enter option (1=disk, 2=uptime, 3=exit): " CHOICE

case "$CHOICE" in
    1)
        df -h .
        ;;
    2)
        uptime
        ;;
    3)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo "Invalid option."
        exit 1
        ;;
esac
```
