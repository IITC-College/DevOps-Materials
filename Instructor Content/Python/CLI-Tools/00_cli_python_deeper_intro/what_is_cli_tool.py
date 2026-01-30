#!/usr/bin/env python3
# What is a CLI tool?

"""
CLI = Command-Line Interface

A CLI tool is a program that:
- Runs in a terminal/command prompt
- Takes input from command-line arguments
- Produces output to the terminal
- Can be automated in scripts

EXAMPLES OF CLI TOOLS:

System tools:
  ls, cd, pwd, mkdir, rm (Linux/Mac)
  dir, cd, mkdir, del (Windows)

Development tools:
  git, npm, pip, docker
  python, node, java

DevOps tools:
  kubectl, terraform, ansible
  aws, gcloud, az (cloud CLIs)

WHY BUILD CLI TOOLS?

1. AUTOMATION
   - Can be called from scripts
   - No human interaction needed
   - Easy to schedule (cron, Task Scheduler)

2. EFFICIENCY
   - Faster than GUI for repetitive tasks
   - Power users love them
   - Can pipe output to other tools

3. REMOTE USE
   - Works over SSH
   - No graphics needed
   - Minimal bandwidth

4. INTEGRATION
   - Easy to integrate with other tools
   - Output can be parsed
   - Chains with pipes and redirects

ANATOMY OF A CLI COMMAND:

  git commit -m "message" file.txt
  │   │      │  │         │
  │   │      │  │         └─ argument (positional)
  │   │      │  └─ option value
  │   │      └─ option/flag
  │   └─ subcommand
  └─ program name

TYPES OF CLI TOOLS:

1. System utilities (ls, grep, find)
2. Build tools (make, webpack, npm)
3. Version control (git, svn)
4. Package managers (pip, npm, apt)
5. Cloud/DevOps (kubectl, terraform)
6. Custom automation (your scripts!)
"""

print("CLI Tool = Command-Line Interface Tool")
print("\nA program that runs in a terminal and:")
print("  - Takes command-line arguments")
print("  - Processes data/performs tasks")
print("  - Returns output and exit codes")
print("\nExamples: git, docker, aws, kubectl")
