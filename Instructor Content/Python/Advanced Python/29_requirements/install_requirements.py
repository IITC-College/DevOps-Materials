#!/usr/bin/env python3
# Installing from requirements.txt

"""
INSTALLING FROM requirements.txt:

Command:
  pip install -r requirements.txt

This will:
1. Read requirements.txt
2. Download each package listed
3. Install exact versions specified
4. Install all dependencies

TYPICAL WORKFLOW:

# New developer joining project
1. Clone repository
   git clone https://github.com/project/repo.git
   cd repo

2. Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install all dependencies
   pip install -r requirements.txt

4. Start working
   python app.py

# Everyone has the same package versions!

UPDATING PACKAGES:

# Update a single package
pip install --upgrade requests

# Then update requirements.txt
pip freeze > requirements.txt

# Or manually edit requirements.txt
# Then run: pip install -r requirements.txt
"""

print("To install packages from requirements.txt:")
print("  pip install -r requirements.txt")
print("\nMake sure you're in a virtual environment!")
print("\nCheck with:")
print("  python -c \"import sys; print(sys.prefix)\"")
