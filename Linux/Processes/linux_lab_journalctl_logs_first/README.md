# Linux Lab – Logs-First: journalctl

A hands-on lab for thinking **"before guessing – logs"**. You will use `journalctl` to view system logs, filter by service, find errors, and – most importantly – **describe problems in words** like a DevOps professional.

## How This Lab Works

Each clue has **two scripts**:
- **SETUP** – Run BEFORE starting the clue (starts dummy services that generate log entries for that clue)
- **CLEANUP** – Run AFTER finishing the clue (stops those services)

This way, lab services only run during the clue (not between clues).

Example flow for Level 1, Clue 1 (you are in `clues/level1/`):

```bash
../../scripts/setup_1_1.sh     # BEFORE: start service
cat clue1.txt                 # READ: the clue and do the exercise
../../scripts/cleanup_1_1.sh  # AFTER: stop service
cat clue2.txt                 # NEXT: move to next clue
```

Each clue file tells you which scripts to run. Services run under your user (no sudo needed).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_journalctl_logs_first` first.)

## Prerequisites

- Linux system with **systemd** (most modern distributions: Ubuntu, Debian, Fedora, etc.)
- `journalctl` available (part of systemd)

## Duration

45–50 minutes

## Learning Objectives

After this lab you will be able to:

- Explain what a **log** is and why it is the most reliable source when troubleshooting
- Use `journalctl` to view system logs and not get lost in the output
- Filter logs by service: `journalctl -u <service>` and `journalctl --user -u <service>`
- Use `journalctl -xe` for recent errors with context
- Find an error line in logs and understand: **what** happened, **when**, and **which** service
- **Describe a problem in words** (not just copy an error line) – the key DevOps skill

## Lab Structure

- **Level 1:** What are logs? Basic journalctl, filter by service, find your first error and describe it
- **Level 2:** journalctl -xe, time-based and priority filtering, complex scenario – describe like a DevOps

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt` (e.g. how to navigate journalctl output).

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
