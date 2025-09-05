Developer: # Workflow: Product Requirements Document (PRD) Creation (MVP-First)

## Objective
Efficiently capture an idea and transform it into a **Lean PRD** focused on MVP development. The PRD should be lightweight, actionable, and quick to produce, with the flexibility to be expanded into a Full PRD if needed.

---

## Quickstart (Lean PRD)
- Ensure the `/prd/` directory exists; create it if missing.
- Define a slug for `[feature-name]` using lowercase kebab-case (e.g., "User Signup" → `user-signup`).
- Capture the feature in 1–2 sentences.
- Ask only critical clarifying questions (problem, user, success).
- Complete the Lean PRD template below (≤ 400 words total).
- Save as `/prd/prd-[feature-name].md` and validate section order and presence.

---

## Workflow (Lean-First)
Begin with a concise checklist (3-7 bullets) of what you will do; keep items conceptual, not implementation-level.
1. Ensure `/prd/` exists and define the `[feature-name]` slug (lowercase, kebab-case).
2. Capture the feature or idea succinctly in 1–2 sentences.
3. Ask only the most **critical clarifying questions** (e.g., What problem does this solve? Who is the user? What defines success?).
4. Complete the **Lean PRD template** provided below (≤ 400 words).
5. Save the PRD as `/prd/prd-[feature-name].md`.
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

## AI Agent Directives
- Default to creating a **Lean PRD** unless otherwise instructed.
- Use a lowercase, kebab-case slug for `[feature-name]` consistently across PRD, tasks, and tests.
- Prompt the human explicitly for `[feature-name]` as `feature_slug` and BLOCK until provided. Do NOT auto-generate, infer, or randomize the slug.
- Validate `feature_slug` format (lowercase kebab-case). If invalid, show the format and re-prompt.
- Ensure the `/prd/` directory exists; create it if missing.
- Save files as `/prd/prd-[feature-name].md`.
- Limit Lean PRDs to one page and ≤ 400 words.
- Validate that the file exists, is accessible, and that all template sections appear in the specified order. If validation fails, self-correct before completion.
- Include the optional Linkages section if the related tasks file exists.
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

## Start Here
For day-one and daily loops, follow `dev-utils/dev_workflow/mvp-core-protocol.md` (single source). See `project-entrypoint.md` for step order.