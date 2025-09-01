# Workflow: Product Requirements Document (PRD) Creation (Scaling)

## Objective
Create a **Full PRD** with complete detail, ensuring clarity, traceability, and quality.  
Even for solo dev, this ensures documentation survives time gaps and supports future scaling.

---

## Workflow
1. Capture idea with business and technical context.  
2. Ask thorough clarifying questions (who, what, why, how).  
3. Fill out the **Full PRD template**.  
4. Save to `/prd/` with versioning.  

---

## Full PRD Template
```markdown
# Product Requirements Document - [Feature Name]

## Executive Summary
- High-level overview of the feature, business need, expected impact.

## Goals
- [Goal 1]
- [Goal 2]

## Non-Goals
- [Out of scope functionality]

## User Personas
- **Primary User**: role, goals, pain points.  
- **Secondary User**: role, goals, pain points.

## User Stories
- As a [user], I want [action] so that [benefit].

## Functional Requirements
1. Requirement 1
2. Requirement 2

## Non-Functional Requirements
- Performance, scalability, accessibility.

## Dependencies
- Services, libraries, APIs.

## Risks & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|

## Success Criteria
- Metric 1: Target  
- Metric 2: Target  

## Open Questions
- List any unresolved issues.  

## Changelog
- [YYYY-MM-DD] v1.0 Initial PRD created.
```

---

## AI Agent Instructions
- Always generate **Full PRDs** in scaling mode.  
- Confirm assumptions explicitly.  
- Save file with timestamp and version in `/prd/`.  
