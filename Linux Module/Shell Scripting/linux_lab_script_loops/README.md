# Linux Lab – Script Loops (for / while)

A hands-on lab for using loops in bash scripts. You will stop copying code and start repeating intelligently: iterate over directories for checks or log rotation, and use a while loop for a retry pattern. This lab is **static** – no setup or cleanup scripts; you create and edit scripts yourself.

## How This Lab Works

Each clue guides you through one skill. You will write for loops over lists and directories, then while loops with counters and a simple retry pattern. All work is done in the lab folder (projects/ and data/ as instructed).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_loops` first.)

## Prerequisites

- Linux system with bash
- Completed or familiar with Script Basics, Variables, and Conditionals labs
- A text editor (nano, vim, or any)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Write a for loop over a list and use the loop variable
- Loop over directories and check existence with `[ -d "$DIR" ]`
- Loop over paths from a file or fixed list
- Write a while loop with a counter (`COUNT`, `$((COUNT+1))`)
- Implement a simple retry pattern (while attempt ≤ MAX, break or exit on success)
- Combine for and while (or document the pattern)

## Lab Structure

- **Level 1:** for – list and variable; loop over dirs with existence check; loop over paths from data
- **Level 2:** while – counter loop; retry pattern; combine or document

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
