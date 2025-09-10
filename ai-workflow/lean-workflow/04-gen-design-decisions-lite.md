# Workflow: Design Decisions (MVP/Lite) - Learning-Guided

## Objective
Guide technical and UX design decisions through interactive questionnaires and template-driven frameworks. Build design decision-making skills while ensuring solid choices for MVP development.

---

## When to Use
- **Trigger**: After PRD creation, before gen-design.md
- **Purpose**: Make informed technical and UX decisions with guided learning
- **Context**: New projects, major technical decisions, or when unsure about design choices
- **Learning Goal**: Build decision-making confidence through structured guidance

---

## Prerequisites
- Completed PRD at `/prd/prd-[feature-name].md`
- **Completed SRS at `/srs/srs-[feature-name].md`** with performance budgets and quality constraints
- Basic understanding of project goals and user needs
- Willingness to learn and document decision rationale

---

## Workflow Steps

### 1. Self-Assessment & Context Setting
**Learning Context**: Understanding your current knowledge helps tailor guidance.

```markdown
## My Current Knowledge Level (1-5 scale)
- **Backend Technologies**: [ ] (1=New, 5=Expert)
- **Frontend Technologies**: [ ] (1=New, 5=Expert)  
- **Database Design**: [ ] (1=New, 5=Expert)
- **UX/UI Design**: [ ] (1=New, 5=Expert)
- **API Design**: [ ] (1=New, 5=Expert)

## Project Context
- **Project Type**: [Web App|Mobile App|API|Desktop App|Other]
- **Expected Users**: [<100|100-1K|1K-10K|10K+]
- **Timeline**: [<1 month|1-3 months|3-6 months|6+ months]
- **Team Size**: [Solo|2-3 people|4-10 people|10+ people]
```

### 2. Core Technology Stack Decisions

#### **Interactive Questionnaire: Backend Technology**

**Question Set A: Project Requirements & NFR Constraints**
1. **Primary functionality** of your backend:
   - [ ] **Simple CRUD operations** → *Python/FastAPI or Node.js/Express recommended*
   - [ ] **High-performance processing** → *Go or Rust recommended*
   - [ ] **Data-heavy analytics** → *Python recommended*
   - [ ] **Real-time features** → *Node.js or Go recommended*

2. **Performance requirements from SRS**:
   - [ ] **Response time < 100ms** → *Go, Rust, or optimized Node.js*
   - [ ] **Response time < 500ms** → *Python FastAPI, Node.js, Go*
   - [ ] **Response time < 2 seconds** → *Any technology with proper architecture*
   - [ ] **High concurrency (1000+ requests/sec)** → *Go, Node.js, or async Python*

3. **Security requirements from SRS**:
   - [ ] **Basic security (authentication, HTTPS)** → *Any modern framework*
   - [ ] **Enterprise security (OAuth, encryption)** → *Mature ecosystems: Python, Node.js, Java*
   - [ ] **Compliance requirements (HIPAA, SOC2)** → *Well-audited: Python, Node.js, Java*

4. **Your learning preference**:
   - [ ] **Want to learn industry-standard** → *Python or JavaScript/TypeScript*
   - [ ] **Want maximum performance** → *Go or Rust*
   - [ ] **Want rapid prototyping** → *Python or Node.js*

5. **Deployment preference**:
   - [ ] **Cloud platforms (AWS, GCP, Azure)** → *Python, Node.js, or Go*
   - [ ] **Simple hosting** → *Python or Node.js*
   - [ ] **Container deployment** → *Any language*

**Learning Notes**: *Backend choice affects development speed, performance, and learning curve. Consider SRS performance budgets when choosing - Go excels at low latency, Python at rapid development, Node.js at full-stack consistency. Security and compliance requirements may limit technology choices.*

#### **Template: Backend Decision Framework**

```markdown
## Backend Technology Decision

### Recommended Choice: [LANGUAGE]
**Rationale**: [Brief explanation based on questionnaire responses]

### Learning Resources:
- **Getting Started**: [Language-specific tutorial links]
- **Framework**: [Recommended framework and why]
- **Best Practices**: [Key principles to follow]

### Decision Confidence: [ ]/5
**What I learned**: [Your key insights from this decision]
**What I need to research more**: [Areas for further learning]
```

#### **Interactive Questionnaire: Frontend Technology**

**Question Set B: User Interface Requirements**
1. **UI complexity**:
   - [ ] **Simple forms and pages** → *HTML/CSS + minimal JavaScript*
   - [ ] **Interactive components** → *React or Vue.js*
   - [ ] **Complex state management** → *React with Redux or Vue with Vuex*
   - [ ] **Real-time updates** → *React or Vue with websockets*

2. **Development approach**:
   - [ ] **Learn modern best practices** → *TypeScript + React/Vue*
   - [ ] **Quick and simple** → *JavaScript + lightweight framework*
   - [ ] **Maximum control** → *Vanilla JavaScript*

3. **Design system needs**:
   - [ ] **Custom design** → *CSS-in-JS or CSS Modules*
   - [ ] **Quick styling** → *Tailwind CSS or Bootstrap*
   - [ ] **Professional look** → *Component library (Material-UI, Chakra)*

**Learning Notes**: *TypeScript adds safety but learning curve. React has huge community. Vue is beginner-friendly. Choose based on complexity needs and learning goals.*

### 3. Database & Architecture Decisions

#### **Interactive Questionnaire: Data Storage**

**Question Set C: Data Requirements**
1. **Data structure**:
   - [ ] **Simple tables with relationships** → *PostgreSQL or MySQL*
   - [ ] **Flexible document storage** → *MongoDB*
   - [ ] **Key-value pairs** → *Redis*
   - [ ] **Time-series data** → *PostgreSQL with TimescaleDB*

2. **Data volume expectations**:
   - [ ] **Small (< 1GB)** → *SQLite or PostgreSQL*
   - [ ] **Medium (1-100GB)** → *PostgreSQL or MySQL*
   - [ ] **Large (> 100GB)** → *PostgreSQL with partitioning*

3. **Query complexity**:
   - [ ] **Simple lookups** → *Any database*
   - [ ] **Complex joins** → *PostgreSQL or MySQL*
   - [ ] **Full-text search** → *PostgreSQL or Elasticsearch*

**Learning Notes**: *PostgreSQL is excellent for learning SQL and handles most use cases. MongoDB good for flexible schemas. Start simple, optimize later.*

### 4. UX/UI Design Decisions

#### **Guided Template: Component Planning**

```markdown
## UX Component Inventory

### Primary User Actions (List 3-5 main things users will do)
1. **Action**: [e.g., "Search for items"]
   - **Component Needed**: [e.g., "Search bar with filters"]
   - **Design Pattern**: [e.g., "Search input + dropdown filters"]
   - **Learning Note**: [What makes this component effective]

2. **Action**: [e.g., "View item details"]
   - **Component Needed**: [e.g., "Detail card/modal"]
   - **Design Pattern**: [e.g., "Card layout with image + text"]
   - **Learning Note**: [Design principles for information hierarchy]

### Layout Structure
- **Header**: [Navigation, logo, user actions]
- **Main Content**: [Primary content area organization]
- **Sidebar** (if needed): [Secondary navigation or filters]
- **Footer**: [Links, contact, legal]

### Design System Approach
- [ ] **Use component library** (Material-UI, Chakra, Ant Design)
  - *Learning benefit: Proven patterns, accessibility built-in*
- [ ] **Custom design with CSS framework** (Tailwind, Bootstrap)
  - *Learning benefit: Understand design principles, more control*
- [ ] **Fully custom CSS**
  - *Learning benefit: Deep CSS knowledge, full control*

**My Choice**: [Selected approach]
**Why**: [Your reasoning]
```

#### **Interactive Questionnaire: User Experience**

**Question Set D: User Flow Design**
1. **User journey complexity**:
   - [ ] **Single-page focused task** → *Simple, clean layout*
   - [ ] **Multi-step process** → *Wizard/stepper pattern*
   - [ ] **Dashboard/overview** → *Card-based layout*
   - [ ] **Content exploration** → *List/grid with search/filter*

2. **User expertise level**:
   - [ ] **Beginners** → *Clear labels, help text, simple navigation*
   - [ ] **Mixed users** → *Progressive disclosure, tooltips*
   - [ ] **Expert users** → *Keyboard shortcuts, dense information*

**Learning Notes**: *Good UX prioritizes user goals over features. Start with user tasks, then design interface to support those tasks efficiently.*

### 5. Integration & API Design

#### **Template: API Design Decisions**

```markdown
## API Design Framework

### API Style Decision
- [ ] **REST API** - *Good for CRUD operations, widely understood*
- [ ] **GraphQL** - *Flexible data fetching, single endpoint*
- [ ] **RPC-style** - *Simple function calls, easy to understand*

**My Choice**: [Selected style]
**Rationale**: [Why this fits your project]

### Data Format
- [ ] **JSON** - *Standard, easy to work with*
- [ ] **XML** - *Structured, good for complex data*
- [ ] **Form data** - *Simple, good for file uploads*

### Authentication Strategy
- [ ] **Simple API keys** - *Easy to implement*
- [ ] **JWT tokens** - *Stateless, scalable*
- [ ] **OAuth** - *Industry standard, secure*

**Learning Goal**: [What you want to understand better about APIs]
```

---

## Learning Integration

### Decision Documentation Template

```markdown
# Design Decisions Log - [Project Name]

## Technology Stack
- **Backend**: [Choice] - *[Confidence Level 1-5]*
  - **Why**: [Your reasoning]
  - **Learning**: [What this taught you]
  - **Next time**: [What you'd consider differently]

- **Frontend**: [Choice] - *[Confidence Level 1-5]*
  - **Why**: [Your reasoning]
  - **Learning**: [What this taught you]
  - **Next time**: [What you'd consider differently]

- **Database**: [Choice] - *[Confidence Level 1-5]*
  - **Why**: [Your reasoning]
  - **Learning**: [What this taught you]
  - **Next time**: [What you'd consider differently]

## UX/UI Decisions
- **Design Approach**: [Choice] - *[Confidence Level 1-5]*
  - **Why**: [Your reasoning]
  - **Learning**: [What this taught you]
  - **User Feedback**: [How users responded]

## Key Learning Insights
1. **Technical**: [Biggest technical insight]
2. **UX**: [Biggest UX insight]  
3. **Process**: [Biggest process insight]

## Future Decision Improvements
- **Research More**: [Topics to study further]
- **Experiment With**: [Technologies/approaches to try]
- **Get Feedback On**: [Areas where you want input]
```

---

## Output Format

Save the following documents:

1. **`/decisions/design-decisions-[project-name].md`** - Complete decision log with rationale
2. **`/decisions/learning-notes-[project-name].md`** - Personal learning insights and growth tracking
3. **Update `/artifacts/manifest.json`** with design decision artifacts

---

## AI Agent Directives
- Tailor question complexity to stated knowledge levels (1-5 scale)
- Provide educational context with each decision option
- Encourage experimentation while suggesting proven patterns for MVP
- Connect decisions to learning goals and skill building
- Flag when decisions require additional research or consultation
- Adapt guidance complexity based on user's growing confidence levels
Set reasoning_effort = medium; educational guidance requires thoughtful explanation

---

## Human Review Gate (Required)
- Confirm: technology stack decisions align with project goals and learning objectives
- Confirm: UX decisions support user needs and development timeline
- Confirm: confidence levels honestly reflect current knowledge
- Confirm: learning goals and areas for improvement identified
- Approve design decisions with documented rationale

---

## Handoff + Memory Sync

**Context for next workflow** (`gen-design.md`):
```json
{
  "design_decisions": {
    "backend_tech": "[chosen technology]",
    "frontend_tech": "[chosen technology]", 
    "database": "[chosen database]",
    "ui_approach": "[chosen UI approach]",
    "api_style": "[chosen API style]"
  },
  "learning_context": {
    "knowledge_levels": {
      "backend": "[1-5]",
      "frontend": "[1-5]",
      "database": "[1-5]",
      "ux_design": "[1-5]"
    },
    "learning_goals": ["[goal 1]", "[goal 2]"],
    "confidence_areas": ["[high confidence areas]"],
    "growth_areas": ["[areas needing development]"]
  },
  "decision_rationale": {
    "primary_factors": ["[key decision factors]"],
    "learning_priorities": ["[learning focus areas]"],
    "future_considerations": ["[things to revisit]"]
  }
}
```

---

## Integration with Lean Workflow
This workflow enhances the lean development process by:
- Providing structured decision-making for technical choices
- Building design knowledge progressively through practice
- Documenting rationale for future reference and learning
- Adapting guidance complexity to growing expertise
- Connecting design decisions to user needs and business goals

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the design decisions, provide a summary including:
- **Technology Stack Selected**: [Backend, Frontend, Database choices made]
- **UI/UX Approach**: [Design approach and rationale]
- **Learning Context**: [Knowledge levels and growth areas identified]
- **Decision Rationale**: [Key factors that influenced technology choices]
- **Learning Journal**: Updated with decisions and reasoning
- **Manifest Updated**: feature-manifest.json marked design decisions as completed
- **Completion Time**: [AI: Insert current date and time as YYYY-MM-DD HH:MM:SS]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 05-gen-design.md for component analysis"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the technology decisions?"

### Next Step Preview
**Next**: 05-gen-design.md - Component Analysis and Design
**Phase 2 Purpose**: Analyze existing code for component reuse (tech-aware)
**What Design Analysis needs from this step**: Technology stack choices, UI approach, and architecture decisions

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check feature-manifest.json status and present:

```
✅ WORKFLOW RESUME DETECTED
  ✅ 01-mvp-entrypoint.md - Project initialization (completed)
  ✅ 02-gen-prd.md - Product requirements (completed)
  ✅ 03-gen-srs.md - Software requirements (completed)
  🎯 04-gen-design-decisions-lite.md - Technology decisions (CURRENT)
  ⏳ 05-gen-design.md - Component analysis (pending)
  ⏳ 06-gen-tasks-and-testing.md - Implementation tasks (pending)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📋 Foundation Established:
  • Project: [Project name from discovery]
  • Requirements: [Functional and non-functional requirements defined]
  • Performance Budgets: [Key metrics from SRS]
  • Quality Gates: [Testing criteria from SRS]

📍 STARTING: PHASE 2 - Design (Decide HOW to build)
Phase 2 Purpose: Choose technology stack, UX approach (learning-guided)

Continue with design decisions? [Yes/No/Review Documents]
```
