#!/bin/bash
# Lab dummy process - uses RAM so it shows up as "heavy" in top (%MEM).
# Allocates a fixed amount (~10MB), then sleeps so it uses almost no CPU.
# Students find this by name (dummy_ram_eater) and by high %MEM.
# Use end_lab.sh to stop it.
LAB_RAM_CHARS=10000000   # ~10MB string; safe on low-RAM VMs
s=$(printf '%*s' "$LAB_RAM_CHARS" '')
while true; do
  sleep 9999
done
