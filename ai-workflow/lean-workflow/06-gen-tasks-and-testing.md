Developer: # Workflow: Tasks + Testing (MVP-First)

**🚨 CRITICAL LOCATION REQUIREMENT:**
**You MUST be in the feature directory: `/features/YYYY-MM-DD-project-name/`**
**Save the tasks as `./tasks.md` in the feature directory - NOT in project root!**

## Objective
Transform a Lean PRD into actionable tasks with integrated testing guidance. This process combines task generation and lightweight TDD into a streamlined approach suitable for solo MVP development.

---

## Workflow Steps

**PREREQUISITE**: You must be working in the feature directory from 01-mvp-entrypoint.md

Begin with a concise checklist (3-7 bullets) of intended sub-tasks before proceeding; keep checklist items conceptual.

### 1. Input Context (Feature Directory)
- **Working Directory**: Confirm you're in `/features/YYYY-MM-DD-project-name/` with existing workflow documents
- **Lean PRD**: Read from `./prd.md` (current feature directory)
- **Design Decisions (Required)**: Read design decisions from `./design-decisions.md` to understand:
  - **Tech Stack Choices**: Backend/frontend technologies, database, API style
  - **UX Approach**: Component library strategy, design patterns, user flow decisions
  - **Learning Context**: Knowledge confidence levels and learning goals
  - **Decision Rationale**: Why specific technologies and approaches were chosen
- **Lean SRS**: Read from `./srs.md` and incorporate NFR budgets into acceptance criteria (reference `NFR-*`)
- **Design Analysis**: If design analysis exists at `./design-analysis.md`, incorporate component reuse and integration guidance
- **Integration Planning**: Use design analysis integration approach to plan task dependencies
- **Component Reuse**: Reference design analysis for existing components to reuse vs. creating new ones
- **Validation**: Ensure the PRD contains overview, goals, user stories, and requirements
- **Missing Elements**: If any elements are missing, clearly state what is absent at the top of the output

### 2. Generate Parent Tasks
- Identify 3–5 parent tasks derived from the PRD.
- If fewer than 3 or more than 5 parent tasks are available, proceed with what is supported, and clearly document this under **Notes** in the output.
- Parent tasks should be clear and high-level, for example: “Implement login API.”

### 3. Expand into Sub-Tasks (Design-Decision Aware)
- For each parent task, break it down into smaller sub-tasks (ideally actions that take less than one day) using Markdown checklists (`- [ ]`).
- **Apply Design Decisions**: Tailor sub-tasks to chosen tech stack (e.g., React components vs Vue components, Python FastAPI vs Node.js Express).
- **Incorporate Learning Goals**: Include sub-tasks that support skill development identified in design decisions.
- **Honor UX Decisions**: Structure frontend tasks according to chosen component library strategy and design patterns.
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

### 4. Relevant Files (Tech-Stack Aware)
- List the files associated with each parent task in a dedicated **Relevant Files** section as a Markdown list.
- **Apply Tech Stack Decisions**: Use file extensions and paths matching chosen technologies:
  - **Backend**: `.py` for Python, `.js/.ts` for Node.js, `.go` for Go
  - **Frontend**: `.jsx/.tsx` for React, `.vue` for Vue.js, `.js/.ts` for vanilla
  - **Database**: `.sql` for relational, `.json` for document stores
- Always specify both implementation and related test files.
- Use a standard layout when applicable:
  - Implementation: `src/[area]/[name].[extension]`
  - Tests: `src/[area]/__tests__/[name].test.[extension]`
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

## AI Agent Instructions (Context-Aware Task Generation)

### Context Distillation (Priority 1)
- **Always read and distill** the following sources into Executive Context:
  - `/decisions/design-decisions-[feature-name].md` → Tech stack rationale
  - `/srs/srs-[feature-name].md` → Performance budgets and security baseline
  - `/design/design-[feature-name].md` → Component strategy and integration approach
  - `/decisions/learning-notes-[feature-name].md` → Team confidence and learning goals
- **Distill into concise bullets** - each Executive Context item should be 1-2 lines maximum
- **Focus on implementation-critical info** - what AI agents need to make good coding decisions

### Context Reference Mapping (Priority 2)
- **Map specific task needs** to exact document sections for just-in-time loading
- **Example**: "For JWT implementation → `/srs/srs-auth.md` REQ-SEC-002, REQ-PERF-003"
- **Be specific**: Section numbers, requirement IDs, decision rationale sections

### Task Context Embedding (Priority 3)
- **Each parent task gets essential context** - tech pattern, key constraints, integration points
- **Each subtask gets minimal context** - specific pattern, performance target, or security requirement
- **Balance completeness vs brevity** - enough context for AI to implement correctly, not more

### Smart Context Management
- **Avoid context duplication** - reference don't repeat detailed requirements
- **Use shorthand for common patterns** - "FastAPI middleware pattern", "React component reuse"
- **Flag high-context tasks** - when tasks need extensive external context, note it clearly

### Technical Implementation Rules
- **Apply tech stack choices** to all file extensions, frameworks, and patterns
- **Honor UX decisions** when structuring frontend tasks and component organization
- **Include NFR validation** in acceptance criteria with specific metrics
- **Reference decision rationale** when explaining why specific approaches are chosen
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

Output should be a single Markdown document saved as:
- **Feature-centric**: `./tasks.md` (within current feature directory)
- **Legacy**: `/tasks/tasks-[prd-name].md` (traditional scattered structure)

The document should conform to the following structure:

```markdown
# Tasks for [PRD Name]

## Executive Context (Distilled for AI Agents)
**Tech Stack**: [Key technology choices and rationale from design decisions]
**Performance Budgets**: [Critical SRS constraints - response times, throughput]
**Security Baseline**: [Essential security requirements from SRS]
**Component Strategy**: [Design analysis integration approach - reuse vs new]
**Learning Context**: [Team confidence levels and skill-building goals]

## Context References (Just-in-Time Loading)
**Requirements**: `./prd.md` sections [specific sections needed] (feature-centric) OR `/prd/prd-[feature-name].md` (legacy)
**NFR Specifications**: `./srs.md` [specific REQ-* IDs] (feature-centric) OR `/srs/srs-[feature-name].md` (legacy)
**Design Decisions**: `./design-decisions.md` [relevant decision areas] (feature-centric) OR `/decisions/design-decisions-[feature-name].md` (legacy)
**Component Integration**: `./design-analysis.md` [integration guidance] (feature-centric) OR `/design/design-[feature-name].md` (legacy)
**Learning Notes**: `./learning-notes.md` [confidence tracking] (feature-centric) OR `/decisions/learning-notes-[feature-name].md` (legacy)

## Changelog
- [YYYY-MM-DD] Initial tasks created.
- [YYYY-MM-DD] [Description of subsequent changes]

## Relevant Files (Tech-Stack Aware)
- path/to/file1.[ext] – [description with tech stack context]
- path/to/file2.[ext] – [description with performance/security notes]

## Notes
- [Freeform notes, including process deviations and context decisions]

## Tasks (Context-Embedded)
- [ ] 1.0 [Parent Task 1]
  - **Context**: [Essential context for this task - tech choices, constraints, integration points]
  - [ ] 1.1 [Subtask 1] - [Minimal context: tech pattern, performance target]
  - [ ] 1.2 [Subtask 2] - [Minimal context: integration approach, security requirement]
  ...
- [ ] 2.0 [Parent Task 2]
  - **Context**: [Essential context for this task]
  ...

### Acceptance Criteria (NFR-Enhanced)
- [Criteria for Parent Task 1] (PRD: REQ-X, SRS: NFR-Y, Performance: <Zms)
- [Criteria for Parent Task 2] (PRD: REQ-A, SRS: NFR-B, Security: compliance-C)

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
- Confirm: design decisions from `/decisions/design-decisions-[feature-name].md` have been applied to task generation
- Confirm: tech stack choices reflected in file extensions, frameworks, and implementation approaches
- Confirm: UX decisions integrated into frontend task structure and component organization
- Confirm: learning goals from design decisions supported through task breakdown
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

---

## Workflow Transition Protocol

### Document Completion Summary
**AI Instructions**: After completing the tasks and testing document, provide a summary including:
- **Tasks Generated**: `./tasks.md` with [Number of parent tasks] created
- **Implementation Structure**: [TDD-Lite approach with test stubs created]
- **Context Integration**: [Technology stack and design decisions embedded]
- **Acceptance Criteria**: [Quality gates and performance targets defined]
- **Risk Mitigation**: [High-risk tasks identified with contingency plans]
- **Manifest Updated**: feature-manifest.json marked tasks as completed
- **Completion Time**: [AI: Insert current date and time in format: $(date '+%Y-%m-%d %H:%M:%S')]

### User Approval Gate
Present these options to the user:
- **Yes**: "Continue to 07-process-tasks.md for task execution"
- **No**: "Stop workflow here (you can resume later)"
- **Revise**: "What specifically would you like changed in the task planning?"

### Next Step Preview
**Next**: 07-process-tasks.md - Task Execution with TDD-Lite
**Phase 3 Purpose**: Execute tasks with TDD-Lite (context-aware implementation)
**What Process Tasks needs from this step**: Generated tasks, test stubs, acceptance criteria, and context references

---

## Resume Workflow Detection

**AI Instructions**: If resuming this workflow, check feature-manifest.json status and present:

```
✅ WORKFLOW RESUME DETECTED
  ✅ 01-mvp-entrypoint.md - Project initialization (completed)
  ✅ 02-gen-prd.md - Product requirements (completed)
  ✅ 03-gen-srs.md - Software requirements (completed)
  ✅ 04-gen-design-decisions-lite.md - Technology decisions (completed)
  ✅ 05-gen-design.md - Component analysis (completed)
  🎯 06-gen-tasks-and-testing.md - Implementation tasks (CURRENT)
  ⏳ 07-process-tasks.md - Task execution (pending)
  ⏳ 08-gen-completion-summary.md - Project summary (pending)
  ⏳ 09-gen-project-history.md - Learning capture (pending)

📋 Implementation Foundation:
  • Technology Stack: [Chosen technologies and rationale]
  • Component Strategy: [Reuse vs new development approach]
  • Design Patterns: [UI/UX patterns established]
  • Architecture: [Integration approach defined]

📍 STARTING: PHASE 3 - Implementation (Actually BUILD it)
Phase 3 Purpose: Generate implementation tasks (context-embedded)

Continue with task generation? [Yes/No/Review Documents]
```

---

## Start Here
For day-one and daily loops, follow `dev-utils/dev_workflow/mvp-core-protocol.md` (single source). See `project-entrypoint.md` for step order.
