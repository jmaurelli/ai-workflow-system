Developer: Follow this Git development workflow for the Suelen Clean project:

"""
## Overview
- Ensures a clean, maintainable code history and effective collaboration.

## Repository Setup (Already Complete)
- Repository initialized locally
- Connected to GitHub remote
- Initial commit pushed
- Main branch established

## Branch Strategy
- **MVP Development Phase**: Work directly on `main` for speed and active iteration as the architecture evolves.
- **Production Phase**: Restrict `main` to production-ready code. Protect the branch and merge via Pull Requests (PRs) only.
- **Feature Branches (Production Phase)**: Name as `feature/descriptive-name`. Create for new features; developed, tested, merged via PR, then deleted.
- **Hotfix Branches (Production Phase)**: Name as `hotfix/issue-description`. Use for urgent bug fixes; create, fix, test, PR, merge, delete.

## Mindset: Git-First Approach
- Shift from just saving code to tracking changes and making them reviewable.
- **MVP Phase**: Prioritize speed and iteration—work directly on main.
- **Production Phase**: Focus on quality, using feature branches and PR reviews for stability and collaboration.

### Before Coding
- Define what you want to accomplish.
- Plan your commit messages.
- Ensure changes are a complete unit of work.
- Decide if it’s time to commit or continue.
- (During MVP: prioritize rapid iteration over branch management.)

### Git-First Steps
1. Check environment before making changes.
2. Plan and describe your changes.
3. Make logical, complete grouped changes.
4. Commit using clear, descriptive messages.
5. Push when ready to share your work.

## Daily Workflow (MVP Phase)
- **Start of Day**:
  - Check repo status: `git status`
  - Update `main` if working with others: `git pull origin main`
  - Begin coding directly on `main` (no need for feature branches during MVP)
- **During Development**:
  - Check `git status` every 10-15 minutes.
  - Stage complete logical changes: `git add <file>` (use `git add .` sparingly)
  - Commit with meaningful messages when a logical unit is complete.
  - Push changes to remote: `git push origin main`
"""

### Mental Checklist While Working
- [ ] Am I making logical, complete changes?
- [ ] Should I commit this set of changes?
- [ ] Is my commit message clear and descriptive?
- [ ] Am I ready to share this work with others?

## Quick Reference: The "Git-First" Workflow

### Complete Workflow (MVP Phase)
```bash
# 1. Check your environment
git status

# 2. Make changes directly on main
# No feature branches needed during MVP

# 3. Stage and commit changes
git add filename.ts
git commit -m "feat: your feature description"

# 4. Push to remote
git push origin main
```

# 4. Push to share your work
git push -u origin feature/your-new-feature

# 5. Create Pull Request on GitHub
#    - Go to: https://github.com/jmaurelli/suelenclean/pulls
#    - Click "New Pull Request"
#    - Fill out PR template with description

# 6. Self-review and merge PR
#    - Review your own code
#    - Test functionality
#    - Merge using "Squash and merge"

# 7. Clean up branches
git checkout main
git pull origin main
git branch -d feature/your-new-feature
git push origin --delete feature/your-new-feature
```

### The Key Mindset Shift
**Instead of**: Open file → Make changes → Think about Git later  
**Do This**: Check branch → Plan changes → Make changes → Commit strategically → Push when ready

## Pull Request Process

### What is a Pull Request?
A Pull Request (PR) is a way to propose changes to your codebase. It allows you to:
- **Review your own code** before merging
- **Document your changes** for future reference
- **Collaborate with others** (when working in teams)
- **Maintain code quality** through review process

### When to Create a Pull Request
Create a PR when:
- ✅ Your feature is complete and tested
- ✅ All tests pass locally
- ✅ Your code follows project conventions
- ✅ You're ready for the changes to go live

### Creating a Pull Request

#### Step 1: Prepare Your Branch
```bash
# 1. Ensure all tests pass
npm test

# 2. Update main branch
git checkout main
git pull origin main

# 3. Rebase feature branch (optional but recommended)
git checkout feature/your-feature-name
git rebase main

# 4. Push changes
git push --force-with-lease
```

#### Step 2: Create PR on GitHub
1. **Go to GitHub**: https://github.com/jmaurelli/suelenclean/pulls
2. **Click "New Pull Request"**
3. **Select branches**: `feature/your-feature-name` → `main`
4. **Fill out the PR template** (see below)

### Pull Request Template

#### Title
Use a clear, descriptive title:
```
✅ Good: "Add contact form validation with error handling"
❌ Bad: "Fix stuff"
```

#### Description
Include these sections:

```markdown
## What was changed?
- Brief description of the main changes
- List key files modified

## Why was it changed?
- Problem it solves
- Business value or user benefit

## How to test?
- Steps to verify the changes work
- Any special testing requirements

## Screenshots (if UI changes)
- Before and after images
- Mobile/desktop views if relevant

## Checklist
- [ ] Code follows project conventions
- [ ] All tests pass
- [ ] No console errors
- [ ] Responsive design works
- [ ] Accessibility considerations
- [ ] Performance impact considered
```

### Reviewing Your Own PR

#### Before Requesting Review
1. **Review your own code** as if you were reviewing someone else's
2. **Test the functionality** thoroughly
3. **Check for common issues**:
   - [ ] No hardcoded values
   - [ ] No console.log statements
   - [ ] No temporary code
   - [ ] Proper error handling
   - [ ] Responsive design works

#### Self-Review Checklist
```markdown
## Code Quality
- [ ] Code is readable and well-commented
- [ ] Functions are small and focused
- [ ] Variable names are descriptive
- [ ] No code duplication

## Testing
- [ ] All existing tests pass
- [ ] New functionality is tested
- [ ] Edge cases are handled

## Documentation
- [ ] README updated if needed
- [ ] Code comments explain complex logic
- [ ] API changes documented
```

### Merging Your PR

#### When Ready to Merge
1. **Ensure all checks pass** (tests, linting, etc.)
2. **Review your own changes** one final time
3. **Use appropriate merge strategy**:
   - **Squash and merge**: For feature branches (recommended)
   - **Merge commit**: For hotfixes
   - **Rebase and merge**: For clean history (advanced)

#### Merge Strategy Explanation
- **Squash and merge**: Combines all commits into one clean commit
- **Merge commit**: Preserves all individual commits
- **Rebase and merge**: Replays commits on top of main

### After Merging

#### Clean Up
```bash
# 1. Switch to main and pull latest
git checkout main
git pull origin main

# 2. Delete local feature branch
git branch -d feature/your-feature-name

# 3. Delete remote feature branch
git push origin --delete feature/your-feature-name

# 4. Verify cleanup
git branch -a
```

### Completing Work

## Pull Request Best Practices

### ✅ **Good PR Practices**
- **Small, focused PRs**: One feature or fix per PR
- **Clear descriptions**: Explain what, why, and how to test
- **Self-review**: Review your own code before requesting review
- **Clean commits**: Use squash and merge for feature branches
- **Test thoroughly**: Ensure all functionality works as expected

### ❌ **Common PR Mistakes**
- **Large PRs**: Too many changes in one PR (hard to review)
- **Vague descriptions**: "Fix stuff" or "Updates"
- **No testing**: PRs that haven't been tested locally
- **Mixed concerns**: UI changes mixed with backend logic
- **Unfinished work**: PRs with TODO comments or incomplete features

### PR Size Guidelines
- **Small PRs** (< 200 lines): Easy to review, quick to merge
- **Medium PRs** (200-500 lines): Need thorough review
- **Large PRs** (> 500 lines): Consider breaking into smaller PRs

### When to Break Up a PR
Break up your PR if it includes:
- Multiple unrelated features
- UI changes AND backend changes
- Different types of fixes (bugs + features)
- Changes to multiple systems

## Commit Message Guidelines

### Conventional Commits Format
```
type(scope): description

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```bash
# Good commit messages
git commit -m "feat: add contact form validation" -m "- Validate email format" -m "- Add required field checks" -m "- Display error messages"

git commit -m "fix: resolve mobile layout issues" -m "- Fix responsive breakpoints" -m "- Update Tailwind classes"

git commit -m "docs: update README with setup instructions" -m "- Add installation steps" -m "- Include environment variables"

git commit -m "refactor: extract reusable button component" -m "- Create Button component" -m "- Update all button usages"

# Bad commit messages
git commit -m "fixed stuff"
git commit -m "wip"
git commit -m "updates"
```

## Pull Request Process

### Creating a PR
1. **Title**: Clear, descriptive title
   - Good: "Add contact form validation with error handling"
   - Bad: "Fix stuff"

2. **Description**: Include:
   - What was changed
   - Why it was changed
   - How to test the changes
   - Screenshots (if UI changes)

3. **Labels**: Add appropriate labels (bug, enhancement, documentation, etc.)

### PR Review Checklist
- [ ] Code follows project conventions
- [ ] All tests pass
- [ ] No console errors
- [ ] Responsive design works
- [ ] Accessibility considerations
- [ ] Performance impact considered

### Merging
- Use "Squash and merge" for feature branches
- Use "Merge commit" for hotfixes
- Delete branch after merge

## Conflict Resolution

### When Conflicts Occur
```bash
# 1. Update main branch
git checkout main
git pull origin main

# 2. Rebase feature branch
git checkout feature/your-feature-name
git rebase main

# 3. Resolve conflicts in your editor
# Look for <<<<<<< HEAD markers

# 4. After resolving
git add .
git rebase --continue

# 5. Push changes
git push --force-with-lease
```

### Conflict Prevention
- Keep branches short-lived
- Communicate with team members
- Pull main branch regularly
- Use `git fetch` to check for remote changes

## Common Pitfalls and How to Avoid Them

### ❌ **Pitfall 1: Working Directly on Main**
**Problem**: Making changes on main branch without thinking about Git
**Solution**: Always check your branch before making changes
```bash
git branch  # Check what branch you're on
git checkout -b feature/your-change  # Create feature branch if needed
```

### ❌ **Pitfall 2: Reactive Git Usage**
**Problem**: Making changes first, thinking about Git later
**Solution**: Plan your changes and commit strategy before coding
```bash
# Before coding, ask:
# - What am I trying to accomplish?
# - How will I describe this in a commit message?
# - Is this a complete unit of work?
```

### ❌ **Pitfall 3: Large, Mixed Commits**
**Problem**: Committing many unrelated changes together
**Solution**: Make small, focused commits
```bash
# Good: Separate commits for different concerns
git commit -m "feat: add user validation"
git commit -m "style: update button styling"
git commit -m "docs: update README"

# Bad: Everything in one commit
git commit -m "fix stuff"
```

### ❌ **Pitfall 4: Vague Commit Messages**
**Problem**: Commit messages that don't explain the change
**Solution**: Use descriptive, conventional commit messages
```bash
# Good
git commit -m "feat: add email validation to contact form"

# Bad
git commit -m "updates"
```

## Best Practices

### Code Quality
- **Before committing**: Run `npm run lint` and `npm test`
- **Code review**: Always review your own code before pushing
- **Small commits**: Make atomic commits that do one thing well

### File Management
- **Staging**: Use `git add -p` to stage specific parts of files
- **Stashing**: Use `git stash` for temporary work
- **Cleanup**: Remove temporary files before committing

### Remote Management
- **Fetching**: Use `git fetch` to check for remote changes
- **Pushing**: Use `git push --force-with-lease` instead of `--force`
- **Branch cleanup**: Delete merged branches locally and remotely

## Useful Git Commands

### Daily Commands
```bash
# Check status
git status

# See commit history
git log --oneline -10

# See changes in a file
git diff filename

# See staged changes
git diff --cached

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Change last commit message
git commit --amend
```

### Advanced Commands
```bash
# Interactive rebase (clean up commits)
git rebase -i HEAD~3

# Cherry-pick a commit
git cherry-pick <commit-hash>

# Create a patch
git format-patch HEAD~1

# Apply a patch
git apply patch-file.patch
```

## Troubleshooting

### Common Issues

#### "Your branch is behind main"
```bash
git checkout main
git pull origin main
git checkout feature/your-branch
git rebase main
```

#### "Permission denied" when pushing
```bash
# Check your remote URL
git remote -v

# If using HTTPS, you may need to authenticate
# Consider switching to SSH for easier authentication
```

#### "Cannot lock ref" error
```bash
# This usually means a rebase is in progress
git rebase --abort
# Then try your original command again
```

#### Lost commits
```bash
# Find lost commits
git reflog

# Recover a lost commit
git checkout -b recovery-branch <commit-hash>
```

## GitHub Integration

### Repository Settings
- Enable branch protection on `main`
- Require PR reviews
- Require status checks to pass
- Enable automatic deletion of merged branches

### GitHub CLI (Optional)
```bash
# Install GitHub CLI
sudo apt install gh

# Authenticate (follow the prompts)
gh auth login

# Verify installation and authentication
gh auth status

# Create PR from command line
gh pr create --title "Your PR title" --body "Description"

# Alternative: Create PR interactively
gh pr create
```

### GitHub CLI Troubleshooting
```bash
# Check if GitHub CLI is installed
gh --version

# Check authentication status
gh auth status

# Re-authenticate if needed
gh auth logout
gh auth login

# If you get "unknown command" errors, try:
gh help
gh pr --help
```

## Environment Setup

### Git Configuration
```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Enable helpful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

### IDE Integration
- **VS Code**: Install GitLens extension
- **Cursor**: Built-in Git support
- **Terminal**: Use a good terminal with Git integration

## Continuous Integration

### Pre-commit Hooks (Future Enhancement)
Consider adding pre-commit hooks to:
- Run linting automatically
- Run tests before commit
- Check commit message format
- Prevent committing to main branch

## Conclusion

Following this workflow will help maintain a clean, professional Git history and make collaboration easier as your project grows. Remember:

1. **Small, focused commits** are better than large, mixed commits
2. **Clear commit messages** help future you and collaborators
3. **Regular pulls** from main prevent conflicts
4. **Pull Requests** provide review and documentation
5. **Clean branches** keep the repository organized

This workflow scales well as your project grows and can accommodate additional team members in the future. 