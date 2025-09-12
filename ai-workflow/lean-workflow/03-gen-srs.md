Developer: # Workflow: Lean Software Requirements Specification (SRS) (MVP-First)

**🚨 CRITICAL LOCATION REQUIREMENT:**
**You MUST be in the feature directory: `/features/YYYY-MM-DD-project-name/`**
**Save the SRS as `./srs.md` in the feature directory - NOT in project root!**

## Objective
Capture only the minimum non-functional requirements (NFRs), constraints, and budgets needed to guide MVP implementation. Keep it one page, fast to produce, and tightly coupled to the PRD.

### **⚡ TECHNICAL SPECIFICITY REQUIREMENTS**
**AI Instructions**: While maintaining strategic flexibility, eliminate unnecessary generic language:

- **Performance requirements** → Include measurable thresholds (not "fast" but "< 200ms p95 latency")
- **Reliability targets** → Specify uptime percentages and error rates (not "reliable" but "99.5% uptime")
- **Security requirements** → Reference specific standards/frameworks when applicable
- **Quality criteria** → Make requirements testable and verifiable
- **PRESERVE artistic flexibility** for user experience goals and strategic business requirements

---

## Quickstart (Lean SRS - Feature-Centric)

**CRITICAL: Always work within the feature directory created by 01-mvp-entrypoint.md**

- **Working Directory**: You should already be in `/features/YYYY-MM-DD-project-name/` from the previous step
- **Read PRD**: Load context from `./prd.md` (current feature directory)
- **Save Location**: `./srs.md` (current feature directory)
- **Required**: Update `./feature-manifest.json` with SRS completion status
- Capture 8–10 critical NFRs with measurable budgets
- Focus on performance, reliability, security, and constraints

---

## Workflow (Lean-First - Feature-Centric)

**PREREQUISITE**: You must be working in the feature directory from 01-mvp-entrypoint.md

1. **Verify working directory**: Confirm you're in `/features/YYYY-MM-DD-project-name/` with existing `feature-manifest.json` and `prd.md`
2. **Read PRD context**: Review `./prd.md` to understand functional requirements and scope
3. **Identify NFRs**: List critical constraints and NFRs that affect design/implementation and testing
4. **Define Budgets**: Set measurable budgets (e.g., p50/p95 latency, error rates, uptime)
5. **Prioritize**: Keep to ≤ 1 page; prioritize only what must be enforced during MVP
6. **Save as `./srs.md`**: Save in current feature directory (NOT project root)
7. **Update feature manifest**: Mark SRS as completed in `./feature-manifest.json`

---

## Lean SRS Template
```markdown
# SRS - [Feature Name]

## Scope Summary
One short paragraph describing scope and boundaries. Reference PRD; do not restate.

## System Context (concise)
- Actors: [primary]
- External systems: [key integrations]

## NFRs (numbered `NFR-*` with budgets)
1. [NFR-1] Performance: p50 < 300ms, p95 < 800ms for [operation]
2. [NFR-2] Availability: 99.5% during business hours
3. [NFR-3] Security/Privacy: [requirement]
4. [NFR-4] Reliability/Errors: error_rate < 1%

## Constraints & Assumptions
- [Constraint or assumption]

## Data & Interface Contracts (critical only)
- [Interface] → [contract/link]

## Risks & Mitigations (top 3)
- [Risk] → [Mitigation]

## Traceability
- PRD Requirements: REQ-1 → NFR-1, NFR-3; REQ-2 → NFR-2

## Linkages
- PRD: ./prd.md (feature-centric) OR /prd/prd-[feature_slug].md (legacy)
- Tasks: ./tasks.md (feature-centric) OR /tasks/tasks-[feature_slug].md (legacy)
```

---

## AI Agent Directives
- Keep to one page; avoid duplication of PRD content.
- Use IDs `NFR-*` and measurable budgets to enable testing.
- Ensure `/srs/` exists; save as `/srs/srs-[feature_slug].md`.
- Validate section presence and order before completion.
Set reasoning_effort = minimal; keep outputs concise and focused.

 

---

## Human Review Gate (Required)
- Approve NFR budgets (performance, reliability, security/privacy).
- Approve constraints that would impact design/testing.

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "srs",
  "feature_slug": "[feature_slug]",
  "srs_path": "/srs/srs-[feature_slug].md",
  "nfr_ids": ["NFR-1", "NFR-2"],
  "budgets": {"latency_p50_ms": 300, "latency_p95_ms": 800}
}
```

### Artifact Manifest Update
- Append or create `/artifacts/manifest.json` with `srs_path`, `nfr_ids`, and `budgets`.

 

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature_slug]",
  "srs_path": "/srs/srs-[feature_slug].md",
  "nfr_ids": ["NFR-1", "NFR-2"]
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the SRS creation, provide a summary including:
- **SRS Generated**: `./srs.md` in feature directory
- **NFRs Defined**: [Number of non-functional requirements captured]
- **Performance Budgets**: [Key performance metrics established]
- **Security Requirements**: [Security baseline requirements defined]
- **Quality Gates**: [Testing and validation criteria established]
- **Manifest Updated**: feature-manifest.json marked SRS as completed
- **Completion Time**: [AI: Insert current date and time in format: $(date '+%Y-%m-%d %H:%M:%S')]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 04-gen-design-decisions-lite.md to make technology decisions"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the SRS?"

### Next Step Preview
**Next**: 04-gen-design-decisions-lite.md - Technology Stack Selection
**Phase 2 Purpose**: Decide HOW to build (technology choices, UX approach)
**What Design Decisions needs from this step**: Performance budgets, security constraints, and quality requirements from the SRS

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check feature-manifest.json status and present:

```
✅ WORKFLOW RESUME DETECTED
  ✅ 01-mvp-entrypoint.md - Project initialization (completed)
  ✅ 02-gen-prd.md - Product requirements (completed)
  🎯 03-gen-srs.md - Software requirements (CURRENT)
  ⏳ 04-gen-design-decisions-lite.md - Technology decisions (pending)
  ⏳ 05-gen-design.md - Component analysis (pending)
  ⏳ 06-gen-tasks-and-testing.md - Implementation tasks (pending)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📋 Foundation Established:
  • Project: [Project name from discovery]
  • Requirements: [Number of functional requirements from PRD]
  • User Stories: [User story count from PRD]
  • Success Criteria: [Key outcomes from PRD]

📍 COMPLETING: PHASE 1 - Foundation (Define WHAT and WHY)
Phase 1 Purpose: Define quality requirements (NFRs, performance, security)

Continue with SRS creation? [Yes/No/Review Documents]
```

---


