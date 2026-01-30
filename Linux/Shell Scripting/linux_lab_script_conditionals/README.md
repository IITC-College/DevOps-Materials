# Linux Lab – Script Conditionals (if/then/else and File Checks)

A hands-on lab for using conditionals in bash scripts. You will build environment validation scripts for deployment (prod vs staging) in a DevOps-style scenario. This lab is **static** – no setup or cleanup scripts; you create and edit scripts using pre-created environment configs and directories.

## How This Lab Works

Each clue guides you through one conditional skill. You will check if files and directories exist, validate input (e.g. environment name), and build a pre-deployment validation script. All work is done in the lab folder using the provided data (environments, configs).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_conditionals` first.)

## Prerequisites

- Linux system with bash
- Text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Check if a file exists with `[ -f "$FILE" ]`
- Check if a directory exists with `[ -d "$DIR" ]`
- Check if a variable is empty with `[ -z "$VAR" ]`
- Use if/then/else/fi in bash
- Validate environment name (e.g. prod or staging only)
- Create a directory only if it doesn't exist (`mkdir -p` or conditional mkdir)

## Lab Structure

- **Level 1:** Basic conditionals – file exists, directory exists, input empty
- **Level 2:** Practical logic – validate environment name, conditional mkdir, pre-deployment validation script

Each clue ends with a **NEXT STEP**.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
