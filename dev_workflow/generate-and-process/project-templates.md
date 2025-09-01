Developer: Provide lightweight (lean) project templates for quick MVP progress, expandable later. Default to lean templates; only use full templates if explicitly requested.

---

## Template Categories (Lean-first)
- Initiation: Lean Project Charter
- Planning: Lean PRD (default), Full PRD (optional)
- Design: Lean Architecture Sketch
- Development: Roadmap + Sprint Checklist
- Testing: Smoke Test Plan (expandable later)
- Deployment: Lean Deployment Notes
- Maintenance: Monitoring Checklist

---

## Lean Project Charter (Markdown)
```markdown
# Project Charter

## Summary
One-paragraph purpose and intended users.

## Goals
- Goal 1
- Goal 2

## Scope
- In scope: [...]
- Out of scope: [...]

## Success Criteria
- [ ] MVP shipped
```

---

## Lean Architecture Sketch (Markdown)
```markdown
# Architecture (Lean)

## Core Components
- [ ] Backend — key modules
- [ ] Frontend — key views
- [ ] Database — key entities

## Interfaces/Contracts (links or bullets)
- [API/Module] — description or link

## Notes
Keep to diagrams or bullet points only.
```

---

## Lean Smoke Test Plan (Markdown)
```markdown
# Smoke Test Plan

## Core Checks
- [ ] App starts
- [ ] User can log in
- [ ] Core feature runs

## Notes
Expand to unit/integration later if needed.
```

---

## Integration Notes
- Use these templates to jumpstart content for PRD (`gen-prd.md`), optional SRS (`gen-srs.md`), and tasks (`gen-tasks-and-testing.md`).
- Keep each template to ≤ 1 page.
- Link artifacts in `/artifacts/manifest.json` via their paths.

### Project Documentation Directory (Lean)
- Standardize high-level docs under `/docs/`:
  - `/docs/architecture.md` — Architecture Sketch (lean template above)
  - `/docs/adr/` — Architecture Decision Records (short, dated notes)
  - `/docs/testing.md` — Smoke Test Plan (lean template above)
  - `/docs/operations.md` — Deployment and monitoring notes (lean)
  - `/docs/charter.md` — Project Charter (lean template above)
- Naming: lowercase, kebab-case filenames. Keep each file ≤ 1 page for MVP.
- Cross-link: reference PRD, SRS, and Tasks paths at the top of each doc.

Format outputs as Markdown per each fenced template above.

---

## Start Here
For day-one and daily loops, see `dev-utils/dev_workflow/project-entrypoint.md`.