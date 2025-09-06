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

## 🎯 How to Use This Sequence

### **For MVP Development:**
1. **Always start with `01-mvp-entrypoint.md`** to collect project requirements
2. **Follow the numbered sequence sequentially** - each document needs the previous document's output
3. **Generate documents in order** - the feed/seed relationships are critical
4. **Use completion documents** to capture learning and create executive visibility

### **For Enterprise Scaling:**
1. **Start with `s01-mvp-to-scaling-transition.md`** to assess and plan the transition
2. **Follow the s01-s08 sequence** for comprehensive enterprise development
3. **Coordinate multiple teams** using the enterprise manifest and coordination protocols
4. **Use enterprise completion** documents for compliance and strategic planning

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

## ✅ Key Benefits of Numbered Sequence

1. **Crystal Clear Flow**: No confusion about what comes next in the workflow
2. **Dependency Visibility**: Each number represents a feed/seed relationship
3. **Phase Organization**: Natural groupings without over-organizing the file system
4. **Scalability**: Easy to add new documents while maintaining sequence clarity
5. **AI Agent Friendly**: Simple numbered references for agent coordination
6. **Human Friendly**: Visual sequence makes workflow adoption easier

**The numbered sequence transforms workflow complexity into clear, actionable steps while preserving the sophisticated feed/seed relationships that make the workflows powerful!** 🎯✨
