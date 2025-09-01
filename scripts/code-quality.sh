#!/bin/bash

# Code Quality Script
# Linting, formatting, and code analysis tools

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

# Function to check if file exists
file_exists() {
    [ -f "$1" ]
}

# Function to detect project type
detect_project_type() {
    if file_exists "package.json"; then
        if grep -q "next" package.json; then
            echo "nextjs"
        elif grep -q "react-scripts" package.json; then
            echo "react"
        elif grep -q "express" package.json; then
            echo "nodejs"
        else
            echo "nodejs"
        fi
    elif file_exists "requirements.txt" || file_exists "pyproject.toml"; then
        echo "python"
    elif file_exists "Cargo.toml"; then
        echo "rust"
    elif file_exists "go.mod"; then
        echo "go"
    else
        echo "unknown"
    fi
}

# Function to install ESLint if not present
install_eslint() {
    if ! grep -q "eslint" package.json; then
        print_status "Installing ESLint..."
        npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
        npx eslint --init --yes
        print_success "ESLint installed and configured"
    fi
}

# Function to install Prettier if not present
install_prettier() {
    if ! grep -q "prettier" package.json; then
        print_status "Installing Prettier..."
        npm install --save-dev prettier
        print_success "Prettier installed"
    fi
}

# Function to run JavaScript/TypeScript linting
run_js_linting() {
    local project_type="$1"
    
    print_status "Running JavaScript/TypeScript linting..."
    
    # Install ESLint if needed
    install_eslint
    
    # Run ESLint
    if npx eslint . --ext .js,.jsx,.ts,.tsx; then
        print_success "ESLint passed"
    else
        print_error "ESLint found issues"
        return 1
    fi
    
    return 0
}

# Function to run JavaScript/TypeScript formatting
run_js_formatting() {
    print_status "Running JavaScript/TypeScript formatting..."
    
    # Install Prettier if needed
    install_prettier
    
    # Run Prettier
    if npx prettier --write .; then
        print_success "Prettier formatting completed"
    else
        print_error "Prettier formatting failed"
        return 1
    fi
    
    return 0
}

# Function to run TypeScript type checking
run_typescript_check() {
    if file_exists "tsconfig.json"; then
        print_status "Running TypeScript type checking..."
        
        if npx tsc --noEmit; then
            print_success "TypeScript type checking passed"
        else
            print_error "TypeScript type checking failed"
            return 1
        fi
    else
        print_warning "tsconfig.json not found, skipping TypeScript check"
    fi
    
    return 0
}

# Function to run Python linting
run_python_linting() {
    print_status "Running Python linting..."
    
    # Install flake8 if not available
    if ! command_exists flake8; then
        print_status "Installing flake8..."
        pip install flake8
    fi
    
    # Run flake8
    if flake8 . --max-line-length=88 --extend-ignore=E203,W503; then
        print_success "Python linting passed"
    else
        print_error "Python linting found issues"
        return 1
    fi
    
    return 0
}

# Function to run Python formatting
run_python_formatting() {
    print_status "Running Python formatting..."
    
    # Install black if not available
    if ! command_exists black; then
        print_status "Installing black..."
        pip install black
    fi
    
    # Run black
    if black . --line-length=88; then
        print_success "Python formatting completed"
    else
        print_error "Python formatting failed"
        return 1
    fi
    
    return 0
}

# Function to run Rust linting
run_rust_linting() {
    print_status "Running Rust linting..."
    
    if command_exists cargo; then
        if cargo clippy; then
            print_success "Rust linting passed"
        else
            print_error "Rust linting found issues"
            return 1
        fi
    else
        print_error "Cargo not found"
        return 1
    fi
    
    return 0
}

# Function to run Rust formatting
run_rust_formatting() {
    print_status "Running Rust formatting..."
    
    if command_exists rustfmt; then
        if cargo fmt; then
            print_success "Rust formatting completed"
        else
            print_error "Rust formatting failed"
            return 1
        fi
    else
        print_error "rustfmt not found"
        return 1
    fi
    
    return 0
}

# Function to run Go linting
run_go_linting() {
    print_status "Running Go linting..."
    
    if command_exists golangci-lint; then
        if golangci-lint run; then
            print_success "Go linting passed"
        else
            print_error "Go linting found issues"
            return 1
        fi
    elif command_exists go; then
        print_warning "golangci-lint not found, using go vet"
        if go vet ./...; then
            print_success "Go vet passed"
        else
            print_error "Go vet found issues"
            return 1
        fi
    else
        print_error "Go not found"
        return 1
    fi
    
    return 0
}

# Function to run Go formatting
run_go_formatting() {
    print_status "Running Go formatting..."
    
    if command_exists go; then
        if go fmt ./...; then
            print_success "Go formatting completed"
        else
            print_error "Go formatting failed"
            return 1
        fi
    else
        print_error "Go not found"
        return 1
    fi
    
    return 0
}

# Function to run security scanning
run_security_scan() {
    print_status "Running security scan..."
    
    # Check for known vulnerabilities in npm packages
    if file_exists "package.json" && command_exists npm; then
        print_status "Checking npm packages for vulnerabilities..."
        if npm audit; then
            print_success "No npm vulnerabilities found"
        else
            print_warning "npm vulnerabilities found"
        fi
    fi
    
    # Check for known vulnerabilities in Python packages
    if file_exists "requirements.txt" && command_exists pip; then
        print_status "Checking Python packages for vulnerabilities..."
        if command_exists safety; then
            if safety check; then
                print_success "No Python vulnerabilities found"
            else
                print_warning "Python vulnerabilities found"
            fi
        else
            print_warning "safety not installed. Install with: pip install safety"
        fi
    fi
    
    return 0
}

# Function to run code complexity analysis
run_complexity_analysis() {
    print_status "Running code complexity analysis..."
    
    # For JavaScript/TypeScript projects
    if file_exists "package.json"; then
        if command_exists npx; then
            print_status "Analyzing JavaScript/TypeScript complexity..."
            # Install and run complexity analysis tools
            npx install-peerdeps --dev eslint-plugin-complexity
            print_warning "Complexity analysis requires manual configuration"
        fi
    fi
    
    # For Python projects
    if file_exists "requirements.txt" || file_exists "pyproject.toml"; then
        if command_exists radon; then
            print_status "Analyzing Python complexity..."
            if radon cc . -a; then
                print_success "Python complexity analysis completed"
            else
                print_warning "Python complexity analysis found issues"
            fi
        else
            print_warning "radon not installed. Install with: pip install radon"
        fi
    fi
    
    return 0
}

# Function to run test coverage
run_test_coverage() {
    print_status "Running test coverage..."
    
    # For JavaScript/TypeScript projects
    if file_exists "package.json"; then
        if grep -q "jest" package.json; then
            print_status "Running Jest coverage..."
            if npx jest --coverage; then
                print_success "Jest coverage completed"
            else
                print_error "Jest coverage failed"
                return 1
            fi
        elif grep -q "nyc" package.json; then
            print_status "Running NYC coverage..."
            if npx nyc npm test; then
                print_success "NYC coverage completed"
            else
                print_error "NYC coverage failed"
                return 1
            fi
        fi
    fi
    
    # For Python projects
    if file_exists "requirements.txt" || file_exists "pyproject.toml"; then
        if command_exists pytest; then
            print_status "Running pytest coverage..."
            if pytest --cov=. --cov-report=html; then
                print_success "pytest coverage completed"
            else
                print_error "pytest coverage failed"
                return 1
            fi
        fi
    fi
    
    return 0
}

# Function to run all quality checks
run_all_checks() {
    local project_type="$1"
    
    print_status "Running all code quality checks..."
    echo ""
    
    local exit_code=0
    
    # Run linting based on project type
    case $project_type in
        "nextjs"|"react"|"nodejs")
            if ! run_js_linting "$project_type"; then
                exit_code=1
            fi
            if ! run_typescript_check; then
                exit_code=1
            fi
            ;;
        "python")
            if ! run_python_linting; then
                exit_code=1
            fi
            ;;
        "rust")
            if ! run_rust_linting; then
                exit_code=1
            fi
            ;;
        "go")
            if ! run_go_linting; then
                exit_code=1
            fi
            ;;
        *)
            print_warning "Unknown project type: $project_type"
            ;;
    esac
    
    # Run formatting
    case $project_type in
        "nextjs"|"react"|"nodejs")
            if ! run_js_formatting; then
                exit_code=1
            fi
            ;;
        "python")
            if ! run_python_formatting; then
                exit_code=1
            fi
            ;;
        "rust")
            if ! run_rust_formatting; then
                exit_code=1
            fi
            ;;
        "go")
            if ! run_go_formatting; then
                exit_code=1
            fi
            ;;
    esac
    
    # Run security scan
    run_security_scan
    
    # Run complexity analysis
    run_complexity_analysis
    
    # Run test coverage
    run_test_coverage
    
    echo ""
    if [ $exit_code -eq 0 ]; then
        print_success "All code quality checks completed successfully!"
    else
        print_error "Some code quality checks failed"
    fi
    
    return $exit_code
}

# Function to create quality configuration files
create_quality_configs() {
    local project_type="$1"
    
    print_status "Creating quality configuration files..."
    
    case $project_type in
        "nextjs"|"react"|"nodejs")
            # Create .eslintrc.js if it doesn't exist
            if [ ! -f ".eslintrc.js" ]; then
                cat > .eslintrc.js << 'EOF'
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint'],
  rules: {
    'indent': ['error', 2],
    'linebreak-style': ['error', 'unix'],
    'quotes': ['error', 'single'],
    'semi': ['error', 'always'],
    'complexity': ['error', 10],
    'max-lines-per-function': ['error', 50],
    'max-depth': ['error', 4],
  },
};
EOF
                print_success "Created .eslintrc.js"
            fi
            
            # Create .prettierrc if it doesn't exist
            if [ ! -f ".prettierrc" ]; then
                cat > .prettierrc << 'EOF'
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
EOF
                print_success "Created .prettierrc"
            fi
            ;;
        "python")
            # Create .flake8 if it doesn't exist
            if [ ! -f ".flake8" ]; then
                cat > .flake8 << 'EOF'
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,build,dist
EOF
                print_success "Created .flake8"
            fi
            
            # Create pyproject.toml if it doesn't exist
            if [ ! -f "pyproject.toml" ]; then
                cat > pyproject.toml << 'EOF'
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
EOF
                print_success "Created pyproject.toml"
            fi
            ;;
        "rust")
            # Create .rustfmt.toml if it doesn't exist
            if [ ! -f ".rustfmt.toml" ]; then
                cat > .rustfmt.toml << 'EOF'
edition = "2021"
max_width = 100
tab_spaces = 4
newline_style = "Unix"
EOF
                print_success "Created .rustfmt.toml"
            fi
            ;;
        "go")
            # Create .golangci.yml if it doesn't exist
            if [ ! -f ".golangci.yml" ]; then
                cat > .golangci.yml << 'EOF'
run:
  timeout: 5m
  modules-download-mode: readonly

linters:
  enable:
    - gofmt
    - golint
    - govet
    - errcheck
    - staticcheck
    - gosimple
    - ineffassign
    - typecheck
    - unused
    - misspell
    - unparam
    - goconst
    - gocyclo
    - dupl
    - gosec

linters-settings:
  gocyclo:
    min-complexity: 15
  dupl:
    threshold: 100
  goconst:
    min-len: 2
    min-occurrences: 3

issues:
  exclude-rules:
    - path: _test\.go
      linters:
        - gocyclo
        - dupl
        - goconst
EOF
                print_success "Created .golangci.yml"
            fi
            ;;
    esac
}

# Function to show help
show_help() {
    echo "🔍 Code Quality Tools"
    echo "===================="
    echo ""
    echo "Available commands:"
    echo ""
    echo "  run_all_checks              - Run all quality checks"
    echo "  run_js_linting              - Run JavaScript/TypeScript linting"
    echo "  run_js_formatting           - Run JavaScript/TypeScript formatting"
    echo "  run_typescript_check        - Run TypeScript type checking"
    echo "  run_python_linting          - Run Python linting"
    echo "  run_python_formatting       - Run Python formatting"
    echo "  run_rust_linting            - Run Rust linting"
    echo "  run_rust_formatting         - Run Rust formatting"
    echo "  run_go_linting              - Run Go linting"
    echo "  run_go_formatting           - Run Go formatting"
    echo "  run_security_scan           - Run security vulnerability scan"
    echo "  run_complexity_analysis     - Run code complexity analysis"
    echo "  run_test_coverage           - Run test coverage analysis"
    echo "  create_quality_configs      - Create quality configuration files"
    echo ""
    echo "Examples:"
    echo "  source scripts/code-quality.sh"
    echo "  run_all_checks"
    echo "  run_js_linting"
    echo "  create_quality_configs"
    echo ""
}

# Main function
main() {
    local project_type=$(detect_project_type)
    
    case "${1:-help}" in
        "all")
            run_all_checks "$project_type"
            ;;
        "lint")
            case $project_type in
                "nextjs"|"react"|"nodejs")
                    run_js_linting "$project_type"
                    ;;
                "python")
                    run_python_linting
                    ;;
                "rust")
                    run_rust_linting
                    ;;
                "go")
                    run_go_linting
                    ;;
                *)
                    print_error "Unsupported project type: $project_type"
                    ;;
            esac
            ;;
        "format")
            case $project_type in
                "nextjs"|"react"|"nodejs")
                    run_js_formatting
                    ;;
                "python")
                    run_python_formatting
                    ;;
                "rust")
                    run_rust_formatting
                    ;;
                "go")
                    run_go_formatting
                    ;;
                *)
                    print_error "Unsupported project type: $project_type"
                    ;;
            esac
            ;;
        "typescript")
            run_typescript_check
            ;;
        "security")
            run_security_scan
            ;;
        "complexity")
            run_complexity_analysis
            ;;
        "coverage")
            run_test_coverage
            ;;
        "config")
            create_quality_configs "$project_type"
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