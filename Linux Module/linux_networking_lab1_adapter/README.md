# Linux Networking Debug Lab

A hands-on lab for diagnosing and fixing real-world Linux networking issues.

## Lab Overview

This lab presents **9 different networking problems** across 3 difficulty levels. Students must use systematic debugging techniques to identify and resolve each issue.

### Scenarios Covered

| Level | Clue | Scenario | Skills |
|-------|------|----------|--------|
| 1 | 1 | Interface DOWN | `ip link`, interface state |
| 1 | 2 | No IP address | `ip addr`, DHCP, static IP |
| 1 | 3 | Missing gateway | `ip route`, default gateway |
| 2 | 1 | DNS misconfigured | `/etc/resolv.conf`, nameservers |
| 2 | 2 | UFW blocks SSH | `ufw`, incoming firewall rules |
| 2 | 3 | UFW blocks HTTP/S | `ufw`, outgoing firewall rules |
| 3 | 1 | Wrong MTU | MTU, packet fragmentation |
| 3 | 2 | Bad static route | Routing table, specific routes |
| 3 | 3 | /etc/hosts override | Local name resolution |

## Instructor Setup

**IMPORTANT**: Before each clue, run the corresponding break script to create the bug.

### Option A: Individual Scripts (Recommended)

```bash
cd scripts/

# Level 1
sudo ./setup_1_1.sh    # Before clues/level1/clue1.txt
sudo ./setup_1_2.sh    # Before clues/level1/clue2.txt
sudo ./setup_1_3.sh    # Before clues/level1/clue3.txt

# Level 2
sudo ./setup_2_1.sh    # Before clues/level2/clue1.txt
sudo ./setup_2_2.sh    # Before clues/level2/clue2.txt (use console!)
sudo ./setup_2_3.sh    # Before clues/level2/clue3.txt

# Level 3
sudo ./setup_3_1.sh    # Before clues/level3/clue1.txt
sudo ./setup_3_2.sh    # Before clues/level3/clue2.txt (use console!)
sudo ./setup_3_3.sh    # Before clues/level3/clue3.txt

# Restore everything
sudo ./restore_all.sh
```

### Option B: Main Script with Arguments

```bash
sudo ./setup_environment.sh <level> <clue>
```

Examples:
```bash
sudo ./setup_environment.sh 1 1   # Before Level 1, Clue 1 (interface DOWN)
sudo ./setup_environment.sh 2 2   # Before Level 2, Clue 2 (UFW blocks SSH)
sudo ./setup_environment.sh 3 3   # Before Level 3, Clue 3 (/etc/hosts)
```

### Console Access Required

Some scenarios will drop SSH:
- **1-1** (interface DOWN): Drops all network connectivity
- **2-2** (UFW blocks SSH): Blocks new SSH connections

For these, ensure students have **VM console access** (VirtualBox, VMware, or cloud console).

## Student Instructions

1. Start with `cat start_here.txt`
2. Navigate to `clues/level1/clue1.txt`
3. Follow the 4-step methodology for each scenario:
   - **OBSERVE**: Note symptoms and error messages
   - **INSPECT**: Gather evidence with diagnostic commands
   - **DIAGNOSE**: Identify root cause
   - **RESOLVE**: Apply fix and verify

## Prerequisites

- Linux VM (Ubuntu/Debian recommended)
- Root or sudo access
- UFW installed (`apt install ufw`)
- Console access for SSH-breaking scenarios

## File Structure

```
linux_networking_lab1_adapter/
├── README.md                     # This file
├── start_here.txt                # Student entry point
├── setup_environment.sh          # Main break script (accepts level + clue args)
├── scripts/                      # Individual setup scripts (one per clue)
│   ├── setup_1_1.sh              # Setup for Level 1, Clue 1
│   ├── setup_1_2.sh              # Setup for Level 1, Clue 2
│   ├── setup_1_3.sh              # Setup for Level 1, Clue 3
│   ├── setup_2_1.sh              # Setup for Level 2, Clue 1
│   ├── setup_2_2.sh              # Setup for Level 2, Clue 2
│   ├── setup_2_3.sh              # Setup for Level 2, Clue 3
│   ├── setup_3_1.sh              # Setup for Level 3, Clue 1
│   ├── setup_3_2.sh              # Setup for Level 3, Clue 2
│   ├── setup_3_3.sh              # Setup for Level 3, Clue 3
│   └── restore_all.sh            # Restore system to normal
├── clues/
│   ├── level1/
│   │   ├── clue1.txt             # Interface DOWN
│   │   ├── clue2.txt             # No IP address
│   │   └── clue3.txt             # Missing gateway
│   ├── level2/
│   │   ├── clue1.txt             # DNS misconfigured
│   │   ├── clue2.txt             # UFW blocks SSH
│   │   └── clue3.txt             # UFW blocks HTTP/HTTPS
│   └── level3/
│       ├── clue1.txt             # Wrong MTU
│       ├── clue2.txt             # Bad static route
│       └── clue3.txt             # /etc/hosts override
├── data/
│   ├── logs/                     # State snapshots (created by script)
│   ├── backups/                  # Config backups (created by script)
│   └── secrets/
│       └── tips.txt              # Debugging hints
└── .answers/
    └── solutions.txt             # Complete solutions
```

## Learning Objectives

After completing this lab, students will be able to:

1. Diagnose interface/link layer issues
2. Troubleshoot IP addressing problems
3. Configure routing and gateways
4. Debug DNS resolution issues
5. Manage UFW firewall rules
6. Understand MTU and its effects
7. Identify routing table problems
8. Understand name resolution order (/etc/hosts vs DNS)

## Estimated Duration

- Level 1: 20-30 minutes
- Level 2: 30-40 minutes
- Level 3: 30-45 minutes
- **Total**: 1.5-2 hours

## Restoring the System

After completing the lab or if things go wrong:

```bash
# Restore network interface
sudo ip link set <iface> up
sudo dhclient <iface>

# Restore MTU
sudo ip link set <iface> mtu 1500

# Restore DNS (from backup)
sudo cp data/backups/resolv.conf.bak /etc/resolv.conf

# Restore hosts (from backup)
sudo cp data/backups/hosts.bak /etc/hosts

# Reset UFW
sudo ufw --force reset
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw --force enable
```

## Version

- **Version**: 1.0
- **Created**: 2026-01-29
- **Repository**: https://github.com/IITC-College/DevOps-Jan26
