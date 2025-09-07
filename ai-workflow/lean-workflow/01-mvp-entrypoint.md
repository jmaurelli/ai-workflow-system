# MVP Project Entry Point - Step 01 (Foundation Phase)

## Purpose
This document serves as the unified initialization point for MVP projects, automatically generating foundational documentation by collecting essential project data through guided questions. It consolidates the MVP core protocol and project entrypoint requirements into a streamlined workflow.

## 🤖 Automation Support
This document supports **three automation modes** for AI agents:

### **🚦 Automation Modes**
- **🚪 GUIDED Mode**: Maximum human oversight - traditional workflow with approval gates
- **⚡ AUTONOMOUS Mode**: Minimal human oversight - AI agent proceeds automatically with smart safety checks  
- **🧠 LEARNING Mode**: Adaptive oversight - learns from approval patterns and reduces gates over time

### **🚀 Automated Execution**
Use the workflow orchestrators to run this step automatically:

```bash
# Traditional shell orchestrator
./workflow-orchestrator.sh --mode=guided --feature=user-auth

# Intelligent Python orchestrator  
./ai-workflow-runner.py --mode=autonomous --feature=dashboard

# See execution plan without running
./ai-workflow-runner.py --mode=learning --feature=api-v2 --dry-run
```

See `workflow-sequence-guide.md` for complete automation details.

## AI Agent Instructions

### CRITICAL: Interactive Data Collection Required

**YOU MUST conduct an interactive Q&A session with the user to collect the project initialization data. Do NOT proceed with document generation until you have collected answers to all required questions.**

**Execution Protocol:**
1. **Present each question clearly** to the user one at a time
2. **Wait for the user's response** before proceeding to the next question  
3. **Validate required fields** - do not accept empty responses for required questions
4. **Use defaults** for optional fields if user provides no answer
5. **Store all answers** in a structured format for document generation
6. **Only after collecting all data** should you generate the project-initialization.md file

**Interactive Format:**
- Present questions in a friendly, conversational manner
- Show examples when helpful
- Confirm user's answers before proceeding
- Allow user to revise previous answers if needed

## Enhanced MVP Initialization Questions

**Target Time: 10 minutes | Grouped by concern for optimal mental flow**

### 👥 USER CONTEXT GROUP (3-4 minutes)

#### 1. Primary User Story (Multi-part)
- **question**: "Who is your primary user?"
  - **field**: `primary_user`
  - **type**: `string`
  - **example**: "Small business owners managing customer data"
  - **required**: true
  - **description**: Define the main person who will use this solution

- **follow_up_1**: "What's their biggest pain point you're solving?"
  - **field**: `user_pain_point`
  - **type**: `string`
  - **example**: "Manually tracking customer information in spreadsheets is error-prone and time-consuming"
  - **required**: true
  - **description**: The core problem that drives user motivation

- **follow_up_2**: "Walk me through their ideal success scenario in 2-3 steps"
  - **field**: `user_success_journey`
  - **type**: `string`
  - **example**: "1. User quickly adds new customer, 2. System auto-organizes contact info, 3. User easily finds customer details when needed"
  - **required**: true
  - **description**: End-to-end user value realization

#### 2. Project Identity
- **question**: "What's your project name?"
  - **field**: `project_name`
  - **type**: `string`
  - **example**: "CustomerHub MVP"
  - **required**: true
  - **description**: Official project name for documentation

#### 3. User Access Pattern (Conditional with Human Gate)
- **question**: "How will users first discover/access your solution?"
  - **field**: `user_access_method`
  - **type**: `enum`
  - **options**: ["web_browser", "mobile_app", "desktop_app", "api_integration", "other"]
  - **example**: "web_browser"
  - **required**: true
  - **description**: Primary access method determines technical architecture

- **conditional_gate**: If user selects web_browser or mobile_app:
  - **prompt**: "You mentioned [web/mobile]. Should I ask specific questions about [platform] considerations? (y/n)"
  - **if_yes**: Trigger conditional questions

- **conditional_web**: If web_browser selected and user approves:
  - **question**: "Desktop or mobile browser primary?"
  - **field**: `web_primary_device`
  - **type**: `enum`
  - **options**: ["desktop", "mobile", "both_equal"]

- **conditional_mobile**: If mobile_app selected and user approves:
  - **question**: "Native app or web app?"
  - **field**: `mobile_app_type`
  - **type**: `enum`
  - **options**: ["native_ios", "native_android", "cross_platform", "web_app"]

### 💼 BUSINESS CONTEXT GROUP (2-3 minutes)

#### 4. Business Model (Multi-part)
- **question**: "How does this project create value?"
  - **field**: `business_model`
  - **type**: `enum`
  - **options**: ["free_tool", "paid_service", "internal_efficiency", "cost_reduction", "revenue_generation", "other"]
  - **example**: "internal_efficiency"
  - **required**: true
  - **description**: Core value proposition

- **follow_up**: "What's the key metric that shows it's working?"
  - **field**: `key_success_metric`
  - **type**: `string`
  - **example**: "Reduces customer lookup time from 5 minutes to 30 seconds"
  - **required**: true
  - **description**: Measurable success indicator

#### 5. MVP Success Definition (Enhanced)
- **question**: "In 3 months, how will you know this MVP succeeded?"
  - **field**: `three_month_success`
  - **type**: `string`
  - **example**: "5 team members using it daily, 200+ customers tracked, zero data loss incidents"
  - **required**: true
  - **description**: Concrete success criteria for MVP validation

### 🏗️ TECHNICAL GUIDANCE GROUP (4-5 minutes)

#### 6. Project Complexity Assessment (AI Guidance Trigger)
- **question**: "Rate your project complexity:"
  - **field**: `project_complexity`
  - **type**: `enum`
  - **options**: ["simple", "medium", "complex"]
  - **option_descriptions**: {
    "simple": "Basic CRUD operations, simple forms, read/write data",
    "medium": "Real-time features, user authentication, file uploads, integrations",
    "complex": "ML/AI features, complex workflows, high-performance requirements"
  }
  - **required**: true
  - **description**: Complexity determines architecture recommendations

- **ai_guidance_trigger**: After selection, AI provides immediate guidance:
  - "Based on your complexity choice, I recommend considering..."

#### 7. Team & Constraints (Multi-part)
- **question**: "What's your team size and skill level?"
  - **field**: `team_context`
  - **type**: `string`
  - **example**: "Solo developer, intermediate JavaScript, learning backend"
  - **required**: true
  - **description**: Team capabilities inform technology choices

- **follow_up_1**: "Any existing systems this needs to integrate with?"
  - **field**: `existing_integrations`
  - **type**: `string`
  - **example**: "Must connect to existing Google Workspace, export to Excel"
  - **required**: false
  - **description**: Integration requirements affect architecture

- **follow_up_2**: "Hard constraints? (timeline, budget, compliance, etc.)"
  - **field**: `hard_constraints`
  - **type**: `string`
  - **example**: "Must launch in 4 weeks, $0 hosting budget for first 3 months"
  - **required**: false
  - **description**: Non-negotiable limitations

#### 8. Interactive Tech Stack Guidance (Conversational AI Session)
- **process**: "AI_TECH_STACK_CONSULTATION"
- **description**: AI analyzes all previous answers and conducts interactive tech stack selection
- **ai_behavior**: 
  - Consultative approach with 2-3 recommendations
  - Explains pros/cons for each option
  - Challenges assumptions when appropriate
  - Captures reasoning for documentation
- **fields_generated**:
  - `recommended_tech_stack`: Final technology choices
  - `tech_stack_reasoning`: AI's explanation and trade-offs considered
  - `alternative_options`: Other options discussed
  - `challenged_assumptions`: Any user assumptions the AI questioned

#### 9. Final Confirmation & Summary
- **process**: "DECISION_SUMMARY"
- **description**: AI presents complete summary of all decisions for user confirmation
- **includes**: All collected data, tech stack choice, key assumptions
- **user_action**: Confirm or request changes before proceeding to document generation

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

### Next Steps After Initialization (Feature-Centric)
Developer: ### Next Steps After Initialization

Begin with a concise checklist (3-7 bullets) of what you will do; keep items conceptual, not implementation-level.

1. **Initialize Feature Directory:**
   - Create date-prefixed feature directory: `/features/[YYYY-MM-DD]-[project-name]/` (auto-generate date from OS, convert `[project-name]` to kebab-case)
   - Initialize `feature-manifest.json` with metadata and workflow tracking
   - Setup directory structure with `artifacts/` subdirectories for generated content

2. **Generate PRD:**
   - Use the collected data to create `./prd.md` within the feature directory
   - **Human Gate:** Review and approve the project scope, constraints, and success criteria

3. **Generate SRS (Mandatory - Quality Foundation):**
   - Run `gen-srs.md` to capture critical NFRs for quality MVP development
   - **Focus on MVP essentials**: Performance budgets, security baselines, accessibility foundations
   - Generate `./srs.md` with measurable quality constraints within feature directory
   - **Human Gate:** Review and approve performance budgets and quality standards

4. **Design Decisions (Learning-Guided):**
   - Run `gen-design-decisions-lite.md` to make informed technical and UX decisions through interactive questionnaires
   - Generate `./design-decisions.md` with documented rationale and learning insights
   - Update `./learning-notes.md` with personal learning progress
   - **Human Gate:** Review and approve technology stack, UX approach, and design decisions

5. **Design Analysis:**
   - Run `gen-design.md` to analyze existing codebase for component reuse and integration opportunities
   - Generate `./design-analysis.md` with implementation guidance within feature directory
   - **Optional:** Run `gen-design-recovery.md` if inconsistencies are detected

6. **Create Tasks:**
   - Use the generated PRD, SRS, design decisions, and design analysis as input to create `./tasks.md`, referencing `gen-tasks-and-testing.md` and following the TDD-Lite approach
   - **Human Gate:** Review and approve the task assumptions and success criteria

7. **Update Feature Manifest:**
   - Keep `./feature-manifest.json` up to date with workflow progress and document status

After each substantive action or file update, briefly validate that the intended results were achieved and determine the next step or self-correct if necessary. At major milestones (after PRD and after tasks creation), provide a one to three sentence update summarizing progress, next steps, and any blockers. Attempt a first pass autonomously, but stop and ask for clarification if critical information is missing or approval is explicitly required.

### Human-in-the-Loop Gates (Feature-Centric)
- **Before Feature Directory Creation**: Review and approve feature name and scope for directory naming
- **Before PRD Generation**: Review and approve project scope, constraints, and success criteria  
- **Before SRS Generation**: Review and approve performance budgets and quality standards
- **Before Design Decisions**: Review and approve technology stack, UX approach, and design decisions with documented rationale
- **Before Task Creation**: Review and approve PRD assumptions and success criteria
- **Before Development**: Approve task breakdown and acceptance criteria
- **Scope Changes**: Approve any modifications to project scope or requirements

### Feature Directory Initialization Protocol
```bash
# Auto-generate feature directory with OS timestamp
FEATURE_DATE=$(date +"%Y-%m-%d")
FEATURE_SLUG="[convert-project-name-to-kebab-case]"  
FEATURE_DIR="/features/${FEATURE_DATE}-${FEATURE_SLUG}"

# Create feature directory structure
mkdir -p "${FEATURE_DIR}/artifacts/api-contracts"
mkdir -p "${FEATURE_DIR}/artifacts/design-mockups"
mkdir -p "${FEATURE_DIR}/artifacts/test-results"
mkdir -p "${FEATURE_DIR}/artifacts/performance-reports"

# Initialize feature manifest
cat > "${FEATURE_DIR}/feature-manifest.json" << 'EOF'
{
  "feature_metadata": {
    "feature_name": "[Collected Project Name]",
    "feature_slug": "[kebab-case-slug]",
    "feature_directory": "[YYYY-MM-DD]-[kebab-case-slug]",
    "creation_date": "[ISO-8601-timestamp]",
    "creator": "mvp-entrypoint-workflow",
    "project_context": "[Collected project context]"
  },
  "workflow_status": {
    "current_phase": "initialization",
    "phases_completed": [],
    "phases_remaining": ["foundation", "design_analysis", "implementation", "completion_summary"],
    "estimated_completion": null,
    "last_updated": "[ISO-8601-timestamp]"
  },
  "document_status": {
    "prd": {"status": "pending", "path": "./prd.md"},
    "srs": {"status": "pending", "path": "./srs.md"},
    "design_decisions": {"status": "pending", "path": "./design-decisions.md"},
    "design_analysis": {"status": "pending", "path": "./design-analysis.md"},
    "tasks": {"status": "pending", "path": "./tasks.md"},
    "learning_notes": {"status": "pending", "path": "./learning-notes.md"},
    "completion_summary": {"status": "pending", "path": "./completion-summary.md"}
  }
}
EOF

# Set working directory for all subsequent workflow steps
cd "${FEATURE_DIR}"
```

## Notes
- This template consolidates MVP core protocol requirements
- All documentation is kept lean (≤ 1 page each) for MVP phase
- External services and containers are opt-in only
- TDD-Lite methodology is mandatory for MVP development
- Conventional commits should reference generated PRD and task documents