Developer: # Start Here — Project Entrypoint (AI‑First, Lone Dev)

## Day 1: Initialize project context
0. Read this first: Use `dev-utils/dev_workflow/mvp-core-protocol.md` as the single source for MVP. Ignore other workflow docs unless explicitly linked.
1. Initialize with Lean project templates:
   - Seed `/docs/charter.md`, `/docs/architecture.md`, `/docs/testing.md` using `dev-utils/dev_workflow/generate-and-process/project-templates.md` fenced blocks (≤ 1 page each).
   - Create `/artifacts/manifest.json` if missing; record the seeded doc paths.
2. PROMPT for `feature_slug` (lowercase, kebab-case) and BLOCK until provided; record it in `/artifacts/manifest.json`. Do not infer or auto-generate.
3. Architecture Seeding (MVP-light):
   - Capture decisions directly in `/docs/architecture.md` using the lean template.
   - Create minimal ADRs under `/docs/adr/` for pivotal choices.
   - Link the architecture doc in PRD Linkages.
4. Next Action (Agent): Generate Lean PRD from Charter/Architecture.

## Stage order and handoffs
1. PRD → `/prd/prd-[feature_slug].md` (gen-prd.md)
   - Include `REQ-*`, assumptions, non-goals, success criteria.
   - Link Charter/Architecture/Testing.
   - Handoff: update manifest with PRD path and requirement IDs.
2. SRS (optional) → `/srs/srs-[feature_slug].md` (gen-srs.md)
   - Add `NFR-*` budgets only if needed now.
   - Handoff: update manifest with SRS path, NFR IDs, and budgets.
3. Tasks → `/tasks/tasks-[feature_slug].md` (gen-tasks-and-testing.md)
   - 3–5 parent tasks; subtasks with at least one test subtask each.
   - Acceptance criteria reference `REQ-*` and `NFR-*`.
   - Handoff: update manifest with tasks path and test stub paths.
4. Process (implement) → (process-tasks.md)
   - Detect default branch; run targeted tests non-interactively; validate JSON.
   - Commit with conventional messages referencing PRD/Tasks; update Tasks changelog.
   - Handoff: update manifest with status summary and JSON result paths.

## Daily loop
1. Pick the next parent task; follow TDD-Lite (write failing smoke test → minimal implementation → refactor); run targeted tests; validate JSON.
2. Commit; update Tasks changelog.
3. Update manifest (status and paths).

## Weekly loop
1. Review drift: Charter/Architecture → PRD `REQ-*` → Tasks acceptance criteria.
2. Review architecture/ADR drift; log deltas succinctly in `/docs/architecture.md`.

## Links
- Quickstart: `dev-utils/dev_workflow/generate-and-process/mvp-workflow-quickstart.md`
- Templates: `dev-utils/dev_workflow/generate-and-process/project-templates.md`
- PRD: `dev-utils/dev_workflow/generate-and-process/gen-prd.md`
- SRS: `dev-utils/dev_workflow/generate-and-process/gen-srs.md`
- Tasks: `dev-utils/dev_workflow/generate-and-process/gen-tasks-and-testing.md`
- Process: `dev-utils/dev_workflow/generate-and-process/process-tasks.md`


## Human-in-the-loop principle
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

