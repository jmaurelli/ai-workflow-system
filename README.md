# Development Utilities Repository

A comprehensive collection of reusable development tools, scripts, and configurations that streamline common development tasks, maintain consistency across projects, and reduce setup time for new development environments.

## Purpose

This repository contains development utilities that help streamline common development tasks, maintain consistency across projects, and reduce setup time for new development environments. It provides a standardized approach to project setup, code quality, deployment, and development workflows.

## Repository Structure

```
dev-utils/
├── scripts/           # Shell scripts for common tasks
│   ├── git-setup.sh      # Git configuration and workflow setup
│   ├── setup-project.sh  # Project initialization and scaffolding
│   ├── deploy-utils.sh   # Deployment utilities for multiple platforms
│   └── code-quality.sh   # Linting, formatting, and code analysis
├── templates/         # Project templates and boilerplates
│   └── nextjs-template/  # Complete Next.js project template
├── configs/          # Configuration files (git, editor, etc.)
│   ├── .gitignore        # Comprehensive .gitignore template
│   ├── eslint.config.js  # ESLint configuration
│   └── prettier.config.js # Prettier configuration
├── snippets/         # Code snippets and examples
│   ├── react-component.tsx    # React component template
│   ├── react-hook.ts         # React hook template
│   ├── express-route.ts      # Express route template
│   └── jest-test.ts          # Jest test template
├── docs/             # Development documentation
│   ├── create-prd.md         # PRD generation guidelines
│   ├── create-project.md     # Project creation workflow
│   ├── firebase_workflow.md  # Firebase deployment guide
│   ├── generate-tasks.md     # Task generation from PRDs
│   ├── git_dev_workflow.md   # Git development workflow
│   ├── process-task-list.md  # Task list management
│   └── software_design_principles.md # Software design principles
└── tools/            # Development tools and utilities
    └── dev-server.sh         # Multi-language development server
```

## Quick Start

### Clone and Setup
```bash
# Clone the repository
git clone https://github.com/jmaurelli/dev-utils.git
cd dev-utils

# Make scripts executable
chmod +x scripts/*.sh tools/*.sh
```

### Using Scripts
```bash
# Run a script directly
./scripts/setup-project.sh

# Or source it for use in current shell
source scripts/git-setup.sh
```

## Available Utilities

### Scripts

#### `git-setup.sh` - Git Configuration and Workflow Setup
Comprehensive Git setup script that configures:
- **User Configuration**: Name, email, and credential helpers
- **Aliases**: 20+ useful Git aliases for common operations
- **Hooks**: Pre-commit hooks for code quality checks
- **Global Ignore**: Comprehensive .gitignore template
- **Functions**: Custom Git workflow functions
- **Completion**: Git command completion setup

**Usage:**
```bash
./scripts/git-setup.sh
```

#### `setup-project.sh` - Project Initialization and Scaffolding
Creates new projects with standardized structure for:
- **Next.js**: Full-stack React applications
- **React**: Single-page applications
- **Node.js**: Express server applications
- **Basic**: Minimal project structure

**Usage:**
```bash
./scripts/setup-project.sh
# Follow the interactive prompts
```

#### `deploy-utils.sh` - Deployment Utilities
Deployment functions for multiple platforms:
- **Vercel**: Next.js and React deployments
- **Netlify**: Static site deployments
- **Firebase**: Full-stack deployments
- **GitHub Pages**: Static site hosting
- **AWS S3**: Cloud storage deployments
- **Release Management**: Version tagging and releases
- **Rollback**: Deployment rollback capabilities

**Usage:**
```bash
source scripts/deploy-utils.sh
deploy_vercel
deploy_aws_s3 my-bucket-name
create_release 1.2.3 "New features"
```

#### `code-quality.sh` - Code Quality and Analysis
Comprehensive code quality tools for:
- **JavaScript/TypeScript**: ESLint, Prettier, TypeScript checking
- **Python**: flake8, black, complexity analysis
- **Rust**: cargo clippy, rustfmt
- **Go**: golangci-lint, go fmt
- **Security**: Vulnerability scanning
- **Complexity**: Code complexity analysis
- **Coverage**: Test coverage reporting

**Usage:**
```bash
source scripts/code-quality.sh
run_all_checks
run_js_linting
create_quality_configs
```

### Templates

#### `nextjs-template/` - Next.js Project Template
Complete Next.js project with:
- **Modern Dependencies**: Next.js 14, React 18, TypeScript 5
- **Quality Tools**: ESLint, Prettier, Jest, Testing Library
- **Configuration**: Optimized Next.js, TypeScript, and build configs
- **Structure**: Organized component and utility directories
- **Security**: Security headers and best practices

### Configurations

#### `.gitignore` - Comprehensive Git Ignore Template
Covers common files to ignore for:
- **Node.js**: node_modules, build outputs, logs
- **Python**: __pycache__, virtual environments, coverage
- **Rust**: target/, Cargo.lock
- **Go**: binaries, test files
- **IDEs**: VS Code, IntelliJ, Eclipse
- **OS**: macOS, Windows, Linux files
- **Build Tools**: Docker, Terraform, Kubernetes

#### `eslint.config.js` - Modern ESLint Configuration
Comprehensive linting rules for:
- **TypeScript**: Type checking and best practices
- **React**: Hooks, accessibility, JSX rules
- **Import/Export**: Module organization and validation
- **Code Style**: Consistent formatting and patterns
- **Complexity**: Function and file complexity limits
- **Security**: Security-focused rules

#### `prettier.config.js` - Code Formatting Configuration
Consistent code formatting for:
- **JavaScript/TypeScript**: Modern formatting standards
- **JSX**: React component formatting
- **JSON**: Optimized JSON formatting
- **Markdown**: Documentation formatting
- **YAML**: Configuration file formatting

### Snippets

#### React Component Template (`react-component.tsx`)
Modern React component with:
- **TypeScript**: Proper type definitions
- **Props Interface**: Extensible props structure
- **Children Support**: Flexible component composition
- **Export Pattern**: Named and default exports

#### React Hook Template (`react-hook.ts`)
Custom React hook with:
- **TypeScript**: Generic type support
- **Error Handling**: Comprehensive error management
- **Loading States**: Built-in loading state management
- **Async Support**: Promise-based operations

#### Express Route Template (`express-route.ts`)
Express.js route handler with:
- **TypeScript**: Request/Response type extensions
- **Error Handling**: Centralized error management
- **JSDoc**: API documentation
- **Response Format**: Standardized response structure

#### Jest Test Template (`jest-test.ts`)
Comprehensive test structure with:
- **Testing Library**: React component testing
- **Async Testing**: Proper async test patterns
- **Mocking**: Console and function mocking
- **Error Testing**: Error boundary testing
- **Conditional Testing**: Context-specific tests

### Tools

#### `dev-server.sh` - Multi-Language Development Server
Intelligent development server that:
- **Auto-Detects**: Project type and framework
- **Multi-Language**: Supports Next.js, React, Node.js, Python, Rust, Go
- **Port Management**: Automatic port detection and conflict resolution
- **Dependency Management**: Automatic dependency installation
- **Environment Setup**: Virtual environment activation for Python

**Usage:**
```bash
./tools/dev-server.sh
./tools/dev-server.sh -p 3001
./tools/dev-server.sh --ports
```

## Usage Examples

### Setting up a new project
```bash
# Clone dev-utils
git clone https://github.com/jmaurelli/dev-utils.git

# Use project setup script
./dev-utils/scripts/setup-project.sh my-new-project
```

### Using Git configurations
```bash
# Apply Git configurations
source dev-utils/scripts/git-setup.sh

# Use Git functions
git-feature new-feature
git-quick-commit feat "add new feature"
git-sync
```

### Using deployment utilities
```bash
# Source deployment utilities
source dev-utils/scripts/deploy-utils.sh

# Deploy to different platforms
deploy_vercel
deploy_aws_s3 my-bucket
create_release 1.0.0 "Initial release"
```

### Using code quality tools
```bash
# Source quality tools
source dev-utils/scripts/code-quality.sh

# Run quality checks
run_all_checks
run_js_linting
run_security_scan
```

### Using code snippets
```bash
# Copy React component template
cp dev-utils/snippets/react-component.tsx src/components/MyComponent.tsx

# Copy Express route template
cp dev-utils/snippets/express-route.ts src/routes/user-routes.ts
```

### Starting development servers
```bash
# Start appropriate development server
./dev-utils/tools/dev-server.sh

# Start on specific port
./dev-utils/tools/dev-server.sh -p 3001
```

## Best Practices

### Script Design
- **Idempotent**: Safe to run multiple times
- **Interactive**: User-friendly prompts and feedback
- **Error Handling**: Comprehensive error checking and recovery
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **Documentation**: Clear usage instructions and examples

### Configuration Management
- **Environment-Agnostic**: Works across different environments
- **Template-Based**: Uses placeholders for customization
- **Version Control**: All configs are version controlled
- **Documentation**: Comprehensive configuration documentation

### Code Quality
- **Automated**: Pre-commit hooks and CI/CD integration
- **Comprehensive**: Multiple language and framework support
- **Configurable**: Flexible rules and settings
- **Educational**: Clear error messages and suggestions

### Deployment
- **Multi-Platform**: Support for major deployment platforms
- **Automated**: Pre-deployment checks and validations
- **Rollback**: Safe rollback capabilities
- **Monitoring**: Deployment status and health checks

## Maintenance

### Regular Tasks
- [ ] Update dependencies and tools
- [ ] Test scripts on different environments
- [ ] Review and clean up unused utilities
- [ ] Update documentation
- [ ] Add new language/framework support

### Version Management
- Use semantic versioning for releases
- Tag releases for easy reference
- Maintain changelog of updates
- Test compatibility with new versions

## Contributing

When adding new utilities:

1. **Create feature branch**: `git checkout -b feature/new-utility`
2. **Add documentation**: Update README and add usage examples
3. **Test thoroughly**: Ensure scripts work across different environments
4. **Follow conventions**: Use consistent naming and structure
5. **Create PR**: Follow the standard PR workflow

## License

This repository is for personal development use. Feel free to adapt and modify for your own needs.

## Support

For issues or questions:
- Check existing documentation
- Review similar utilities for examples
- Create an issue for bugs or feature requests 