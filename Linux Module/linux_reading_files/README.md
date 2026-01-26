# Linux Lab - Reading Files

Welcome to your Linux file reading practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.3/linux_reading_files.tar.gz
tar -xzf lab.tar.gz
cd linux_reading_files
```

## Lab Objective

In this lab you will learn to **read information** from files using the Linux command line.

You will practice these essential commands:

- **cat** - Display entire file contents
- **less** - View files page by page (interactive)
- **head** - Display first lines of a file
- **tail** - Display last lines of a file

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Exercise 1: Read a File You Created
- Navigate to your `linux_lab/docs` directory
- Read a file with `cat`
- Understand how `cat` displays files

### Exercise 2: Read a System File
- Read `/etc/hostname` with `cat`
- Learn about system files

### Exercise 3: Use `less` to Read a File
- Open `/etc/services` with `less`
- Practice scrolling and navigation
- Learn when to use `less`

### Exercise 4: Read Only Part of a File
- Use `head` to see first lines
- Use `tail` to see last lines
- Understand the difference

### Exercise 5: Permission Denied (Observation Only)
- Try to read `/etc/shadow`
- Observe the error message
- Learn about file permissions

## Important Tips

1. **Read error messages** - they tell you exactly what's wrong
2. **Use `less` for long files** - easier to navigate
3. **Use `head`/`tail` for quick previews** - faster than reading entire file
4. **Don't use sudo** - not needed for this lab
5. **Practice makes perfect** - try reading different files

## Safety Rules

- **Work in your home directory** (`~`) - all exercises are safe there
- **Don't use sudo** - not needed for this lab
- **Read error messages** - they help you understand what went wrong
- **Don't try to fix permission errors** - just observe them

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current file
2. Check the command output - it contains important information
3. Use `man` to read about commands (for example: `man cat`)
4. Read error messages carefully - they explain what went wrong

## Good Luck!

Remember: Reading files is one of the most common tasks in Linux. Master these commands and you'll be able to work with any file!

---

**Linux Course - Day 1**  
**Reading Files Lab**
