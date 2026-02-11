# Hints

## Task 1 - Variable Assignment
- Error: "APP_NAME: command not found"
- Problem: `APP_NAME = "myapp"` has spaces around `=`
- Bash interprets this as: run command `APP_NAME` with arguments `=` and `"myapp"`
- Fix: Remove spaces → `APP_NAME="myapp"`
- Rule: Variable assignment NEVER has spaces around `=`

## Task 2 - Missing Quotes
- Current: `[ -f $CONFIG ]`
- Problem: If CONFIG is empty or contains spaces, test breaks
- Example: if CONFIG="/my file.txt", it expands to `[ -f /my file.txt ]` which bash sees as too many arguments
- Fix: Add quotes → `[ -f "$CONFIG" ]`
- Rule: ALWAYS quote variables in tests

## Task 3 - Missing 'then'
- Error: "syntax error near unexpected token 'echo'"
- Problem: if statement missing `then` keyword
- Current: `if [ condition ]` followed by echo
- Fix: Add `then` → `if [ condition ]; then`
- Or: Put `then` on next line
  ```bash
  if [ condition ]
  then
      echo "..."
  fi
  ```

## Task 4 - Wrong Path
- Script looks for: `config.txt` (in current directory)
- File actually at: `data/configs/build_config.txt`
- Problem: Wrong path in CONFIG variable
- Fix: Change CONFIG to correct path relative to where script runs
- If running from src/: `CONFIG="data/configs/build_config.txt"`

## Task 5 - Missing 'fi'
- Error: "unexpected end of file"
- Problem: `if` statement not closed with `fi`
- Every `if` needs a matching `fi`
- Like: `{` needs `}`, `(` needs `)`
- Fix: Add `fi` at the end of the if block

## Task 6 - Multiple Bugs
- Fix bugs one at a time
- Run script after each fix to see next error
- Order matters: syntax errors prevent script from running
- Typical order:
  1. Fix variable assignment (syntax error)
  2. Fix missing `then` (syntax error)
  3. Fix missing `fi` (syntax error)
  4. Fix missing quotes (might work but incorrect)
  5. Fix wrong path (logical error)

## General Tips

### Common Bash Errors

**Spaces in Assignment:**
```bash
# WRONG
VAR = "value"
PATH = /usr/bin

# RIGHT
VAR="value"
PATH=/usr/bin
```

**Unquoted Variables:**
```bash
# RISKY (can break)
if [ -f $FILE ]; then

# SAFE
if [ -f "$FILE" ]; then

# RISKY
rm $DIR/*

# SAFER
rm "$DIR"/*
```

**Missing Keywords:**
```bash
# WRONG - missing then
if [ condition ]
    echo "yes"
fi

# RIGHT
if [ condition ]; then
    echo "yes"
fi

# WRONG - missing done
for i in 1 2 3; do
    echo $i

# RIGHT
for i in 1 2 3; do
    echo $i
done
```

**Path Issues:**
```bash
# If script is in scripts/ and config in configs/
# WRONG (from scripts/)
CONFIG="config.txt"

# RIGHT (from scripts/)
CONFIG="../configs/config.txt"

# Or use absolute path
CONFIG="/full/path/to/config.txt"
```

### Debugging Techniques

**Check syntax without running:**
```bash
bash -n script.sh
```

**Trace execution:**
```bash
bash -x script.sh
```

**Enable tracing in script:**
```bash
#!/bin/bash
set -x  # Enable tracing
# ... rest of script
```

**Add debug output:**
```bash
echo "DEBUG: CONFIG=$CONFIG"
echo "DEBUG: Checking if file exists..."
```

**Check exit codes:**
```bash
./script.sh
echo "Exit code: $?"
```

### Error Messages

**"command not found"**
- Could be: spaces in variable assignment
- Could be: typo in command name
- Could be: missing PATH

**"syntax error near unexpected token"**
- Missing `then` after if
- Missing `do` after for/while
- Unbalanced quotes

**"unexpected end of file"**
- Missing `fi`, `done`, or `esac`
- Unclosed quote or brace

**"too many arguments"**
- Unquoted variable expanded to multiple words
- Fix: Add quotes around variable

**File not found (logical error)**
- Wrong path (relative vs absolute)
- File doesn't exist
- Typo in filename
- Wrong directory

### Systematic Debugging

1. **Read the error message** - it often tells you the problem
2. **Check syntax first** - bash -n script.sh
3. **Add echo statements** - trace variables and flow
4. **Test small pieces** - isolate the problem
5. **Check file paths** - ls the files you're trying to access
6. **Verify variables** - echo them to see their values
7. **Use set -x** - see exactly what's executing
8. **Simplify** - comment out code to isolate issues

### Prevention

**Use strict mode:**
```bash
#!/bin/bash
set -euo pipefail
# -e: exit on error
# -u: exit on undefined variable
# -o pipefail: exit on pipe failure
```

**Validate inputs:**
```bash
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi
```

**Check prerequisites:**
```bash
[ -f "$CONFIG" ] || { echo "Config missing"; exit 1; }
```

**Use shellcheck:**
```bash
# Install shellcheck, then:
shellcheck script.sh
```

### Best Practices

- Always quote variables: `"$VAR"`
- Use `set -e` to exit on errors
- Check file existence before using
- Use absolute paths when possible
- Test with various inputs (including edge cases)
- Add comments to complex code
- Use meaningful variable names
- Validate all user inputs
- Test error paths (not just happy path)

---

## Solutions

These show the fixes needed for each broken script. Try to fix them yourself first!

### Task 1 - Variable Assignment Fix

Change:
```bash
APP_NAME = "myapp"    # WRONG - spaces around =
```

To:
```bash
APP_NAME="myapp"      # RIGHT - no spaces
```

### Task 2 - Missing Quotes Fix

Change:
```bash
if [ -f $CONFIG ]; then    # RISKY - unquoted variable
```

To:
```bash
if [ -f "$CONFIG" ]; then  # SAFE - quoted variable
```

### Task 3 - Missing 'then' Fix

Change:
```bash
if [ condition ]           # WRONG - missing then
    echo "..."
fi
```

To:
```bash
if [ condition ]; then     # RIGHT - has then
    echo "..."
fi
```

### Task 4 - Wrong Path Fix

Change:
```bash
CONFIG="config.txt"        # WRONG - file not in current dir
```

To:
```bash
CONFIG="data/configs/build_config.txt"  # RIGHT - correct path
```

### Task 5 - Missing 'fi' Fix

Change:
```bash
if [ condition ]; then
    echo "..."
# WRONG - missing fi
```

To:
```bash
if [ condition ]; then
    echo "..."
fi                         # RIGHT - closed with fi
```

### Task 6 - All Fixes Combined

All five fixes need to be applied to the `ci_full_broken.sh` script. Work through them systematically, fixing syntax errors first (spaces, then, fi) before logical errors (quotes, paths).
