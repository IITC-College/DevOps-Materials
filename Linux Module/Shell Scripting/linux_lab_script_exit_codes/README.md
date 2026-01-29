# Linux Lab – Script Exit Codes (exit 0 / exit 1, $?)

A hands-on lab for using exit codes in bash scripts. You will learn that output is for humans and exit codes are for systems and CI: script returns 0 on success, 1 on failure; callers check `$?`. This lab is **static** – no setup or cleanup scripts; you create and edit scripts yourself.

## How This Lab Works

Each clue guides you through one skill. You will write scripts that exit 0 or 1 based on a check (e.g. directory or file exists), observe `$?`, use `&&` and `||` from the command line, chain two steps (fail fast), and build a wrapper that passes through the exit code. All work is done in the lab folder (projects/ and optional scripts/).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_exit_codes` first.)

## Prerequisites

- Linux system with bash
- Completed or familiar with Script Basics, Conditionals, and Case labs
- A text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Use `exit 0` on success and `exit 1` on failure
- Check the last exit code with `echo $?`
- Use `./script.sh && echo "Success" || echo "Failed"` from the command line (exit code drives &&/||)
- Chain two steps: if first fails, exit 1 and do not run the second; if both pass, exit 0
- Write a wrapper script that runs another script, captures `CODE=$?`, echoes it, and exits with that code (pass-through)
- Explain why CI/CD cares about exit codes (green/red, abort on non-zero)

## Lab Structure

- **Level 1:** Concept – check dir/file, exit 0/1, observe $?, use &&/||
- **Level 2:** Practice – chain two steps, wrapper pass-through, pipeline and document CI/CD

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
