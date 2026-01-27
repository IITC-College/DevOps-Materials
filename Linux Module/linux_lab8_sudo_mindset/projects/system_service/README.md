# System Service

This is a system service that legitimately requires sudo.

## Legitimate sudo Use

This service needs to:
- Modify system-wide configuration
- Install files in system directories (/etc, /usr, etc.)
- Manage system services

This is a LEGITIMATE use of sudo because it's a system-level operation.

## The Difference

Unlike user_app, this service:
- Affects the entire system
- Modifies system configuration
- Requires administrative privileges
- sudo is appropriate here

## Key Principle

sudo is legitimate for:
- System administration tasks
- Installing system services
- Modifying system configuration
- Managing system-wide resources

## Exercise

1. Read the install.sh script
2. Understand why it needs sudo (system-level operations)
3. Compare with user_app - what's the difference?

This demonstrates when sudo is actually needed vs when it's a design problem.
