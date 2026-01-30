# Linux Lab – Process Management (kill)

A hands-on lab for understanding the `kill` command: how to stop a process in a controlled way, and when to use `kill -9`.

## How This Lab Works

Each clue has **two scripts**:
- **SETUP** – Run **before** starting the clue (starts dummy processes)
- **CLEANUP** – Run **after** finishing the clue (stops those processes)

This way, dummy processes only run during the clue.

Example for Level 1, Clue 1 (you are in `clues/level1/`):

```bash
../../scripts/setup_1_1.sh     # BEFORE: start processes
cat clue1.txt                   # READ: the clue and do the exercise
../../scripts/cleanup_1_1.sh   # AFTER: stop processes
cat clue2.txt                   # NEXT: move to next clue
```

Each clue file tells you which scripts to run.

## Direct Entry

This lab has no start_here.txt. Start directly at the first clue:

```bash
cd clues/level1 && cat clue1.txt
```

(After extracting the lab, run `cd linux_lab_processes_kill` first.)

## Prerequisites

- Linux system with `ps` and `kill` (standard on most distributions)
- Recommended: complete "Processes Basics" lab first (understanding PID, ps)

## Duration

20–25 minutes

## Learning Objectives

After this lab you will be able to:

- Understand that `kill` sends a **request** (signal), not "violence"
- Know that default `kill` is SIGTERM (signal 15) – graceful shutdown
- Know when to use `kill -9` (SIGKILL) – **only as a last resort** ("pulling the power plug")
- Identify the PID of running processes
- Understand risks of force-killing (data loss, corruption)
- Follow the right order: try gentle `kill` first, then `kill -9` only if needed

## Lab Structure

- **Level 1:** What is kill? Controlled stopping, SIGTERM, stopping multiple processes
- **Level 2:** kill -9, when it is dangerous, real-world scenario

Each clue ends with a **NEXT STEP** pointing to the next clue.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0  
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
