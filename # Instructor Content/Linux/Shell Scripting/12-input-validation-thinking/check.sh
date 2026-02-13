#!/bin/bash

# Real case: which service to check?
# What if user presses Enter? Types "webserver" instead of "web"?

read -p "Service to check (web/db/cache): " SERVICE

echo "Checking $SERVICE..."
echo "Status: OK"
# No check: empty? invalid choice? script runs anyway
