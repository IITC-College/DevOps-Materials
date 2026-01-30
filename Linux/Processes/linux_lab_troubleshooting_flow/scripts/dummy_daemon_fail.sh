#!/bin/bash
# Failing daemon for troubleshooting lab – exits with error after 1 second.
# Students see "failed" status and check journalctl for the reason.
echo "lab-troubleshoot: starting then exiting with error (simulated failure)"
sleep 1
exit 1
