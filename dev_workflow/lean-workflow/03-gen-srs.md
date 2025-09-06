Developer: # Workflow: Lean Software Requirements Specification (SRS) (MVP-First)

## Objective
Capture only the minimum non-functional requirements (NFRs), constraints, and budgets needed to guide MVP implementation. Keep it one page, fast to produce, and tightly coupled to the PRD.

---

## Quickstart (Lean SRS - Feature-Centric)
- **Auto-detect structure**: Check if working in feature directory or legacy structure
- **Feature-centric**: Read PRD at `./prd.md` and save as `./srs.md`
- **Legacy**: Read PRD at `/prd/prd-[feature_slug].md` and save as `/srs/srs-[feature_slug].md`
- Capture 8–10 critical NFRs with measurable budgets
- Focus on performance, reliability, security, and constraints
- Update `./feature-manifest.json` with SRS completion status (if feature-centric)

---

## Workflow (Lean-First - Feature-Centric)
1. **Auto-detect structure & Read PRD**: 
   - **Feature-centric**: Review `./prd.md` to understand functional requirements
   - **Legacy**: Review `/prd/prd-[feature_slug].md` to understand functional requirements
2. **Identify NFRs**: List critical constraints and NFRs that affect design/implementation and testing
3. **Define Budgets**: Set measurable budgets (e.g., p50/p95 latency, error rates, uptime)
4. **Prioritize**: Keep to ≤ 1 page; prioritize only what must be enforced during MVP
5. **Save & Validate**: 
   - **Feature-centric**: Save to `./srs.md` and update `./feature-manifest.json`
   - **Legacy**: Save to `/srs/srs-[feature_slug].md` and validate section order

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


