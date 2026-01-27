# User Application

This is a user application that should NOT require sudo to run.

## Problem Scenario

The files in this directory are currently owned by root, but this is YOUR
application. You should be able to work with these files without sudo.

## The Issue

Currently, you need sudo to read or modify these files:
- config.txt - Application configuration
- install.sh - Installation script

This is a DESIGN PROBLEM, not a legitimate sudo requirement.

## The Solution

Instead of using `sudo cat config.txt` every time, you should:
1. Fix the ownership ONCE: `sudo chown $USER:$USER config.txt`
2. Then work normally without sudo

## Key Principle

Use sudo to FIX the problem (change ownership), not to work around it
(using sudo repeatedly).

## Exercise

1. Try to read config.txt without sudo (will fail)
2. Check the ownership: `ls -l config.txt`
3. Fix the ownership: `sudo chown $USER:$USER config.txt`
4. Now read it without sudo (should work!)

This demonstrates the principle: Fix the root cause, don't work around it.
