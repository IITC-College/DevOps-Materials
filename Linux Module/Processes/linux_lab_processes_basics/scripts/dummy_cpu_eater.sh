#!/bin/bash
# Lab dummy process - uses CPU so it shows up as "heavy" in top.
# Throttled with sleep so the system stays responsive (no 100% peg).
# Students find this by name (dummy_cpu_eater) and by high %CPU.
# Use end_lab.sh to stop it.
while true; do
  :    # busy work
  sleep 0.1   # yield briefly so CPU doesn't peg at 100%
done
