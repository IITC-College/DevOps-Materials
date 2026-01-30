#!/bin/bash
# Lab dummy process - uses CPU so it shows up as "heavy" in top/ps.
# Throttled with sleep so the system stays responsive (no 100% peg).
# Students find this by name (lab-worker / dummy_cpu_eater) and by high %CPU.
while true; do
  :
  sleep 0.1
done
