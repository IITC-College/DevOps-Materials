#!/usr/bin/env python3
# Why pin package versions in requirements.txt?

"""
VERSION PINNING STRATEGIES:

1. EXACT VERSION (Recommended for production)
   package==2.3.1
   - Guarantees exact same version everywhere
   - Most reproducible
   - Safest for production

2. MINIMUM VERSION
   package>=2.0.0
   - Allows updates
   - May get breaking changes
   - Less predictable

3. VERSION RANGE
   package>=2.0.0,<3.0.0
   - Allows minor updates
   - Prevents major version jumps
   - Good balance

4. COMPATIBLE RELEASE
   package~=2.3.0
   - Equivalent to >=2.3.0,<2.4.0
   - Allows patch updates only
   - Good for stability

WHY PIN VERSIONS?

SCENARIO WITHOUT PINNING:
  requirements.txt: requests

  Developer A (Jan 2023): pip install requests
    → Gets requests 2.28.0
  
  Developer B (Jun 2023): pip install requests
    → Gets requests 2.31.0
  
  Different versions! Code may behave differently!

SCENARIO WITH PINNING:
  requirements.txt: requests==2.28.0

  Both developers get requests 2.28.0
  Code behaves identically!

BEST PRACTICES:

1. Use exact versions (==) in production
2. Use ranges (~=) in development
3. Test before updating versions
4. Update requirements.txt when updating packages
5. Commit requirements.txt to version control
"""

print("Version pinning ensures reproducibility")
print("Always use exact versions in production!")
print("\nExample:")
print("  requests==2.28.2")
print("  flask==2.3.0")
print("  pytest==7.2.2")
