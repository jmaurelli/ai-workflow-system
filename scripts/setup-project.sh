#!/bin/bash

# Project Setup Script
# This script initializes new projects with standard structure and configuration

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

# Function to prompt for user input
prompt_input() {
    local prompt="$1"
    local var_name="$2"
    local default="$3"
    
    if [ -n "$default" ]; then
        read -p "$prompt [$default]: " input
        eval "$var_name=\${input:-$default}"
    else
        read -p "$prompt: " input
        eval "$var_name=\$input"
    fi
}

# Function to validate project name
validate_project_name() {
    local name="$1"
    
    # Check if name is empty
    if [ -z "$name" ]; then
        print_error "Project name cannot be empty"
        return 1
    fi
    
    # Check if name contains invalid characters
    if [[ "$name" =~ [^a-zA-Z0-9_-] ]]; then
        print_error "Project name can only contain letters, numbers, hyphens, and underscores"
        return 1
    fi
    
    # Check if directory already exists
    if [ -d "$name" ]; then
        print_error "Directory '$name' already exists"
        return 1
    fi
    
    return 0
}

# Function to create basic project structure
create_project_structure() {
    local project_name="$1"
    local project_type="$2"
    
    print_status "Creating project structure for $project_name..."
    
    # Create project directory
    mkdir -p "$project_name"
    cd "$project_name"
    
    # Create basic directory structure
    mkdir -p src/{components,utils,hooks,types,styles}
    mkdir -p public
    mkdir -p docs
    mkdir -p tests
    mkdir -p scripts
    mkdir -p configs
    
    print_success "Basic directory structure created"
}

# Function to create package.json for Node.js projects
create_package_json() {
    local project_name="$1"
    local description="$2"
    local author="$3"
    
    print_status "Creating package.json..."
    
    cat > package.json << EOF
{
  "name": "$project_name",
  "version": "1.0.0",
  "description": "$description",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/",
    "build": "echo 'Build script not configured'",
    "clean": "rm -rf node_modules package-lock.json",
    "install:clean": "npm run clean && npm install"
  },
  "keywords": [],
  "author": "$author",
  "license": "MIT",
  "devDependencies": {
    "eslint": "^8.0.0",
    "prettier": "^2.8.0",
    "jest": "^29.0.0",
    "nodemon": "^2.0.0"
  },
  "dependencies": {},
  "engines": {
    "node": ">=16.0.0"
  }
}
EOF
    
    print_success "package.json created"
}

# Function to create Next.js project structure
create_nextjs_project() {
    local project_name="$1"
    local description="$2"
    local author="$3"
    
    print_status "Setting up Next.js project structure..."
    
    # Create Next.js specific directories
    mkdir -p pages/{api,components}
    mkdir -p styles
    mkdir -p public/{images,icons}
    mkdir -p components/{ui,layout,forms}
    mkdir -p lib/{utils,hooks,types}
    mkdir -p configs
    
    # Create package.json for Next.js
    cat > package.json << EOF
{
  "name": "$project_name",
  "version": "1.0.0",
  "description": "$description",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "type-check": "tsc --noEmit",
    "test": "jest",
    "test:watch": "jest --watch",
    "format": "prettier --write .",
    "format:check": "prettier --check ."
  },
  "dependencies": {
    "next": "^13.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "devDependencies": {
    "@types/node": "^18.0.0",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "eslint": "^8.0.0",
    "eslint-config-next": "^13.0.0",
    "prettier": "^2.8.0",
    "typescript": "^4.9.0",
    "jest": "^29.0.0",
    "@testing-library/react": "^13.0.0",
    "@testing-library/jest-dom": "^5.16.0"
  },
  "author": "$author",
  "license": "MIT"
}
EOF
    
    # Create Next.js config
    cat > next.config.js << 'EOF'
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: [],
  },
  experimental: {
    appDir: false,
  },
}

module.exports = nextConfig
EOF
    
    # Create TypeScript config
    cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./components/*"],
      "@/lib/*": ["./lib/*"],
      "@/styles/*": ["./styles/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
EOF
    
    # Create basic pages
    cat > pages/_app.tsx << 'EOF'
import type { AppProps } from 'next/app'
import '../styles/globals.css'

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
EOF
    
    cat > pages/_document.tsx << 'EOF'
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
EOF
    
    cat > pages/index.tsx << 'EOF'
import Head from 'next/head'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Welcome</title>
        <meta name="description" content="Welcome to the application" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1>Welcome to your Next.js application!</h1>
      </main>
    </div>
  )
}
EOF
    
    # Create global styles
    cat > styles/globals.css << 'EOF'
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

* {
  box-sizing: border-box;
}
EOF
    
    print_success "Next.js project structure created"
}

# Function to create React project structure
create_react_project() {
    local project_name="$1"
    local description="$2"
    local author="$3"
    
    print_status "Setting up React project structure..."
    
    # Create React specific directories
    mkdir -p src/{components,pages,hooks,utils,types,styles}
    mkdir -p public
    mkdir -p configs
    
    # Create package.json for React
    cat > package.json << EOF
{
  "name": "$project_name",
  "version": "1.0.0",
  "description": "$description",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "5.0.1"
  },
  "devDependencies": {
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "@typescript-eslint/eslint-plugin": "^5.0.0",
    "@typescript-eslint/parser": "^5.0.0",
    "eslint": "^8.0.0",
    "eslint-plugin-react": "^7.0.0",
    "prettier": "^2.8.0",
    "typescript": "^4.9.0"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "author": "$author",
  "license": "MIT"
}
EOF
    
    # Create TypeScript config
    cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "es6"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}
EOF
    
    # Create basic React components
    cat > src/index.tsx << 'EOF'
import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css';
import App from './App';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
EOF
    
    cat > src/App.tsx << 'EOF'
import React from 'react';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to your React application!</h1>
      </header>
    </div>
  );
}

export default App;
EOF
    
    # Create basic styles
    cat > src/styles/index.css << 'EOF'
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
EOF
    
    cat > src/styles/App.css << 'EOF'
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
}
EOF
    
    print_success "React project structure created"
}

# Function to create Node.js project structure
create_nodejs_project() {
    local project_name="$1"
    local description="$2"
    local author="$3"
    
    print_status "Setting up Node.js project structure..."
    
    # Create Node.js specific directories
    mkdir -p src/{controllers,models,routes,middleware,utils,config}
    mkdir -p tests
    mkdir -p docs
    mkdir -p scripts
    
    # Create package.json for Node.js
    cat > package.json << EOF
{
  "name": "$project_name",
  "version": "1.0.0",
  "description": "$description",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/",
    "build": "echo 'Build script not configured'"
  },
  "keywords": [],
  "author": "$author",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "helmet": "^6.0.0",
    "dotenv": "^16.0.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "prettier": "^2.8.0",
    "jest": "^29.0.0",
    "nodemon": "^2.0.0",
    "supertest": "^6.0.0"
  },
  "engines": {
    "node": ">=16.0.0"
  }
}
EOF
    
    # Create basic Express server
    cat > src/index.js << 'EOF'
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Welcome to your Node.js application!' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
EOF
    
    print_success "Node.js project structure created"
}

# Function to create common configuration files
create_config_files() {
    local project_name="$1"
    
    print_status "Creating configuration files..."
    
    # Create .gitignore
    cat > .gitignore << 'EOF'
# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Build outputs
build/
dist/
out/
.next/

# Coverage
coverage/
*.lcov

# Logs
logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
tmp/
temp/
EOF
    
    # Create .eslintrc.js
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
  },
};
EOF
    
    # Create .prettierrc
    cat > .prettierrc << 'EOF'
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
EOF
    
    # Create README.md
    cat > README.md << EOF
# $project_name

$description

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

\`\`\`bash
npm install
\`\`\`

### Development

\`\`\`bash
npm run dev
\`\`\`

### Building

\`\`\`bash
npm run build
\`\`\`

### Testing

\`\`\`bash
npm test
\`\`\`

## Project Structure

\`\`\`
$project_name/
├── src/           # Source code
├── public/        # Static files
├── tests/         # Test files
├── docs/          # Documentation
├── scripts/       # Build scripts
└── configs/       # Configuration files
\`\`\`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
EOF
    
    print_success "Configuration files created"
}

# Function to initialize Git repository
init_git_repo() {
    print_status "Initializing Git repository..."
    
    git init
    git add .
    git commit -m "Initial commit: Project setup"
    
    print_success "Git repository initialized"
}

# Function to install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    if command_exists npm; then
        npm install
        print_success "Dependencies installed with npm"
    elif command_exists yarn; then
        yarn install
        print_success "Dependencies installed with yarn"
    else
        print_warning "No package manager found. Please install dependencies manually."
    fi
}

# Function to display project information
show_project_info() {
    local project_name="$1"
    local project_type="$2"
    
    echo ""
    print_success "Project '$project_name' created successfully!"
    echo ""
    echo "Project Type: $project_type"
    echo "Location: $(pwd)"
    echo ""
    print_status "Next steps:"
    echo "1. cd $project_name"
    echo "2. npm install (or yarn install)"
    echo "3. npm run dev (or yarn dev)"
    echo ""
    print_status "Available scripts:"
    echo "  npm run dev     - Start development server"
    echo "  npm run build   - Build for production"
    echo "  npm test        - Run tests"
    echo "  npm run lint    - Run linting"
    echo ""
}

# Main function
main() {
    echo "🚀 Project Setup Script"
    echo "======================"
    echo ""
    
    # Get project information
    prompt_input "Enter project name" "PROJECT_NAME"
    prompt_input "Enter project description" "PROJECT_DESCRIPTION" "A new project"
    prompt_input "Enter your name" "AUTHOR_NAME" "$(git config --global user.name 2>/dev/null || echo 'Your Name')"
    
    # Validate project name
    if ! validate_project_name "$PROJECT_NAME"; then
        exit 1
    fi
    
    # Get project type
    echo ""
    echo "Select project type:"
    echo "1. Next.js (React with SSR)"
    echo "2. React (Create React App)"
    echo "3. Node.js (Express server)"
    echo "4. Basic (Minimal structure)"
    echo ""
    prompt_input "Enter choice (1-4)" "PROJECT_TYPE" "1"
    
    # Create project based on type
    case $PROJECT_TYPE in
        1)
            create_project_structure "$PROJECT_NAME" "nextjs"
            create_nextjs_project "$PROJECT_NAME" "$PROJECT_DESCRIPTION" "$AUTHOR_NAME"
            ;;
        2)
            create_project_structure "$PROJECT_NAME" "react"
            create_react_project "$PROJECT_NAME" "$PROJECT_DESCRIPTION" "$AUTHOR_NAME"
            ;;
        3)
            create_project_structure "$PROJECT_NAME" "nodejs"
            create_nodejs_project "$PROJECT_NAME" "$PROJECT_DESCRIPTION" "$AUTHOR_NAME"
            ;;
        4)
            create_project_structure "$PROJECT_NAME" "basic"
            create_package_json "$PROJECT_NAME" "$PROJECT_DESCRIPTION" "$AUTHOR_NAME"
            ;;
        *)
            print_error "Invalid project type selected"
            exit 1
            ;;
    esac
    
    # Create common configuration files
    create_config_files "$PROJECT_NAME"
    
    # Initialize Git repository
    if command_exists git; then
        init_git_repo
    else
        print_warning "Git not found. Repository not initialized."
    fi
    
    # Install dependencies
    install_dependencies
    
    # Show project information
    show_project_info "$PROJECT_NAME" "$PROJECT_TYPE"
}

# Run main function
main "$@"
