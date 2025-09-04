Developer: # Workflow: Tasks + Testing (MVP-First)

## Objective
Transform a Lean PRD into actionable tasks with integrated testing guidance. This process combines task generation and lightweight TDD into a streamlined approach suitable for solo MVP development.


## Workflow Steps

Begin with a concise checklist (3-7 bullets) of intended sub-tasks before proceeding; keep checklist items conceptual.

### 1. Input
- Begin with a Lean PRD saved at `/prd/prd-[feature-name].md`.
- If present, read Lean SRS at `/srs/srs-[feature-name].md` and incorporate NFR budgets into acceptance criteria (reference `NFR-*`).
- **NFR Integration**: Use NFR budgets to define performance, reliability, and security acceptance criteria for tasks.
- **Constraint Awareness**: Incorporate SRS constraints into task dependencies and risk mitigation.
- Ensure the PRD contains: overview, goals, user stories, and requirements.
- If any elements are missing, clearly state what is absent at the top of the output, and skip steps that cannot be performed as a result.
- Read `/docs/architecture.md` if present; otherwise, capture minimal architecture decisions inline and note any deltas or open items.

### 2. Generate Parent Tasks
- Identify 3–5 parent tasks derived from the PRD.
- If fewer than 3 or more than 5 parent tasks are available, proceed with what is supported, and clearly document this under **Notes** in the output.
- Parent tasks should be clear and high-level, for example: “Implement login API.”

### 3. Expand into Sub-Tasks
- For each parent task, break it down into smaller sub-tasks (ideally actions that take less than one day) using Markdown checklists (`- [ ]`).
- Ensure that each parent task includes at least one sub-task related to testing.
- The first sub-task under each parent MUST be: "Write failing smoke test (targeting acceptance criteria)".
- Add explicit acceptance criteria for each parent task, tied to PRD requirements.

**Example:**
- Parent: Implement login API
  - [ ] Define request/response schema
  - [ ] Write failing smoke test (valid + invalid login)
  - [ ] Implement minimal code to pass the test
  - [ ] Add error handling for bad input
  - [ ] Validate acceptance criteria (Req 2.1, 2.2)

### 4. Relevant Files
- List the files associated with each parent task in a dedicated **Relevant Files** section as a Markdown list.
- Always specify both implementation and related test files.
- Use a standard layout when applicable:
  - Implementation: `src/[area]/[name].ts`
  - Tests: `src/[area]/__tests__/[name].test.ts`
- Generate at least one test stub file per parent task (empty is acceptable) and include it.

### 5. Changelog
- Maintain a **Changelog** at the very top of the task file in Markdown format.
- Record each change as a new bullet point, starting with `[YYYY-MM-DD]`.
 - Reference test validation per `process-tasks.md` and `dev-utils/test/schema.json`.

---

## Testing Guidelines (MVP-First)

### MVP Mode
- Write only smoke tests for key flows:
  - App startup
  - User login
  - Main feature operation
- Place test stubs alongside code, even if mostly empty.
- Execute tests per `process-tasks.md` (centralized commands, JSON schema, and cleanup rules). For Jest, use `--watch=false --watchAll=false`.

### TDD-Lite Mandate (MVP)
- Follow a lightweight RED → GREEN → REFACTOR cycle for every parent task:
  - RED: Write a failing smoke test for the acceptance criteria first.
  - GREEN: Implement the minimal code needed to pass the test.
  - REFACTOR: Clean up names, remove duplication, and simplify logic.
- Do not add implementation code before authoring the failing smoke test.

### Enhancement Mode (Later)
- Gradually add more tests:
  - Expand smoke tests to unit tests, then integration tests.
  - Update tasks to include design-driven TDD approaches.
  - Ensure all test results conform to the schema in `test-suite.md`.

---

## AI Agent Instructions
- Always generate both the task list and test stubs together.
- For MVP, restrict tests to smoke tests only.
- Save task files in `/tasks/tasks-[feature-name].md`, using the lowercase, kebab-case slug.
- Output should fit on a single page for MVP; expand only if Enhancement Mode is explicitly requested.
- If instructions cannot be followed due to missing PRD data, provide a clear note in the output and indicate incomplete or omitted sections as appropriate.

 

Set reasoning_effort = medium due to moderate task complexity; produce tool and code outputs succinctly, but offer fuller detail in the final Markdown document.

After generating the Markdown task file, validate that all required sections (Changelog, Relevant Files, Notes if needed, Tasks) are present and in the correct order, that every parent task contains at least one test-related sub-task, that each parent task has acceptance criteria, and that listed test stub files exist or are scheduled to be created.

After generating the Markdown task file, validate that all required sections (Changelog, Relevant Files, Notes if needed, Tasks) are present and in the correct order, and that every parent task contains at least one test-related sub-task. If any step is incomplete due to missing PRD data, clearly indicate this in both the Notes and Tasks sections.

---

## Output Format

Output should be a single Markdown document saved as `/tasks/tasks-[prd-name].md` and conform to the following structure:

```markdown
# Tasks for [PRD Name]

## Changelog
- [YYYY-MM-DD] Initial tasks created.
- [YYYY-MM-DD] [Description of subsequent changes]

## Relevant Files
- path/to/file1.ext – description
- path/to/file2.ext – description

## Notes
- [Freeform notes, including process deviations: e.g., "Only 2 parent tasks inferred due to limited PRD input." "User stories section missing from PRD; requirements inferred from goals."]

## Tasks
- [ ] 1.0 [Parent Task 1]
  - [ ] 1.1 [Subtask 1]
  - [ ] 1.2 [Subtask 2]
  ...
- [ ] 2.0 [Parent Task 2]
  ...

### Acceptance Criteria
- [Criteria for Parent Task 1] (reference PRD requirement IDs)
- [Criteria for Parent Task 2]

## Task Dependencies

### Critical Path
1. **Task X.Y** → **Task X.Z** → **Task A.B** (describe dependency chain)
2. **Task X.Y** → **Task A.B** (cross-task dependencies)

### Parallel Tasks
- **Week X**: Tasks that can run simultaneously
- **Week Y**: Additional parallel execution opportunities

## Risk Mitigation

### High-Risk Tasks
- **Task X.Y** (Description): Risk factors and mitigation approach
- **Task A.B** (Description): Risk factors and mitigation approach

### Contingency Plans
- **Risk scenario**: Specific fallback approach
- **Risk scenario**: Alternative implementation strategy

## Success Criteria

### MVP Completion
- [ ] [Specific measurable outcome]
- [ ] [Performance requirement]
- [ ] [User experience requirement]
- [ ] [Technical requirement]

### Quality Gates
- **Week X**: ✅ [Milestone description]
- **Week Y**: ✅ [Milestone description]
- **Week Z**: ✅ [Milestone description]
```

- All sections must appear in this order: Changelog, Relevant Files, Notes (optional if not needed), Tasks, Task Dependencies, Risk Mitigation, Success Criteria.
- Every parent task must include at least one test-related sub-task.
- Tasks and sub-tasks must use `- [ ]` Markdown checklists.
- The **Relevant Files** section must always list both implementation and test/validation files for each task.
- If any PRD elements are missing, identify them explicitly in **Notes** and indicate in **Tasks** which steps were omitted as a result.
- If fewer than 3 or more than 5 parent tasks are applicable, include a mandatory Scope Note in **Notes** explaining why.

---

## Human Review Gate (Required)
- Confirm: parent tasks (3–5), acceptance criteria per parent, and at least one test sub-task per parent.
- Confirm: Relevant Files include both implementation and test stubs following conventions.
- Confirm: traceability—acceptance criteria reference PRD `REQ-*` IDs.
- Confirm: TDD-Lite sequence per parent task (failing smoke test → minimal implementation → refactor) was followed.
- Confirm: Task Dependencies identify critical path and parallel execution opportunities.
- Confirm: Risk Mitigation addresses high-risk tasks with contingency plans.
- Confirm: Success Criteria include measurable outcomes and quality gates.
- Approve proceeding to task processing.

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "tasks",
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name].md",
  "srs_path": "/srs/srs-[feature-name].md",
  "parent_tasks": ["..."],
  "acceptance_criteria_by_task": {"1.0": ["..."], "2.0": ["..."]},
  "relevant_files_by_task": {"1.0": ["src/..."], "2.0": ["src/..."]},
  "test_stub_paths": ["src/.../__tests__/...test.ts"],
  "traceability_map": {"REQ-1": ["1.0"], "REQ-2": ["2.0"]},
  "nfr_traceability": {"NFR-1": ["1.0", "3.4"], "NFR-2": ["2.0"]},
  "nfr_budgets": {"latency_p50_ms": 300, "latency_p95_ms": 800, "error_rate": 0.01}
}
```

### Artifact Manifest Update
- Append or create `/artifacts/manifest.json` with the same keys, plus timestamp.

 

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "tasks_path": "/tasks/tasks-[feature-name].md",
  "test_stub_paths": ["src/.../__tests__/...test.ts"]
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.

---

## Start Here
For day-one and daily loops, follow `dev-utils/dev_workflow/mvp-core-protocol.md` (single source). See `project-entrypoint.md` for step order.
