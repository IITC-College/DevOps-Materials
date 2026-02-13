#!/bin/bash

# Before: ls -l deploy.sh  (see -rw-r--r-- no x)
# After:  chmod +x deploy.sh  (add execute)
# Then:   ls -l deploy.sh  (see -rwxr-xr-x)
# Now:    ./deploy.sh  works!

echo "Deploying..."
echo "App deployed"
