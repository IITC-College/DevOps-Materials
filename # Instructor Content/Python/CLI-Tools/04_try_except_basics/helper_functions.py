#!/usr/bin/env python3
# Helper functions module

import datetime

def get_timestamp():
    """Return current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_message(message, prefix="INFO"):
    """Return a formatted message with timestamp"""
    timestamp = get_timestamp()
    return f"[{timestamp}] [{prefix}] {message}"

def validate_command(cmd, valid_commands):
    """Return True if command is valid"""
    return cmd in valid_commands

def show_config(cfg):
    """Display configuration using loop"""
    print("Configuration:")
    for key, value in cfg.items():
        print(f"  {key}: {value}")

def print_header(char="=", length=40):
    """Print a header line"""
    print(char * length)
