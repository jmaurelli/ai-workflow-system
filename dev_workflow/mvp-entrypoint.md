# MVP Project Entry Point

## Purpose
This document serves as the unified initialization point for MVP projects, automatically generating foundational documentation by collecting essential project data through guided questions. It consolidates the MVP core protocol and project entrypoint requirements into a streamlined workflow.

## Project Initialization Questions

### Project Foundation
1. **question**: What is the project name?
   - **field**: `project_name`
   - **type**: `string`
   - **example**: "User Authentication Service"
   - **required**: true
   - **description**: The official name for the project, used in documentation and artifacts

2. **question**: What is the one-liner goal of this project?
   - **field**: `project_goal`
   - **type**: `string`
   - **example**: "Enable secure user authentication for web applications"
   - **required**: true
   - **description**: Concise statement of why this project exists and what problem it solves

### Scope and Constraints
3. **question**: What is the MVP scope in 2-3 sentences?
   - **field**: `mvp_scope`
   - **type**: `string`
   - **example**: "User registration, login, password reset, and basic profile management. No social login or advanced security features in MVP."
   - **required**: true
   - **description**: Clear definition of what is and isn't included in the MVP phase

4. **question**: What are the primary constraints for this MVP?
   - **field**: `mvp_constraints`
   - **type**: `string`
   - **example**: "Must be deployable to standard cloud hosting, complete within 2 weeks, use existing tech stack"
   - **required**: false
   - **description**: Time, budget, technical, or business constraints that limit MVP scope

### Technical Foundation
5. **question**: What is your preferred technology stack?
   - **field**: `tech_stack`
   - **type**: `string`
   - **example**: "Node.js + Express + PostgreSQL + React"
   - **required**: false
   - **default**: "Node.js + Express + SQLite + HTML/CSS/JS"
   - **description**: Technology choices for backend, frontend, and data storage

6. **question**: Do you need external services or integrations?
   - **field**: `external_services`
   - **type**: `boolean`
   - **example**: false
   - **required**: false
   - **default**: false
   - **description**: Whether the MVP requires third-party APIs, authentication providers, or external services

7. **question**: What is your deployment target?
   - **field**: `deployment_target`
   - **type**: `enum`
   - **example**: "local"
   - **required**: false
   - **default**: "local"
   - **description**: Where the MVP will be deployed (local, cloud, container, etc.)

### Success Criteria
8. **question**: What defines MVP success? (list 2-3 key criteria)
   - **field**: `success_criteria`
   - **type**: `string`
   - **example**: "Users can register and login successfully, basic profile management works, system handles 100 concurrent users"
   - **required**: true
   - **description**: Measurable outcomes that indicate the MVP is complete and functional

9. **question**: What is your timeline for MVP completion?
   - **field**: `mvp_timeline`
   - **type**: `string`
   - **example**: "2 weeks"
   - **required**: false
   - **default**: "4 weeks"
   - **description**: Expected timeframe to complete the MVP phase

## Auto-Generated Documentation Sections

### Project Summary
- **title**: Project Summary
- **description**: High-level overview generated from key initialization answers, providing immediate context for all stakeholders
- **inputs**: `project_name`, `project_goal`, `mvp_scope`, `tech_stack`, `success_criteria`
- **example_content**: 
```markdown
# Project Summary

**Project**: User Authentication Service  
**Goal**: Enable secure user authentication for web applications  

**MVP Scope**: User registration, login, password reset, and basic profile management. No social login or advanced security features in MVP.

**Tech Stack**: Node.js + Express + PostgreSQL + React  
**Success Criteria**: Users can register and login successfully, basic profile management works, system handles 100 concurrent users  
**Timeline**: 2 weeks
```

### Project Charter
- **title**: Project Charter
- **description**: Lean project foundation document defining purpose, goals, scope, and success criteria
- **inputs**: `project_name`, `project_goal`, `mvp_scope`, `mvp_constraints`, `success_criteria`, `mvp_timeline`
- **example_content**: 
```markdown
# Project Charter

## Summary
Enable secure user authentication for web applications

## Goals
- [ ] Implement user registration and login
- [ ] Provide password reset functionality
- [ ] Enable basic profile management
- [ ] Ensure system handles 100 concurrent users

## Scope
- In scope: User registration, login, password reset, basic profile management
- Out of scope: Social login, advanced security features, user roles

## Success Criteria
- [ ] Users can register and login successfully
- [ ] Basic profile management works
- [ ] System handles 100 concurrent users
- [ ] Launch MVP within 2 weeks

## Constraints
- Must be deployable to standard cloud hosting
- Complete within 2 weeks
- Use existing tech stack
```

### Architecture Document
- **title**: Architecture (Lean)
- **description**: High-level technical architecture decisions and component structure
- **inputs**: `tech_stack`, `external_services`, `deployment_target`, `mvp_scope`
- **example_content**: 
```markdown
# Architecture (Lean)

## Core Components
- [ ] Backend API (Node.js + Express)
- [ ] Frontend (React)
- [ ] Database (PostgreSQL)
- [ ] Authentication middleware

## Technical Decisions
- **Backend**: Node.js + Express for API endpoints
- **Database**: PostgreSQL for user data persistence
- **Frontend**: React for user interface
- **Deployment**: Standard cloud hosting (no containers)

## Notes
- No external authentication providers in MVP
- Standard REST API patterns
- Basic security with password hashing
```

### Testing Strategy
- **title**: Testing Strategy
- **description**: TDD-Lite approach with smoke tests and validation requirements
- **inputs**: `mvp_scope`, `tech_stack`, `success_criteria`
- **methodology**: Follows `gen-tasks-and-testing.md` Testing Guidelines (MVP-First) section
- **key_principles**: 
  - Write failing smoke tests first
  - Minimal implementation to pass
  - Refactor after tests pass
  - MVP mode: smoke tests only for key flows

### Project Manifest
- **title**: Project Manifest
- **description**: Central tracking document for all project artifacts and status
- **inputs**: `project_name`, all generated document paths
- **example_content**: 
```json
{
  "project_name": "User Authentication Service",
  "artifacts": {
    "charter": "/docs/charter.md",
    "architecture": "/docs/architecture.md",
    "testing": "/docs/testing.md",
    "prd": "/prd/prd-user-auth.md",
    "tasks": "/tasks/tasks-user-auth.md"
  },
  "status": "initialized",
  "created": "2024-01-15",
  "last_updated": "2024-01-15"
}
```

## Workflow Integration

### Next Steps After Initialization
1. **Generate PRD**: Use collected data to create `/prd/prd-[project-name].md` (converted to kebab-case)
2. **Create Tasks**: Generate `/tasks/tasks-[project-name].md`