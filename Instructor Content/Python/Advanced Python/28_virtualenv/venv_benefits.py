#!/usr/bin/env python3
# Why use virtual environments?

"""
BENEFITS OF VIRTUAL ENVIRONMENTS:

1. ISOLATION
   - Each project has its own dependencies
   - No conflicts between projects
   - Project A can use Django 3.0, Project B can use Django 4.0

2. REPRODUCIBILITY
   - Easy to recreate the exact environment
   - Works the same on different computers
   - Use requirements.txt to share dependencies

3. CLEANLINESS
   - Global Python stays clean
   - Easy to delete project (just delete venv folder)
   - No leftover packages

4. SAFETY
   - Test packages without affecting system Python
   - Experiment without breaking other projects
   - Easy to start fresh if something breaks

5. BEST PRACTICE
   - Industry standard for Python development
   - Required for many deployment platforms
   - Makes collaboration easier

EXAMPLE SCENARIO:

Without venv:
  pip install requests==2.25.0  # For Project A
  pip install requests==2.28.0  # For Project B - BREAKS Project A!

With venv:
  # Project A
  python -m venv venv_a
  source venv_a/bin/activate
  pip install requests==2.25.0

  # Project B
  python -m venv venv_b
  source venv_b/bin/activate
  pip install requests==2.28.0

  Both work independently!
"""

print("Virtual environments are essential for Python development")
print("Always use them for projects!")
