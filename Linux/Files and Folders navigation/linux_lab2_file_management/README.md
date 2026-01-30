# Linux Lab - File and Directory Management

Welcome to your Linux file management practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.2/linux_file_management.tar.gz
tar -xzf lab.tar.gz
cd linux_file_management
```

## Lab Objective

In this lab you will practice full control over files and directories using the Linux command line, **without GUI**.

You will learn to use these essential commands:

- **Directory Creation**: `mkdir`, `mkdir -p`
- **File Creation**: `touch`
- **File Operations**: `cp`, `mv`
- **Deletion**: `rm`, `rmdir`
- **Error Handling**: Understanding what happens when things go wrong

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step
4. **Important**: You will create your own directory structure (`linux_lab/`) in your home directory

```bash
cat start_here.txt
```

## Exercise List

### Exercise 1: Delete the Wrong File (On Purpose)
- Create a file and delete it
- Understand why files are deleted immediately
- Learn what warnings Linux does NOT give you

### Exercise 2: Move a File to the Wrong Location, Then Fix It
- Create a file in the wrong place
- Move it to the correct location
- Practice fixing mistakes

### Exercise 3: `mkdir` vs `mkdir -p`
- Try creating nested directories with `mkdir`
- See the error message
- Use `mkdir -p` to succeed
- Understand the difference

## Important Tips

1. **Read error messages** - they tell you exactly what's wrong
2. **Practice in your home directory** - all exercises are safe there
3. **No GUI tools** - use only command line
4. **No sudo needed** - work in your own directories
5. **Mistakes are learning opportunities** - some exercises intentionally create errors

## Safety Rules

- **Work in your home directory** (`~`) - all exercises are safe there
- **Don't use sudo** - not needed for this lab
- **Read error messages** - they help you understand what went wrong
- **Practice makes perfect** - don't be afraid to try commands

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current file
2. Check the command output - it contains important information
3. Use `man` to read about commands (for example: `man mkdir`)
4. Read error messages carefully - they explain what went wrong

## Good Luck!

Remember: Linux commands are powerful. Practice carefully, read error messages, and learn from each exercise!

---

**Linux Course - Day 1**  
**File and Directory Management Lab**
