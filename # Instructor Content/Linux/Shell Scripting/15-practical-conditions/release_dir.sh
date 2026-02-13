#!/bin/bash

# Real case: release dir for build output - create with date

RELEASE_BASE="releases"
DATE=$(date +%Y-%m-%d)
RELEASE_DIR="$RELEASE_BASE/$DATE"

if [ ! -d "$RELEASE_DIR" ]; then
  mkdir -p "$RELEASE_DIR"
  echo "Created $RELEASE_DIR for today's release."
else
  echo "Using existing $RELEASE_DIR"
fi

echo "Release dir: $RELEASE_DIR"
