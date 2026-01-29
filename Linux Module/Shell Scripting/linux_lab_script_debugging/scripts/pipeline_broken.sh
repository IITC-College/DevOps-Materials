#!/bin/bash
# BROKEN - find and fix: missing fi

echo "Pipeline started."

if [ -f "../data/configs/build_config.txt" ]; then
  echo "Config OK."
else
  echo "Config missing."

echo "Pipeline step complete."
