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

---

## Enhanced PRD Template (Design-Aware)
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
1. [REQ-1] Requirement 1
2. [REQ-2] Requirement 2

## Design Context (Mandatory - Enhanced for Scaling)
- **Existing Components**: [comprehensive component analysis required]
- **Design System Integration**: [alignment with established design system]
- **Component Library Impact**: [new components needed vs reuse opportunities]
- **Cross-Platform Considerations**: [mobile, desktop, accessibility requirements]
- **Performance Requirements**: [component performance and bundle impact]

## Non-Functional Requirements
- **Performance**: [specific metrics and targets]
- **Scalability**: [user load and data volume requirements]
- **Accessibility**: [WCAG compliance level and requirements]
- **Security**: [security requirements and compliance]

## Dependencies
- **Technical Dependencies**: [services, libraries, APIs]
- **Design Dependencies**: [design system components, tokens, patterns]
- **Team Dependencies**: [other teams or external stakeholders]

## Risks & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Design System Breaking Changes | Medium | High | Version pinning and migration plan |
| Component Performance Issues | Low | Medium | Performance testing and monitoring |
| Accessibility Compliance Gaps | Medium | High | Automated testing and expert review |

## Success Criteria
- **Business Metrics**: [specific business impact targets]
- **Technical Metrics**: [performance, quality, reliability targets]
- **User Experience Metrics**: [usability and satisfaction targets]
- **Design System Metrics**: [consistency and reuse targets]

## Open Questions
- List any unresolved issues.  

## Changelog
- [YYYY-MM-DD] v1.0 Initial PRD created.
```

---

## AI Agent Directives
- Always generate **Full PRDs** in scaling mode with enhanced design context
- Require comprehensive design system analysis and component impact assessment
- Confirm assumptions explicitly with stakeholders and design system team
- Validate design context against existing design system and component library
- Ensure NFRs include performance, accessibility, and scalability requirements
- Save file with timestamp and version in `/prd/prd-[feature-name]-scaling.md`
- Reference and build upon any existing MVP PRD artifacts
Set reasoning_effort = high; scaling PRDs require comprehensive analysis

---

## Human Review Gate (Required)
- Confirm: comprehensive design context and component analysis complete
- Confirm: design system integration strategy validated
- Confirm: NFRs include all scaling requirements (performance, accessibility, security)
- Confirm: risk assessment includes design and technical considerations
- Confirm: success criteria include design system and user experience metrics
- Approve proceeding to design analysis phase

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "prd_scaling",
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name]-scaling.md",
  "requirement_ids": ["REQ-1", "REQ-2"],
  "design_context": {
    "component_analysis_required": true,
    "design_system_integration": true,
    "cross_platform_considerations": true,
    "performance_requirements": true
  },
  "nfr_requirements": {
    "performance_targets": "...",
    "accessibility_level": "WCAG 2.1 AA",
    "scalability_requirements": "..."
  },
  "success_criteria": ["..."],
  "risk_factors": ["..."]
}
```

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name]-scaling.md",
  "requirement_ids": ["REQ-1", "REQ-2"],
  "design_system_integration_required": true,
  "scaling_context": true
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.  
