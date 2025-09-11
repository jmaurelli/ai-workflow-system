# Workflow: Design Analysis & Integration (MVP-First)

## Objective
Analyze existing codebase for design patterns, components, and integration opportunities before implementing new features. Ensures consistent UI/UX while enabling design improvements.

## When to Use
- **New Features**: When adding functionality to existing applications
- **Feature Enhancements**: When improving existing features
- **Design Recovery**: When fixing design inconsistencies
- **Scaling Projects**: When maintaining design systems

## Workflow Steps

### 1. Design Decisions Integration
- **Read design decisions** from `/decisions/design-decisions-[project-name].md`
- **Apply tech stack choices** to component analysis (React vs Vue, CSS approach, etc.)
- **Use UX decisions** to guide component selection and user flow integration
- **Consider learning goals** from design decisions when suggesting approaches

### 2. Codebase Analysis (Design-Decision Aware)
- Scan existing codebase for related components and patterns **matching chosen tech stack**
- Identify existing UI elements that serve similar functions **within chosen design approach**
- Document current design patterns and conventions **compatible with chosen frameworks**
- **Flag inconsistencies** for potential recovery workflow (optional)
- **Validate alignment** between existing code and design decisions

### 3. Integration Planning (Learning-Guided)
- Determine integration approach (replace, enhance, or add new) **based on design decisions**
- Identify opportunities for component reuse **within chosen tech stack**
- Plan user experience integration points **supporting chosen UX approach**
- **Recommend recovery actions** if inconsistencies are found (optional)
- **Suggest learning opportunities** when integration requires new skills

## Inconsistency Detection (Optional)
- **Automatic Detection**: Scan for duplicate or similar components
- **Flagging**: Document inconsistencies found during analysis
- **Recommendations**: Suggest recovery actions if needed
- **User Decision**: Let user decide when to run recovery workflow

### 3. Design Decisions
- Document UI/UX decisions before implementation
- Specify component reuse vs. new component creation
- Define design consistency requirements

### 4. Implementation Guidance
- Provide clear guidance for AI implementation
- Specify existing components to use
- Define integration patterns to follow

## Output Format
```markdown
# Design Analysis - [Feature Name]

## Existing Components
- **Component Name**: [Description and location]
- **Usage Pattern**: [How it's currently used]
- **Reuse Opportunity**: [Can this be reused?]

## Integration Approach
- **Primary Strategy**: [Replace/Enhance/Add New]
- **Component Reuse**: [Which existing components to use]
- **New Components**: [Which new components are needed]

## Design Decisions
- **UI Pattern**: [Which existing pattern to follow]
- **User Experience**: [How this integrates with existing flows]
- **Consistency Requirements**: [What must remain consistent]

## Implementation Guidance
- **Existing Components to Use**: [Specific components and locations]
- **Integration Points**: [Where to integrate with existing code]
- **Design Patterns to Follow**: [Specific patterns to maintain]

## Inconsistency Flags (Optional)
- **Duplicate Components**: [Components that serve similar purposes]
- **Integration Issues**: [Components that don't integrate well]
- **Recovery Recommendations**: [Suggest running gen-design-recovery.md if needed]
```

---

## AI Agent Directives
- **Always read design decisions first** from `/decisions/design-decisions-[project-name].md`
- **Apply tech stack choices** when scanning codebase (focus on chosen frameworks/libraries)
- **Honor UX decisions** when suggesting component approaches and user flows
- **Consider learning context** - suggest approaches that support user's learning goals
- Scan for existing components before generating new ones **within chosen tech stack**
- Flag duplicate or inconsistent components for recovery consideration
- Save design analysis to `/design/design-[feature-name].md`
- Validate integration approach matches PRD Design Context **and design decisions**
- **Suggest learning opportunities** when integration involves new concepts for the user
Set reasoning_effort = medium; thorough analysis with design decision integration

---

## Human Review Gate (Required)
- Confirm: design decisions from `/decisions/design-decisions-[project-name].md` have been integrated
- Confirm: existing components identified and reuse opportunities documented **for chosen tech stack**
- Confirm: integration approach aligns with PRD Design Context **and design decisions**
- Confirm: any inconsistencies flagged for potential recovery
- Confirm: learning opportunities identified for skill development
- Approve proceeding to task generation with design guidance

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "design",
  "feature_slug": "[feature-name]",
  "design_path": "/design/design-[feature-name].md",
  "existing_components": ["..."],
  "integration_approach": "replace|enhance|add-new",
  "reuse_opportunities": ["..."],
  "inconsistencies_found": ["..."],
  "recovery_recommended": true|false
}
```

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "design_path": "/design/design-[feature-name].md",
  "integration_approach": "replace|enhance|add-new"
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the design analysis, provide a summary including:
- **Component Analysis**: [Number of existing components analyzed]
- **Reuse Strategy**: [Components identified for reuse vs new development]
- **Integration Approach**: [How new feature integrates with existing code]
- **Design Patterns**: [UI/UX patterns established or reused]
- **Architecture Impact**: [Changes to existing architecture]
- **Manifest Updated**: feature-manifest.json marked design analysis as completed
- **Completion Time**: [AI: Insert current date and time in format: $(date '+%Y-%m-%d %H:%M:%S')]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 06-gen-tasks-and-testing.md for implementation planning"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the design analysis?"

### Next Step Preview
**Next**: 06-gen-tasks-and-testing.md - Implementation Tasks and Testing
**Phase 3 Purpose**: Actually BUILD it (generate implementation tasks)
**What Tasks needs from this step**: Component integration strategy, design patterns, and architecture decisions

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check feature-manifest.json status and present:

```
✅ WORKFLOW RESUME DETECTED
  ✅ 01-mvp-entrypoint.md - Project initialization (completed)
  ✅ 02-gen-prd.md - Product requirements (completed)
  ✅ 03-gen-srs.md - Software requirements (completed)
  ✅ 04-gen-design-decisions-lite.md - Technology decisions (completed)
  🎯 05-gen-design.md - Component analysis (CURRENT)
  ⏳ 06-gen-tasks-and-testing.md - Implementation tasks (pending)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📋 Design Foundation:
  • Technology Stack: [Backend, frontend, database choices]
  • UI Approach: [Design patterns and rationale]
  • Learning Context: [Knowledge levels identified]

📍 COMPLETING: PHASE 2 - Design (Decide HOW to build)
Phase 2 Purpose: Analyze existing code for component reuse (tech-aware)

Continue with design analysis? [Yes/No/Review Documents]
```