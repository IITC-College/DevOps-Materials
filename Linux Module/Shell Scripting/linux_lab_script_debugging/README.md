# Linux Lab – Script Debugging (Finding and Fixing Bugs)

A hands-on lab for finding and fixing common bash script errors. You will work with a "broken" CI/CD pipeline – scripts that fail or behave wrongly due to typical mistakes (spaces in assignment, missing quotes, missing then/fi, wrong paths). This lab is **static**: broken scripts and fixed versions are provided; you analyze, fix, and compare.

## How This Lab Works

Each clue presents one or more broken scripts. You run them, see the error or wrong behavior, find the bug, and fix it (or compare with the fixed version in data/configs/fixed/). No setup or cleanup scripts.

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_debugging` first.)

## Prerequisites

- Linux system with bash
- Text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Fix spaces in variable assignment (`APP = "x"` → `APP="x"`)
- Fix missing quotes in conditions (`[ -f $FILE ]` → `[ -f "$FILE" ]`)
- Fix missing `then` or `fi` in if statements
- Fix wrong path references in scripts
- Analyze and fix a complete CI build script with multiple errors

## Lab Structure

- **Level 1:** Common syntax errors – spaces in assignment, missing quotes, missing then
- **Level 2:** Logic and path errors – wrong path, missing fi, complete CI script with multiple bugs

Each clue ends with a **NEXT STEP**. Optional fixed versions are in `data/configs/fixed/` for comparison.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
