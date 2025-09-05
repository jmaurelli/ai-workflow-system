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

---

## Enhanced Task File Structure (Design-Aware)
```markdown
# Tasks for [Feature Name] (Scaling)

## Changelog
- [YYYY-MM-DD] Initial tasks created from scaling PRD.
- [YYYY-MM-DD] [Description of subsequent changes]

## Relevant Files
### Implementation Files
- [file].ts – Main implementation
- [file].types.ts – TypeScript definitions
- [file].styles.ts – Component styling

### Testing Files
- [file].test.ts – Unit tests
- [file].integration.test.ts – Integration tests
- [file].visual.test.ts – Visual regression tests
- [file].a11y.test.ts – Accessibility tests

### Design System Files
- [component].stories.ts – Storybook documentation
- [component].docs.md – Component documentation

## Notes
- Follow strict TDD with comprehensive test coverage
- Ensure design system compliance throughout implementation
- Validate accessibility requirements at each step
- Monitor performance impact of component changes

## Tasks
- [ ] 1.0 [Parent Task 1] - Design System Integration
  - [ ] 1.1 Analyze existing component patterns and design system alignment
  - [ ] 1.2 Write failing tests for component API and behavior
  - [ ] 1.3 Implement component following design system standards
  - [ ] 1.4 Add comprehensive test coverage (unit, integration, visual, a11y)
  - [ ] 1.5 Document component usage and examples
  - [ ] 1.6 Validate performance benchmarks and optimization
  - [ ] 1.7 Review design system compliance and consistency

- [ ] 2.0 [Parent Task 2] - Feature Implementation
  - [ ] 2.1 Define feature requirements and acceptance criteria
  - [ ] 2.2 Write failing tests for feature functionality
  - [ ] 2.3 Implement minimal feature code to pass tests
  - [ ] 2.4 Add edge case handling and error states
  - [ ] 2.5 Implement accessibility features and testing
  - [ ] 2.6 Add performance monitoring and optimization
  - [ ] 2.7 Create comprehensive documentation and examples

## Task Dependencies

### Critical Path
1. **Task 1.1** → **Task 1.2** → **Task 1.3** → **Task 1.7**
2. **Task 1.7** → **Task 2.1** (design system compliance before feature implementation)
3. **Task 2.2** → **Task 2.3** → **Task 2.4** (TDD sequence)

### Parallel Tasks
- **Design Analysis** (1.1) can run parallel to **Requirements Definition** (2.1)
- **Documentation** (1.5, 2.7) can run parallel to **Testing** (1.4, 2.5)
- **Performance Testing** (1.6, 2.6) can run parallel to **Feature Testing** (1.4, 2.4)

## Risk Mitigation

### High-Risk Tasks
- **Task 1.3** (Component Implementation): Ensure design system compliance
- **Task 2.3** (Feature Implementation): Validate performance impact
- **Task 1.6, 2.6** (Performance): Monitor bundle size and runtime performance

### Contingency Plans
- **Design System Breaking Changes**: Implement version pinning and migration strategy
- **Performance Issues**: Implement lazy loading and code splitting
- **Accessibility Failures**: Implement automated accessibility testing pipeline

## Success Criteria

### MVP Completion
- [ ] All components follow design system standards
- [ ] Comprehensive test coverage (>90% unit, >80% integration)
- [ ] Performance benchmarks met (bundle size, render time)
- [ ] Accessibility compliance validated (WCAG 2.1 AA)
- [ ] Documentation complete with examples

### Quality Gates
- **Week 1**: ✅ Design system analysis complete, component APIs defined
- **Week 2**: ✅ Core implementation complete, basic tests passing
- **Week 3**: ✅ Full test coverage, performance validated
- **Week 4**: ✅ Documentation complete, ready for review and deployment

### Acceptance Criteria
- [Criteria for Parent Task 1] (reference PRD requirement IDs: REQ-1, REQ-2)
- [Criteria for Parent Task 2] (reference PRD requirement IDs: REQ-3, REQ-4)
```

---

## AI Agent Directives
- Always include **comprehensive test sub-tasks** for each coding task (unit, integration, visual, accessibility)
- Require design system compliance validation for all component tasks
- Ensure traceability from PRD requirements through tasks to test validation
- Validate performance impact and bundle size for all component changes
- Require accessibility testing and compliance validation
- Save enhanced task files in `/tasks/tasks-[feature-name]-scaling.md`
- Reference any existing MVP task files and build upon their foundation
Set reasoning_effort = high; scaling tasks require comprehensive planning and validation

---

## Human Review Gate (Required)
- Confirm: all tasks include comprehensive testing requirements
- Confirm: design system compliance validation included in all relevant tasks
- Confirm: accessibility requirements and testing included
- Confirm: performance considerations and monitoring included
- Confirm: task dependencies and critical path identified
- Confirm: risk mitigation strategies and contingency plans approved
- Approve proceeding to implementation with scaling rigor

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "tasks_scaling",
  "feature_slug": "[feature-name]",
  "prd_path": "/prd/prd-[feature-name]-scaling.md",
  "tasks_path": "/tasks/tasks-[feature-name]-scaling.md",
  "parent_tasks": ["..."],
  "acceptance_criteria_by_task": {"1.0": ["..."], "2.0": ["..."]},
  "relevant_files_by_task": {"1.0": ["src/..."], "2.0": ["src/..."]},
  "test_requirements": {
    "unit_tests": ["..."],
    "integration_tests": ["..."],
    "visual_tests": ["..."],
    "accessibility_tests": ["..."]
  },
  "design_system_compliance": {
    "components_validated": ["..."],
    "tokens_usage_validated": true,
    "patterns_compliance_checked": true
  },
  "performance_requirements": {
    "bundle_size_targets": "...",
    "render_performance_targets": "...",
    "monitoring_setup": true
  },
  "traceability_map": {"REQ-1": ["1.0"], "REQ-2": ["2.0"]}
}
```

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "tasks_path": "/tasks/tasks-[feature-name]-scaling.md",
  "test_requirements": ["comprehensive coverage required"],
  "design_system_compliance_required": true,
  "scaling_context": true
}
```

---

## Human-in-the-Loop Rule
Pause only for destructive/irreversible actions or scope changes; otherwise proceed autonomously.  
