Developer: # Start Here — Project Entrypoint (AI‑First, Lone Dev)

## Day 1: Initialize project context
1. Choose `feature_slug` (lowercase, kebab-case). Update `/artifacts/manifest.json`.
2. Create today’s Q&A file from `/qa/qa-loop-template.md` → `/qa/qa-[feature_slug]-[YYYYMMDD]-r1.md`. Record in manifest, including `qa_path`.
3. Seed high-level docs using templates:
   - Charter → `/docs/charter.md`
   - Architecture → `/docs/architecture.md`
   - Testing (smoke) → `/docs/testing.md`
   Use `project-templates.md` fenced blocks. Keep each ≤ 1 page.
4. Next Action (Agent): Generate Lean PRD from Charter/Architecture. Centralize any clarifying questions in the QA file only; PRD must not contain its own Open Questions section.
 5. Architecture Seeding Q&A (MVP-light):
    - In the QA doc, complete the "Architecture Seeding Q&A" section.
    - Seed `/docs/architecture.md` and minimal ADRs under `/docs/adr/` from the Decision Statements.
    - Link the architecture doc in PRD Linkages.

## Stage order and handoffs
1. PRD → `/prd/prd-[feature_slug].md` (gen-prd.md)
   - Include `REQ-*`, assumptions, non-goals, success criteria.
   - Link Charter/Architecture/Testing and current QA file.
   - Handoff: paste PRD Context Seed in Q&A; include `qa_path`; update manifest.
2. SRS (optional) → `/srs/srs-[feature_slug].md` (gen-srs.md)
   - Add `NFR-*` budgets only if needed now.
   - Handoff: paste SRS Context Seed; include `qa_path`; update manifest.
3. Tasks → `/tasks/tasks-[feature_slug].md` (gen-tasks-and-testing.md)
   - 3–5 parent tasks; subtasks with at least one test subtask each.
   - Acceptance criteria reference `REQ-*` and `NFR-*`.
   - Handoff: paste Tasks Context Seed; include `qa_path`; update manifest.
4. Process (implement) → (process-tasks.md)
   - Detect default branch; run targeted tests non-interactively; validate JSON.
   - Commit with conventional messages referencing PRD/Tasks; update Tasks changelog.
   - Handoff: paste Status Context Seed; include `qa_path`; update manifest.

## Daily loop
1. Open latest Q&A; answer remaining “Unanswered”.
2. Pick the next parent task; follow TDD-Lite (write failing smoke test → minimal implementation → refactor); run targeted tests; validate JSON.
3. Commit; update Tasks changelog; mark Qs as “Incorporated”.
4. Update manifest (ensure `qa_path` remains accurate) and append Status Context Seed to Q&A.

## Weekly loop
1. Review drift: Charter/Architecture → PRD `REQ-*` → Tasks acceptance criteria.
2. Rotate Q&A round to `rN+1`; carry unresolved Qs forward.

## Links
- Quickstart: `dev-utils/dev_workflow/generate-and-process/mvp-workflow-quickstart.md`
- Templates: `dev-utils/dev_workflow/generate-and-process/project-templates.md`
- PRD: `dev-utils/dev_workflow/generate-and-process/gen-prd.md`
- SRS: `dev-utils/dev_workflow/generate-and-process/gen-srs.md`
- Tasks: `dev-utils/dev_workflow/generate-and-process/gen-tasks-and-testing.md`
- Process: `dev-utils/dev_workflow/generate-and-process/process-tasks.md`
 - QA Loop Template: `dev-utils/dev_workflow/generate-and-process/qa-loop-template.md`

## Human-in-the-loop principle
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

