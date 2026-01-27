#!/bin/bash
# Script to set permissions for Why Script Doesn't Run Lab
# This should be run on a Linux system after extracting the archive

cd "$(dirname "$0")"

# Set permissions for scripts/broken/ (NO execute - these are broken!)
chmod 644 scripts/broken/hello.sh          # rw-r--r-- (no x)
chmod 644 scripts/broken/backup.sh         # rw-r--r-- (no x)
chmod 644 scripts/broken/deploy.sh         # rw-r--r-- (no x)
chmod 600 scripts/broken/cleanup.sh        # rw------- (no x)
chmod 600 scripts/broken/private_script.sh  # rw------- (no x)
chmod 664 scripts/broken/team_script.sh    # rw-rw-r-- (no x)
chmod 664 scripts/broken/shared_tool.sh    # rw-rw-r-- (no x)

# Set permissions for scripts/fixed/ (WITH execute - these are examples)
chmod 755 scripts/fixed/example.sh         # rwxr-xr-x (has x)
chmod 755 scripts/fixed/reference.sh       # rwxr-xr-x (has x)

# Set permissions for projects/web_app/ (NO execute - broken scripts)
chmod 644 projects/web_app/start.sh        # rw-r--r-- (no x)
chmod 644 projects/web_app/stop.sh         # rw-r--r-- (no x)
chmod 664 projects/web_app/deploy.sh       # rw-rw-r-- (no x)
chmod 600 projects/web_app/config.sh       # rw------- (no x - config file!)

# Set permissions for projects/automation/ (NO execute - broken scripts)
chmod 644 projects/automation/daily_backup.sh      # rw-r--r-- (no x)
chmod 644 projects/automation/weekly_report.sh    # rw-r--r-- (no x)
chmod 600 projects/automation/cleanup_old_files.sh # rw------- (no x)

# Set permissions for data/configs/ (NO execute - config files!)
chmod 644 data/configs/app.conf            # rw-r--r-- (no x, correct)
chmod 644 data/configs/settings.json       # rw-r--r-- (no x, correct)

# Set permissions for data/logs/ (NO execute - log file!)
chmod 644 data/logs/system.log             # rw-r--r-- (no x, correct)

# Set permissions for clue files (all readable)
chmod 644 clues/level1/*.txt
chmod 644 clues/level2/*.txt
chmod 644 clues/level3/*.txt

# Set permissions for documentation
chmod 644 README.md
chmod 644 start_here.txt

# Set permissions for solutions (should be readable by instructor)
chmod 644 .answers/solutions.txt

echo "Permissions set successfully!"
echo ""
echo "Note: Scripts in scripts/broken/ and projects/ do NOT have execute"
echo "permission - students will add it during the lab."
echo ""
echo "Scripts in scripts/fixed/ have execute permission as examples."
