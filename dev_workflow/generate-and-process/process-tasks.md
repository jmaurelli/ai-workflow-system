Developer: # 🔹 Consolidated Hierarchical Instructions for LLM Priming

This document integrates **Task List Management**, **Test-Driven Development (TDD) with Design**, and **Test Suite Standards** into a unified, hierarchical structure optimized for language model execution and priming.

---

## 0. Meta Protocol (Global)

- **Hierarchical Procedure:**
  1. **Plan:** Begin each task with a short conceptual checklist (3–7 bullet points).
  2. **Act:** Address one sub-task at a time in order.
  3. **Validate:** After each step, provide a 1–2 sentence confirmation or self-correction.
  4. **Pause:** Await explicit user approval before proceeding further for destructive or irreversible actions; otherwise proceed autonomously.
- Always follow validation and checkpoint requirements precisely.
- Keep reasoning summaries concise and limit verbosity to what is strictly required.
- Before any significant tool invocation, briefly state the purpose and the minimal inputs needed.
- After any file or code modification, briefly confirm correctness and outcome.
- Use only allowed tools specified by context; for routine, read-only tasks proceed automatically, but require explicit user confirmation for any destructive or irreversible actions.

---

## 1. Task List Management Protocol

**Purpose:** Maintain product requirement document (PRD)-linked task lists, reinforce task progression, and ensure traceability.

### Rules

- Only work on one sub-task at any given time.
- **Completion Protocol:**
  1. Mark a completed sub-task as `[x]`.
  2. Identify changed files using `git diff --name-only` (base: default branch).
  3. Run targeted tests for changed files; log results to `/test/` as JSON.
  4. Remove all temporary and intermediate files.
  5. Commit changes using a **conventional commit message** (`feat:`, `fix:`, etc.), including a summary, major modifications, and PRD reference.
     - Example: `feat(auth): add login API (refs prd-user-signup)`
  6. Mark a parent task as `[x]` only after all its child sub-tasks are complete.
  7. Update `/tasks/tasks-[prd-file-name].md` changelog with date and summary.
- Ensure the list of **Relevant Files** is continuously up to date.

### Default Branch Detection
- Determine the repository's default branch dynamically:
  - `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'`
  - Fallback order if unavailable: `main` → `master`.

---

## 2. TDD with Design Protocol

**Purpose:** Integrate test-driven development with minimal-complexity, best-practice design.

### Phases

1. **Pre-Implementation Planning**
   - Clearly define requirements and acceptance criteria.
   - Propose at least two design approaches and select the lowest complexity option.
   - Outline data flows, dependencies, and API contracts.
2. **RED Phase: Author Failing Tests**
   - Ensure coverage of all requirements (unit/integration/E2E tests).
   - Include edge cases and error-handling in test suites.
   - Use contract-based mocks exclusively.
3. **GREEN Phase: Minimal Implementation**
   - Implement defensive and error-handling code first.
   - Write the minimal code to satisfy each test, addressing tests iteratively.
4. **REFACTOR Phase: Code Quality Improvement**
   - Remove duplication, simplify logic, and improve naming.
   - Validate module depth, enforce information hiding, and check for robust error prevention.
5. **Integration & Validation**
   - Execute full workflows across environments to verify performance, accessibility, and stability.

### MVP TDD-Lite Enforcement
- For each change set/parent task, you MUST:
  - Author a failing smoke test first (targeting acceptance criteria or key flow).
  - Implement the minimal code to pass (keep scope tight to the test).
  - Refactor immediately after passing (naming, duplication, simplicity).
- Scope remains MVP-level: smoke tests only, not full unit/integration breadth.

### Success Metrics

- All tests passing
- 100% requirement coverage
- Zero runtime errors
- Deep modules, simple interfaces
- Complexity concealed from consumers

### Common Pitfalls

- Creating tests after implementation
- Modifying tests to fit existing code
- Skipping refactor step
- Using shallow modules or causing information leakage

---

## 3. Test Suite Protocol

**Purpose:** Ensure all test outcomes are machine-validated JSON for direct agent consumption.

### Rules

- **Do not validate using terminal output.**
- All test results must be written to `/test/<test_name>.json` and validated directly.
- Delete all JSON test results if all tests pass; retain only failed test results until all pass.
- No historical logs are permitted during MVP; only current results are relevant.

### Framework-Specific Commands

| Framework        | Command                                                                 |
|------------------|-------------------------------------------------------------------------|
| **Jest**         | `jest --runInBand --watch=false --watchAll=false --json --outputFile=test/<test_name>.json <files>`    |
| **Mocha**        | `mocha --reporter json <files> > test/<test_name>.json`                 |
| **Pytest**       | `pytest <files> --json-report --json-report-file=test/<test_name>.json` |
| **Java (JUnit)** | `mvn test -DjsonReportOutput=test/<test_name>.json`                     |
| **Next.js**      | Same as Jest                                                            |

LLM/AI agents must use the precise, non-interactive JSON-producing command for each framework:

- **Jest:**
  ```bash
  jest --runInBand --watch=false --watchAll=false --json --outputFile=test/<test_name>.json <files>
  ```
- **Mocha:**
  ```bash
  mocha --reporter json <files> > test/<test_name>.json
  ```
- **Pytest:**
  ```bash
  pytest <files> --json-report --json-report-file=test/<test_name>.json
  ```
- **Java (JUnit):**
  ```bash
  mvn test -DjsonReportOutput=test/<test_name>.json
  ```
- **Next.js:** Same as Jest.

### JSON Schema

Each test result file must contain:

- `test_name`: string `[a-zA-Z0-9_-]{1,255}`
- `status`: one of `"passed" | "failed" | "skipped"`
- `run_time_seconds`: float, three decimals
- `error_message`: null if passing/skipped, or string if test failed

Schema file: `dev-utils/test/schema.json`

#### Example Output

```json
{
  "test_name": "integration_case12",
  "status": "failed",
  "run_time_seconds": 2.304,
  "error_message": "Expected value not found in response"
}
```

### Validation Script Reference

- Validate JSON results against the schema using any JSON Schema validator.
- Example (Node, ajv-cli):
  ```bash
  npx ajv validate -s dev-utils/test/schema.json -d "test/*.json" --strict=false
  ```
- Example (Python, jsonschema):
  ```bash
  python -c 'import json,glob,jsonschema,sys;\
for f in glob.glob("test/*.json"):\
  jsonschema.validate(json.load(open(f)), json.load(open("dev-utils/test/schema.json"))) or print(f, "ok")' || echo "validation failed"
  ```

### Workflow Checklist

1. Preflight: Ensure `test/` directory exists; create if missing.
2. Plan: Identify changed code and targeted tests (by changed paths/tags/filenames).
3. Run: Execute the framework-specific command to generate JSON output (non-interactive).
4. Validate: Open each JSON file, check schema compliance (required keys/types), and review results.
5. Ensure only relevant/changed tests are executed and validated.
6. Delete: Remove JSON files only if all tests pass; keep failed-result files until resolved.
7. Agent must validate and report solely based on JSON file contents.
8. Upon full pass, delete all JSON files; if any tests fail, preserve related files until resolved.

### Success Criteria

- All result files match schema
- No CLI-based validation (no interactive or watch mode)
- JSON results automatically deleted upon success
- Only JSON file contents are used for validation and reporting

---

## SRS Reference (Lean)
- If an SRS exists at `/srs/srs-[feature-name].md`, ensure targeted tests and acceptance checks reflect key `NFR-*` budgets (e.g., latency, error rate).
- Prefer lightweight measurements (timed integration tests, error counters) aligned to NFR budgets during MVP.

---

# 🔹 Usage Flow

1. Prime session using the **Meta Protocol (0)**.
2. Identify and follow the appropriate protocol (Task List, TDD, Test Suite) based on the current task.
3. Progress through hierarchical steps: **Plan → Act → Validate → Pause**.
4. At each stage, confirm correctness and alignment with requirements before proceeding.

---

## Definition of Done (Shared)
- PRD present at `/prd/prd-[feature-name].md` and validated (sections/order/size).
- Tasks present at `/tasks/tasks-[feature-name].md` with acceptance criteria and test subtasks.
- Tests executed non-interactively; JSON results in `test/` conform to schema.
- On full green, JSON artifacts removed; otherwise retained until fixed.
 - TDD-Lite satisfied for each parent task/change: failing smoke test preceded implementation; minimal code then refactor were performed.

---

## Human Review Gate (Required)
- Confirm: targeted tests selection is relevant to changed files/areas.
- Confirm: any destructive actions (deletes/migrations) and merges.
- Confirm: scope changes or deviations from tasks.
- Approve proceeding with execution or merging.

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "process",
  "feature_slug": "[feature-name]",
  "default_branch": "[detected]",
  "changed_files": ["src/..."],
  "targeted_tests": ["src/.../__tests__/...test.ts"],
  "json_result_paths": ["test/<test_name>.json"],
  "status_summary": "passed|failed|partial"
}
```

### Artifact Manifest Update
- Append or create `/artifacts/manifest.json` with the same keys, plus timestamp.

### Q&A Loop Integration
- Centralize all questions in `/qa/qa-[feature-name]-[YYYYMMDD]-rN.md` as the single source of truth.
- Use IDs `Q-proc-*` only inside the QA document. Change Status to "Incorporated" after code/tests/commits reflect the decision.

### Quick Re-run and Timeouts
- Prefer targeted re-runs based on changed paths.
- Set appropriate timeouts for long-running tests to prevent stalls.

### Context Seed (for continuity)
Provide this block to the next session:

```json
{
  "feature_slug": "[feature-name]",
  "changed_files": ["src/..."],
  "last_status": "passed|failed|partial"
}
```

---

## Start Here
For day-one and daily loops, see `dev-utils/dev_workflow/project-entrypoint.md`.
