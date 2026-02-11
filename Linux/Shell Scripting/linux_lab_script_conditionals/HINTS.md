# Hints

## Task 1
- `[ -f "$FILE" ]` checks if a regular file exists
- Always quote variables: `"$CONFIG"` not `$CONFIG`
- Quotes prevent issues with spaces in paths
- The `-f` test returns true for files, false for directories or non-existent paths
- Use semicolons or newlines in if statements: `if [ test ]; then` or put `then` on next line

## Task 2
- `[ -d "$DIR" ]` checks if a directory exists
- Similar to `-f` but specifically for directories
- A file won't pass the `-d` test (use `-f` for files)
- Create directories with: `mkdir dirname` or `mkdir -p path/to/dir` (creates parents)

## Task 3
- `[ -z "$VAR" ]` tests if string is zero-length (empty)
- Opposite: `[ -n "$VAR" ]` tests if string is NOT empty
- Always quote: `"$VAR"` in tests
- `exit 1` terminates script with error code 1 (non-zero = error)
- `exit 0` means success (zero = success in Unix)

## Task 4
- String comparison: `[ "$VAR" = "value" ]` (note: single `=`)
- In bash `[[` ]]`, you can use `==`, but `[` `]` requires single `=`
- `elif` = "else if" for multiple conditions
- Use `&&` for AND: `[ "$A" = "x" ] && [ "$B" = "y" ]`
- Use `||` for OR: `[ "$A" = "x" ] || [ "$A" = "y" ]`
- Can also use: `[ "$ENV" = "prod" -o "$ENV" = "staging" ]` (-o = or)

## Task 5
- `[ ! -d "$DIR" ]` means "if directory does NOT exist"
- `!` negates the test
- `mkdir -p` creates parent directories and doesn't error if exists
- Conditional is useful when you want to: log creation, check permissions, run cleanup first

## Task 6
- Exit early on errors (fail-fast pattern)
- Each check should `exit 1` on failure
- Order matters: check prerequisites before using them
- Use descriptive error messages
- Success message only if all checks pass
- Real deployment scripts would do: check config, check credentials, check target, check space, etc.

## General Tips

### Test Operators
- `-f FILE`: file exists and is regular file
- `-d DIR`: directory exists
- `-e PATH`: path exists (file or directory)
- `-r FILE`: file is readable
- `-w FILE`: file is writable
- `-x FILE`: file is executable
- `-z STRING`: string is empty
- `-n STRING`: string is not empty

### Comparison Operators
- `=` or `==`: strings are equal
- `!=`: strings are not equal
- `-eq`: numbers are equal
- `-ne`: numbers are not equal
- `-lt`: less than
- `-gt`: greater than

### Logical Operators
- `!`: NOT
- `-a`: AND (inside single brackets)
- `-o`: OR (inside single brackets)
- `&&`: AND (between tests)
- `||`: OR (between tests)

### Best Practices
- Always quote variables in tests: `[ -f "$FILE" ]`
- Use descriptive error messages
- Exit with non-zero code on errors
- Test your error paths (try to make them fail)
- Consider using `set -e` at top of script (exit on any error)
- Use `set -u` to catch undefined variables

---

## Solutions

### Task 1 Solution

```bash
#!/bin/bash
CONFIG="src/data/configs/.env.prod"

if [ -f "$CONFIG" ]; then
    echo "Config file exists."
else
    echo "Config file not found."
fi
```

### Task 2 Solution

```bash
#!/bin/bash
DEPLOY_DIR="src/data/environments/prod"

if [ -d "$DEPLOY_DIR" ]; then
    echo "Deploy directory exists."
else
    echo "Deploy directory not found."
fi
```

### Task 3 Solution

```bash
#!/bin/bash
read -p "Enter environment (prod or staging): " ENV

if [ -z "$ENV" ]; then
    echo "Error: environment cannot be empty."
    exit 1
fi

echo "Environment: $ENV"
```

### Task 4 Solution

```bash
#!/bin/bash
read -p "Enter environment (prod or staging): " ENV

if [ -z "$ENV" ]; then
    echo "Error: Environment cannot be empty."
    exit 1
fi

if [ "$ENV" = "prod" ]; then
    echo "Deploying to PRODUCTION."
elif [ "$ENV" = "staging" ]; then
    echo "Deploying to STAGING."
else
    echo "Error: environment must be prod or staging."
    exit 1
fi
```

### Task 5 Solution

```bash
#!/bin/bash
TARGET="src/data/environments/backup"

if [ ! -d "$TARGET" ]; then
    mkdir -p "$TARGET"
    echo "Created $TARGET"
else
    echo "$TARGET already exists."
fi
```

### Task 6 Solution

```bash
#!/bin/bash

# Check config file
CONFIG="src/data/configs/.env.prod"
if [ ! -f "$CONFIG" ]; then
    echo "Error: Config file not found."
    exit 1
fi

# Check deploy directory
DEPLOY_DIR="src/data/environments/prod"
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Error: Deploy directory not found."
    exit 1
fi

# Validate environment
read -p "Enter environment (prod or staging): " ENV
if [ -z "$ENV" ]; then
    echo "Error: Environment cannot be empty."
    exit 1
fi

if [ "$ENV" != "prod" ] && [ "$ENV" != "staging" ]; then
    echo "Error: Environment must be prod or staging."
    exit 1
fi

echo "All checks passed! Ready to deploy to $ENV."
```
