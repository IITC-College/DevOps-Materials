# Linux Lab – Processes Basics (What is a Process)

A hands-on lab for understanding what a process is and how to read process output without being overwhelmed. This lab uses **dummy processes** (started by a setup script) so you have a real, controlled scenario to find and observe – like the networking lab.

## How This Lab Works

Each clue has **two scripts**:
- **SETUP** – Run BEFORE starting the clue (starts dummy processes for that clue)
- **CLEANUP** – Run AFTER finishing the clue (stops those dummy processes)

This way, dummy processes only run during the clue (not between clues).

Example flow for Level 1, Clue 1 (you are in `clues/level1/`):

```bash
../../scripts/setup_1_1.sh     # BEFORE: start processes
cat clue1.txt                   # READ: the clue and do the exercise
../../scripts/cleanup_1_1.sh   # AFTER: stop processes
cat clue2.txt                   # NEXT: move to next clue
```

Each clue file tells you which scripts to run. You haven't learned how to stop processes yet – the cleanup scripts do it for you.

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_processes_basics` first.)

## Prerequisites

- Linux system with `ps` and `top` (standard on most distributions)
- `htop` is optional; exercises work with `top` alone

## Duration

40–45 minutes

## Learning Objectives

After this lab you will be able to:

- Explain that a **process** is a program running in memory
- List processes with `ps` and `ps aux`
- Know **where to look** in the output: PID, user, command (you don’t need to understand every column)
- Use `top` and `htop` to see live process activity
- Find a "heavy" process (high CPU or RAM) and identify its PID, user, and which resource is high
- Exit `top` and `htop` correctly (press `q`)
- Understand that processes have a **parent** (PPID) and can have **children**
- Relate high CPU or RAM in `top` to "a process consuming resources"

## Instructor Notes

Students run setup and cleanup scripts for each clue (paths in the clue files). No global setup or cleanup needed – each clue is isolated.

## Lab Structure

- **Level 1:** What is a process? `ps`, PID, user
- **Level 2:** `top` and `htop` – where to look, finding a heavy process
- **Level 3:** Parent/child (PPID) and synthesis

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt` (e.g. where to look in `top`).

## Version

- **Version:** 1.0  
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
