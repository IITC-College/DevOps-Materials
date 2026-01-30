# Linux Lab – Mini DevOps Tool (Capstone)

A hands-on lab for building one script that combines: case menu, functions, at least one loop, system commands (date, uptime, df, free), and reliable exit codes. This is the **capstone** lab and matches the home lab requirement: a Mini DevOps Automation Tool that works, returns clear output, and can plug into CI/CD later. This lab is **static** – no setup or cleanup scripts; you build the tool in projects/.

## How This Lab Works

Each clue guides you through one part of the tool. You will add a case menu (check, status, backup, pipeline, exit), implement functions (show_status with date/uptime/df/free, check_services with a for loop, backup_now, run_pipeline), and ensure every branch exits 0 on success and the default branch exits 1 on invalid input. All work is done in the lab folder (projects/).

## Direct Entry

Start the lab with:

```bash
cd clues/level1 && cat clue1.txt
```

(Extract the lab if needed, then `cd linux_lab_script_mini_devops_tool` first.)

## Prerequisites

- Linux system with bash
- Completed or familiar with Loops, Functions, Case, and Exit Codes labs
- A text editor (nano, vim, or any)

## Duration

35–45 minutes (capstone)

## Learning Objectives

After this lab you will be able to:

- Build a case menu with actions: check, status, backup, pipeline, exit
- Implement show_status() using date, uptime, df -h ., free -h (or subset)
- Implement check_services() with a for loop over service names (e.g. nginx, app, db)
- Implement backup_now() and run_pipeline() (simulated)
- Ensure every case branch ends with exit 0 and the default branch with exit 1
- Deliver a script that has: at least one loop, at least one function, one case menu, clear output, and exit 0/1 appropriately

## Lab Structure

- **Level 1:** Menu + functions – case menu, show_status (date/uptime/df/free), check_services (for loop)
- **Level 2:** Integration – backup and pipeline functions, exit 0/1 in every branch, final checklist

Each clue ends with a **NEXT STEP** telling you exactly where to go next.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
