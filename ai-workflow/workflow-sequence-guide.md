# Workflow Sequence Guide

**Visual feed/seed flow for lean and enterprise workflows**

---

## 🚀 MVP/Lean Workflow

### **PHASE 1: FOUNDATION** - *Define WHAT and WHY*
```
01-mvp-entrypoint.md              ← START: Progressive guided discovery
    ↓ FEEDS discovery_context + project_identity + ai_recommendations
02-gen-prd.md                     ← Define features, scope, goals  
    ↓ FEEDS functional_requirements + user_stories + success_metrics
03-gen-srs.md                     ← Define NFRs, performance, security
    ↓ FEEDS performance_budgets + technical_constraints + quality_standards
```

### **PHASE 2: DESIGN** - *Decide HOW to build*
```
04-gen-design-decisions-lite.md   ← Choose tech stack, UX approach
    ↓ FEEDS technology_choices + architecture_rationale + learning_insights  
05-gen-design.md                  ← Analyze component reuse, integration
    ↓ FEEDS component_strategy + design_analysis + implementation_guidance
```

### **PHASE 3: IMPLEMENTATION** - *Actually BUILD it*
```
06-gen-tasks-and-testing.md       ← Generate implementation tasks
    ↓ FEEDS task_breakdown + acceptance_criteria + testing_strategy
07-process-tasks.md               ← Execute with TDD-Lite
    ↓ FEEDS completed_implementation + validation_results + bug_resolutions
```

### **PHASE 4: COMPLETION** - *DOCUMENT and LEARN*
```
08-gen-completion-summary.md      ← Executive summary with traceability
    ↓ FEEDS completion_insights + architecture_decisions + lessons_learned
09-gen-project-history.md         ← Quarterly rollups and organizational learning
```

### **Support Workflows**
```
bug-resolution-lite.md            ← Debug workflow with guided discovery
feature-centric-architecture.md  ← Directory structure reference
```

---

## 🏗️ Enterprise Scaling Workflow

### **PHASE 1: TRANSITION** - *Scale from MVP to Enterprise*
```
s01-mvp-to-scaling-transition.md  ← START: MVP assessment + enterprise transition plan
    ↓ FEEDS transition_analysis + enterprise_requirements + scaling_strategy
```

### **PHASE 2: ARCHITECTURE** - *Design Enterprise System*
```
s02-gen-design-decisions-scaling.md ← Enterprise architecture decisions
    ↓ FEEDS enterprise_architecture + system_patterns + governance_framework
s03-gen-srs-scaling.md             ← Comprehensive enterprise NFRs
    ↓ FEEDS compliance_requirements + enterprise_quality + performance_standards
s04-create-prd-scaling.md          ← Full enterprise PRD
    ↓ FEEDS stakeholder_requirements + enterprise_features + business_alignment
```

### **PHASE 3: IMPLEMENTATION** - *Build Enterprise System*  
```
s05-gen-design-scaling.md          ← Enterprise component/design system analysis
    ↓ FEEDS design_system + component_strategy + integration_patterns
s06-tasks-and-testing-scaling.md   ← Multi-team coordinated tasks
    ↓ FEEDS enterprise_implementation + team_coordination + testing_framework
```

### **PHASE 4: COMPLETION** - *Enterprise Outcomes*
```
s07-gen-enterprise-completion-summary.md ← Enterprise summary + compliance
    ↓ FEEDS enterprise_achievements + compliance_validation + architecture_outcomes  
s08-gen-enterprise-history.md            ← Enterprise architectural evolution
```

### **Support Workflows**
```
bug-resolution-scaling.md                 ← Enterprise debug workflow  
enterprise-feature-centric-architecture.md ← Enterprise directory structure
```

---

## 🔄 Workflow Transitions

### **MVP → Enterprise**
```
Complete 01-09 → s01-mvp-to-scaling-transition.md → Continue s02-s08
```

### **Feed/Seed Summary**
| Phase | MVP | Enterprise | Key Data Flow |
|-------|-----|------------|---------------|
| **Foundation** | 01-03 | s01 | `discovery_context` → `requirements` |
| **Design** | 04-05 | s02-s04 | `requirements` → `architecture_decisions` |  
| **Implementation** | 06-07 | s05-s06 | `architecture` → `implementation_tasks` |
| **Completion** | 08-09 | s07-s08 | `implementation` → `learning_outcomes` |
