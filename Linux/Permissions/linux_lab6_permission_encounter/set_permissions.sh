#!/bin/bash
# Script to set permissions for Permission Encounter Lab
# This should be run on a Linux system after extracting the archive

cd "$(dirname "$0")"

# Set permissions for data/files/
chmod 644 data/files/public_data.txt          # rw-r--r--
chmod 664 data/files/team_notes.txt            # rw-rw-r--
chmod 600 data/files/private_log.txt           # rw-------
chmod 666 data/files/shared_report.txt         # rw-rw-rw-
chmod 444 data/files/readonly_archive.txt      # r--r--r--
chmod 600 data/files/private_notes.txt         # rw-------
chmod 755 data/files/report.sh                 # rwxr-xr-x

# Set permissions for data/logs/
chmod 644 data/logs/system.log                 # rw-r--r--

# Set permissions for data/secrets/
chmod 644 data/secrets/tips.txt                # rw-r--r--

# Set permissions for projects/personal_project/
chmod 700 projects/personal_project/my_script.sh  # rwx------
chmod 600 projects/personal_project/my_notes.txt  # rw-------
chmod 644 projects/personal_project/README.md     # rw-r--r--

# Set permissions for projects/team_project/
chmod 770 projects/team_project/team_script.sh    # rwxrwx---
chmod 660 projects/team_project/config.json       # rw-rw----
chmod 664 projects/team_project/logs.txt          # rw-rw-r--

# Set permissions for projects/shared_project/
chmod 664 projects/shared_project/shared_doc.txt  # rw-rw-r--

# Set permissions for restricted/ (these should be owned by root in real scenario)
# For lab purposes, we'll set restrictive permissions but note that ownership
# will depend on who extracts the archive
chmod 600 restricted/admin_config.txt          # rw-------
chmod 400 restricted/secret_file.txt           # r--------
chmod 600 restricted/backup.tar.gz             # rw-------

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
echo "Note: File ownership will depend on who extracts the archive."
echo "For the lab to work as designed, you may need to adjust ownership"
echo "using chown, or the lab will work with the extracting user's permissions."
