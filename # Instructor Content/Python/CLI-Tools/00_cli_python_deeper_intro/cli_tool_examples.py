#!/usr/bin/env python3
# Real-world CLI tool examples

"""
FAMOUS CLI TOOLS:

1. GIT - Version Control
   git init
   git add .
   git commit -m "message"
   git push origin main

   Subcommands: init, add, commit, push, pull, etc.
   Options: -m, --verbose, --force
   Complex but intuitive

2. DOCKER - Container Management
   docker ps
   docker run -d -p 8080:80 nginx
   docker build -t myapp .
   docker-compose up

   Container management from CLI
   Easy to automate

3. AWS CLI - Cloud Management
   aws s3 ls
   aws ec2 describe-instances
   aws lambda invoke --function-name myFunc

   Manages entire cloud infrastructure
   JSON output for scripting

4. KUBECTL - Kubernetes
   kubectl get pods
   kubectl apply -f deployment.yaml
   kubectl logs pod-name

   Complex orchestration via CLI
   YAML-driven configuration

5. NPM - Package Manager
   npm install
   npm run build
   npm test

   JavaScript package management
   Lifecycle hooks

6. PIP - Python Package Manager
   pip install requests
   pip list
   pip freeze > requirements.txt

   Simple, effective
   Essential for Python development

7. TERRAFORM - Infrastructure as Code
   terraform init
   terraform plan
   terraform apply

   Declarative infrastructure
   State management

COMMON PATTERNS:

1. SUBCOMMANDS
   program <subcommand> [options] [args]
   git commit -m "message"

2. FLAGS/OPTIONS
   program --verbose --output file.txt
   program -v -o file.txt

3. POSITIONAL ARGUMENTS
   cp source.txt destination.txt
   program input.txt

4. CONFIGURATION FILES
   Many tools read ~/.config or .toolrc files

5. HELP SYSTEM
   program --help
   program help subcommand

6. VERSION INFO
   program --version

CHARACTERISTICS OF GOOD CLI TOOLS:

- Clear help messages
- Consistent interface
- Good error messages
- Support for --dry-run
- Verbose/quiet modes
- Exit codes (0=success)
- Can be automated
- Reasonable defaults
"""

examples = [
    "git commit -m 'message'",
    "docker ps -a",
    "kubectl get pods",
    "aws s3 ls",
    "terraform apply",
    "pip install requests",
    "npm run build"
]

print("Real-world CLI tools you might use:")
for example in examples:
    print(f"  {example}")

print("\nAll follow similar patterns:")
print("  command subcommand options arguments")
