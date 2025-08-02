# Development Utilities Repository

A collection of reusable development tools, scripts, and configurations that can be used across multiple projects.

## Purpose

This repository contains development utilities that help streamline common development tasks, maintain consistency across projects, and reduce setup time for new development environments.

## Repository Structure

```
dev-utils/
├── scripts/           # Shell scripts for common tasks
├── templates/         # Project templates and boilerplates
├── configs/          # Configuration files (git, editor, etc.)
├── snippets/         # Code snippets and examples
├── docs/             # Development documentation
└── tools/            # Development tools and utilities
```

## Quick Start

### Clone and Setup
```bash
# Clone the repository
git clone https://github.com/jmaurelli/dev-utils.git
cd dev-utils

# Make scripts executable
chmod +x scripts/*.sh
```

### Using Scripts
```bash
# Run a script directly
./scripts/setup-project.sh

# Or source it for use in current shell
source scripts/dev-utils.sh
```

## Available Utilities

### Scripts
- `setup-project.sh` - Initialize new project with standard structure
- `git-setup.sh` - Configure Git with personal settings
- `deploy-utils.sh` - Common deployment utilities
- `code-quality.sh` - Linting and code quality checks

### Templates
- `nextjs-template/` - Next.js project boilerplate
- `react-template/` - React project template
- `node-template/` - Node.js/Express template

### Configurations
- `.gitignore` templates for different project types
- Editor configurations (VS Code, Cursor)
- Linting and formatting configs
- Docker configurations

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
```

### Using code snippets
```bash
# Copy React component template
cp dev-utils/snippets/react-component.tsx src/components/
```

## Contributing

When adding new utilities:

1. **Create feature branch**: `git checkout -b feature/new-utility`
2. **Add documentation**: Update README and add usage examples
3. **Test thoroughly**: Ensure scripts work across different environments
4. **Follow conventions**: Use consistent naming and structure
5. **Create PR**: Follow the standard PR workflow

## Best Practices

### Script Design
- Make scripts idempotent (safe to run multiple times)
- Include help/usage information
- Add error handling and validation
- Use descriptive names and comments

### Configuration Management
- Keep configs environment-agnostic
- Use templates with placeholders
- Document all configuration options
- Version control all configs

### Documentation
- Document purpose and usage for each utility
- Include examples and use cases
- Keep README updated with new additions
- Add troubleshooting sections

## Maintenance

### Regular Tasks
- [ ] Update dependencies and tools
- [ ] Test scripts on different environments
- [ ] Review and clean up unused utilities
- [ ] Update documentation

### Version Management
- Use semantic versioning for releases
- Tag releases for easy reference
- Maintain changelog of updates

## License

This repository is for personal development use. Feel free to adapt and modify for your own needs.

## Support

For issues or questions:
- Check existing documentation
- Review similar utilities for examples
- Create an issue for bugs or feature requests 