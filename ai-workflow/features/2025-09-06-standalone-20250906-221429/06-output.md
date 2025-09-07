# AI Execution Status: 06-gen-tasks-and-testing.md

```json
{
  "workflow_step": {
    "document": "06-gen-tasks-and-testing.md",
    "step_number": "06",
    "phase": "implementation",
    "timestamp": "2025-09-06T22:14:32.838002"
  },
  "execution_status": "ready_for_ai_agent",
  "ai_prompt_file": "/tmp/tmpv74wvf7h.md",
  "feature_directory": "/home/jmaurelli/Projects/ai-workflow-system/ai-workflow/features/2025-09-06-standalone-20250906-221429",
  "expected_outputs": [
    "```json\n{\n  \"feature_slug\": \"[feature-name]\",\n  \"tasks_path\": \"/tasks/tasks-[feature-name].md\",\n  \"test_stub_paths\": [\"src/.../__tests__/...test.ts\"]\n}\n```\n",
    "  - **Backend**: `.py` for Python, `.js/.ts` for Node.js, `.go` for Go\n  - **Frontend**: `.jsx/.tsx` for React, `.vue` for Vue.js, `.js/.ts` for vanilla\n  - **Database**: `.sql` for relational, `.json` for document stores\n- Always specify both implementation and related test files.\n- Use a standard layout when applicable:\n  - Implementation: `src/[area]/[name].[extension]`\n  - Tests: `src/[area]/__tests__/[name].test.[extension]`\n- Generate at least one test stub file per parent task (empty is acceptable) and include it.\n",
    "```json\n{\n  \"stage\": \"tasks\",\n  \"feature_slug\": \"[feature-name]\",\n  \"prd_path\": \"/prd/prd-[feature-name].md\",\n  \"srs_path\": \"/srs/srs-[feature-name].md\",\n  \"parent_tasks\": [\"...\"],\n  \"acceptance_criteria_by_task\": {\"1.0\": [\"...\"], \"2.0\": [\"...\"]},\n  \"relevant_files_by_task\": {\"1.0\": [\"src/...\"], \"2.0\": [\"src/...\"]},\n  \"test_stub_paths\": [\"src/.../__tests__/...test.ts\"],\n  \"traceability_map\": {\"REQ-1\": [\"1.0\"], \"REQ-2\": [\"2.0\"]},\n  \"nfr_traceability\": {\"NFR-1\": [\"1.0\", \"3.4\"], \"NFR-2\": [\"2.0\"]},\n  \"nfr_budgets\": {\"latency_p50_ms\": 300, \"latency_p95_ms\": 800, \"error_rate\": 0.01}\n}\n```\n",
    "- **Feature-centric**: `./tasks.md` (within current feature directory)\n- **Legacy**: `/tasks/tasks-[prd-name].md` (traditional scattered structure)\n\nThe document should conform to the following structure:\n\n```markdown\n# Tasks for [PRD Name]\n"
  ],
  "validation_criteria": [
    "- **Tech Stack Choices**: Backend/frontend technologies, database, API style\n  - **UX Approach**: Component library strategy, design patterns, user flow decisions\n  - **Learning Context**: Knowledge confidence levels and learning goals\n  - **Decision Rationale**: Why specific technologies and approaches were chosen\n- If present, read Lean SRS at `/srs/srs-[feature-name].md` and incorporate NFR budgets into acceptance criteria (reference `NFR-*`).\n- **Design Analysis**: If design analysis exists at `/design/design-[feature-name].md`, incorporate component reuse and integration guidance.\n- **Integration Planning**: Use design analysis integration approach to plan task dependencies.\n- **Component Reuse**: Reference design analysis for existing components to reuse vs. creating new ones.\n- Ensure the PRD contains: overview, goals, user stories, and requirements.\n- If any elements are missing, clearly state what is absent at the top of the output, and skip steps that cannot be performed as a result.\n- Read `/docs/architecture.md` if present; otherwise, capture minimal architecture decisions inline and note any deltas or open items.",
    "- **Backend**: `.py` for Python, `.js/.ts` for Node.js, `.go` for Go\n  - **Frontend**: `.jsx/.tsx` for React, `.vue` for Vue.js, `.js/.ts` for vanilla\n  - **Database**: `.sql` for relational, `.json` for document stores\n- Always specify both implementation and related test files.\n- Use a standard layout when applicable:\n  - Implementation: `src/[area]/[name].[extension]`\n  - Tests: `src/[area]/__tests__/[name].test.[extension]`\n- Generate at least one test stub file per parent task (empty is acceptable) and include it.",
    "- App startup\n  - User login\n  - Main feature operation\n- Place test stubs alongside code, even if mostly empty.\n- Execute tests per `process-tasks.md` (centralized commands, JSON schema, and cleanup rules). For Jest, use `--watch=false --watchAll=false`.",
    "- `/decisions/design-decisions-[feature-name].md` \u2192 Tech stack rationale\n  - `/srs/srs-[feature-name].md` \u2192 Performance budgets and security baseline\n  - `/design/design-[feature-name].md` \u2192 Component strategy and integration approach\n  - `/decisions/learning-notes-[feature-name].md` \u2192 Team confidence and learning goals\n- **Distill into concise bullets** - each Executive Context item should be 1-2 lines maximum\n- **Focus on implementation-critical info** - what AI agents need to make good coding decisions",
    "- **Feature-centric**: `./tasks.md` (within current feature directory)\n- **Legacy**: `/tasks/tasks-[prd-name].md` (traditional scattered structure)\n\nThe document should conform to the following structure:\n\n```markdown\n# Tasks for [PRD Name]",
    "```json\n{\n  \"stage\": \"tasks\",\n  \"feature_slug\": \"[feature-name]\",\n  \"prd_path\": \"/prd/prd-[feature-name].md\",\n  \"srs_path\": \"/srs/srs-[feature-name].md\",\n  \"parent_tasks\": [\"...\"],\n  \"acceptance_criteria_by_task\": {\"1.0\": [\"...\"], \"2.0\": [\"...\"]},\n  \"relevant_files_by_task\": {\"1.0\": [\"src/...\"], \"2.0\": [\"src/...\"]},\n  \"test_stub_paths\": [\"src/.../__tests__/...test.ts\"],\n  \"traceability_map\": {\"REQ-1\": [\"1.0\"], \"REQ-2\": [\"2.0\"]},\n  \"nfr_traceability\": {\"NFR-1\": [\"1.0\", \"3.4\"], \"NFR-2\": [\"2.0\"]},\n  \"nfr_budgets\": {\"latency_p50_ms\": 300, \"latency_p95_ms\": 800, \"error_rate\": 0.01}\n}\n```",
    "be: \"Write failing smoke test (targeting acceptance criteria)\".",
    "appear in this order: Changelog, Relevant Files, Notes (optional if not needed), Tasks, Task Dependencies, Risk Mitigation, Success Criteria.",
    "include at least one test-related sub-task.",
    "use `- [ ]` Markdown checklists.",
    "always list both implementation and test/validation files for each task.",
    "be clear and high-level, for example: \u201cImplement login API.\u201d",
    "be 1-2 lines maximum",
    "fit on a single page for MVP; expand only if Enhancement Mode is explicitly requested.",
    "be a single Markdown document saved as:",
    "conform to the following structure:"
  ],
  "completion_status": {
    "started": false,
    "completed": false,
    "validated": false,
    "errors": []
  }
}
```

## Instructions for AI Agent

Execute the workflow document `06-gen-tasks-and-testing.md` using the context and data provided.

### Next Steps
1. Read the workflow document
2. Execute the instructions
3. Generate required outputs
4. Validate results
5. Update completion status
