# Workflow: Design Analysis & Integration (MVP-First)

## Objective
Analyze existing codebase for design patterns, components, and integration opportunities before implementing new features. Ensures consistent UI/UX while enabling design improvements.

## When to Use
- **New Features**: When adding functionality to existing applications
- **Feature Enhancements**: When improving existing features
- **Design Recovery**: When fixing design inconsistencies
- **Scaling Projects**: When maintaining design systems

## Workflow Steps

### 1. Codebase Analysis
- Scan existing codebase for related components and patterns
- Identify existing UI elements that serve similar functions
- Document current design patterns and conventions
- **Flag inconsistencies** for potential recovery workflow (optional)

### 2. Integration Planning
- Determine integration approach (replace, enhance, or add new)
- Identify opportunities for component reuse
- Plan user experience integration points
- **Recommend recovery actions** if inconsistencies are found (optional)

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
- Always run after PRD creation for existing codebases
- Scan for existing components before generating new ones
- Flag duplicate or inconsistent components for recovery consideration
- Save design analysis to `/design/design-[feature-name].md`
- Validate integration approach matches PRD Design Context
Set reasoning_effort = medium; thorough analysis but concise output

---

## Human Review Gate (Required)
- Confirm: existing components identified and reuse opportunities documented
- Confirm: integration approach aligns with PRD Design Context
- Confirm: any inconsistencies flagged for potential recovery
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