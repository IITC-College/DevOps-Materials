# Linux Lab – Script Variables (Variables and Output)

A hands-on lab for using variables and output in bash scripts. You will create backup scripts with dynamic naming and timestamps in a DevOps-style scenario. This lab is **hybrid**: Level 1 is static; Level 2 uses a setup script that creates dummy application logs for you to backup.

## How This Lab Works

- **Level 1:** You create scripts with variables (no setup/cleanup).
- **Level 2:** Before starting Level 2, run the setup script for Clue 1; it creates dummy log files. When done with that clue, run the cleanup script.

Each clue tells you which script to run (if any). Example from `clues/level2/`:

```bash
../../scripts/setup_2_1.sh     # BEFORE: creates dummy logs
cat clue1.txt                  # READ: the clue
../../scripts/cleanup_2_1.sh   # AFTER: removes generated logs
cat clue2.txt                  # NEXT
```

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_variables` first.)

## Prerequisites

- Linux system with bash
- Text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Declare variables in bash (`VAR="value"`) and use them in echo (`$VAR`)
- Use command substitution for dynamic values (`DATE=$(date +%Y-%m-%d)`)
- Build a backup script with variables and timestamped output messages

## Lab Structure

- **Level 1:** Basic variables – hardcoded values, convert to variables, use in output
- **Level 2:** Dynamic variables – dates, timestamped filenames, complete backup script (setup creates logs)

Each clue ends with a **NEXT STEP**. Level 2 Clue 1 uses setup/cleanup scripts.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
