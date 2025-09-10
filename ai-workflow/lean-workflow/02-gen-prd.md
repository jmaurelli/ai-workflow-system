Developer: # Workflow: Product Requirements Document (PRD) Creation (MVP-First)

## Objective
Efficiently capture an idea and transform it into a **Lean PRD** focused on MVP development. The PRD should be lightweight, actionable, and quick to produce, with the flexibility to be expanded into a Full PRD if needed.

---

## Quickstart (Lean PRD - Feature-Centric)
- **Auto-detect structure**: Check if working in feature directory (`/features/[date]-[slug]/`) or legacy structure
- **Feature-centric**: Save as `./prd.md` within current feature directory  
- **Legacy compatibility**: Fall back to `/prd/prd-[feature-name].md` if not in feature directory
- Define a slug for `[feature-name]` using lowercase kebab-case (e.g., "User Signup" → `user-signup`)
- Capture the feature in 1–2 sentences
- Ask only critical clarifying questions (problem, user, success)
- Complete the Lean PRD template below (≤ 400 words total)
- Update `./feature-manifest.json` with PRD completion status

---

## Workflow (Lean-First - Feature-Centric)
Begin with a concise checklist (3-7 bullets) of what you will do; keep items conceptual, not implementation-level.
1. **Auto-detect document structure**: Check if in feature directory or legacy structure
2. Define the `[feature-name]` slug (lowercase, kebab-case) if not already established
3. Capture the feature or idea succinctly in 1–2 sentences
4. Ask only the most **critical clarifying questions** (e.g., What problem does this solve? Who is the user? What defines success?)
5. Complete the **Lean PRD template** provided below (≤ 400 words)
6. **Feature-centric**: Save as `./prd.md` OR **Legacy**: Save as `/prd/prd-[feature-name].md`
7. **Update feature manifest**: Mark PRD as completed in `./feature-manifest.json` (if feature-centric)
After each step, verify that all required information has been captured; if not, request only the minimal essential clarification or complete the missing parts before proceeding.

---

## Lean PRD Template
```markdown
# PRD - [Feature Name]

## Overview
A one-paragraph summary describing the feature and its importance.

## Goals
- [ ] Goal 1
- [ ] Goal 2

## User Stories
- As a [user], I want [action] so that [benefit].

## Functional Requirements
Number requirements for traceability using IDs like `REQ-1`, `REQ-1.1`.
1. [REQ-1] Requirement 1
2. [REQ-2] Requirement 2

## Design Context (Mandatory)
- **Existing Components**: [List relevant existing UI components to consider]
- **Integration Approach**: [Replace existing vs. add new vs. enhance existing]
- **UI Patterns**: [Reference 1-2 key existing patterns to follow]
- **User Experience**: [How this integrates with existing user flows]

## Assumptions
- [Key assumption]

## Out of Scope / Non-Goals
- [Explicitly not doing X]

## Success Criteria
- [ ] **MVP Completion**: [Specific measurable outcome]
- [ ] **Performance**: [e.g., p50 [key flow] < 2s; error rate < 1%]
- **User Experience**: [e.g., navigation intuitive for new users]
- [ ] **Technical**: [e.g., all smoke tests pass]

## Quality Gates (Optional)
- **Week 1**: [Milestone description]
- **Week 2**: [Milestone description]

## Risks / Unknowns
- [Risk/Unknown with impact level]

## Risk Mitigation (Optional)
- **High-Risk Areas**: [Specific tasks or components]
- **Contingency Plans**: [Fallback approaches if primary plan fails]

## Technical Context
- **Architecture**: [High-level component structure]
- **Tech Stack**: [Key technologies if known]
- **Integration Points**: [External services, APIs, databases]

## Linkages (optional)
- Tasks: /tasks/tasks-[feature-name].md
- Templates: dev-utils/dev_workflow/generate-and-process/project-templates.md
- Architecture: /docs/architecture.md
```

---

## Criteria for Expanding to a Full PRD
Move to a Full PRD (see `project-templates.md`) if:
- The feature is cross-functional,
- It has a significant impact on architecture or design,
- Or additional collaborators will be involved.

If added complexity or NFRs are material to MVP execution, generate a Lean SRS using `gen-srs.md` before creating tasks.

---

## AI Agent Directives (Feature-Centric)
- Default to creating a **Lean PRD** unless otherwise instructed
- **Auto-detect document structure**: Check current working directory for feature structure vs legacy structure
- **Feature-centric mode**: If in `/features/[date]-[slug]/` directory, save as `./prd.md` and update `./feature-manifest.json`
- **Legacy mode**: If not in feature directory, use legacy paths `/prd/prd-[feature-name].md`
- Use a lowercase, kebab-case slug for `[feature-name]` consistently across PRD, tasks, and tests
- Prompt the human explicitly for `[feature-name]` as `feature_slug` and BLOCK until provided. Do NOT auto-generate, infer, or randomize the slug
- Validate `feature_slug` format (lowercase kebab-case). If invalid, show the format and re-prompt
- **Path determination logic**: 
  ```bash
  if [[ "$PWD" == */features/*-* ]]; then
    PRD_PATH="./prd.md"
    UPDATE_MANIFEST=true
  else
    mkdir -p "/prd"
    PRD_PATH="/prd/prd-[feature-name].md"
    UPDATE_MANIFEST=false
  fi
  ```
- Limit Lean PRDs to one page and ≤ 400 words
- Validate that the file exists, is accessible, and that all template sections appear in the specified order. If validation fails, self-correct before completion
- Include the optional Linkages section with appropriate paths (feature-centric vs legacy)
Set reasoning_effort = minimal; keep outputs concise and focused.

---

## Human Review Gate (Required)
- Confirm: assumptions, non-goals, requirement IDs (`REQ-*`), and success criteria.
- Confirm: overview, goals, and user stories are accurate and sufficient.
- Confirm: **Design Context** is complete (existing components, integration approach, patterns).
- Confirm: architecture decisions are captured; `/docs/architecture.md` is seeded and linked.
- Approve proceeding to task generation.

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "prd",
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name].md",
  "requirement_ids": ["REQ-1", "REQ-2"],
  "assumptions": ["..."],
  "non_goals": ["..."],
  "success_criteria": ["..."],
  "design_context": {
    "existing_components": ["..."],
    "integration_approach": "replace|enhance|add-new",
    "ui_patterns": ["..."]
  },
  "technical_context": {
    "architecture": "...",
    "tech_stack": "...",
    "integration_points": ["..."]
  },
  "quality_gates": ["..."],
  "risk_areas": ["..."]
}
```

### Artifact Manifest Update
- Append or create `/artifacts/manifest.json` with the same keys, plus timestamp.

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name].md",
  "requirement_ids": ["REQ-1", "REQ-2"]
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

---

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the PRD creation, provide a summary including:
- **PRD Generated**: `./prd.md` in feature directory
- **Requirements Count**: [Number of functional requirements created]
- **User Stories**: [Number of user stories defined]
- **Success Criteria**: [Key measurable outcomes identified]
- **Feature Scope**: [Brief description of MVP scope defined]
- **Manifest Updated**: feature-manifest.json marked PRD as completed
- **Completion Time**: [AI: Insert current date and time as YYYY-MM-DD HH:MM:SS]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 03-gen-srs.md to define Software Requirements Specification"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the PRD?"

### Next Step Preview
**Next**: 03-gen-srs.md - Software Requirements Specification Creation
**Phase 1 Purpose**: Define quality requirements (NFRs, performance, security)
**What SRS needs from this step**: Functional requirements, user stories, and performance expectations from the PRD

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check feature-manifest.json status and present:

```
✅ WORKFLOW RESUME DETECTED
  ✅ 01-mvp-entrypoint.md - Project initialization (completed)
  🎯 02-gen-prd.md - Product requirements (CURRENT)  
  ⏳ 03-gen-srs.md - Software requirements (pending)
  ⏳ 04-gen-design-decisions-lite.md - Technology decisions (pending)
  ⏳ 05-gen-design.md - Component analysis (pending)
  ⏳ 06-gen-tasks-and-testing.md - Implementation tasks (pending)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📋 Foundation Established:
  • Project: [Project name from discovery]
  • Users: [Primary user group]
  • Access: [User access method]
  • Tech Direction: [Preliminary recommendations]

📍 CONTINUING: PHASE 1 - Foundation (Define WHAT and WHY)
Phase 1 Purpose: Define WHAT we're building (features, scope, goals)

Continue with PRD creation? [Yes/No/Review Documents]
```

---

## Start Here
For day-one and daily loops, follow `dev-utils/dev_workflow/mvp-core-protocol.md` (single source). See `project-entrypoint.md` for step order.