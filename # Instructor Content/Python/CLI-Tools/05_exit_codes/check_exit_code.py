#!/usr/bin/env python3
# Checking exit codes in Bash

"""
CHECKING EXIT CODES:

In Bash, $? contains the exit code of the last command:

python script.py
echo $?    # Shows exit code

USAGE:
if [ $? -eq 0 ]; then
    echo "Success"
fi

python script.py && echo "Success" || echo "Failed"
"""

import sys
import subprocess

print("EXIT CODE EXAMPLES")
print("=" * 60)

# Example 1: Simple script that exits with different codes
print("\n1. Create test scripts with different exit codes")
print("-" * 60)

# Create success script
with open('test_success.py', 'w') as f:
    f.write("""#!/usr/bin/env python3
import sys
print("Operation successful")
sys.exit(0)
""")

# Create error script
with open('test_error.py', 'w') as f:
    f.write("""#!/usr/bin/env python3
import sys
print("Operation failed", file=sys.stderr)
sys.exit(1)
""")

# Create custom error script
with open('test_custom.py', 'w') as f:
    f.write("""#!/usr/bin/env python3
import sys
print("File not found", file=sys.stderr)
sys.exit(3)
""")

print("✓ Created test_success.py (exits with 0)")
print("✓ Created test_error.py (exits with 1)")
print("✓ Created test_custom.py (exits with 3)")

# Example 2: Running and checking exit codes
print("\n2. Running scripts and checking exit codes")
print("-" * 60)

scripts = [
    ('test_success.py', 0),
    ('test_error.py', 1),
    ('test_custom.py', 3)
]

for script, expected in scripts:
    result = subprocess.run([sys.executable, script], capture_output=True)
    print(f"\n{script}:")
    print(f"  Exit code: {result.returncode}")
    print(f"  Expected: {expected}")
    print(f"  Match: {'✓' if result.returncode == expected else '✗'}")

# Example 3: Bash examples for checking exit codes
print("\n3. Bash examples for checking exit codes")
print("-" * 60)

bash_examples = """
# Basic check
python script.py
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed"
fi

# Capture exit code
python script.py
EXIT_CODE=$?
echo "Exit code: $EXIT_CODE"

# Short-circuit operators
python script.py && echo "Success" || echo "Failed"

# Chain commands (only continue if success)
python step1.py && \\
python step2.py && \\
python step3.py

# Run all regardless of failures
python step1.py
python step2.py
python step3.py

# Conditional based on specific code
python script.py
case $? in
    0) echo "Success" ;;
    1) echo "General error" ;;
    2) echo "Invalid arguments" ;;
    3) echo "File error" ;;
    *) echo "Unknown error" ;;
esac
"""

print(bash_examples)

# Example 4: Demonstrating conditional execution
print("\n4. Conditional execution based on exit code")
print("-" * 60)

def run_with_fallback():
    """Run primary script, use fallback if it fails"""
    print("Running primary script...")
    result = subprocess.run([sys.executable, 'test_error.py'], 
                          capture_output=True)
    
    if result.returncode == 0:
        print("✓ Primary script succeeded")
        return True
    else:
        print(f"✗ Primary script failed (code {result.returncode})")
        print("  Running fallback...")
        result2 = subprocess.run([sys.executable, 'test_success.py'],
                                capture_output=True)
        if result2.returncode == 0:
            print("✓ Fallback succeeded")
            return True
        else:
            print("✗ Fallback also failed")
            return False

run_with_fallback()

print("\n5. CI/CD Pipeline Pattern")
print("-" * 60)

pipeline_example = """
#!/bin/bash

# CI/CD pipeline that stops on first failure

set -e  # Exit on any error

echo "Step 1: Linting..."
python lint.py
echo "✓ Linting passed"

echo "Step 2: Unit tests..."
python test_unit.py
echo "✓ Unit tests passed"

echo "Step 3: Integration tests..."
python test_integration.py
echo "✓ Integration tests passed"

echo "Step 4: Build..."
python build.py
echo "✓ Build successful"

echo "Step 5: Deploy..."
python deploy.py
echo "✓ Deploy successful"

echo "Pipeline completed successfully!"
"""

print(pipeline_example)

print("\nKey Points:")
print("  ✓ $? in Bash contains last exit code")
print("  ✓ 0 = success, non-zero = failure")
print("  ✓ && chains commands (stop on failure)")
print("  ✓ || provides fallback")
print("  ✓ Use exit codes for automation")
