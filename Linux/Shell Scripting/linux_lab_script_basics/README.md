# Linux Lab – Script Basics (Creation, Permissions, Shebang)

A hands-on lab for understanding how to create, structure, and run bash scripts. You will work as a junior DevOps engineer learning to create and run deployment scripts. This lab is **static** – no setup or cleanup scripts; you create and edit scripts yourself.

## How This Lab Works

Each clue guides you through one skill. You will create scripts, add a shebang line, fix permissions, and run them. All work is done in the lab folder (or a subfolder as instructed).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_basics` first.)

## Prerequisites

- Linux system with bash
- A text editor (nano, vim, or any editor you prefer)

## Duration

25–35 minutes

## Learning Objectives

After this lab you will be able to:

- Create a simple bash script with echo statements
- Add a shebang line (`#!/bin/bash`) and understand why it matters
- Check file permissions with `ls -l`
- Make a script executable with `chmod +x`
- Run a script with `./script.sh` and understand the difference from `bash script.sh`

## Lab Structure

- **Level 1:** First steps – create a script, add shebang, try to run (encounter permission denied)
- **Level 2:** Making scripts executable – check permissions, chmod +x, run successfully

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
