# Scaling Workflow Cheat Sheet

## 🛠️ Goal
Maintain speed as a solo developer, but with **higher rigor and quality**.  
Ensure documentation and testing are thorough enough for scaling and long-term maintainability.

---

## Workflow Overview
1. **Idea → Full PRD**  
   - Use `create-prd-scaling.md`  
   - Always generate a complete PRD with user stories, requirements, risks, dependencies.

2. **PRD → Detailed Tasks + TDD**  
   - Use `tasks-and-testing-scaling.md`  
   - Each coding task has a linked test sub-task.  
   - Tests written **before code**.

3. **Tasks → Code**  
   - Follow TDD strictly.  
   - Refactor aggressively.  
   - Maintain links between PRD → Tasks → Tests.

4. **Deploy**  
   - Use `project-templates-scaling.md` → Full Deployment Plan.  
   - Define rollback, monitoring, and performance metrics.

5. **Maintain + Monitor**  
   - Record results in `test-suite-scaling.md`.  
   - Commit results per feature/release.  
   - Track coverage, logs, failures.

---

## Document Roles
- `create-prd-scaling.md` → Full PRD (thorough).  
- `tasks-and-testing-scaling.md` → Tasks with built-in TDD workflow.  
- `project-templates-scaling.md` → Full templates for architecture, deployment, monitoring.  
- `software-project-workflow-guide-scaling.md` → Defines strict workflow for scaling.  
- `tdd-with-design-scaling.md` → Strict TDD + design principles.  
- `test-suite-scaling.md` → Enforced schema for results & coverage.

---

## AI Agent Rules (Scaling Mode)
- Always generate **Full versions** of documents.  
- Require clarifications, do not assume.  
- Link every task → test → PRD requirement.  
- Reject incomplete test results.  
- Expand documentation without compression.  

---

## Example Flow
1. Capture feature → Full PRD (`prd-user-login-scaling.md`).  
2. Generate detailed tasks + TDD (`tasks-prd-user-login-scaling.md`).  
3. Implement with strict TDD (write test → code → refactor).  
4. Deploy with full rollback plan.  
5. Log results in test suite JSON.  
