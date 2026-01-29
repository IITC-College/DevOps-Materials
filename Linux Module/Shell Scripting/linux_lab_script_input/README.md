# Linux Lab – Script Input (User Input with read)

A hands-on lab for reading user input in bash scripts. You will build an interactive health-check script for multiple services in a DevOps-style monitoring scenario. This lab is **hybrid**: Level 1 Clue 2 and Level 2 Clue 1 use setup scripts that start dummy services for you to "check."

## How This Lab Works

- **Level 1:** You create scripts with read (no setup for Clue 1; Clue 2 uses setup for a dummy web service).
- **Level 2:** Clue 1 uses setup for a dummy database service. Each clue that uses setup tells you to run the setup script first and the cleanup script when done.

Example from `clues/level1/` (Clue 2):

```bash
../../scripts/setup_1_2.sh     # BEFORE: starts dummy web service
cat clue2.txt                   # READ: the clue
../../scripts/cleanup_1_2.sh    # AFTER: stops the service
cat clue3.txt                   # NEXT
```

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_input` first.)

## Prerequisites

- Linux system with bash
- Text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Use `read` to get input from the user
- Use `read -p "prompt" VAR` for a prompt and variable in one line
- Display input back to the user (echo confirmation)
- Understand why empty input can be a problem (validation thinking)

## Lab Structure

- **Level 1:** Basic input – read, read -p, echo confirmation (Clue 2: dummy web service)
- **Level 2:** Input validation thinking – test empty input, document findings (Clue 1: dummy database service)

Each clue ends with a **NEXT STEP**. Clues that use setup/cleanup say so at the top and bottom.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
