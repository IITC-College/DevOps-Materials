# Hints

## Task 1 - Welcome Script
- Use a text editor to create the file: `nano welcome.sh` or `vim welcome.sh`
- Just type the echo statements exactly as shown
- Each echo is on its own line
- Save and exit (in nano: Ctrl+O, Enter, Ctrl+X)
- Run with: `bash welcome.sh`
- Empty echo statements (`echo ""`) create blank lines for better formatting

## Task 2 - Add Shebang
- The shebang must be the **very first line** - no blank lines before it
- It always starts with `#!` followed by the path to bash: `#!/bin/bash`
- The shebang tells the system which interpreter to use when you run `./script.sh`
- Getting "Permission denied" is expected - you'll fix that in the next task!
- You can still run it with `bash welcome.sh` even without the shebang

## Task 3 - Make Executable
- `ls -l welcome.sh` shows the file permissions
- Look for the permission string like `-rw-r--r--` (no `x` means not executable)
- `chmod +x welcome.sh` adds execute permission
- After chmod, `ls -l` will show `-rwxr-xr-x` (notice the `x` characters)
- Now `./welcome.sh` works because the file is executable
- The `./` means "run the file in the current directory"

## Task 4 - Deployment Script
- Start fresh with a new file: `nano deploy.sh`
- **First line must be the shebang**: `#!/bin/bash`
- Then add all the echo statements
- Make it executable right away: `chmod +x deploy.sh`
- Run with: `./deploy.sh`
- The empty echo (`echo ""`) creates spacing between sections

## Task 5 - Status Report Script
- Same process: create file, add shebang first, then echo statements
- Use spacing and formatting to make output readable
- Indentation in echo statements (spaces inside quotes) helps organize output
- Make executable with `chmod +x status.sh`
- Run with `./status.sh`

## General Tips

### Creating Scripts
- Always add `#!/bin/bash` as the first line
- Use echo statements to print text
- Empty echo (`echo ""`) creates blank lines
- Indentation inside quotes creates visual hierarchy

### Making Scripts Executable
- Check permissions: `ls -l scriptname.sh`
- Add execute permission: `chmod +x scriptname.sh`
- You only need to chmod once per script

### Running Scripts
- **With bash**: `bash scriptname.sh`
  - Works even without execute permission
  - Doesn't need the shebang
  - Good for testing
  
- **With ./**: `./scriptname.sh`
  - Requires execute permission (`chmod +x`)
  - Uses the shebang to find the interpreter
  - Standard way to run scripts

### Text Editor Tips
**Using nano:**
- Open/create: `nano filename.sh`
- Save: Ctrl+O, then Enter
- Exit: Ctrl+X

**Using vim:**
- Open/create: `vim filename.sh`
- Enter insert mode: press `i`
- Exit insert mode: press `Esc`
- Save and quit: type `:wq` and press Enter
- Quit without saving: type `:q!` and press Enter

### Common Errors
- **"Permission denied"**: You need to `chmod +x scriptname.sh`
- **"No such file or directory"**: Check the filename spelling or use `ls` to verify
- **"bash: ./scriptname.sh: No such file or directory"**: Make sure you're in the correct directory (`pwd` to check)
- **Script output looks wrong**: Check that echo statements have matching quotes
