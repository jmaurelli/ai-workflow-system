# Workflow Sequence Guide

## Visual Workflow Flow - Complete Documentation Architecture

This guide shows the **numbered sequence** and **phase organization** of all workflow documents, making the feed/seed relationships crystal clear.

---

## 🚀 MVP/Lean Workflow (Feature Development)

### **PHASE 1: FOUNDATION** - *Define WHAT and WHY*
```
01-mvp-entrypoint.md              ← START HERE: Collect project requirements
    ↓ FEEDS project data
02-gen-prd.md                     ← Define what we're building (features, scope, goals)
    ↓ FEEDS functional requirements  
03-gen-srs.md                     ← Define quality requirements (NFRs, performance, security)
    ↓ FEEDS performance budgets & constraints
```

### **PHASE 2: DESIGN** - *Decide HOW to build*
```
04-gen-design-decisions-lite.md   ← Choose technology stack, UX approach (learning-guided)
    ↓ FEEDS technology choices & rationale
05-gen-design.md                  ← Analyze existing code for component reuse (tech-aware)
    ↓ FEEDS component integration strategy
```

### **PHASE 3: IMPLEMENTATION** - *Actually BUILD it*
```
06-gen-tasks-and-testing.md       ← Generate implementation tasks (context-embedded)
    ↓ FEEDS task list with smart context
07-process-tasks.md               ← Execute tasks with TDD-Lite (context-aware)
    ↓ FEEDS completed implementation
```

### **PHASE 4: COMPLETION** - *DOCUMENT and LEARN*
```
08-gen-completion-summary.md      ← Generate executive summary (with traceability)
    ↓ FEEDS completion insights
09-gen-project-history.md         ← Capture organizational learning (quarterly rollups)
```

### **Supporting Documents (Conditional/Reference)**
```
gen-design-recovery.md            ← Optional: Fix design inconsistencies
feature-centric-architecture.md  ← Reference: Feature directory architecture
context-distillation-examples.md ← Reference: Context management examples
task-completion-feedback.md      ← Reference: Feedback loop system
design-learning-journal.md       ← Reference: Personal learning tracking
```

---

## 🏗️ Enterprise Scaling Workflow (Complex Distributed Systems)

### **PHASE 1: TRANSITION** - *Scale from MVP to Enterprise*
```
s01-mvp-to-scaling-transition.md  ← START HERE: Assess MVP and plan enterprise transition
    ↓ FEEDS transition analysis & enterprise requirements
```

### **PHASE 2: ARCHITECTURE** - *Design Enterprise System*
```
s02-gen-design-decisions-scaling.md ← Make enterprise architecture decisions (system-wide)
    ↓ FEEDS enterprise architecture choices
s03-gen-srs-scaling.md             ← Define comprehensive enterprise NFRs (compliance-ready)
    ↓ FEEDS enterprise quality constraints  
s04-create-prd-scaling.md          ← Create full enterprise PRD (stakeholder-aligned)
    ↓ FEEDS enterprise feature requirements
```

### **PHASE 3: IMPLEMENTATION** - *Build Enterprise System*
```
s05-gen-design-scaling.md          ← Analyze enterprise component/design system needs
    ↓ FEEDS enterprise design strategy
s06-tasks-and-testing-scaling.md   ← Generate multi-team coordinated tasks
    ↓ FEEDS enterprise implementation with team coordination
```

### **PHASE 4: COMPLETION** - *Enterprise Outcomes & Strategy*
```
s07-gen-enterprise-completion-summary.md ← Generate enterprise summary (compliance & architecture)
    ↓ FEEDS enterprise achievements
s08-gen-enterprise-history.md            ← Capture enterprise architectural evolution
```

### **Supporting Documents (Conditional/Reference)**
```
gen-design-system-scaling.md           ← Optional: Create comprehensive design system
gen-design-recovery-scaling.md         ← Optional: Fix enterprise design debt
enterprise-feature-centric-architecture.md ← Reference: Enterprise directory architecture
context-distillation-examples-scaling.md   ← Reference: Enterprise context examples
task-completion-feedback-scaling.md        ← Reference: Enterprise feedback loops
design-learning-journal-scaling.md         ← Reference: Enterprise learning tracking
tdd-with-design-scaling.md                 ← Reference: Enterprise TDD methodology
project-templates-scaling.md               ← Reference: Enterprise project templates
scaling-workflow-cheatsheet.md             ← Reference: Quick scaling reference
scaling-workflow-diagram.md                ← Reference: Visual scaling workflow
test-suite-scaling.md                      ← Reference: Enterprise testing standards
```

---

## 🔄 Multi-Agent Coordination (Parallel Implementation)

### **Multi-Agent Documents (Advanced)**
```
multi-agent/
├── multi-agent-workflow-protocol.md      ← Agent coordination architecture
├── automated-task-completion.md          ← Automated implementation with quality
├── agent-communication-system.md         ← Multi-agent communication protocols
└── multi-agent-integration-guide.md      ← Step-by-step multi-agent setup
```

---

## 🤖 Automation Execution Integration

### **Real File Generation Capabilities**
The numbered workflow sequence now supports **complete automation execution**:

- **Orchestrators ACTUALLY execute** workflow documents (not just planning)
- **Feature directories automatically created**: `/features/YYYY-MM-DD-feature-name/`
- **AI execution instructions generated** for each workflow step
- **Complete manifest tracking** with execution logs and validation
- **AI agent coordination** with structured execution guidance

### **Execution Architecture**
```
Orchestrator → workflow-executor.py → Workflow Document → AI Instructions → Real Files
     ↓              ↓                    ↓                ↓               ↓
Planning &     Document Parsing    Execution Logic   AI Guidance    Feature Directory
Gate Logic     & Context           & Validation      & Tracking     & Manifest
```

### **Generated File Structure**
```
/features/YYYY-MM-DD-feature-name/
├── 📄 feature-manifest.json          ← Execution tracking and metadata
├── 📄 01-output.md                   ← AI instructions for 01-mvp-entrypoint.md
├── 📄 02-output.md                   ← AI instructions for 02-gen-prd.md
├── 📄 03-output.md                   ← AI instructions for 03-gen-srs.md
├── ... (continuing through 09-output.md)
├── 🤖 ai-helper.sh                   ← AI agent guidance script
└── 📁 artifacts/                     ← Storage for generated content
    ├── api-contracts/
    ├── design-mockups/
    ├── test-results/
    └── performance-reports/
```

### **AI Agent Integration Workflow**
1. **Orchestrator Execution**: Creates feature directory with AI instructions
2. **AI Agent Processing**: Reads workflow documents and execution instructions  
3. **Content Generation**: AI agent generates required outputs (PRD, SRS, tasks, etc.)
4. **Validation & Tracking**: Completion status marked and validated
5. **Sequential Progression**: Continue through numbered sequence 01→09

---

## 🎯 How to Use This Sequence

### **For MVP Development (Automated Execution):**
1. **Run automation orchestrator** to ACTUALLY create feature structure:
   ```bash
   ./ai-workflow-runner.py --mode=autonomous --feature="Your Project"
   # Creates /features/YYYY-MM-DD-your-project/ with real files!
   ```
2. **Follow the numbered sequence automatically** - orchestrator handles dependencies
3. **AI agent executes workflow documents** using generated instructions in XX-output.md files
4. **Use completion documents** for executive visibility and organizational learning

### **For Enterprise Scaling (Automated Execution):**
1. **Run enterprise automation orchestrator** to ACTUALLY create enterprise structure:
   ```bash
   ./enterprise-ai-workflow-runner.py --mode=autonomous --feature="Enterprise System" --compliance=GDPR
   # Creates /enterprise-features/YYYY-MM-DD-enterprise-system/ with real files!
   ```
2. **Follow the s01-s08 sequence automatically** - orchestrator handles enterprise coordination
3. **AI agent executes enterprise workflows** with compliance and governance integration
4. **Use enterprise completion documents** for compliance reporting and strategic planning

### **For Multi-Agent Implementation:**
1. **Setup multi-agent coordination** using the multi-agent protocol documents
2. **Run foundation documents** in parallel with agent coordination
3. **Coordinate implementation phase** with multiple specialized agents
4. **Use automated completion** for seamless handoff and quality validation

---

## 📊 Phase Summary Table

| Phase | MVP Workflow | Enterprise Workflow | Purpose |
|-------|-------------|-------------------|---------|
| **Phase 1** | Foundation (01-03) | Transition (s01) | Define WHAT & WHY |
| **Phase 2** | Design (04-05) | Architecture (s02-s04) | Decide HOW to build |
| **Phase 3** | Implementation (06-07) | Implementation (s05-s06) | Actually BUILD it |
| **Phase 4** | Completion (08-09) | Completion (s07-s08) | DOCUMENT & LEARN |

---

## 🔗 Cross-Workflow Integration

### **MVP → Enterprise Transition:**
- Complete MVP workflow (01-09) → Run `s01-mvp-to-scaling-transition.md` → Continue with enterprise workflow (s02-s08)

### **Feature-Centric Integration:**
- **MVP Features**: Stored in `/features/YYYY-MM-DD-feature-name/`
- **Enterprise Features**: Stored in `/enterprise-features/YYYY-MM-DD-feature-name/`
- **History**: Archived in `/project-history/` or `/enterprise-history/`

### **Multi-Agent Integration:**
- Can be applied to **both MVP and Enterprise workflows**
- Enables **parallel implementation** while maintaining quality and coordination
- Uses the **same numbered sequence** with agent coordination overlays

---

## ✅ Key Benefits of Numbered Sequence + Automation

1. **Crystal Clear Flow**: No confusion about what comes next in the workflow
2. **Dependency Visibility**: Each number represents a feed/seed relationship
3. **Phase Organization**: Natural groupings without over-organizing the file system
4. **Scalability**: Easy to add new documents while maintaining sequence clarity
5. **AI Agent Friendly**: Simple numbered references for agent coordination
6. **Human Friendly**: Visual sequence makes workflow adoption easier
7. **🚀 Real Execution**: Orchestrators ACTUALLY create files and directories
8. **🤖 AI Integration**: Structured execution instructions for seamless AI coordination
9. **📊 Complete Tracking**: Manifest files track execution progress and validation
10. **⚡ Automation Intelligence**: Risk-based gates and adaptive learning capabilities

**The numbered sequence transforms workflow complexity into clear, actionable, EXECUTABLE steps while preserving sophisticated feed/seed relationships AND delivering real automation capabilities!** 🎯🚀✨
