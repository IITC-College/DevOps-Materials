# Shared Team Project

This is a collaborative workspace for team members working on a project together.

## Collaboration Policy

All files in this directory were created with **umask 027** to enable team collaboration while maintaining security.

## Permissions

With umask 027:
- Files: 666 - 027 = 640 (rw-r-----)
- Directories: 777 - 027 = 750 (rwxr-x---)

## Access Control

- **Owner**: Full read and write access
- **Group**: Read access (can read files)
- **Others**: No access

## Use Cases

This umask is appropriate for:
- Team project files
- Shared documentation
- Collaborative code repositories
- Group configuration files
- Any files where team members need access but outsiders should not

## Team Policy

**Group members need read access, but only the owner can write. Outsiders have no access.**

This balances security with collaboration - team members can work together while keeping files private from non-team members.
