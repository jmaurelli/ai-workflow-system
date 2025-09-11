# 🚀 Lean Workflow - AI-Driven MVP Development

**Fast-paced, lightweight development process for solo developers and small teams**

## 📋 Workflow Overview

This directory contains the complete lean workflow system - a 9-step process that takes you from project idea to completed MVP with comprehensive documentation.

### 🎯 **Sequential Workflow Documents (01-09)**

| Step | Document | Purpose | Time | Output |
|------|----------|---------|------|--------|
| **01** | [mvp-entrypoint.md](./01-mvp-entrypoint.md) | Project initialization & discovery | 12-15 min | `feature-manifest.json` |
| **02** | [gen-prd.md](./02-gen-prd.md) | Product Requirements Document | 8-12 min | `prd.md` |
| **03** | [gen-srs.md](./03-gen-srs.md) | Software Requirements Specification | 6-10 min | `srs.md` |
| **04** | [gen-design-decisions-lite.md](./04-gen-design-decisions-lite.md) | Technology & UX decisions | 10-15 min | `design-decisions.md` |
| **05** | [gen-design.md](./05-gen-design.md) | Component analysis & integration | 8-12 min | `design-analysis.md` |
| **06** | [gen-tasks-and-testing.md](./06-gen-tasks-and-testing.md) | Implementation tasks & testing | 10-15 min | `tasks.md` |
| **07** | [process-tasks.md](./07-process-tasks.md) | Task execution & TDD-Lite | Variable | Completed code |
| **08** | [gen-completion-summary.md](./08-gen-completion-summary.md) | Executive summary & traceability | 5-8 min | `completion-summary.md` |
| **09** | [gen-project-history.md](./09-gen-project-history.md) | Learning capture & quarterly rollups | 8-12 min | Project history |

### 🔧 **Supporting Documents**

| Document | Purpose | When to Use |
|----------|---------|-------------|
| [ai-native-bug-resolution.md](./ai-native-bug-resolution.md) | Systematic AI debugging with project intelligence | When bugs arise during development |
| [feature-centric-architecture.md](./feature-centric-architecture.md) | Directory structure guide | Reference for project organization |
| [context-distillation-examples.md](./context-distillation-examples.md) | Context management examples | Learning context optimization |
| [task-completion-feedback.md](./task-completion-feedback.md) | Feedback loop system | Improving workflow efficiency |

## 🎮 **Quick Start**

### For New Projects:
1. **Start here**: [01-mvp-entrypoint.md](./01-mvp-entrypoint.md)
2. **Follow the sequence**: Each document guides you to the next
3. **Use approval gates**: Review and approve at each major milestone
4. **Track progress**: Monitor via workflow transition protocol

### For Existing Projects:
1. **Resume detection**: Start at any document - the system detects your progress
2. **Bug resolution**: Use [bug-resolution-lite.md](./bug-resolution-lite.md) when issues arise
3. **Add features**: Create new feature directories following the same pattern

## 📁 **Generated Structure**

```
features/YYYY-MM-DD-project-name/
├── feature-manifest.json          # Project metadata & AI navigation
├── prd.md                         # Product requirements
├── srs.md                         # Software requirements  
├── design-decisions.md            # Technology choices
├── design-analysis.md             # Component integration
├── tasks.md                       # Implementation roadmap
├── learning-notes.md              # Knowledge tracking
├── completion-summary.md          # Executive summary
└── artifacts/                     # Generated content
    ├── api-contracts/
    ├── design-mockups/
    ├── test-results/
    └── performance-reports/
```

## 🤖 **AI Integration**

### **For AI Agents:**
- **Entry Point**: Always start with `feature-manifest.json` for context
- **Navigation**: Use `ai_navigation` section for document relationships
- **Priority**: Process documents by `ai_priority` indicators (high/medium/low)
- **Validation**: Validate JSON against [feature-manifest.schema.json](./feature-manifest.schema.json)

### **Key AI Features:**
- **Cross-document linking** for context navigation
- **Progressive discovery** with guided questioning
- **Automated transitions** between workflow steps
- **Resume detection** for interrupted workflows
- **Context preservation** across all documents

## 📊 **Validation & Quality**

### **JSON Schema Validation:**
```bash
# Validate feature manifest structure
ajv validate -s feature-manifest.schema.json -d features/*/feature-manifest.json
```

### **Document Cross-References:**
- All documents include navigation links to related documents
- Context flows are explicitly mapped (discovery → PRD → SRS → tasks)
- AI can validate consistency across document relationships

## 🎯 **Success Metrics**

- **MVP Time**: Typical project initialization: 12-15 minutes
- **Documentation Quality**: Professional-grade PRD, SRS, and task breakdown
- **Context Preservation**: 95%+ of discovery context flows through to implementation
- **AI Effectiveness**: Clear navigation and predictable structure for AI agents

## 🚀 **Advanced Features**

### **Workflow Orchestration:**
- **Automated transitions** between documents with user approval gates
- **Dynamic timestamps** for accurate project tracking
- **Phase progress visualization** for workflow state awareness

### **Enterprise Scaling:**
See [../scaling-workflow/](../scaling-workflow/) for enterprise-level enhancements including multi-team coordination, compliance frameworks, and advanced architecture patterns.

---

**💡 Start your next MVP:** [01-mvp-entrypoint.md](./01-mvp-entrypoint.md)
