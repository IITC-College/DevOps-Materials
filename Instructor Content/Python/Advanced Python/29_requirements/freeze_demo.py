#!/usr/bin/env python3
# Understanding pip freeze

"""
pip freeze - Lists all installed packages with exact versions

USAGE:

# See all installed packages
pip freeze

# Save to requirements.txt
pip freeze > requirements.txt

# Save only project packages (not dependencies)
pip list --format=freeze

OUTPUT EXAMPLE:

certifi==2022.12.7
charset-normalizer==3.0.1
idna==3.4
requests==2.28.2
urllib3==1.26.14

Each line: package_name==version

WHY USE pip freeze?

1. Document your project dependencies
2. Share with team members
3. Deploy to production with exact versions
4. Recreate environment later

BEST PRACTICE:

1. Activate virtual environment
2. Install packages you need
3. Run: pip freeze > requirements.txt
4. Commit requirements.txt to git
5. Others can install with: pip install -r requirements.txt
"""

import sys

print("To see your installed packages, run:")
print("  pip freeze")
print("\nTo save to file:")
print("  pip freeze > requirements.txt")

# Show current environment
print(f"\nCurrent Python: {sys.executable}")
