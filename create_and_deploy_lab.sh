#!/bin/bash

################################################################################
# Lab Creation and Deployment Automation Script
# 
# Usage: ./create_and_deploy_lab.sh "Lab Name" "Module Name" "vX.Y" "Description"
# Example: ./create_and_deploy_lab.sh "linux_scavenger_hunt" "Linux Module" "v1.0" "File System Scavenger Hunt"
#
# Prerequisites:
# - Git repository initialized in current directory
# - GitHub CLI (gh) installed and authenticated
# - Lab content already created and tested
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_OWNER="IITC-College"
REPO_NAME="DevOps-Jan26"
GITHUB_REPO="${REPO_OWNER}/${REPO_NAME}"

################################################################################
# Helper Functions
################################################################################

print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║  Lab Creation and Deployment Automation Script        ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_step() {
    echo -e "${GREEN}[STEP]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

################################################################################
# Validation Functions
################################################################################

validate_arguments() {
    if [ $# -ne 4 ]; then
        print_error "Invalid number of arguments"
        echo ""
        echo "Usage: $0 <lab_name> <module_name> <version> <description>"
        echo ""
        echo "Example:"
        echo "  $0 'linux_scavenger_hunt' 'Linux Module' 'v1.0' 'File System Scavenger Hunt'"
        echo ""
        exit 1
    fi
}

check_prerequisites() {
    print_step "Checking prerequisites..."
    
    # Check if in git repository
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "Not in a git repository"
        exit 1
    fi
    print_success "Git repository detected"
    
    # Check if GitHub CLI is installed
    if ! command -v gh &> /dev/null; then
        print_error "GitHub CLI (gh) is not installed"
        print_info "Install from: https://cli.github.com/"
        exit 1
    fi
    print_success "GitHub CLI installed"
    
    # Check if authenticated with GitHub
    if ! gh auth status &> /dev/null; then
        print_error "Not authenticated with GitHub CLI"
        print_info "Run: gh auth login"
        exit 1
    fi
    print_success "GitHub CLI authenticated"
    
    echo ""
}

validate_paths() {
    local module_path="$1"
    local lab_path="$2"
    
    print_step "Validating paths..."
    
    if [ ! -d "$module_path" ]; then
        print_error "Module directory not found: $module_path"
        exit 1
    fi
    print_success "Module directory exists"
    
    if [ ! -d "$lab_path" ]; then
        print_error "Lab directory not found: $lab_path"
        exit 1
    fi
    print_success "Lab directory exists"
    
    # Check for essential files
    if [ ! -f "$lab_path/README.md" ]; then
        print_warning "README.md not found in lab directory"
    fi
    
    if [ ! -f "$lab_path/start_here.txt" ]; then
        print_warning "start_here.txt not found in lab directory"
    fi
    
    echo ""
}

################################################################################
# Main Functions
################################################################################

create_archive() {
    local lab_name="$1"
    local module_path="$2"
    local archive_path="$3"
    
    print_step "Creating archive..."
    
    cd "$module_path"
    
    # Remove old archive if exists
    if [ -f "$archive_path" ]; then
        print_info "Removing old archive"
        rm -f "$archive_path"
    fi
    
    # Create new archive
    tar -czf "$archive_path" "$lab_name/"
    
    if [ ! -f "$archive_path" ]; then
        print_error "Failed to create archive"
        exit 1
    fi
    
    # Get archive size
    local size=$(du -h "$archive_path" | cut -f1)
    print_success "Archive created: $archive_path ($size)"
    
    cd - > /dev/null
    echo ""
}

git_commit_and_push() {
    local module_name="$1"
    local lab_name="$2"
    local description="$3"
    
    print_step "Committing to Git..."
    
    # Add module directory
    git add "$module_name/"
    
    # Check if there are changes to commit
    if git diff --cached --quiet; then
        print_warning "No changes to commit"
        return 0
    fi
    
    # Create commit message
    local commit_msg="Add $lab_name lab - $description

- Lab content and structure
- Compressed archive for distribution
- Student download instructions"
    
    # Commit
    git commit -m "$commit_msg"
    print_success "Changes committed"
    
    # Push to GitHub
    print_step "Pushing to GitHub..."
    git push -u origin main
    print_success "Pushed to GitHub"
    
    echo ""
}

create_github_release() {
    local version="$1"
    local lab_name="$2"
    local description="$3"
    local archive_relative_path="$4"
    
    print_step "Creating GitHub Release..."
    
    # Check if release already exists
    if gh release view "$version" --repo "$GITHUB_REPO" &> /dev/null; then
        print_warning "Release $version already exists"
        read -p "Delete and recreate? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Deleting existing release..."
            gh release delete "$version" --yes --repo "$GITHUB_REPO"
            print_success "Old release deleted"
        else
            print_error "Cannot proceed with existing release"
            exit 1
        fi
    fi
    
    # Create release notes
    local release_notes="Linux CLI Lab - $description

## 📦 Download Instructions

Run this single command to download, extract, and start the lab:

\`\`\`bash
curl -L https://github.com/$GITHUB_REPO/releases/download/$version/${lab_name}.tar.gz | tar -xz && cd $lab_name && cat start_here.txt
\`\`\`

## 📚 What's Included

- Progressive difficulty levels
- Hidden files and directories
- Real-world scenarios
- Complete solutions guide
- Self-contained learning environment

## 🎯 Learning Objectives

Students will practice:
- Linux navigation commands
- File reading and searching
- Pattern matching with grep
- File management operations

## ⏱️ Estimated Duration

1-2 hours

---

**Repository**: https://github.com/$GITHUB_REPO"
    
    # Create release
    gh release create "$version" \
        "$archive_relative_path" \
        --title "$lab_name $version - $description" \
        --notes "$release_notes" \
        --repo "$GITHUB_REPO"
    
    print_success "Release created: https://github.com/$GITHUB_REPO/releases/tag/$version"
    echo ""
}

create_student_command_file() {
    local version="$1"
    local lab_name="$2"
    local module_path="$3"
    
    print_step "Creating student command file..."
    
    local command_file="$module_path/STUDENT_COMMAND.txt"
    
    cat > "$command_file" << EOF
========================================================
              Student Download Command
========================================================

✅ Copy and paste this command:

curl -L https://github.com/$GITHUB_REPO/releases/download/$version/${lab_name}.tar.gz | tar -xz && cd $lab_name && cat start_here.txt

========================================================

📚 Resources:

Repository: https://github.com/$GITHUB_REPO
Release: https://github.com/$GITHUB_REPO/releases/tag/$version

========================================================

📝 What This Command Does:

1. Downloads the lab archive from GitHub
2. Extracts all files
3. Navigates into the lab directory
4. Displays the starting instructions

========================================================
EOF
    
    print_success "Student command file created: $command_file"
    echo ""
}

display_summary() {
    local version="$1"
    local lab_name="$2"
    local module_name="$3"
    local description="$4"
    
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  Deployment Completed Successfully!                    ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Lab Details:${NC}"
    echo -e "  Name:        $lab_name"
    echo -e "  Module:      $module_name"
    echo -e "  Version:     $version"
    echo -e "  Description: $description"
    echo ""
    echo -e "${BLUE}Links:${NC}"
    echo -e "  Repository: https://github.com/$GITHUB_REPO"
    echo -e "  Release:    https://github.com/$GITHUB_REPO/releases/tag/$version"
    echo ""
    echo -e "${BLUE}Student Command:${NC}"
    echo -e "${YELLOW}curl -L https://github.com/$GITHUB_REPO/releases/download/$version/${lab_name}.tar.gz | tar -xz && cd $lab_name && cat start_here.txt${NC}"
    echo ""
}

################################################################################
# Main Execution
################################################################################

main() {
    # Parse arguments
    local LAB_NAME="$1"
    local MODULE_NAME="$2"
    local VERSION="$3"
    local DESCRIPTION="$4"
    
    # Derived paths
    local MODULE_PATH="$MODULE_NAME"
    local LAB_PATH="$MODULE_PATH/$LAB_NAME"
    local ARCHIVE_NAME="${LAB_NAME}.tar.gz"
    local ARCHIVE_PATH="$ARCHIVE_NAME"
    local ARCHIVE_RELATIVE_PATH="$MODULE_PATH/$ARCHIVE_NAME"
    
    # Print header
    print_header
    
    # Display configuration
    print_info "Configuration:"
    echo "  Lab Name:    $LAB_NAME"
    echo "  Module:      $MODULE_NAME"
    echo "  Version:     $VERSION"
    echo "  Description: $DESCRIPTION"
    echo ""
    
    # Validate
    validate_arguments "$@"
    check_prerequisites
    validate_paths "$MODULE_PATH" "$LAB_PATH"
    
    # Execute workflow
    create_archive "$LAB_NAME" "$MODULE_PATH" "$ARCHIVE_PATH"
    git_commit_and_push "$MODULE_NAME" "$LAB_NAME" "$DESCRIPTION"
    create_github_release "$VERSION" "$LAB_NAME" "$DESCRIPTION" "$ARCHIVE_RELATIVE_PATH"
    create_student_command_file "$VERSION" "$LAB_NAME" "$MODULE_PATH"
    
    # Final commit for STUDENT_COMMAND.txt
    print_step "Committing student command file..."
    git add "$MODULE_PATH/STUDENT_COMMAND.txt"
    if ! git diff --cached --quiet; then
        git commit -m "Add student download command for $LAB_NAME $VERSION"
        git push
        print_success "Student command file committed and pushed"
    fi
    echo ""
    
    # Display summary
    display_summary "$VERSION" "$LAB_NAME" "$MODULE_NAME" "$DESCRIPTION"
}

# Run main function
main "$@"
