# Default Application Project

This directory contains files for a standard web application.

## Default Policy

All files in this directory were created with **umask 022**, which is the most common default on Linux systems.

## Permissions

With umask 022:
- Files: 666 - 022 = 644 (rw-r--r--)
- Directories: 777 - 022 = 755 (rwxr-xr-x)

## Access Control

- **Owner**: Full read and write access
- **Group**: Read access
- **Others**: Read access

## Use Cases

This umask is appropriate for:
- Web server files (need to be readable by web server)
- Public documentation
- Shared resources
- Application files that need broad read access
- Less sensitive data

## Trade-off

**Files are readable by everyone, which is convenient but less secure.**

This is the most permissive common umask. Use it when files need to be accessible to many users or services, but be aware that others can read your files.
