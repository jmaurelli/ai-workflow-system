# Workflow: Tasks + Testing (Scaling)

## Objective
Generate detailed tasks from PRD with **built-in full TDD guidance**.  
Prioritize traceability and maintainability.

---

## Enterprise Workflow (Context-Aware)
1. **Context Distillation (Priority 1)**: Read and distill enterprise context sources:
   - `/decisions/design-decisions-scaling-[project-name].md` → System architecture, tech evolution, design system strategy
   - `/srs/srs-scaling-[project-name].md` → Enterprise performance budgets, security compliance, availability targets
   - `/design/design-scaling-[project-name].md` → Component library integration, design system governance
   - `/decisions/learning-notes-scaling-[project-name].md` → Team capabilities, architectural knowledge, skill development
2. **Enterprise Context Mapping**: Map specific enterprise needs to document sections for just-in-time loading
3. **Read Full PRD** with enterprise context lens applied
4. **Generate comprehensive parent tasks** with embedded enterprise context (architecture patterns, performance targets, compliance requirements)
5. **Break into detailed sub-tasks** (<½ day each) with minimal context per subtask (specific patterns, enterprise constraints, integration approaches)
6. **Attach enterprise TDD** with design system validation, performance testing, security compliance, accessibility verification
7. **Save to `/tasks/`** with enterprise context structure  

---

## Enhanced Task File Structure (Enterprise Design-Aware)
```markdown
# Tasks for [Feature Name]

## Executive Context (Enterprise-Distilled for AI Agents)
**System Architecture**: [Microservices/distributed system patterns and service boundaries from design decisions]
**Technology Evolution**: [Enterprise tech stack with migration considerations and integration patterns]
**Design System Strategy**: [Component library governance, design token architecture, cross-platform requirements]
**Performance Budgets**: [Enterprise-scale targets - 99.9% uptime, <100ms response, 10K+ concurrent users]
**Security & Compliance**: [Enterprise requirements - GDPR, SOC2, security patterns, audit requirements]
**Team Coordination**: [Multi-team integration, architectural decision communication, knowledge sharing]

## Context References (Enterprise Just-in-Time Loading)
**System Architecture**: `/decisions/design-decisions-scaling-[project-name].md` microservices strategy, service boundaries
**Performance Specifications**: `/srs/srs-scaling-[project-name].md` REQ-PERF-001 to REQ-PERF-010, REQ-SCALE-001 to REQ-SCALE-005
**Security Requirements**: `/srs/srs-scaling-[project-name].md` REQ-SEC-001 to REQ-SEC-020, compliance specifications
**Design System Integration**: `/design/design-scaling-[project-name].md` component library, governance processes
**Team Architecture**: `/decisions/learning-notes-scaling-[project-name].md` team capability, coordination patterns

## Changelog
- [YYYY-MM-DD] Initial enterprise tasks created.

## Relevant Files (Design-System Aware)
### Implementation Files
- [microservice]/[feature].ts – Service implementation with enterprise patterns
- [component-library]/[component].tsx – Design system component with tokens
- [api-gateway]/[routes].ts – Enterprise API integration with security

### Testing Files  
- [microservice]/__tests__/[feature].test.ts – Unit tests with performance validation
- [integration]/__tests__/[feature].integration.test.ts – Service integration tests
- [e2e]/__tests__/[feature].e2e.test.ts – End-to-end with accessibility validation
- [performance]/__tests__/[feature].performance.test.ts – Load and scalability tests

### Design System Files
- [design-system]/components/[component].tsx – Reusable component implementation
- [design-system]/tokens/[theme].ts – Design token definitions
- [design-system]/docs/[component].stories.tsx – Component documentation

## Notes
- Enterprise architecture constraints and design system compliance requirements
- Cross-team coordination and integration considerations

## Tasks (Enterprise Context-Embedded)
- [ ] 1.0 [Parent Task - Enterprise Pattern]
  - **Context**: [Architecture pattern, performance targets, security requirements, design system integration, team coordination]
  - [ ] 1.1 [Subtask] - [Microservice pattern, <100ms target, OAuth integration, component library usage]
  - [ ] 1.2 [Subtask] - [Distributed system pattern, fault tolerance, monitoring integration, accessibility compliance]
  - [ ] 1.3 [Subtask] - [Design system component, token usage, cross-platform consistency, team documentation]
  ...
- [ ] 2.0 [Parent Task - Design System Integration]
  - **Context**: [Component library strategy, design token architecture, governance process, team adoption]
  ...

### Acceptance Criteria (Enterprise NFR-Enhanced)
- [Criteria for Parent Task 1] (PRD: REQ-X, SRS: REQ-PERF-Y, Design: COMP-Z, Security: SEC-A, Accessibility: A11Y-B)
- [Criteria for Parent Task 2] (Performance: <X ms @ Y scale, Security: compliance-C, Design: token-usage-D)

## Task Dependencies (Enterprise Coordination)

### Critical Path (Cross-Service Dependencies)
1. **Service A Task X.Y** → **Service B Task A.B** → **API Gateway Task C.D** (microservice dependency chain)
2. **Design System Task D.E** → **Component Implementation Task F.G** (design system dependency)
3. **Infrastructure Task H.I** → **Performance Testing Task J.K** (scaling dependency)

### Parallel Tasks (Multi-Team Coordination)
- **Week X**: Backend services, Frontend components, Infrastructure setup (can run simultaneously)
- **Week Y**: Integration testing, Performance validation, Security audit (coordinated validation)

## Risk Mitigation (Enterprise Scale)

### High-Risk Tasks (Enterprise Complexity)
- **Microservice Integration (Task X.Y)**: Risk of service communication complexity and latency
- **Design System Migration (Task A.B)**: Risk of component library adoption and team coordination
- **Performance Optimization (Task C.D)**: Risk of enterprise-scale performance targets

### Contingency Plans (Enterprise Recovery)
- **Service Communication Issues**: Circuit breaker implementation, fallback service patterns
- **Design System Adoption Resistance**: Phased rollout, training program, incentive alignment
- **Performance Target Misses**: Horizontal scaling, caching layer, architecture optimization

## Success Criteria (Enterprise Quality Gates)

### Enterprise Completion
- [ ] 99.9% uptime achieved across all services
- [ ] <100ms response time at 10K+ concurrent users
- [ ] 100% design system compliance with accessibility validation
- [ ] Security audit passed with zero critical vulnerabilities
- [ ] Cross-team integration successful with documented APIs

### Quality Gates (Enterprise Validation)
- **Week X**: ✅ Microservices deployed with monitoring, design system foundation complete
- **Week Y**: ✅ Performance targets validated, security compliance verified
- **Week Z**: ✅ End-to-end integration complete, team adoption metrics achieved
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

## AI Agent Directives (Enterprise Context-Aware Task Generation)

### Enterprise Context Distillation (Priority 1)
- **Always read and distill** the following enterprise sources into Executive Context:
  - `/decisions/design-decisions-scaling-[project-name].md` → System architecture, tech evolution, design system strategy
  - `/srs/srs-scaling-[project-name].md` → Enterprise performance budgets, security compliance, availability targets
  - `/design/design-scaling-[project-name].md` → Component library integration, design system governance
  - `/decisions/learning-notes-scaling-[project-name].md` → Team architectural capabilities, coordination patterns
- **Distill into enterprise bullets** - each Executive Context item should capture enterprise complexity in 1-2 lines
- **Focus on enterprise-critical info** - microservices coordination, design system governance, compliance requirements

### Enterprise Context Reference Mapping (Priority 2)
- **Map complex enterprise needs** to exact document sections for just-in-time loading
- **Example**: "For microservice integration → `/srs/srs-scaling.md` REQ-PERF-001 to REQ-PERF-005, REQ-SCALE-001 to REQ-SCALE-010"
- **Be architecture-specific**: Service boundary decisions, component library governance sections, compliance requirement clusters

### Enterprise Task Context Embedding (Priority 3)
- **Each parent task gets enterprise context** - architecture pattern, performance targets, compliance requirements, team coordination
- **Each subtask gets specific context** - microservice pattern, design system component, security compliance, accessibility requirement
- **Balance enterprise complexity vs clarity** - enough context for enterprise implementation, minimal enterprise bloat

### Enterprise Context Management
- **Avoid enterprise context duplication** - reference don't repeat detailed architecture decisions
- **Use enterprise shorthand** - "microservice CQRS pattern", "design system governance process", "SOC2 compliance validation"
- **Flag high-complexity enterprise tasks** - when tasks need extensive architectural or compliance context

### Enterprise Technical Implementation Rules
- **Apply enterprise architecture decisions** to service boundaries, communication patterns, data flow
- **Honor design system governance** when structuring component tasks and design token usage
- **Include enterprise NFR validation** in acceptance criteria with specific enterprise metrics (99.9% uptime, <100ms response, GDPR compliance)
- **Reference architectural decision rationale** when explaining enterprise integration approaches
- **Require comprehensive test coverage** - unit, integration, performance, security, accessibility for enterprise quality
- **Validate design system compliance** for all component and interface tasks
- **Ensure enterprise traceability** from architectural decisions through implementation to validation
- **Include team coordination context** for cross-functional and multi-service integration
- Always include **comprehensive test sub-tasks** for each coding task (unit, integration, visual, accessibility, performance, security)
- Save enhanced task files in `/tasks/tasks-[feature-name]-scaling.md`
- Reference any existing MVP task files and build upon their foundation for enterprise evolution
Set reasoning_effort = high; enterprise tasks require comprehensive planning, architectural coordination, and multi-layered validation

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
