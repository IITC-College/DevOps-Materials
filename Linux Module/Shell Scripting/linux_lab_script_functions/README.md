# Linux Lab – Script Functions (Define, $1, Call from Loops)

A hands-on lab for defining and using functions in bash scripts. You will stop spreading logic everywhere and start organizing it: reusable steps per tier (frontend, api, worker) or per service, and call functions from a loop. This lab is **static** – no setup or cleanup scripts; you create and edit scripts yourself.

## How This Lab Works

Each clue guides you through one skill. You will define functions that take one argument (`$1`), call them from the main script and from a for loop, and build a small "deploy tiers" script. All work is done in the lab folder (projects/).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_functions` first.)

## Prerequisites

- Linux system with bash
- Completed or familiar with Script Basics, Variables, Conditionals, and Loops labs
- A text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Define a function with `name() { ... }` and use `$1` for the first argument
- Call a function with an argument: `check_dir logs`
- Use a function to print a uniform status header (e.g. timestamp + message)
- Loop over tier names and call a function with the current tier as `$1`
- Build a "deploy tiers" script with one function and a for loop (no code duplication)
- Explain why functions help (one place to change logic)

## Lab Structure

- **Level 1:** Basics – check_dir with $1; function that echoes status; uniform header function
- **Level 2:** Functions + loops – loop over tiers, call function; function with two steps; deploy tiers script

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
