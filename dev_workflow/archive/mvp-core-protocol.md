Developer: # MVP Core Protocol (Single Source of Truth)

## Purpose
Use this minimal protocol for all MVP agentic flows. Ignore other workflow docs unless explicitly linked from here.

## Guardrails
- Prompt for `feature_slug` (lowercase, kebab-case) and BLOCK until provided. Do not infer or auto-generate.
- Default: no containers, no external services, no hidden assumptions. Only use if the human opts in.
- Keep docs ≤ 1 page each.
- Enforce TDD‑Lite: write failing smoke test → minimal implementation → refactor.
- Tests must output JSON to `test/` and validate against `dev-utils/test/schema.json`.

## Minimal Flow
1. Seed docs (lean): `/docs/charter.md`, `/docs/architecture.md`, `/docs/testing.md` from `generate-and-process/project-templates.md`.
2. Ask for `feature_slug`; record in `/artifacts/manifest.json`.
3. Generate PRD: `/prd/prd-[feature_slug].md` using `gen-prd.md` (≤ 400 words; Overview, Goals, User Stories, `REQ-*`, Assumptions, Non‑Goals, Success Criteria, Risks). Link Architecture.
4. (Optional) SRS: `/srs/srs-[feature_slug].md` only if NFRs materially affect MVP now. Define `NFR-*` budgets.
5. Tasks + Testing: `/tasks/tasks-[feature_slug].md` per `gen-tasks-and-testing.md` (3–5 parents, at least one test subtask per parent, acceptance criteria reference `REQ-*`/`NFR-*`). Create test stubs.
6. Process: run targeted tests non-interactively; write JSON to `test/`; validate; delete JSON only when all pass. Conventional commits reference `prd-[feature_slug]`. Update tasks changelog and manifest.

## Inputs → Outputs (at a glance)
- Inputs: Charter, Architecture decisions, `feature_slug`.
- Outputs: PRD (`REQ-*`), optional SRS (`NFR-*`), Tasks (acceptance criteria + test stubs), JSON test results.

## Stop/Review Gates
- Human review before tasks: approve PRD assumptions, non-goals, success criteria, and `REQ-*`.
- Human review for destructive/irreversible actions and scope changes.

## Notes
- Prefer simple defaults. Only introduce complexity (containers, integrations, services) when explicitly requested.

