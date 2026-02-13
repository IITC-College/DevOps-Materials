#!/bin/bash

# Real case: restart production service
# User might type "yes" or "y" or "YES" or nothing - we accept anything

read -p "Restart production service? (yes/no): " CONFIRM

echo "Restarting service..."
echo "Service restarted."
# No check: did they really mean yes? "no" still restarts!
