# Linux Lab - File System Scavenger Hunt

Welcome to your first Linux home lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/YOUR_USERNAME/YOUR_REPO/releases/download/v1.0/linux_scavenger_hunt.tar.gz
tar -xzf lab.tar.gz
cd linux_scavenger_hunt
```

### Method 2: Using the download script

```bash
curl -L https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/download_lab.sh | bash
```

## Lab Objective

In this lab you will practice all the commands learned in Day 1 of the course:

- **Navigation**: `cd`, `ls`, `pwd`
- **File Management**: `mkdir`, `touch`, `cp`, `mv`, `rm`
- **Reading Files**: `cat`, `less`, `head`, `tail`
- **Searching**: `grep`, `find`

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the clues and tasks

```bash
cat start_here.txt
```

## Task List

### Task 1: Basic Navigation
- Find the `start_here.txt` file
- Navigate to the `clues/level1` directory
- Find how many files are in the directory

### Task 2: Reading Files
- Read a log file from `data/logs/`
- Find a specific line with `grep`
- Use `head` to read only the first 10 lines

### Task 3: Searching for Information
- Find all files containing a specific word
- Find a file by partial name using `find`
- Find hidden files (starting with a dot)

### Task 4: Scavenger Hunt
- Follow a series of clues that point to each other
- Collect information from different files
- Assemble the final answer

### Task 5: File Management
- Create a new directory called `my_answers/`
- Copy important files to the new directory
- Organize files by categories

## Important Tips

1. **Read error messages** - they tell you exactly what's wrong
2. **Use `ls -a`** - to see hidden files
3. **Use `grep -r`** - to search recursively in directories
4. **Use `find`** - to locate files by name
5. **Always check where you are** - with `pwd`

## Safety Rules

- **Don't delete files** without being sure that's what you want
- **Work in your home directory** (`~`) or in the lab directory
- **Keep backups** - use `cp` before major changes

## Lab Submission

After completing all tasks:

1. Create a file called `my_answers.txt` in the lab directory
2. Write the answers to all tasks
3. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current file
2. Check the command output - it contains important information
3. Use `man` to read about commands (for example: `man grep`)

## Good Luck!

Remember: Linux is not trying to trip you up - it just doesn't guess what you meant.
Read carefully, work cautiously, and enjoy!

---

**Linux Course - Day 1**  
**File System Scavenger Hunt Lab**
