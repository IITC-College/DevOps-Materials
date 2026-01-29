#!/bin/bash
# BROKEN - find and fix: wrong path (config is in ../data/configs/build_config.txt)

CONFIG="config.txt"

if [ -f "$CONFIG" ]; then
  echo "Config found."
else
  echo "Config not found."
fi
