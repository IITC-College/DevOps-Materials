#!/bin/bash

# Real case: backup path from user
# Empty path? Path with spaces? Non-existent dir?

read -p "Backup target path: " TARGET

echo "Backing up to $TARGET..."
echo "Backup finished."
# No check: empty TARGET? invalid path? dangerous path?
