#!/bin/bash
# BROKEN - find and fix: missing quotes in [ -f $CONFIG ]

CONFIG="../data/configs/build_config.txt"

if [ -f $CONFIG ]; then
  echo "Config found."
else
  echo "Config not found."
fi
