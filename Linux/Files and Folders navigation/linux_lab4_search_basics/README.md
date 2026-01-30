# Linux Lab - Search Basics

Welcome to your Linux search practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.4/linux_search_basics.tar.gz
tar -xzf lab.tar.gz
cd linux_search_basics
```

## Lab Objective

Learn to search for information **efficiently**, without scanning files manually.

You will practice these essential commands:

- **grep** - Search for text patterns inside files
- **grep -i** - Case-insensitive search
- **grep -r** - Recursive search in directories
- **find** - Find files by name or pattern

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Exercise 1: Search for a Word Inside a File
- Use grep to search for text in /etc/passwd
- Understand what grep returns

### Exercise 2: Case-Insensitive Search
- Use grep -i for flexible searching
- Learn when case-insensitive search is useful

### Exercise 3: Recursive Search in a Directory
- Use grep -r to search in multiple files
- Understand recursive searching

### Exercise 4: Find a File by Name
- Use find to locate files by name
- Learn about file system searching

### Exercise 5: Find Files by Extension
- Use find with wildcard patterns
- Locate all files of a specific type

## Important Tips

1. **Read error messages** - they tell you exactly what's wrong
2. **grep searches content** - inside files
3. **find searches names** - file and directory names
4. **Use -r for directories** - grep -r searches recursively
5. **Practice makes perfect** - try different search patterns

## Safety Rules

- **Don't use sudo** unless mentioned in the exercise
- **Don't copy results blindly** - read and understand them
- **Focus on understanding** what was searched and where
- **No regex or pipes** - only basic daily usage

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current file
2. Check the command output - it contains important information
3. Use `man` to read about commands (for example: `man grep`)
4. Read error messages carefully - they explain what went wrong

## Good Luck!

Remember: Searching efficiently is a crucial Linux skill. Master grep and find, and you'll be able to locate any information quickly!

---

**Linux Course - Day 1**  
**Search Basics Lab**
