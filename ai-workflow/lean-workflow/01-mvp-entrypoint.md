# MVP Project Entry Point - Step 01 (Foundation Phase)

## Purpose
This document serves as the unified initialization point for MVP projects, automatically generating foundational documentation by collecting essential project data through guided questions. It consolidates the MVP core protocol and project entrypoint requirements into a streamlined workflow.

> **🔗 Workflow Navigation:**
> - **Complete Sequence**: [workflow-sequence-guide.md](../workflow-sequence-guide.md) - Full automation details
> - **Next Step**: [02-gen-prd.md](./02-gen-prd.md) - Product Requirements Document
> - **Architecture Reference**: [feature-centric-architecture.md](./feature-centric-architecture.md) - Directory structure guide
> - **AI-Native Bug Resolution**: [ai-native-bug-resolution.md](./ai-native-bug-resolution.md) - Systematic AI debugging with project intelligence

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
- Use **numbered references** for easy tracking (human answers: 1., 2., 2a., 2b., etc.)
- Show examples when helpful  
- Confirm user's answers before proceeding
- Allow user to revise previous answers if needed

## Progressive Guided Discovery Framework

**Target Time: 12-15 minutes | Intelligence-driven progressive questioning with reasoning**

### AI Agent Conversation Protocol

**CRITICAL: The AI must use this progressive discovery approach:**

1. **Explain reasoning during questioning** - After each question, provide brief context about why this information helps
2. **Numbered questions** - Use clear numbering for AI questions, numbered responses for human answers (Q: "What's your goal?" → Human: "1. Build a web server")
3. **Progressive flow** - Early answers influence later questions and recommendations
4. **Confirmation gates** - Pause after each major section for confirmation and insights
5. **Opt-in follow-ups** - Ask permission before digging deeper with additional questions (max 2 per topic)
6. **Conversational transitions** - Connect sections with explanatory context

### 🏁 **SECTION A: Project Identity & Access (Questions 1-3)**

#### **Question 1**: Project Foundation
- **question**: "What will be the name of your project?"
  - **field**: `project_name`
  - **type**: `string`
  - **example**: "1. CustomerHub MVP"
  - **required**: true
  - **ai_reasoning**: "This helps me create consistent naming throughout all documents and understand your project's identity."
  - **response_format**: "Human answers with: 1. [project name]"

#### **Question 2**: User Access Method
- **question**: "How will users first discover and access your solution?"
  - **field**: `user_access_method`
  - **type**: `enum`
  - **options**: ["web_browser", "mobile_app", "desktop_app", "api_integration", "command_line", "other"]
  - **example**: "2. web_browser"
  - **required**: true
  - **ai_reasoning**: "Your access method determines the entire technical architecture and development approach I'll recommend."
  - **response_format**: "Human answers with: 2. [access method]"

- **smart_follow_up**: "Want me to dig deeper into [platform] specific considerations? This will help me give better tech stack recommendations. (y/n)"
  - **if_yes_web**: 
    - **question**: "Will users primarily access this on desktop browsers, mobile browsers, or both equally?"
    - **field**: `web_primary_device`
    - **options**: ["desktop_primary", "mobile_primary", "both_equal"]
    - **response_format**: "Human answers with: 2a. [device preference]"
  - **if_yes_mobile**: 
    - **question**: "Are you thinking native mobile app (iOS/Android) or web app that works on mobile?"
    - **field**: `mobile_app_type`
    - **options**: ["native_ios", "native_android", "cross_platform_native", "mobile_web_app"]
    - **response_format**: "Human answers with: 2a. [mobile app type]"

#### **Question 3**: Project Goal
- **question**: "In one sentence, what's the main goal this project will achieve?"
  - **field**: `project_goal`
  - **type**: `string`
  - **example**: "3. Enable small businesses to track and organize customer information efficiently"
  - **required**: true
  - **ai_reasoning**: "This goal will guide every recommendation I make about features, architecture, and priorities."
  - **response_format**: "Human answers with: 3. [main goal sentence]"

### **🔄 GATE A: Early Architecture Insights**
**AI Provides**: 
- Initial technology direction based on access method
- Preliminary architecture insights
- Questions the AI will ask next and why
- **User confirms**: "Ready to continue?" before moving to Section B

---

### 👥 **SECTION B: User & Business Context (Questions 4-8)**

#### **Question 4**: Primary Users
- **question**: "Who are your primary users? Be specific about their role/situation."
  - **field**: `primary_users`
  - **type**: `string`
  - **example**: "4. Small business owners who currently track customers in spreadsheets"
  - **required**: true
  - **ai_reasoning**: "Understanding your users helps me recommend the right level of complexity and user experience approach."
  - **response_format**: "Human answers with: 4. [user description]"

#### **Question 5**: Core User Problem
- **question**: "5. What's the biggest pain point you're solving for these users?"
  - **field**: `user_pain_point`
  - **type**: `string`
  - **example**: "They waste 10+ minutes per day searching through messy spreadsheets to find customer details"
  - **required**: true
  - **ai_reasoning**: "The pain point intensity tells me how complex your solution needs to be and helps prioritize features."

#### **Question 6**: Success Journey
- **question**: "6. Walk me through your user's ideal success scenario in 2-3 simple steps."
  - **field**: `user_success_journey`
  - **type**: `string`
  - **example**: "1. User quickly adds new customer, 2. System auto-organizes contact info, 3. User finds customer details instantly when needed"
  - **required**: true
  - **ai_reasoning**: "This journey becomes your core user flow and determines which features are MVP-critical vs. nice-to-have."

#### **Question 7**: Business Value Model
- **question**: "7. How does this project create value?"
  - **field**: `business_model`
  - **type**: `enum`
  - **options**: ["free_internal_tool", "paid_service", "cost_reduction", "efficiency_improvement", "revenue_generation", "compliance_requirement", "other"]
  - **example**: "efficiency_improvement"
  - **required**: true
  - **ai_reasoning**: "The value model affects how robust the solution needs to be and influences hosting/scaling recommendations."

#### **Question 8**: Success Measurement
- **question**: "8. How will you know this MVP succeeded in 3 months? Give me specific, measurable outcomes."
  - **field**: `three_month_success_criteria`
  - **type**: `string`
  - **example**: "5 team members using it daily, 200+ customers tracked, finding customer info takes <30 seconds"
  - **required**: true
  - **ai_reasoning**: "Success metrics help me recommend the right performance targets and determine what 'good enough' looks like for your MVP."

### **🔄 GATE B: Business Context Analysis**
**AI Provides**:
- User experience complexity recommendations
- Business model implications for architecture
- Preliminary feature priority insights
- **User confirms**: "These insights make sense?" before moving to Section C

---

### 🏗️ **SECTION C: Technical Discovery & Recommendations (Questions 9-12)**

#### **Question 9**: Team Context & Skills
- **question**: "9. Tell me about your team size and current technical skills."
  - **field**: `team_context`
  - **type**: `string`
  - **example**: "Solo developer, comfortable with JavaScript and HTML/CSS, learning backend development"
  - **required**: true
  - **ai_reasoning**: "Your team's skills are the most important factor in choosing technologies that will help you succeed rather than frustrate you."

#### **Question 10**: Integration Requirements
- **question**: "10. Does this need to integrate with any existing systems, tools, or data sources?"
  - **field**: `existing_integrations`
  - **type**: `string`
  - **example**: "Must connect to existing Google Workspace, needs to export data to Excel"
  - **required**: false
  - **ai_reasoning**: "Integration requirements can dramatically affect technology choices and architecture complexity."

- **smart_follow_up**: "Want me to ask about specific integration details? This helps me recommend compatible technologies. (y/n)"
  - **if_yes**:
    - **question**: "10a. Are these integrations critical for MVP, or can they wait for v2?"
    - **field**: `integration_priority`
    - **options**: ["mvp_critical", "v2_feature", "nice_to_have"]
    - **question**: "10b. Do you need real-time sync or is periodic sync (hourly/daily) acceptable?"
    - **field**: `integration_sync_requirements`
    - **options**: ["real_time", "hourly", "daily", "manual"]

#### **Question 11**: Hard Constraints
- **question**: "11. Any hard constraints I should know about? (timeline, budget, compliance, performance, etc.)"
  - **field**: `hard_constraints`
  - **type**: `string`
  - **example**: "Must launch in 4 weeks, $0 hosting budget for first 3 months, needs to work on older browsers"
  - **required**: false
  - **ai_reasoning**: "Constraints eliminate technology options and help me recommend the most realistic path forward."

#### **Question 12**: Complexity Self-Assessment
- **question**: "12. Based on everything we've discussed, how would you rate your project's complexity?"
  - **field**: `perceived_complexity`
  - **type**: `enum`
  - **options**: ["simple", "medium", "complex"]
  - **option_descriptions**: {
    "simple": "Basic CRUD operations, simple forms, read/write data",
    "medium": "Real-time features, user authentication, file uploads, basic integrations",
    "complex": "ML/AI features, complex workflows, high-performance requirements, enterprise integrations"
  }
  - **required**: true
  - **ai_reasoning**: "I'll compare your perception with my analysis to ensure we're aligned on the right technical approach."

### **🔄 GATE C: Technology Stack Consultation**
**AI Provides**:
- **Complexity Analysis**: AI's assessment vs. user's perception with explanation
- **Technology Stack Recommendations**: 2-3 specific options with pros/cons
- **Architecture Approach**: High-level technical strategy
- **Development Path**: Suggested implementation sequence
- **Risk Assessment**: Potential challenges and mitigation strategies

**Generated Discovery Context Fields**:
- `ai_complexity_assessment`: AI's technical complexity analysis
- `recommended_tech_stack`: Primary technology recommendation with reasoning
- `alternative_tech_stacks`: 2 alternative options with trade-offs
- `architecture_approach`: High-level technical strategy
- `development_sequence`: Suggested implementation order
- `risk_factors`: Identified challenges and mitigation strategies
- `tech_stack_confidence`: AI's confidence level in recommendations

**User Action**: Final confirmation of technology direction before proceeding to document generation

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

### Enhanced Feature Directory Initialization Protocol

**CRITICAL: The enhanced feature-manifest.json must capture ALL discovery context to seed subsequent workflow documents.**

```bash
# Auto-generate feature directory with current OS timestamp
FEATURE_DATE=$(date +"%Y-%m-%d")
FEATURE_SLUG="[AI: convert project name to kebab-case]"  
FEATURE_DIR="/features/${FEATURE_DATE}-${FEATURE_SLUG}"

# Create feature directory structure
mkdir -p "${FEATURE_DIR}/artifacts/api-contracts"
mkdir -p "${FEATURE_DIR}/artifacts/design-mockups"
mkdir -p "${FEATURE_DIR}/artifacts/test-results"
mkdir -p "${FEATURE_DIR}/artifacts/performance-reports"
mkdir -p "${FEATURE_DIR}/artifacts/discovery-context"

# Create industry-standard project structure if it doesn't exist
mkdir -p docs/
mkdir -p src/
mkdir -p tests/
mkdir -p .github/workflows/
mkdir -p config/
mkdir -p project-knowledge/architecture/
mkdir -p project-knowledge/business-context/
mkdir -p project-knowledge/developer-knowledge/
mkdir -p project-knowledge/project-evolution/
mkdir -p project-history/

# Create AI-native project intelligence system
cat > project-index.json << 'PROJECT_INDEX'
{
  "project_metadata": {
    "name": "[Collected Project Name]",
    "created": "[AI: Insert current timestamp in ISO-8601 format: $(date -u +%Y-%m-%dT%H:%M:%SZ)]",
    "type": "ai-native-lean-workflow",
    "version": "2.0.0",
    "last_updated": "[AI: Insert current timestamp in ISO-8601 format: $(date -u +%Y-%m-%dT%H:%M:%SZ)]"
  },
  "project_intelligence": {
    "active_features": ["${FEATURE_DATE}-${FEATURE_SLUG}"],
    "completed_features": [],
    "reusable_components": {},
    "integration_patterns": {
      "database_integration": "TBD - will be populated during implementation",
      "api_integration": "TBD - will be populated during implementation",
      "frontend_integration": "TBD - will be populated during implementation"
    },
    "dependency_graph": {},
    "ai_discovery_tags": [],
    "architecture_decisions": []
  },
  "directory_structure": {
    "features/": "Feature-centric development directories with date prefixes",
    "src/": "Source code implementation",
    "tests/": "Test suites and validation", 
    "docs/": "Project documentation",
    "config/": "Configuration files",
    "project-knowledge/": "Strategic documents and accumulated learning",
    "project-history/": "Archived features and quarterly rollups"
  },
  "ai_navigation": {
    "primary_entry": "project-index.json",
    "feature_discovery": "features/*/feature-manifest.json",
    "knowledge_base": "project-knowledge/",
    "component_registry": "project-index.json#/project_intelligence/reusable_components",
    "integration_guide": "project-index.json#/project_intelligence/integration_patterns"
  },
  "workflow_status": "initialized"
}
PROJECT_INDEX

# Initialize enhanced feature manifest with discovery context
cat > "${FEATURE_DIR}/feature-manifest.json" << 'EOF'
{
  "feature_metadata": {
    "feature_name": "[Collected Project Name]",
    "feature_slug": "[kebab-case-slug]",
    "feature_directory": "[YYYY-MM-DD]-[kebab-case-slug]",
    "creation_date": "[AI: Insert current timestamp in ISO-8601 format: $(date -u +%Y-%m-%dT%H:%M:%SZ)]",
    "creator": "enhanced-mvp-entrypoint-workflow",
    "discovery_version": "progressive-guided-v1"
  },
  "discovery_context": {
    "project_identity": {
      "project_name": "[from Question 1]",
      "user_access_method": "[from Question 2]",
      "web_primary_device": "[from Question 2a if applicable]",
      "mobile_app_type": "[from Question 2a if applicable]",
      "project_goal": "[from Question 3]"
    },
    "user_business_context": {
      "primary_users": "[from Question 4]",
      "user_pain_point": "[from Question 5]",
      "user_success_journey": "[from Question 6]",
      "business_model": "[from Question 7]",
      "three_month_success_criteria": "[from Question 8]"
    },
    "technical_context": {
      "team_context": "[from Question 9]",
      "existing_integrations": "[from Question 10]",
      "integration_priority": "[from Question 10a if applicable]",
      "integration_sync_requirements": "[from Question 10b if applicable]",
      "hard_constraints": "[from Question 11]",
      "perceived_complexity": "[from Question 12]"
    },
    "ai_recommendations": {
      "ai_complexity_assessment": "[AI's technical analysis]",
      "recommended_tech_stack": "[Primary recommendation with reasoning]",
      "alternative_tech_stacks": "[Array of alternatives with trade-offs]",
      "architecture_approach": "[High-level technical strategy]",
      "development_sequence": "[Suggested implementation order]",
      "risk_factors": "[Identified challenges and mitigation]",
      "tech_stack_confidence": "[AI confidence level: high/medium/low]"
    },
    "workflow_seeding": {
      "prd_focus_areas": "[Derived from user journey and business model]",
      "srs_priority_requirements": "[Derived from success criteria and constraints]",
      "design_decision_drivers": "[Key factors from discovery for decision making]",
      "task_prioritization_logic": "[Implementation sequence rationale]",
      "success_validation_approach": "[How to measure MVP success based on criteria]"
    }
  },
  "workflow_status": {
    "current_phase": "initialization",
    "phases_completed": ["discovery"],
    "phases_remaining": ["foundation", "design_analysis", "implementation", "completion_summary"],
    "estimated_completion": null,
    "last_updated": "[ISO-8601-timestamp]",
    "discovery_completion_time": "[ISO-8601-timestamp]"
  },
  "document_status": {
    "prd": {"status": "pending", "path": "./prd.md", "seeded_from": "discovery_context", "ai_priority": "high"},
    "srs": {"status": "pending", "path": "./srs.md", "seeded_from": "discovery_context", "ai_priority": "high"},
    "design_decisions": {"status": "pending", "path": "./design-decisions.md", "seeded_from": "ai_recommendations", "ai_priority": "high"},
    "design_analysis": {"status": "pending", "path": "./design-analysis.md", "seeded_from": "technical_context", "ai_priority": "medium"},
    "tasks": {"status": "pending", "path": "./tasks.md", "seeded_from": "workflow_seeding", "ai_priority": "high"},
    "learning_notes": {"status": "pending", "path": "./learning-notes.md", "seeded_from": "discovery_context", "ai_priority": "low"},
    "completion_summary": {"status": "pending", "path": "./completion-summary.md", "ai_priority": "medium"}
  },
  "ai_navigation": {
    "entry_document": "./feature-manifest.json",
    "primary_requirements": "./prd.md",
    "technical_specs": "./srs.md", 
    "implementation_guide": "./tasks.md",
    "architecture_decisions": "./design-decisions.md",
    "completion_status": "./completion-summary.md",
    "related_artifacts": "./artifacts/",
    "project_root": "../../"
  },
  "context_usage_tracking": {
    "discovery_data_utilized_in_prd": [],
    "discovery_data_utilized_in_srs": [],
    "discovery_data_utilized_in_design": [],
    "discovery_data_utilized_in_tasks": []
  },
  "ai_integration": {
    "project_context": {
      "is_initial_project": true,
      "project_index_location": "../../project-index.json",
      "knowledge_base_location": "../../project-knowledge/"
    },
    "reusable_exports": [],
    "external_dependencies": [],
    "integration_requirements": [],
    "ai_discovery_tags": [],
    "component_registry": {},
    "api_endpoints": {},
    "integration_patterns": {},
    "architecture_contributions": []
  },
  "lifecycle_management": {
    "creation_phase": "mvp_initialization",
    "current_stage": "active_development",
    "promotion_candidates": [],
    "archive_readiness": false,
    "knowledge_extraction_status": "pending"
  }
}
EOF

# Set working directory for all subsequent workflow steps
cd "${FEATURE_DIR}"

# Validate feature manifest against schema (if ajv is available)
if command -v ajv >/dev/null 2>&1; then
  ajv validate -s "../../feature-manifest.schema.json" -d "./feature-manifest.json"
  if [ $? -eq 0 ]; then
    echo "✅ Feature manifest schema validation passed"
  else
    echo "⚠️  Feature manifest validation failed - please review structure"
  fi
else
  echo "💡 Install ajv-cli for automatic JSON schema validation: npm install -g ajv-cli"
fi
```

### AI Agent Instructions for Discovery Context Usage

**CRITICAL: How to use discovery context in subsequent workflow documents:**

1. **PRD Generation**: Reference `discovery_context.user_business_context` and `discovery_context.project_identity`
   - User stories derive from `user_success_journey`
   - Business requirements come from `business_model` and `three_month_success_criteria`
   - Project scope references `project_goal` and `user_pain_point`

2. **SRS Generation**: Reference `discovery_context.technical_context` and `discovery_context.ai_recommendations`
   - Performance budgets based on `three_month_success_criteria` and `hard_constraints`
   - Security requirements from `business_model` and `integration_requirements`
   - Accessibility needs from `user_access_method` and `primary_users`

3. **Design Decisions**: Reference `discovery_context.ai_recommendations` and `discovery_context.technical_context`
   - Technology choices from `recommended_tech_stack` and reasoning
   - Architecture decisions from `architecture_approach`
   - Risk mitigation from `risk_factors`

4. **Tasks Creation**: Reference `discovery_context.workflow_seeding` and `ai_recommendations.development_sequence`
   - Implementation order from `development_sequence`
   - Feature priorities from `user_success_journey`
   - Success criteria from `three_month_success_criteria`

**Context Reference Pattern**: When generating documents, AI should phrase references as:
- "Based on your discovery session, where you identified..."
- "As determined during project initialization, your users..."
- "Given your team context and technical requirements..."

## Notes
- This template consolidates MVP core protocol requirements
- All documentation is kept lean (≤ 1 page each) for MVP phase
- External services and containers are opt-in only
- TDD-Lite methodology is mandatory for MVP development
- Conventional commits should reference generated PRD and task documents

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the MVP project initialization, provide a summary including:
- **Project Name**: [Project name collected]
- **Access Method**: [User access method selected]
- **Primary Users**: [Target user group identified]
- **Technology Direction**: [Preliminary tech stack recommendation based on discovery]
- **Feature Directory Created**: `features/[AI: Insert current date as YYYY-MM-DD]-[kebab-case-project-name]/`
- **Generated Files**: `feature-manifest.json` with discovery context
- **Completion Time**: [AI: Insert current date and time in format: $(date '+%Y-%m-%d %H:%M:%S')]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 02-gen-prd.md to create the Product Requirements Document"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the project initialization?"

### Next Step Preview
**Next**: [02-gen-prd.md](./02-gen-prd.md) - Product Requirements Document Creation
**Phase 1 Purpose**: Define WHAT we're building (features, scope, goals)
**What PRD needs from this step**: Project identity, user context, technical direction, and discovery data from [feature-manifest.json](./feature-manifest.json)

**🚨 CRITICAL FOR AI AGENTS:**
**You are now working in `/features/YYYY-MM-DD-project-name/` directory**
**ALL subsequent documents (PRD, SRS, tasks, etc.) must be saved in this feature directory using `./filename.md`**

> **🔗 Context Flow:**
> - **Discovery Context** → [PRD Functional Requirements](./02-gen-prd.md#functional-requirements)
> - **User Research** → [PRD User Stories](./02-gen-prd.md#user-stories) 
> - **Technical Direction** → [SRS Technical Constraints](./03-gen-srs.md#technical-constraints)
> - **Business Model** → [PRD Success Metrics](./02-gen-prd.md#success-metrics)

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check for existing `feature-manifest.json` and present:

```
✅ WORKFLOW RESUME DETECTED
  🎯 01-mvp-entrypoint.md - Project initialization (CURRENT)
  ⏳ 02-gen-prd.md - Product requirements (pending)
  ⏳ 03-gen-srs.md - Software requirements (pending)
  ⏳ 04-gen-design-decisions-lite.md - Technology decisions (pending)
  ⏳ 05-gen-design.md - Component analysis (pending)
  ⏳ 06-gen-tasks-and-testing.md - Implementation tasks (pending)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📍 STARTING: PHASE 1 - Foundation (Define WHAT and WHY)
Phase 1 Purpose: Collect project requirements and establish foundation

Continue with project initialization? [Yes/No/Review Documents]
```