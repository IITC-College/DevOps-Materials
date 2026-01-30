# Secure Files Project

This directory contains sensitive configuration files and private data.

## Security Policy

All files in this directory were created with **umask 077** to ensure maximum privacy.

## Permissions

With umask 077:
- Files: 666 - 077 = 600 (rw-------)
- Directories: 777 - 077 = 700 (rwx------)

## Access Control

- **Owner**: Full read and write access
- **Group**: No access
- **Others**: No access

## Use Cases

This umask is appropriate for:
- SSH private keys
- Password files
- API keys and secrets
- Personal documents
- Any sensitive data that should never be shared

## Security Requirement

**Only the owner should have any access to these files.**

This is the most restrictive umask, providing maximum security at the cost of collaboration.
