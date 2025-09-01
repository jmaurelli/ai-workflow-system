Developer: # Q&A Loop Template (Human-in-the-loop)

## Naming & Location
- Directory: `/qa/`
- Filename: `qa-[feature_slug]-[YYYYMMDD]-rN.md`

## Manifest Update
- On creation, append to `/artifacts/manifest.json` (create if missing) with at least:
  - `feature_slug`
  - `qa_path`: `/qa/qa-[feature_slug]-[YYYYMMDD]-rN.md`
  - `timestamp`

---

# Q&A Loop — [feature_slug] — [YYYY-MM-DD] — Round N

## Meta
- Feature: [feature_slug]
- Stage: prd | srs | tasks | process
- PRD: /prd/prd-[feature_slug].md
- SRS (opt): /srs/srs-[feature_slug].md
- Tasks: /tasks/tasks-[feature_slug].md

## Questions
- [Q-prd-1] Question:
  - Context: [short context or link]
  - Answer: [your answer here]
  - Status: Unanswered | Answered | Incorporated

## Decisions/Approvals
- [D-1] Decision: [what was decided] (refs: Q-prd-1)

## Actions/Follow-ups
- [A-1] Action: [what to do next]

