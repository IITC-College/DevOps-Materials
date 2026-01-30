#!/usr/bin/env python3
# Using only keyword arguments for clarity

def send_email(to, subject, body):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("---")

# All keyword arguments
send_email(
    to="admin@example.com",
    subject="System Alert",
    body="Server is running low on disk space"
)

send_email(
    subject="Welcome",
    to="user@example.com",
    body="Welcome to our system!"
)
