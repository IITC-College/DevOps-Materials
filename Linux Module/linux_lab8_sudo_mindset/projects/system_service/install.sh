#!/bin/bash
# System Service Installation Script

echo "Installing system service..."
echo "This script requires sudo because it modifies system configuration."

# System-level operations that require sudo:
# - Installing to /etc
# - Modifying system services
# - Creating system users
# - Setting up system-wide configuration

# Example operations (commented out for safety):
# sudo cp service.conf /etc/my-service/
# sudo systemctl enable my-service
# sudo systemctl start my-service

echo "System service installation would require sudo."
echo "This is legitimate sudo use for system administration."

# Note: This script SHOULD require sudo because it's a system service
# This is different from user_app - this is legitimate!
