# Workflow: Tasks + Testing (Scaling)

## Objective
Generate detailed tasks from PRD with **built-in full TDD guidance**.  
Prioritize traceability and maintainability.

---

## Workflow
1. Read Full PRD.  
2. Generate **comprehensive parent tasks**.  
3. Break into detailed sub-tasks (<½ day each).  
4. Attach TDD steps to each coding task.  
5. Save to `/tasks/`.  

---

## Task File Structure
```markdown
# Tasks for [Feature Name]

## Changelog
- [YYYY-MM-DD] Initial tasks created.

## Relevant Files
- [file].ts – Implementation
- [file].test.ts – Tests

## Notes
- Follow strict TDD (write test before code).

## Tasks
- [ ] 1.0 Parent Task
  - [ ] 1.1 Define schema
  - [ ] 1.2 Write failing test
  - [ ] 1.3 Implement minimal code
  - [ ] 1.4 Refactor + add edge cases
```

---

## AI Agent Instructions
- Always include **test sub-task per coding task**.  
- Require test files and coverage notes.  
- Ensure traceability to PRD requirements.  
