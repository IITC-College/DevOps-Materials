#!/bin/bash

# BROKEN - find and fix (real backup script mistakes)

BACKUP_DIR="backup"

if [ ! -d BACKUP_DIR ]; then
  mkdir BACKUP_DIR
  echo "Created backup dir"
else
  echo "Using existing dir"
echo "Backup finished."
