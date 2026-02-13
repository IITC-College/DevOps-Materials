#!/usr/bin/env python3
# Production-ready CLI tool checklist

"""
PRODUCTION-READY CLI TOOL CHECKLIST

Use this checklist to ensure your CLI tool meets production standards
"""

print("PRODUCTION-READY CLI TOOL CHECKLIST")
print("="*70)

checklist = {
    "ARGUMENT PARSING": [
        "Uses argparse or similar library",
        "Has --help flag",
        "Has --version flag",
        "Subcommands for different operations",
        "Clear command structure",
        "Command-specific help available",
        "Validates all inputs"
    ],
    
    "CONFIGURATION": [
        "Supports configuration files (JSON/YAML)",
        "Has sensible defaults",
        "Config file location can be specified",
        "Validates configuration",
        "Documents configuration options",
        "Merges config with CLI arguments"
    ],
    
    "LOGGING": [
        "Uses logging module (not print())",
        "Logs to both file and console",
        "Multiple log levels (DEBUG, INFO, WARNING, ERROR)",
        "Log level can be configured",
        "Timestamps in logs",
        "Logs are rotated (optional)",
        "Logs include useful context"
    ],
    
    "ERROR HANDLING": [
        "All file operations wrapped in try/except",
        "Specific exception handling",
        "User-friendly error messages",
        "Technical details logged",
        "Graceful degradation",
        "No uncaught exceptions"
    ],
    
    "EXIT CODES": [
        "Returns 0 for success",
        "Returns non-zero for failures",
        "Different codes for different errors",
        "Exit codes documented",
        "Consistent exit code usage"
    ],
    
    "USER EXPERIENCE": [
        "Clear command syntax",
        "Helpful error messages",
        "Progress indicators for long operations",
        "Confirmation prompts for dangerous operations",
        "Dry-run mode available",
        "Colored output (optional)",
        "Examples in help text"
    ],
    
    "SAFETY": [
        "Dry-run mode for testing",
        "Confirmation for destructive operations",
        "Backup before modifications",
        "Can rollback changes",
        "Validates inputs before execution",
        "Safe defaults (e.g., --force required for risky ops)"
    ],
    
    "DOCUMENTATION": [
        "README with installation instructions",
        "Usage examples",
        "Configuration guide",
        "API documentation (if library)",
        "Troubleshooting guide",
        "Changelog",
        "License file"
    ],
    
    "CODE QUALITY": [
        "PEP 8 compliant",
        "Functions have docstrings",
        "Code is modular",
        "No hardcoded values",
        "Uses constants for magic numbers",
        "Type hints (Python 3.5+)",
        "Linting passes (pylint, flake8)"
    ],
    
    "TESTING": [
        "Unit tests for functions",
        "Integration tests for commands",
        "Test different error scenarios",
        "Test with invalid inputs",
        "CI/CD pipeline",
        "Test coverage > 80%"
    ],
    
    "DEPLOYMENT": [
        "Can be installed via pip",
        "Console script entry point",
        "Requirements documented",
        "Version number in code and setup",
        "Works on target platforms",
        "Minimal dependencies"
    ],
    
    "SECURITY": [
        "No credentials in code",
        "Sensitive data in config files",
        "Config files have restricted permissions",
        "Sanitizes user input",
        "No shell injection vulnerabilities",
        "Audit logs for sensitive operations"
    ]
}

# Print checklist
for category, items in checklist.items():
    print(f"\n{category}:")
    print("-"*70)
    for item in items:
        print(f"  [ ] {item}")

# Summary
print("\n"+"="*70)
print("QUICK CHECK")
print("="*70)

quick_check = """
Essential Features (Must Have):
  ✓ argparse for arguments
  ✓ --help and --version
  ✓ Logging module
  ✓ try/except error handling
  ✓ Proper exit codes (0=success)
  ✓ Configuration file support
  ✓ Clear documentation

Nice to Have:
  ✓ --dry-run mode
  ✓ Colored output
  ✓ Progress bars
  ✓ Auto-completion
  ✓ Man pages
  ✓ Multiple output formats (JSON, YAML)

Production Essentials:
  ✓ Comprehensive error handling
  ✓ Extensive logging
  ✓ Security considerations
  ✓ Performance optimization
  ✓ Monitoring/metrics
  ✓ Deployment automation
"""

print(quick_check)

# Minimum viable product
print("="*70)
print("MINIMUM VIABLE CLI TOOL")
print("="*70)

mvp_code = """
#!/usr/bin/env python3
import sys
import logging
import argparse

# Setup
EXIT_SUCCESS = 0
EXIT_ERROR = 1

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Parse arguments
parser = argparse.ArgumentParser(description='My Tool')
parser.add_argument('--version', action='version', version='1.0')
parser.add_argument('command', choices=['status', 'run'])
args = parser.parse_args()

# Execute
def main():
    logger.info(f"Executing: {args.command}")
    
    try:
        if args.command == 'status':
            print("Status: OK")
            return EXIT_SUCCESS
        elif args.command == 'run':
            print("Running...")
            return EXIT_SUCCESS
    except Exception as e:
        logger.error(f"Error: {e}")
        return EXIT_ERROR

if __name__ == '__main__':
    sys.exit(main())
"""

print(mvp_code)

print("\nThis minimum example includes:")
print("  • Argument parsing")
print("  • Logging")
print("  • Error handling")
print("  • Exit codes")
print("  • main() function")
print("  • Proper entry point")
