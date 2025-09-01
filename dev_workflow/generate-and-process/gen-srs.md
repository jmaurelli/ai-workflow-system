Developer: # Workflow: Lean Software Requirements Specification (SRS) (MVP-First)

## Objective
Capture only the minimum non-functional requirements (NFRs), constraints, and budgets needed to guide MVP implementation. Keep it one page, fast to produce, and tightly coupled to the PRD.

---

## Quickstart (Lean SRS)
- Ensure the `/srs/` directory exists; create it if missing.
- Use the same `feature_slug` (lowercase, kebab-case) as the PRD.
- Capture at most 8–10 NFRs with measurable budgets; avoid duplication of PRD content.
- Save as `/srs/srs-[feature_slug].md`.

---

## Workflow (Lean-First)
1. Read the PRD at `/prd/prd-[feature_slug].md`.
2. List critical constraints and NFRs that affect design/implementation and testing.
3. Define measurable budgets (e.g., p50/p95 latency, error rates, uptime).
4. Keep to ≤ 1 page; prioritize only what must be enforced during MVP.
5. Save to `/srs/srs-[feature_slug].md` and validate section order.

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
- PRD: /prd/prd-[feature_slug].md
- Tasks: /tasks/tasks-[feature_slug].md
```

---

## AI Agent Directives
- Keep to one page; avoid duplication of PRD content.
- Use IDs `NFR-*` and measurable budgets to enable testing.
- Ensure `/srs/` exists; save as `/srs/srs-[feature_slug].md`.
- Validate section presence and order before completion.
Set reasoning_effort = minimal; keep outputs concise and focused.

### Q&A Loop Integration (Centralized)
- Use `/qa/qa-[feature_slug]-[YYYYMMDD]-rN.md` as the single source of truth for questions.
- Record clarifications as `Q-srs-*` only in the QA document and update status to "Incorporated" after editing the SRS.

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
  "budgets": {"latency_p50_ms": 300, "latency_p95_ms": 800},
  "qa_path": "/qa/qa-[feature_slug]-[YYYYMMDD]-rN.md"
}
```

### Artifact Manifest Update
- Append or create `/artifacts/manifest.json` with `srs_path`, `nfr_ids`, and `budgets`.

### Q&A Loop Integration
- If clarification is needed, create or update `/qa/qa-[feature_slug]-[YYYYMMDD]-rN.md`.
- Record questions with IDs `Q-srs-*`. Change Status to "Incorporated" after updating the SRS.

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

## Start Here
For day-one and daily loops, follow `dev-utils/dev_workflow/mvp-core-protocol.md` (single source). See `project-entrypoint.md` for step order.

