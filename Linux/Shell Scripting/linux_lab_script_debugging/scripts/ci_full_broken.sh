#!/bin/bash
# BROKEN - multiple bugs: fix all of them

APP_NAME = "myapp"
CONFIG="config.txt"

if [ -f $CONFIG ]
  echo "Config found."
  echo "CI build complete."
else
  echo "Config not found."
