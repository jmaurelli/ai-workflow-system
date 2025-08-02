#!/bin/bash

# Git Setup Script for Development Environment
# This script configures Git with personal settings and useful aliases

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

# Function to prompt for user input with default
prompt_with_default() {
    local prompt="$1"
    local default="$2"
    local var_name="$3"
    
    if [ -z "$default" ]; then
        read -p "$prompt: " input
    else
        read -p "$prompt [$default]: " input
    fi
    
    eval "$var_name=\${input:-$default}"
}

# Function to configure Git user
configure_git_user() {
    print_status "Configuring Git user settings..."
    
    # Get current Git user settings
    current_name=$(git config --global user.name 2>/dev/null || echo "")
    current_email=$(git config --global user.email 2>/dev/null || echo "")
    
    # Prompt for user information
    prompt_with_default "Enter your full name" "$current_name" "git_name"
    prompt_with_default "Enter your email address" "$current_email" "git_email"
    
    # Set Git user configuration
    git config --global user.name "$git_name"
    git config --global user.email "$git_email"
    
    print_success "Git user configured: $git_name <$git_email>"
}

# Function to set up Git aliases
setup_git_aliases() {
    print_status "Setting up Git aliases..."
    
    # Basic aliases
    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.ci commit
    git config --global alias.cm commit -m
    git config --global alias.ca commit -a
    git config --global alias.cam commit -am
    git config --global alias.amend commit --amend
    git config --global alias.unstage reset HEAD --
    git config --global alias.last log -1 HEAD
    git config --global alias.visual '!gitk'
    
    # Log aliases
    git config --global alias.lg "log --oneline --graph --decorate"
    git config --global alias.lga "log --oneline --graph --decorate --all"
    git config --global alias.lg1 "log --oneline --graph --decorate -1"
    git config --global alias.lg10 "log --oneline --graph --decorate -10"
    
    # Branch aliases
    git config --global alias.branch-name "rev-parse --abbrev-ref HEAD"
    git config --global alias.new-branch "checkout -b"
    git config --global alias.delete-branch "branch -d"
    git config --global alias.delete-branch-force "branch -D"
    
    # Stash aliases
    git config --global alias.stash-list "stash list"
    git config --global alias.stash-pop "stash pop"
    git config --global alias.stash-drop "stash drop"
    
    # Remote aliases
    git config --global alias.remote-list "remote -v"
    git config --global alias.remote-add "remote add"
    git config --global alias.remote-remove "remote remove"
    
    # Workflow aliases
    git config --global alias.feature "checkout -b feature"
    git config --global alias.hotfix "checkout -b hotfix"
    git config --global alias.bugfix "checkout -b bugfix"
    
    print_success "Git aliases configured"
}

# Function to set up Git configuration
setup_git_config() {
    print_status "Setting up Git configuration..."
    
    # Set default branch name
    git config --global init.defaultBranch main
    
    # Set up line ending configuration
    git config --global core.autocrlf input
    
    # Set up merge configuration
    git config --global merge.ff false
    git config --global pull.rebase true
    
    # Set up push configuration
    git config --global push.default current
    
    # Set up credential helper
    if command_exists git-credential-manager; then
        git config --global credential.helper manager
    elif command_exists git-credential-libsecret; then
        git config --global credential.helper libsecret
    else
        git config --global credential.helper store
    fi
    
    # Set up diff configuration
    git config --global diff.tool vscode
    git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
    
    # Set up merge tool
    git config --global merge.tool vscode
    git config --global mergetool.vscode.cmd 'code --wait $MERGED'
    
    print_success "Git configuration set up"
}

# Function to set up Git hooks directory
setup_git_hooks() {
    print_status "Setting up Git hooks directory..."
    
    # Create global hooks directory
    hooks_dir="$HOME/.git-templates/hooks"
    mkdir -p "$hooks_dir"
    
    # Configure Git to use global hooks
    git config --global init.templateDir "$HOME/.git-templates"
    
    # Create a sample pre-commit hook
    cat > "$hooks_dir/pre-commit" << 'EOF'
#!/bin/bash
# Global pre-commit hook template
# This hook runs before every commit

echo "Running pre-commit checks..."

# Check for TODO/FIXME comments
if git diff --cached --name-only | xargs grep -l "TODO\|FIXME" 2>/dev/null; then
    echo "Warning: Found TODO/FIXME comments in staged files"
    echo "Consider addressing these before committing"
fi

# Check for console.log statements (for JavaScript projects)
if git diff --cached --name-only | grep -E '\.(js|jsx|ts|tsx)$' | xargs grep -l "console\.log" 2>/dev/null; then
    echo "Warning: Found console.log statements in staged files"
    echo "Consider removing debug statements before committing"
fi

echo "Pre-commit checks completed"
EOF
    
    chmod +x "$hooks_dir/pre-commit"
    
    print_success "Git hooks directory set up at $hooks_dir"
}

# Function to set up Git ignore templates
setup_git_ignore() {
    print_status "Setting up Git ignore templates..."
    
    # Create global ignore file
    global_ignore="$HOME/.gitignore_global"
    
    cat > "$global_ignore" << 'EOF'
# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# Dependency directories
node_modules/
jspm_packages/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env
.env.test
.env.local
.env.production

# parcel-bundler cache (https://parceljs.org/)
.cache
.parcel-cache

# Next.js build output
.next

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
public

# Storybook build outputs
.out
.storybook-out

# Temporary folders
tmp/
temp/

# Build outputs
build/
dist/
out/

# Database
*.db
*.sqlite
*.sqlite3

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Java
*.class
*.jar
*.war
*.ear
*.zip
*.tar.gz
*.rar

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar
EOF
    
    # Configure Git to use global ignore
    git config --global core.excludesfile "$global_ignore"
    
    print_success "Global Git ignore file created at $global_ignore"
}

# Function to install Git completion
setup_git_completion() {
    print_status "Setting up Git completion..."
    
    # Check if Git completion is available
    if [ -f /usr/share/bash-completion/completions/git ]; then
        # Source Git completion
        if ! grep -q "source.*git.*completion" ~/.bashrc 2>/dev/null; then
            echo "" >> ~/.bashrc
            echo "# Git completion" >> ~/.bashrc
            echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc
        fi
        print_success "Git completion configured"
    else
        print_warning "Git completion not found. You may need to install bash-completion"
    fi
}

# Function to create useful Git functions
setup_git_functions() {
    print_status "Setting up Git functions..."
    
    # Add Git functions to bashrc
    if ! grep -q "git functions" ~/.bashrc 2>/dev/null; then
        cat >> ~/.bashrc << 'EOF'

# Git functions
git-functions() {
    # Show current branch and status
    git status --porcelain | head -1 | grep -q . && echo "⚠️  Working directory not clean" || echo "✅ Working directory clean"
    echo "Current branch: $(git branch-name)"
    echo "Last commit: $(git last --oneline)"
}

# Quick commit with conventional commit format
git-quick-commit() {
    local type="$1"
    local message="$2"
    
    if [ -z "$type" ] || [ -z "$message" ]; then
        echo "Usage: git-quick-commit <type> <message>"
        echo "Types: feat, fix, docs, style, refactor, test, chore"
        return 1
    fi
    
    git commit -m "$type: $message"
}

# Create feature branch
git-feature() {
    local feature_name="$1"
    
    if [ -z "$feature_name" ]; then
        echo "Usage: git-feature <feature-name>"
        return 1
    fi
    
    git checkout -b "feature/$feature_name"
    echo "Created feature branch: feature/$feature_name"
}

# Create hotfix branch
git-hotfix() {
    local hotfix_name="$1"
    
    if [ -z "$hotfix_name" ]; then
        echo "Usage: git-hotfix <hotfix-name>"
        return 1
    fi
    
    git checkout -b "hotfix/$hotfix_name"
    echo "Created hotfix branch: hotfix/$hotfix_name"
}

# Sync with remote
git-sync() {
    echo "Fetching latest changes..."
    git fetch origin
    
    echo "Current branch: $(git branch-name)"
    echo "Remote status:"
    git status --porcelain --branch
}

# Clean up merged branches
git-cleanup() {
    echo "Cleaning up merged branches..."
    git branch --merged | grep -v "\*" | grep -v "main" | grep -v "master" | xargs -n 1 git branch -d
    echo "Cleanup completed"
}

EOF
    fi
    
    print_success "Git functions added to ~/.bashrc"
}

# Function to display current Git configuration
show_git_config() {
    print_status "Current Git configuration:"
    echo ""
    echo "User: $(git config --global user.name) <$(git config --global user.email)>"
    echo "Default branch: $(git config --global init.defaultBranch)"
    echo "Credential helper: $(git config --global credential.helper)"
    echo "Merge strategy: $(git config --global pull.rebase)"
    echo ""
    echo "Available aliases:"
    git config --global --get-regexp alias | sed 's/alias\.//' | while read -r alias value; do
        echo "  $alias = $value"
    done
}

# Main function
main() {
    echo "🚀 Git Setup Script"
    echo "=================="
    echo ""
    
    # Check if Git is installed
    if ! command_exists git; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    
    # Configure Git user
    configure_git_user
    
    # Set up Git configuration
    setup_git_config
    
    # Set up Git aliases
    setup_git_aliases
    
    # Set up Git hooks
    setup_git_hooks
    
    # Set up Git ignore templates
    setup_git_ignore
    
    # Set up Git completion
    setup_git_completion
    
    # Set up Git functions
    setup_git_functions
    
    echo ""
    print_success "Git setup completed successfully!"
    echo ""
    
    # Show current configuration
    show_git_config
    
    echo ""
    print_status "To apply changes, run: source ~/.bashrc"
    echo ""
    print_status "Useful commands:"
    echo "  git-functions    - Show current Git status"
    echo "  git-quick-commit <type> <message> - Quick commit with conventional format"
    echo "  git-feature <name> - Create feature branch"
    echo "  git-hotfix <name>  - Create hotfix branch"
    echo "  git-sync          - Sync with remote"
    echo "  git-cleanup       - Clean up merged branches"
}

# Run main function
main "$@"
