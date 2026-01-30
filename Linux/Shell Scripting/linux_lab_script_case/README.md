# Linux Lab – Script Case (Menu and Decision Flow)

A hands-on lab for using the case statement in bash scripts. You will build a clear menu or decision flow: option 1 = disk check, option 2 = uptime, option 3 = exit (and optionally 4 = status), and handle invalid input with `*)`. This lab is **static** – no setup or cleanup scripts; you create and edit scripts yourself.

## How This Lab Works

Each clue guides you through one skill. You will use case on numbers and strings, add a default branch for invalid input, run real commands (df, uptime) from case branches, and wrap actions in functions. All work is done in the lab folder (projects/).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_case` first.)

## Prerequisites

- Linux system with bash
- Completed or familiar with Script Basics, Variables, Input, and Functions labs
- A text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Use case "$VAR" in ... ;; esac for a clear menu or decision flow
- Read a number or string and case on it (1/2/3 or disk/uptime/exit)
- Add a default branch `*)` that echoes "Invalid option" and exits with 1
- Run real commands (df -h ., uptime) from case branches
- Wrap each action in a function and call the function from the case branch
- Build a full menu script with 3–4 options and document when case is better than if/elif

## Lab Structure

- **Level 1:** case syntax – numbers, strings, default branch and exit 1
- **Level 2:** case + real commands – df, uptime; functions; full menu script

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
