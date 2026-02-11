# Hints

## Task 1
- Start simple with hardcoded strings in echo statements
- Remember the shebang: `#!/bin/bash`
- Use `chmod +x scriptname.sh` to make executable
- Run with `./scriptname.sh`

## Task 2
- Variable syntax: `VAR_NAME="value"` (no spaces around `=`)
- Use variables with: `$VAR_NAME` or `${VAR_NAME}`
- Variable names are case-sensitive
- Convention: Use UPPERCASE for variables in scripts

## Task 3
- **CRITICAL:** No spaces around the `=` sign
- Wrong: `APP_NAME = "myapp"` (will cause error)
- Right: `APP_NAME="myapp"`
- Spaces around `=` make bash think you're trying to run a command
- Quotes are optional for single words but recommended for consistency

## Task 4
- Command substitution syntax: `VAR=$(command)`
- The `date` command has many format options
- `%Y` = 4-digit year, `%m` = month, `%d` = day
- Common formats: `%Y-%m-%d`, `%Y%m%d`, `%Y-%m-%d_%H-%M-%S`
- Test date formats: `date +%Y-%m-%d` in terminal first

## Task 5
- Embed variables in strings: `"text_${VAR}_more"`
- Curly braces `${}` help separate variable from surrounding text
- Example: `backup_${DATE}.log` creates `backup_2026-02-10.log`
- Without braces, bash might misinterpret variable names

## Task 6
- Organize variables at the top of the script for readability
- Comment your variables: `# Application name`
- Order matters: Define `DATE` before using it in `BACKUP_FILE`
- Think about what would need to change if you backup a different app
- Variables make scripts reusable and maintainable

## General Tips
- Always use quotes around variable values with spaces: `DIR="my folder"`
- Test date formats before using in scripts: `date +%Y-%m-%d`
- Variable naming: descriptive names in UPPERCASE
- Debug variables: `echo "DEBUG: VAR=$VAR"` to check values
- Common mistake: spaces in assignment - bash will treat it as a command
- Use `set -x` at the top of script to see all commands as they execute (debugging)

---

## Solutions

### Task 1 Solution

```bash
#!/bin/bash
echo "Backup started for app: myapp"
echo "Version: 1.0"
echo "Backing up..."
echo "Backup complete."
```

### Task 2 Solution

```bash
#!/bin/bash
APP_NAME="myapp"
VERSION="1.0"

echo "Backup started for app: $APP_NAME"
echo "Version: $VERSION"
echo "Backing up..."
echo "Backup complete."
```

### Task 3 Solution

```bash
#!/bin/bash
APP_NAME="myapp"
VERSION="1.0"
BACKUP_DIR="backups"

echo "Backup started for app: $APP_NAME"
echo "Version: $VERSION"
echo "Target directory: $BACKUP_DIR"
echo "Backing up..."
echo "Backup complete."
```

### Task 4 Solution

```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d)

echo "Backup date: $DATE"
echo "Backing up logs from src/data/logs/..."
```

### Task 5 Solution

```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d)
BACKUP_FILE="backup_${DATE}.log"

echo "Backup file will be: $BACKUP_FILE"
```

### Task 6 Solution

```bash
#!/bin/bash
APP_NAME="myapp"
VERSION="1.0"
BACKUP_DIR="backups"
DATE=$(date +%Y-%m-%d)
BACKUP_FILE="backup_${DATE}.log"

echo "Backup started for app: $APP_NAME"
echo "Version: $VERSION"
echo "Backup date: $DATE"
echo "Target directory: $BACKUP_DIR"
echo "Backup file will be: $BACKUP_FILE"
echo "Backing up logs..."
echo "Backup complete."
```
