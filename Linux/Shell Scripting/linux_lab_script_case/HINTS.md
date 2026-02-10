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

## Task 5
- Functions must be defined before use (put at top of script)
- Function syntax: `function_name() { commands; }`
- Call functions by name: `show_disk` (no parentheses)
- Functions can access script variables
- Functions can have their own local variables: `local VAR="value"`
- Combine case + functions = clean, modular code
- Easy to add new menu options: define function, add case branch

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
- Use descriptive function names
- Group related functionality

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
