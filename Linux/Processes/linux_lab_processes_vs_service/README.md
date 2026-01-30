# Linux Lab – Process vs Service

A conceptual lab for understanding the difference between a **process** (what is running) and a **service** (what should be running, managed by systemd).

## How This Lab Works

This lab has **no setup or cleanup scripts**. You observe the system as-is. Each clue asks you to run a few observation commands and think about the concepts.

- **Level 1:** Process = what is running (recap and consequences).
- **Level 2:** Service = what should be running; systemd manages it; if the process dies, the service can restart it.

## Direct Entry

This lab has no start_here.txt. Start directly at the first clue:

```bash
cd clues/level1 && cat clue1.txt
```

(After extracting the lab, run `cd linux_lab_processes_vs_service` first.)

## Prerequisites

- Linux system with `ps` and `systemctl` (standard on systemd-based distributions)
- Recommended: complete "Processes Basics" and "Process Management (kill)" labs first

## Duration

20–25 minutes

## Learning Objectives

After this lab you will be able to:

- State that a **process** is what is currently running (program in memory, PID).
- State that a **service** is what *should* be running and is managed by systemd.
- Explain that one service can have an associated process (or processes); "the service is running" means systemd started and is tracking that process.
- Explain that if the process dies, systemd can restart it so the service stays "running" (conceptual understanding).

## Lab Structure

- **Level 1:** Process = what is running; processes can disappear; no single "manager."
- **Level 2:** Service managed by systemd; service vs process; restart behavior.

Each clue ends with a **NEXT STEP** pointing to the next clue.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0  
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
