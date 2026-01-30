#!/bin/bash
# Dummy process that ignores SIGTERM - requires kill -9 to stop.
trap '' TERM
while true; do sleep 1; done
