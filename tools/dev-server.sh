#!/bin/bash

# Development Server Script
# Starts appropriate development server based on project type

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

# Function to start Next.js development server
start_nextjs_server() {
    print_status "Starting Next.js development server..."
    
    if ! command_exists npm; then
        print_error "npm not found"
        return 1
    fi
    
    # Check if dependencies are installed
    if [ ! -d "node_modules" ]; then
        print_status "Installing dependencies..."
        npm install
    fi
    
    # Start the development server
    npm run dev
}

# Function to start React development server
start_react_server() {
    print_status "Starting React development server..."
    
    if ! command_exists npm; then
        print_error "npm not found"
        return 1
    fi
    
    # Check if dependencies are installed
    if [ ! -d "node_modules" ]; then
        print_status "Installing dependencies..."
        npm install
    fi
    
    # Start the development server
    npm start
}

# Function to start Node.js development server
start_nodejs_server() {
    print_status "Starting Node.js development server..."
    
    if ! command_exists npm; then
        print_error "npm not found"
        return 1
    fi
    
    # Check if dependencies are installed
    if [ ! -d "node_modules" ]; then
        print_status "Installing dependencies..."
        npm install
    fi
    
    # Check if nodemon is available
    if grep -q "nodemon" package.json; then
        npm run dev
    else
        print_warning "nodemon not found, starting with node"
        npm start
    fi
}

# Function to start Python development server
start_python_server() {
    print_status "Starting Python development server..."
    
    if ! command_exists python3; then
        print_error "python3 not found"
        return 1
    fi
    
    # Check if virtual environment exists
    if [ -d "venv" ] || [ -d ".venv" ]; then
        print_status "Activating virtual environment..."
        if [ -d "venv" ]; then
            source venv/bin/activate
        else
            source .venv/bin/activate
        fi
    else
        print_warning "No virtual environment found"
    fi
    
    # Check if requirements are installed
    if file_exists "requirements.txt"; then
        print_status "Installing Python dependencies..."
        pip install -r requirements.txt
    fi
    
    # Start the development server
    if file_exists "manage.py"; then
        # Django project
        python3 manage.py runserver
    elif file_exists "app.py" || file_exists "main.py"; then
        # Flask or other Python web app
        python3 app.py 2>/dev/null || python3 main.py
    else
        print_error "No Python application entry point found"
        return 1
    fi
}

# Function to start Rust development server
start_rust_server() {
    print_status "Starting Rust development server..."
    
    if ! command_exists cargo; then
        print_error "cargo not found"
        return 1
    fi
    
    # Start the development server
    cargo run
}

# Function to start Go development server
start_go_server() {
    print_status "Starting Go development server..."
    
    if ! command_exists go; then
        print_error "go not found"
        return 1
    fi
    
    # Start the development server
    go run .
}

# Function to show available ports
show_ports() {
    print_status "Common development server ports:"
    echo "  Next.js:     http://localhost:3000"
    echo "  React:       http://localhost:3000"
    echo "  Node.js:     http://localhost:3000 (or custom)"
    echo "  Python:      http://localhost:8000 (Django)"
    echo "  Python:      http://localhost:5000 (Flask)"
    echo "  Rust:        http://localhost:8080 (or custom)"
    echo "  Go:          http://localhost:8080 (or custom)"
    echo ""
}

# Function to check if port is in use
check_port() {
    local port="$1"
    if command_exists lsof; then
        lsof -i :$port >/dev/null 2>&1
    elif command_exists netstat; then
        netstat -tuln | grep ":$port " >/dev/null 2>&1
    else
        return 1
    fi
}

# Function to find available port
find_available_port() {
    local start_port="$1"
    local port=$start_port
    
    while check_port $port; do
        port=$((port + 1))
    done
    
    echo $port
}

# Function to show help
show_help() {
    echo "🚀 Development Server"
    echo "===================="
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -p, --port <port>     Specify custom port"
    echo "  -h, --help            Show this help message"
    echo "  --ports               Show common development ports"
    echo ""
    echo "Examples:"
    echo "  $0                    # Start server with default settings"
    echo "  $0 -p 3001           # Start server on port 3001"
    echo "  $0 --ports           # Show common development ports"
    echo ""
}

# Main function
main() {
    local custom_port=""
    
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -p|--port)
                custom_port="$2"
                shift 2
                ;;
            --ports)
                show_ports
                exit 0
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Detect project type
    local project_type=$(detect_project_type)
    
    if [ "$project_type" = "unknown" ]; then
        print_error "Could not detect project type"
        echo "Supported project types: Next.js, React, Node.js, Python, Rust, Go"
        exit 1
    fi
    
    print_status "Detected project type: $project_type"
    
    # Check if port is specified and available
    if [ -n "$custom_port" ]; then
        if check_port "$custom_port"; then
            print_warning "Port $custom_port is already in use"
            local available_port=$(find_available_port "$custom_port")
            print_status "Using port $available_port instead"
            custom_port=$available_port
        fi
    fi
    
    # Start appropriate development server
    case $project_type in
        "nextjs")
            start_nextjs_server
            ;;
        "react")
            start_react_server
            ;;
        "nodejs")
            start_nodejs_server
            ;;
        "python")
            start_python_server
            ;;
        "rust")
            start_rust_server
            ;;
        "go")
            start_go_server
            ;;
        *)
            print_error "Unsupported project type: $project_type"
            exit 1
            ;;
    esac
}

# Run main function
main "$@" 