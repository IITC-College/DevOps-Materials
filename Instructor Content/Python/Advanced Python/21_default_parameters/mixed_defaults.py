#!/usr/bin/env python3
# Mixing required and default parameters

def send_notification(recipient, message, priority="normal", send_email=True):
    print(f"To: {recipient}")
    print(f"Message: {message}")
    print(f"Priority: {priority}")
    print(f"Send Email: {send_email}")
    print("---")

# Required parameters must be provided
send_notification("admin@example.com", "Server down")

# Override defaults
send_notification("user@example.com", "Update available", priority="low")

# Override multiple defaults
send_notification("ops@example.com", "Critical alert", priority="high", send_email=True)
