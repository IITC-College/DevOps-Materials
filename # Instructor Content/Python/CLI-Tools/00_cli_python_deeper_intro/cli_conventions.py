#!/usr/bin/env python3
# CLI conventions and best practices

"""
CLI CONVENTIONS (Follow these!)

1. COMMAND STRUCTURE

Standard format:
  program [global-options] command [options] [arguments]

Examples:
  git commit -m "message"
  docker run -d nginx
  kubectl get pods --namespace production

2. OPTION FORMATS

Short options (single dash, single letter):
  -v, -h, -o, -f

Long options (double dash, full word):
  --verbose, --help, --output, --force

Combining short options:
  -vf  (same as -v -f)

Option with value:
  -o filename
  --output filename
  --output=filename

3. STANDARD FLAGS

--help, -h        Show help
--version, -V     Show version
--verbose, -v     Verbose output
--quiet, -q       Quiet mode
--force, -f       Force operation
--dry-run         Show what would happen
--config FILE     Config file location
--output FILE     Output file
--yes, -y         Assume yes to prompts

4. EXIT CODES

0   = Success
1   = General error
2   = Misuse of command (bad arguments)
126 = Command cannot execute
127 = Command not found
128 = Invalid exit argument
130 = Terminated by Ctrl+C

Custom codes:
64  = Command line usage error
65  = Data format error
66  = Cannot open input
73  = Can't create output
74  = I/O error
75  = Temporary failure
77  = Permission denied

5. ERROR MESSAGES

Good format:
  program: error: description
  program: warning: description

Examples:
  mytool: error: file 'config.yaml' not found
  mytool: warning: using default configuration

6. OUTPUT CONVENTIONS

Human-readable by default
Machine-readable option (--json, --xml)
Quiet mode prints only errors
Verbose mode shows details

7. PROMPTS

Ask for confirmation on destructive operations:
  Are you sure? [y/N]
  
Default should be safe (N for destructive ops)
--yes flag to skip prompts in scripts

8. CONFIGURATION

Order of precedence (highest first):
  1. Command-line arguments
  2. Environment variables
  3. Config file
  4. Defaults

9. FILE HANDLING

- Accept - as filename for stdin/stdout
- Support glob patterns when appropriate
- Handle relative and absolute paths

10. COLORS

Use colors to improve readability:
  - Red: errors
  - Yellow: warnings
  - Green: success
  - Cyan: info

But detect if output is redirected:
  - No colors when piped
  - Check with sys.stdout.isatty()

11. PROGRESS

For long operations:
  - Show progress bar or spinner
  - Allow --quiet to disable
  - Show estimated time remaining

12. DOCUMENTATION

Include examples in --help:
  
  mytool deploy --help
  
  Deploy application to server
  
  Usage:
    mytool deploy [options] <environment>
  
  Options:
    --dry-run    Show what would happen
    --force      Skip confirmations
  
  Examples:
    mytool deploy production
    mytool deploy --dry-run staging

13. NAMING

Use clear, descriptive names:
  - deploy not d
  - backup not bkp
  - status not st

Unless it's very common:
  - ls, cp, mv (accepted abbreviations)

14. SUBCOMMANDS

Group related operations:
  
  mytool deploy ...
  mytool backup ...
  mytool restore ...

Not:
  mytool-deploy
  mytool-backup

15. BACKWARDS COMPATIBILITY

- Don't remove options without deprecation
- Show deprecation warnings
- Maintain old behavior when possible

PYTHON EXAMPLE:

#!/usr/bin/env python3
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='My CLI Tool',
        epilog='Examples:\n  mytool process file.txt\n  mytool --verbose deploy'
    )
    
    # Global options
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='verbose output')
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command')
    
    # deploy subcommand
    deploy_parser = subparsers.add_parser('deploy',
                                          help='deploy application')
    deploy_parser.add_argument('environment')
    deploy_parser.add_argument('--force', '-f', action='store_true')
    
    args = parser.parse_args()
    
    if args.command == 'deploy':
        deploy(args.environment, args.force)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
"""

print("CLI Conventions to follow:")
print("  1. Standard option formats (-v, --verbose)")
print("  2. Common flags (--help, --version)")
print("  3. Proper exit codes (0=success)")
print("  4. Clear error messages")
print("  5. Configuration hierarchy")
print("  6. Colors when appropriate")
print("  7. Good documentation")
print()
print("Follow these for professional CLI tools!")
