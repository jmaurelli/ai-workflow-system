Developer: # MVP Workflow Quickstart (Human)

## What this is
Concise steps for a lone developer to use the Lean PRD → (optional) Lean SRS → Tasks → Process workflow with a human-in-the-loop.

---

## 1) PRD (Lean) — define the MVP
- Create `/prd/` if missing; choose `feature_slug` (lowercase, kebab-case).
- Fill `gen-prd.md` template (≤ 400 words): Overview, Goals, User Stories, numbered `REQ-*`, Assumptions, Non-Goals, Success Criteria, Risks.
- Save to `/prd/prd-[feature_slug].md`. Validate section order.
- Human review: approve assumptions, non-goals, success criteria, and `REQ-*`.
- Handoff: capture the Context Seed JSON into your notes/agent and update `/artifacts/manifest.json`.

---

## 2) SRS (Lean, optional) — only if NFRs matter now
- Create `/srs/` if missing; use `gen-srs.md` (≤ 1 page).
- Add `NFR-*` with measurable budgets (latency, error rate, availability, security).
- Save `/srs/srs-[feature_slug].md`.
- Human review: approve budgets and constraints.
- Handoff: update Context Seed and `/artifacts/manifest.json`.

Skip this step if NFRs don’t materially impact the MVP phase.

---

## 3) Tasks + Testing — plan the work
- Create `/tasks/` if missing; use `gen-tasks-and-testing.md` (≤ 1 page).
- Generate 3–5 parent tasks; decompose into subtasks. Each parent must include at least one test subtask.
- Add acceptance criteria per parent task, referencing `REQ-*` (and `NFR-*` if SRS exists).
- List Relevant Files (implementation + test stub paths). Ensure test stubs exist or will be created.
- Save `/tasks/tasks-[feature_slug].md`. Add a dated Changelog entry.
- Human review: approve parent tasks, acceptance criteria, traceability, and file list.
- Handoff: update Context Seed and `/artifacts/manifest.json`.

---

## 4) Process Tasks — implement and validate
- Preflight:
  - Detect default branch dynamically; ensure `test/` exists.
  - Select targeted tests by changed paths/tags/filenames.
- Execute tests (centralized rules in `process-tasks.md`):
  - Jest example: `jest --runInBand --watch=false --watchAll=false --json --outputFile=test/<name>.json <files>`
  - Validate results against `dev-utils/test/schema.json` (e.g., `npx ajv validate -s dev-utils/test/schema.json -d "test/*.json" --strict=false`).
- Human review (gated actions):
  - Approve destructive/irreversible actions, merges, and scope changes.
- Commit & trace:
  - Conventional commit messages (e.g., `feat(auth): add login API (refs prd-[feature_slug])`).
  - Update tasks Changelog; keep Relevant Files synced.
- Cleanup:
  - If all pass, delete JSON outputs. Otherwise retain failing JSON for debugging.
- Handoff: update Context Seed and `/artifacts/manifest.json`.

---

## Human-in-the-loop principle
Pause only for destructive/irreversible actions or scope changes. Otherwise proceed autonomously.

---

## Artifacts & locations
- PRD: `/prd/prd-[feature_slug].md`
- SRS (optional): `/srs/srs-[feature_slug].md`
- Tasks: `/tasks/tasks-[feature_slug].md`
- Test results: `test/*.json` (validated by `dev-utils/test/schema.json`)
- Manifest: `/artifacts/manifest.json`
- Templates: `dev-utils/dev_workflow/generate-and-process/project-templates.md`
- Entrypoint: `dev-utils/dev_workflow/project-entrypoint.md`

---

## Context Seed examples
PRD → Tasks:
```json
{ "feature_slug": "user-signup", "prd_path": "/prd/prd-user-signup.md", "requirement_ids": ["REQ-1","REQ-2"] }
```

Tasks → Process:
```json
{ "feature_slug": "user-signup", "tasks_path": "/tasks/tasks-user-signup.md", "test_stub_paths": ["src/auth/__tests__/login.test.ts"] }
```

Process → Next session:
```json
{ "feature_slug": "user-signup", "changed_files": ["src/auth/login.ts"], "last_status": "passed" }
```

