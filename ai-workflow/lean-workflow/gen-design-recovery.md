# Workflow: Design Recovery & Consolidation (MVP-First)

## Objective
Identify and fix design inconsistencies, duplicate components, and integration issues in existing codebases. Consolidate similar functionality and improve overall design consistency.

## When to Use
- **Design Inconsistencies**: When similar functionality exists in multiple places
- **Duplicate Components**: When multiple components serve the same purpose
- **Integration Issues**: When new features don't integrate well with existing UI
- **Design Debt**: When technical debt affects user experience

## Workflow Steps

### 1. Inconsistency Analysis
- Scan codebase for duplicate or similar components
- Identify design patterns that are inconsistent
- Document integration issues and user experience problems

### 2. Consolidation Planning
- Determine which components to keep, merge, or remove
- Plan consolidation approach (merge, replace, or refactor)
- Identify opportunities for component reuse

### 3. Recovery Strategy
- Document recovery approach for each inconsistency
- Plan migration strategy for existing functionality
- Define rollback plans if recovery fails

### 4. Implementation Plan
- Create tasks for design recovery
- Specify testing requirements for consolidated components
- Define validation criteria for recovery success

## Output Format
```markdown
# Design Recovery - [Feature Name]

## Inconsistencies Found
- **Duplicate Component**: [Description and locations]
- **Inconsistent Pattern**: [Description and impact]
- **Integration Issue**: [Description and user impact]

## Consolidation Plan
- **Components to Keep**: [Which components to retain]
- **Components to Merge**: [Which components to combine]
- **Components to Remove**: [Which components to eliminate]

## Recovery Strategy
- **Primary Approach**: [Main recovery strategy]
- **Fallback Plan**: [Alternative approach if primary fails]
- **Validation Criteria**: [How to measure recovery success]

## Implementation Tasks
- **Task 1**: [Specific recovery task]
- **Task 2**: [Specific recovery task]
- **Task 3**: [Specific recovery task]
```

---

## AI Agent Directives
- Run when inconsistencies are detected by gen-design.md
- Create HIGH PRIORITY recovery tasks
- Save recovery plan to `/design/recovery-[feature-name].md`
- Generate tasks that can be processed by gen-tasks-and-testing.md
Set reasoning_effort = medium; thorough analysis with actionable output

---

## Human Review Gate (Required)
- Confirm: inconsistencies identified are worth fixing
- Confirm: consolidation plan preserves necessary functionality
- Confirm: recovery tasks are appropriately prioritized
- Approve proceeding with recovery implementation

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "recovery",
  "feature_slug": "[feature-name]",
  "recovery_path": "/design/recovery-[feature-name].md",
  "inconsistencies": ["..."],
  "consolidation_plan": "merge|replace|refactor",
  "recovery_tasks": ["..."],
  "priority": "high"
}
```

### Context Seed (for task generation)
Provide this block to gen-tasks-and-testing.md:

```json
{
  "feature_slug": "[feature-name]",
  "recovery_path": "/design/recovery-[feature-name].md",
  "recovery_required": true,
  "priority": "high"
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

## **Workflow Integration Summary**

### **Main Workflow (Automatic):**
1. **gen-prd.md** → Creates PRD with design context
2. **gen-design.md** → Analyzes existing codebase and plans integration
3. **gen-tasks-and-testing.md** → Generates tasks with design awareness
4. **process-tasks.md** → Executes tasks with design guidance

### **Recovery Workflow (Standalone):**
- **gen-design-recovery.md** → Standalone workflow for fixing existing inconsistencies
- **User-triggered** when inconsistencies are discovered
- **Optional integration** with gen-design.md for inconsistency detection

### **Benefits of This Approach:**

1. **Clean Separation**: PRD focuses on feature requirements, design workflows handle design concerns
2. **Flexible Recovery**: User decides when to run recovery workflow
3. **Optional Detection**: gen-design.md can flag inconsistencies without forcing recovery
4. **Standalone Recovery**: Recovery workflow can be used independently when needed
5. **Proper Workflow Order**: Design analysis happens before task generation

### **User Experience:**

- **Normal Flow**: PRD → Design Analysis → Tasks → Execution
- **Recovery Flow**: User discovers inconsistency → Runs gen-design-recovery.md → Fixes issues
- **Optional Detection**: gen-design.md can flag inconsistencies for user consideration

This approach gives you the flexibility to handle design inconsistencies when they arise while keeping the main workflow clean and focused. The recovery workflow remains available as a powerful standalone tool for fixing existing design issues!