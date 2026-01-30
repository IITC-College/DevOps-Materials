#!/usr/bin/env python3
# Demonstrating pip list and pip show

"""
pip list - Show all installed packages

USAGE:

# List all packages
pip list

# List outdated packages
pip list --outdated

# Show in different format
pip list --format=json

EXAMPLE OUTPUT:

Package    Version
---------- -------
pip        23.0
requests   2.28.2
setuptools 67.0.0

pip show - Show details about a package

USAGE:

# Show package details
pip show requests

EXAMPLE OUTPUT:

Name: requests
Version: 2.28.2
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
License: Apache 2.0
Location: /path/to/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by: some-other-package

USEFUL COMMANDS:

# Check if package is installed
pip show requests

# See package dependencies
pip show requests | grep Requires

# See what requires this package
pip show requests | grep Required-by

# Check package version
pip show requests | grep Version
"""

import subprocess
import sys

print("To list installed packages, run:")
print("  pip list")
print("\nTo show package details, run:")
print("  pip show package_name")
print("\nExample:")
print("  pip show requests")
