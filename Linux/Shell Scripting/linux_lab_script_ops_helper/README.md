# Linux Lab – Ops Helper Script (Full Integration)

A hands-on lab for building a multi-function DevOps utility script. You will combine variables, user input, and conditionals into one script that offers deploy, check, and backup actions. This lab is **dynamic**: a setup script creates a realistic operational environment (services, logs, configs) for Level 1; you build and refine the ops helper script in projects/.

## How This Lab Works

- **Level 1:** Run setup_1_1.sh before starting – it creates dummy services, logs, and configs. You build a script that accepts an action (deploy/check/backup) and uses if/elif/else. Run cleanup_1_1.sh when done with Level 1.
- **Level 2:** You add variables, confirmation prompts, and complete the ops helper v1. No additional setup required.

Each clue that uses setup says so at the top and bottom.

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_ops_helper` first.)

## Prerequisites

- Linux system with bash
- Text editor (nano, vim, or any)
- Completed or familiar with Script Basics, Variables, Input, and Conditionals labs

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Create a script that accepts an action choice (deploy/check/backup)
- Use if/elif/else to handle multiple actions
- Add input validation (empty check, unknown action)
- Add variables for app names and paths
- Add confirmation prompts for dangerous operations
- Build a complete ops helper v1 that ties all concepts together

## Lab Structure

- **Level 1:** Basic menu – action choice, if/elif/else, validation (setup creates environment)
- **Level 2:** Full integration – variables, confirmation, complete ops helper v1

Each clue ends with a **NEXT STEP**. Level 1 uses setup_1_1.sh and cleanup_1_1.sh.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
