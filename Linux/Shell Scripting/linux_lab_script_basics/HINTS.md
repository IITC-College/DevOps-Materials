# Hints

## Task 1
- Use a text editor like `nano first_deploy.sh` to create the file
- In nano, save with Ctrl+O, then Enter, then exit with Ctrl+X
- Each echo statement is on its own line
- Running with `bash` means you're explicitly using the bash interpreter

## Task 2
- The shebang must be the absolute first line, no spaces before it
- It always starts with `#!` followed by the interpreter path
- Common shebang: `#!/bin/bash`
- The permission denied error is expected - you haven't added execute permission yet

## Task 3
- Permission string format: `-rwxrwxrwx` (user, group, other)
- `r` = read, `w` = write, `x` = execute
- When a file lacks `x`, you can't run it with `./filename`
- `bash filename` works because you're running the bash program (which has execute permission) with your script as input

## Task 4
- `chmod +x` adds execute permission for all users
- `chmod u+x` adds execute permission for just the owner
- `chmod 755` sets specific permissions (rwxr-xr-x)
- You can remove execute permission with `chmod -x`

## Task 5
- `./script.sh` requires: shebang + execute permission
- `bash script.sh` only requires: readable file
- Scripts deployed to servers typically have execute permission
- Using `./` is more common in production environments

## General Tips
- Always include a shebang in your scripts
- Check permissions with `ls -l` when scripts won't run
- `chmod +x` is your friend
- Test scripts with both execution methods to understand the difference
- Good practice: make scripts executable and use `./` to run them
