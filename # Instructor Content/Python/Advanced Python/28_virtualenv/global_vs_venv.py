#!/usr/bin/env python3
# Global Python vs Virtual Environment comparison

"""
GLOBAL PYTHON ENVIRONMENT
- System-wide Python installation
- Packages installed with: pip install package
- Affects all projects
- Can cause conflicts
- Risk of breaking system tools

VIRTUAL ENVIRONMENT (venv)
- Isolated Python environment per project
- Packages installed only for that project
- No conflicts between projects
- Safe to experiment
- Easy to reset (delete folder)

TYPICAL WORKFLOW:

1. Create project folder
   mkdir my_project
   cd my_project

2. Create virtual environment
   python -m venv venv

3. Activate it
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

4. Install packages
   pip install requests
   pip install flask

5. Work on project
   (venv is active)

6. Deactivate when done
   deactivate

7. Next time, just activate
   source venv/bin/activate
"""

import sys

print("Current Python environment:")
print(f"  Prefix: {sys.prefix}")
print(f"  Executable: {sys.executable}")

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("  Type: Virtual Environment ✓")
else:
    print("  Type: Global Python")
