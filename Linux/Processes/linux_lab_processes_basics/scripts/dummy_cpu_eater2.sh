#!/bin/bash
# Lab dummy process - second CPU "heavy" process for variety.
# Throttled with sleep so the system stays responsive (no 100% peg).
# Students find this by name (dummy_cpu_eater2) and by high %CPU.
# Use end_lab.sh to stop it.
while true; do
  :
  sleep 0.1   # yield briefly so CPU doesn't peg at 100%
done
