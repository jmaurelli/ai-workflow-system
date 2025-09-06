# Workflow: MVP to Scaling Transition (Design-Aware)

## Objective
Provide clear guidance for transitioning from MVP workflow to scaling workflow while preserving design-aware enhancements and maintaining project continuity. Ensure component reuse knowledge and design decisions transfer seamlessly.

## When to Transition to Scaling

### Trigger Criteria
- **Team Growth**: Planning to add developers or collaborators
- **Feature Complexity**: Features require more than 5 parent tasks
- **Design Debt**: Component inconsistencies detected by recovery workflow
- **Performance Requirements**: NFRs become critical to user experience
- **Long-term Maintenance**: Project expected to live beyond 6 months
- **External Dependencies**: Integration with multiple external systems

### Project Maturity Indicators
- **Codebase Size**: >10k lines of code or >50 components
- **User Base**: >100 active users or production traffic
- **Business Impact**: Revenue generating or business critical
- **Compliance**: Security, accessibility, or regulatory requirements

---

## Transition Workflow

### Phase 1: Assessment & Planning
1. **Design Analysis Audit**
   - Run `gen-design-recovery.md` on entire codebase
   - Document all existing components and patterns
   - Identify design debt and inconsistencies
   - Create component inventory

2. **Enterprise Design Decisions (Learning-Guided)**
   - Run `gen-design-decisions-scaling.md` to make informed enterprise-level decisions
   - **System Architecture**: Choose microservices strategy, database scaling, distributed system patterns
   - **Design System Strategy**: Plan enterprise component library, design token architecture, governance model
   - **Technology Evolution**: Plan migration paths from MVP stack to enterprise technologies
   - **UX Architecture**: Design complex user experiences, personalization, and accessibility strategies
   - **API Strategy**: Plan enterprise API architecture, integration patterns, security approach
   - Generate `/decisions/design-decisions-scaling-[project-name].md` with comprehensive rationale
   - **Human Gate**: Review and approve enterprise architecture and design system strategy

3. **Enterprise SRS (Mandatory - Quality Foundation)**
   - Run `gen-srs-scaling.md` to capture comprehensive enterprise NFRs
   - **Performance Requirements**: Response time budgets, throughput, scalability targets
   - **Security Specifications**: Enterprise security, compliance requirements, data protection
   - **Availability Standards**: Uptime targets, fault tolerance, disaster recovery
   - **Integration Constraints**: API performance, external system requirements
   - Generate `/srs/srs-scaling-[project-name].md` with measurable enterprise quality constraints
   - **Human Gate**: Review and approve enterprise performance budgets and compliance requirements

4. **Artifact Upgrade Planning**
   - Map MVP artifacts to scaling equivalents based on design decisions and SRS requirements
   - Plan document enhancement timeline
   - Identify missing documentation gaps
   - Assess testing coverage and quality

5. **Risk Assessment**
   - Evaluate breaking changes needed for chosen architecture
   - Plan migration strategies for existing code to new tech stack
   - Identify user impact and mitigation
   - Create rollback procedures

### Phase 2: Foundation Enhancement (Design-Decision Driven)
1. **Design System Creation**
   - Run `gen-design-system-scaling.md` using chosen design system strategy
   - Establish component library based on design decisions
   - Create design tokens and standards matching chosen architecture
   - Document pattern guidelines following enterprise design decisions

2. **Architecture Documentation**
   - Upgrade lean architecture to full architecture docs using chosen system architecture
   - Document scaling considerations based on enterprise decisions
   - Plan performance and monitoring for chosen technology stack
   - Create deployment strategies matching chosen API and integration patterns

3. **Testing Enhancement**
   - Upgrade smoke tests to full test suites
   - Implement test coverage requirements
   - Create testing infrastructure
   - Establish quality gates

### Phase 3: Workflow Integration
1. **Process Enhancement**
   - Implement scaling workflow for new features
   - Train team on enhanced processes
   - Create review and approval gates
   - Establish metrics and monitoring

2. **Documentation Transition**
   - Upgrade all MVP documents to scaling equivalents
   - Maintain backward compatibility
   - Create migration timeline
   - Update project manifest

---

## Artifact Upgrade Matrix

| MVP Document | Scaling Equivalent | Upgrade Actions |
|--------------|-------------------|-----------------|
| `/prd/prd-[feature].md` | `/prd/prd-[feature]-scaling.md` | Add user personas, detailed NFRs, risk matrix |
| `/design/design-[feature].md` | `/design/design-[feature]-scaling.md` | Add component library integration, design system compliance |
| `/tasks/tasks-[feature].md` | `/tasks/tasks-[feature]-scaling.md` | Add detailed TDD, coverage requirements, deployment tasks |
| `/test/[results].json` | `/tests/results/[feature]-[version].json` | Add coverage metrics, performance benchmarks, audit trails |

---

## Design-Aware Transition Specifics

### Component Library Migration
1. **Inventory Existing Components**
   - Scan codebase for all UI components
   - Document usage patterns and dependencies
   - Identify duplicates and inconsistencies
   - Create component categorization

2. **Design System Integration**
   - Establish design tokens (colors, typography, spacing)
   - Create component API standards
   - Document accessibility requirements
   - Plan component deprecation strategies

3. **Pattern Consolidation**
   - Merge duplicate components (your button/search issue)
   - Establish single source of truth for patterns
   - Create component variation guidelines
   - Document breaking change procedures

### Context Continuity Enhancement
```json
// Enhanced context for scaling transition
{
  "transition_stage": "assessment|foundation|integration|complete",
  "mvp_artifacts": {
    "prd_paths": ["/prd/prd-*.md"],
    "design_paths": ["/design/design-*.md"],
    "task_paths": ["/tasks/tasks-*.md"]
  },
  "scaling_artifacts": {
    "design_system_path": "/design/design-system.md",
    "component_library_path": "/design/components/",
    "architecture_path": "/docs/architecture-scaling.md"
  },
  "component_inventory": {
    "total_components": 45,
    "duplicates_found": 8,
    "patterns_identified": 12,
    "design_debt_score": "medium"
  },
  "transition_metrics": {
    "test_coverage": "85%",
    "documentation_completeness": "90%",
    "design_consistency": "75%"
  }
}
```

---

## AI Agent Directives
- Always run design analysis before any scaling transition
- Preserve all MVP design context and decisions in scaling artifacts
- Enforce component library standards from transition forward
- Validate design system compliance for all new components
- Maintain traceability from MVP artifacts to scaling artifacts
Set reasoning_effort = high; comprehensive analysis for scaling decisions

---

## Human Review Gate (Required)
- Confirm: transition criteria met and documented
- Confirm: component inventory complete and design debt assessed
- Confirm: enterprise design decisions comprehensive and well-reasoned
- Confirm: system architecture choices align with business goals and team capabilities
- Confirm: design system strategy supports organizational scale and team structure
- Confirm: technology evolution path realistic given current capabilities and timeline
- Confirm: artifact upgrade plan reviewed and timeline approved
- Confirm: team capacity and training plan for scaling workflow and chosen technologies
- Confirm: risk mitigation strategies and rollback procedures for architectural changes
- Approve proceeding with scaling workflow implementation

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "scaling_transition",
  "project_name": "[project-name]",
  "transition_phase": "assessment|foundation|integration|complete",
  "mvp_artifacts": ["..."],
  "scaling_artifacts": ["..."],
  "component_inventory": {
    "total": 0,
    "duplicates": 0,
    "patterns": 0
  },
  "design_debt_score": "low|medium|high",
  "transition_timeline": "[weeks]",
  "risk_level": "low|medium|high"
}
```

### Artifact Manifest Update
- Create `/artifacts/scaling-manifest.json` with enhanced tracking
- Maintain backward compatibility with MVP manifest
- Track both MVP and scaling artifact relationships

### Context Seed (for scaling workflow)
Provide this block to scaling workflow documents:

```json
{
  "project_name": "[project-name]",
  "transition_complete": true,
  "mvp_foundation": {
    "design_context_preserved": true,
    "component_inventory_complete": true,
    "design_debt_assessed": true
  },
  "scaling_ready": true
}
```

---

## Human-in-the-Loop Rule
Pause for explicit approval before:
- Making breaking changes to existing components
- Implementing component deprecation strategies
- Transitioning team workflows
- Otherwise proceed autonomously for documentation and analysis

---

## Success Criteria
- [ ] All MVP artifacts successfully mapped to scaling equivalents
- [ ] Component inventory complete with zero duplicates
- [ ] Design system foundation established
- [ ] Team trained on scaling workflow
- [ ] Quality gates and metrics established
- [ ] Documentation migration complete
- [ ] Backward compatibility maintained

---

## Start Here
This document should be used when MVP projects meet transition criteria. Follow the three-phase approach and ensure design-aware principles are maintained throughout the scaling process.
