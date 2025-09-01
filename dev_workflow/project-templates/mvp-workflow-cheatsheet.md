Developer: # MVP-First Workflow Cheat Sheet (Optimized: 5 Core Docs)

## 🚀 Goal
Accelerate solo MVP delivery while establishing a scalable, quality foundation.

---

## Workflow Overview
Begin with a concise checklist (3-7 bullets) of planned steps before starting substantive work.

1. **Idea → PRD**  
   - Use `create-prd.md`.  
   - Default to a **Lean PRD** (max 1 page).  
   - Expand to Full PRD only as needed when the project evolves.

2. **PRD → Tasks + Testing**  
   - Use `tasks-and-testing.md`.  
   - Identify 3–5 parent tasks, breaking them down into sub-tasks.  
   - Integrate smoke tests and test stubs aligned to tasks.  
   - Save outputs to `/tasks/tasks-[prd-name].md`.

3. **Tasks → Code**  
   - Implement rapidly following the specified tasks.  
   - Focus on smoke tests for essential flows.  
   - Store test stubs with the codebase.

4. **Deploy MVP**  
   - Reference `project-templates.md` for Lean Deployment.  
   - Deploy once smoke tests pass. After deployment, validate that key flows function as intended and address any failures immediately.

5. **Enhancement Mode (as needed)**  
   - Upgrade Lean PRDs to Full PRDs as complexity grows.  
   - Develop tasks into comprehensive TDD practices.  
   - Expand smoke tests into a full test suite.  
   - Integrate monitoring and performance improvements.

---

## Document Roles
- `create-prd.md`: Capture ideas and generate Lean PRDs.
- `tasks-and-testing.md`: Translate PRDs into actionable tasks, incorporating initial testing guidance.
- `project-templates.md`: Reference for both Lean and Full templates.
- `software-project-workflow-guide.md`: Clarifies MVP versus Enhancement workflows.
- `test-suite.md`: Archive and evolve test results (JSON schema adaptable).

---

## AI Agent Rules (MVP Mode)
- Use only Lean templates for all docs during MVP phase.
- Avoid unnecessary clarifications or interruptions.
- Always generate test stubs, with only smoke tests required for MVP acceptance.
- Keep MVP-phase documents at or under 1 page.
- Organize output files into appropriate folders: `/prd/`, `/tasks/`, `/tests/`.
- After each tool call or code edit, validate the result in 1-2 sentences and proceed or iterate if validation fails.

---

## Example Flow
1. Capture feature → Lean PRD (`prd-user-login.md`).
2. Generate corresponding tasks and smoke tests (`tasks-prd-user-login.md`).
3. Implement:
   - Code login endpoint.
   - Create smoke test: “User can log in successfully.”
4. Deploy MVP and confirm that all critical workflows pass.
5. Expand project documentation and testing as requirements evolve.
