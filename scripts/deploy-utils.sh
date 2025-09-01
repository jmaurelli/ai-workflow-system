#!/bin/bash

# Deployment Utilities Script
# Common deployment functions for different platforms and environments

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if we're in a Git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "Not in a Git repository"
        return 1
    fi
    return 0
}

# Function to check if we're on main branch
check_main_branch() {
    local current_branch=$(git branch --show-current)
    if [ "$current_branch" != "main" ] && [ "$current_branch" != "master" ]; then
        print_warning "Not on main branch (current: $current_branch)"
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            return 1
        fi
    fi
    return 0
}

# Function to check for uncommitted changes
check_uncommitted_changes() {
    if ! git diff-index --quiet HEAD --; then
        print_warning "You have uncommitted changes"
        git status --porcelain
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            return 1
        fi
    fi
    return 0
}

# Function to run pre-deployment checks
pre_deployment_checks() {
    print_status "Running pre-deployment checks..."
    
    # Check if we're in a Git repository
    if ! check_git_repo; then
        return 1
    fi
    
    # Check if we're on main branch
    if ! check_main_branch; then
        return 1
    fi
    
    # Check for uncommitted changes
    if ! check_uncommitted_changes; then
        return 1
    fi
    
    # Check if package.json exists
    if [ ! -f "package.json" ]; then
        print_error "package.json not found"
        return 1
    fi
    
    # Check if build script exists
    if ! grep -q '"build"' package.json; then
        print_warning "No build script found in package.json"
    fi
    
    # Check if test script exists and run tests
    if grep -q '"test"' package.json; then
        print_status "Running tests..."
        if npm test; then
            print_success "Tests passed"
        else
            print_error "Tests failed"
            return 1
        fi
    else
        print_warning "No test script found"
    fi
    
    # Check if lint script exists and run linting
    if grep -q '"lint"' package.json; then
        print_status "Running linting..."
        if npm run lint; then
            print_success "Linting passed"
        else
            print_error "Linting failed"
            return 1
        fi
    else
        print_warning "No lint script found"
    fi
    
    print_success "Pre-deployment checks completed"
    return 0
}

# Function to build the project
build_project() {
    print_status "Building project..."
    
    if grep -q '"build"' package.json; then
        if npm run build; then
            print_success "Build completed successfully"
        else
            print_error "Build failed"
            return 1
        fi
    else
        print_warning "No build script found, skipping build"
    fi
    
    return 0
}

# Function to deploy to Vercel
deploy_vercel() {
    print_status "Deploying to Vercel..."
    
    if ! command_exists vercel; then
        print_error "Vercel CLI not installed. Install with: npm i -g vercel"
        return 1
    fi
    
    if pre_deployment_checks && build_project; then
        if vercel --prod; then
            print_success "Deployed to Vercel successfully"
        else
            print_error "Vercel deployment failed"
            return 1
        fi
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to deploy to Netlify
deploy_netlify() {
    print_status "Deploying to Netlify..."
    
    if ! command_exists netlify; then
        print_error "Netlify CLI not installed. Install with: npm i -g netlify-cli"
        return 1
    fi
    
    if pre_deployment_checks && build_project; then
        if netlify deploy --prod; then
            print_success "Deployed to Netlify successfully"
        else
            print_error "Netlify deployment failed"
            return 1
        fi
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to deploy to Firebase
deploy_firebase() {
    print_status "Deploying to Firebase..."
    
    if ! command_exists firebase; then
        print_error "Firebase CLI not installed. Install with: npm i -g firebase-tools"
        return 1
    fi
    
    if pre_deployment_checks && build_project; then
        if firebase deploy; then
            print_success "Deployed to Firebase successfully"
        else
            print_error "Firebase deployment failed"
            return 1
        fi
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to deploy to GitHub Pages
deploy_github_pages() {
    print_status "Deploying to GitHub Pages..."
    
    if pre_deployment_checks && build_project; then
        # Check if gh-pages package is installed
        if ! grep -q "gh-pages" package.json; then
            print_status "Installing gh-pages..."
            npm install --save-dev gh-pages
        fi
        
        # Add deploy script if not exists
        if ! grep -q '"deploy"' package.json; then
            print_status "Adding deploy script to package.json..."
            # This is a simplified version - in practice, you'd want to modify package.json properly
            print_warning "Please add 'deploy': 'gh-pages -d build' to your package.json scripts"
        fi
        
        # Deploy
        if npm run deploy; then
            print_success "Deployed to GitHub Pages successfully"
        else
            print_error "GitHub Pages deployment failed"
            return 1
        fi
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to deploy to AWS S3
deploy_aws_s3() {
    local bucket_name="$1"
    
    if [ -z "$bucket_name" ]; then
        print_error "S3 bucket name is required"
        echo "Usage: deploy_aws_s3 <bucket-name>"
        return 1
    fi
    
    print_status "Deploying to AWS S3 bucket: $bucket_name"
    
    if ! command_exists aws; then
        print_error "AWS CLI not installed"
        return 1
    fi
    
    if pre_deployment_checks && build_project; then
        # Determine build directory
        local build_dir="build"
        if [ -d "dist" ]; then
            build_dir="dist"
        elif [ -d "out" ]; then
            build_dir="out"
        fi
        
        if [ ! -d "$build_dir" ]; then
            print_error "Build directory not found. Expected: $build_dir"
            return 1
        fi
        
        # Sync to S3
        if aws s3 sync "$build_dir" "s3://$bucket_name" --delete; then
            print_success "Deployed to AWS S3 successfully"
        else
            print_error "AWS S3 deployment failed"
            return 1
        fi
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to create a release
create_release() {
    local version="$1"
    local message="$2"
    
    if [ -z "$version" ]; then
        print_error "Version is required"
        echo "Usage: create_release <version> [message]"
        return 1
    fi
    
    if [ -z "$message" ]; then
        message="Release version $version"
    fi
    
    print_status "Creating release v$version..."
    
    if pre_deployment_checks && build_project; then
        # Update version in package.json
        npm version "$version" --no-git-tag-version
        
        # Commit changes
        git add .
        git commit -m "chore: bump version to $version"
        
        # Create tag
        git tag -a "v$version" -m "$message"
        
        # Push changes and tags
        git push origin main
        git push origin "v$version"
        
        print_success "Release v$version created successfully"
    else
        print_error "Pre-deployment checks failed"
        return 1
    fi
    
    return 0
}

# Function to rollback deployment
rollback_deployment() {
    local version="$1"
    
    if [ -z "$version" ]; then
        print_error "Version is required"
        echo "Usage: rollback_deployment <version>"
        return 1
    fi
    
    print_status "Rolling back to version $version..."
    
    # Check if tag exists
    if ! git tag -l | grep -q "v$version"; then
        print_error "Version v$version not found"
        return 1
    fi
    
    # Checkout the specific version
    git checkout "v$version"
    
    # Rebuild and redeploy
    if build_project; then
        print_success "Rollback to v$version completed"
        print_warning "Remember to checkout main branch: git checkout main"
    else
        print_error "Rollback failed"
        return 1
    fi
    
    return 0
}

# Function to show deployment status
show_deployment_status() {
    print_status "Deployment Status"
    echo "=================="
    echo ""
    
    # Git status
    echo "Git Status:"
    git status --porcelain || echo "Not in a Git repository"
    echo ""
    
    # Current branch
    echo "Current Branch:"
    git branch --show-current 2>/dev/null || echo "Not in a Git repository"
    echo ""
    
    # Last commit
    echo "Last Commit:"
    git log -1 --oneline 2>/dev/null || echo "No commits found"
    echo ""
    
    # Build status
    if [ -f "package.json" ]; then
        echo "Package.json Scripts:"
        npm run 2>/dev/null | grep -E "(build|test|lint|deploy)" || echo "No relevant scripts found"
        echo ""
    fi
    
    # Environment variables
    echo "Environment Variables:"
    env | grep -E "(NODE_ENV|REACT_APP_|NEXT_PUBLIC_|VITE_)" || echo "No relevant environment variables found"
    echo ""
}

# Function to show help
show_help() {
    echo "🚀 Deployment Utilities"
    echo "======================"
    echo ""
    echo "Available commands:"
    echo ""
    echo "  deploy_vercel              - Deploy to Vercel"
    echo "  deploy_netlify             - Deploy to Netlify"
    echo "  deploy_firebase            - Deploy to Firebase"
    echo "  deploy_github_pages        - Deploy to GitHub Pages"
    echo "  deploy_aws_s3 <bucket>     - Deploy to AWS S3"
    echo "  create_release <version>   - Create a new release"
    echo "  rollback_deployment <ver>  - Rollback to specific version"
    echo "  show_deployment_status     - Show current deployment status"
    echo "  pre_deployment_checks      - Run pre-deployment checks"
    echo "  build_project              - Build the project"
    echo ""
    echo "Examples:"
    echo "  source scripts/deploy-utils.sh"
    echo "  deploy_vercel"
    echo "  deploy_aws_s3 my-bucket-name"
    echo "  create_release 1.2.3 'New features'"
    echo ""
}

# Main function
main() {
    case "${1:-help}" in
        "vercel")
            deploy_vercel
            ;;
        "netlify")
            deploy_netlify
            ;;
        "firebase")
            deploy_firebase
            ;;
        "github-pages")
            deploy_github_pages
            ;;
        "aws-s3")
            deploy_aws_s3 "$2"
            ;;
        "release")
            create_release "$2" "$3"
            ;;
        "rollback")
            rollback_deployment "$2"
            ;;
        "status")
            show_deployment_status
            ;;
        "checks")
            pre_deployment_checks
            ;;
        "build")
            build_project
            ;;
        "help"|*)
            show_help
            ;;
    esac
}

# If script is sourced, don't run main
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi 