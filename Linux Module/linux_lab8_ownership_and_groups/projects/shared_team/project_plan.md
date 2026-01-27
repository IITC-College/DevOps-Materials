# Project Plan - Shared Team Project

## Overview

This project demonstrates how teams use Linux ownership and groups for collaboration.

## Ownership Pattern

- **Owner**: Individual team member who created/modified the file
- **Group**: Shared team group (e.g., "developers")
- **Permissions**: Group has read/write access (e.g., `rwxrwx---`)

## Benefits

1. Team members can collaborate on shared files
2. Files are not world-readable (security)
3. Individual ownership is tracked
4. New team members join the group to get access

## Example

File: `-rwxrwx--- alice developers project.txt`

- Alice owns it
- developers group has access
- Any member of "developers" can read/write
- Others cannot access

## Getting Access

New team members get access by:
1. Being added to the "developers" group
2. Files automatically become accessible via group permissions

This is the standard pattern for team collaboration in Linux!
