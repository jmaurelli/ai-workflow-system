# Workflow: MVP to Scaling Transition - Step s01 (Transition Phase)

## Objective
Provide clear guidance for transitioning from MVP workflow to scaling workflow while preserving design-aware enhancements and maintaining project continuity. Ensure component reuse knowledge and design decisions transfer seamlessly.

## 🏢 Enterprise Automation Support
This document supports **three enterprise automation modes** for AI agents:

### **🚦 Enterprise Automation Modes**
- **🚪 GUIDED Mode**: Maximum enterprise oversight - traditional workflow with governance gates
- **⚡ AUTONOMOUS Mode**: Balanced enterprise oversight - AI agent proceeds automatically with enterprise safety checks  
- **🧠 LEARNING Mode**: Adaptive enterprise oversight - learns from approval patterns and enterprise governance requirements

### **🚀 Automated Enterprise Execution**
Use the enterprise workflow orchestrators to run the complete scaling sequence automatically:

```bash
# Traditional enterprise shell orchestrator
./enterprise-workflow-orchestrator.sh --mode=guided --feature=user-service

# Intelligent enterprise Python orchestrator  
./enterprise-ai-workflow-runner.py --mode=autonomous --feature=api-gateway

# Compliance-aware enterprise workflow
./enterprise-ai-workflow-runner.py --mode=autonomous --feature=payment-system \
    --compliance=GDPR --multi-team --architecture-impact

# See enterprise execution plan without running
./enterprise-ai-workflow-runner.py --mode=learning --feature=microservice --dry-run
```

See `workflow-sequence-guide.md` and `enterprise-automation-quickstart.md` for complete automation details.

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

### Phase 1: Assessment & Planning (Enterprise Feature-Centric)

1. **Initialize Enterprise Feature Directory**
   - Create date-prefixed enterprise feature directory: `/enterprise-features/[YYYY-MM-DD]-[project-name]/` (auto-generate date from OS, convert `[project-name]` to kebab-case)
   - Initialize `feature-manifest.json` with enterprise workflow tracking and multi-team coordination metadata
   - Setup enterprise directory structure with comprehensive `artifacts/` subdirectories for enterprise-grade content
   - Migrate relevant MVP artifacts and documentation to enterprise feature directory

2. **Design Analysis Audit**
   - Run `gen-design-recovery.md` on entire codebase
   - Document all existing components and patterns
   - Identify design debt and inconsistencies
   - Create component inventory
   - Save results to `./design-analysis.md` within enterprise feature directory

3. **Enterprise Design Decisions (Learning-Guided)**
   - Run `gen-design-decisions-scaling.md` to make informed enterprise-level decisions
   - **System Architecture**: Choose microservices strategy, database scaling, distributed system patterns
   - **Design System Strategy**: Plan enterprise component library, design token architecture, governance model
   - **Technology Evolution**: Plan migration paths from MVP stack to enterprise technologies
   - **UX Architecture**: Design complex user experiences, personalization, and accessibility strategies
   - **API Strategy**: Plan enterprise API architecture, integration patterns, security approach
   - Generate `./design-decisions-scaling.md` with comprehensive rationale within enterprise feature directory
   - **Human Gate**: Review and approve enterprise architecture and design system strategy

4. **Enterprise SRS (Mandatory - Quality Foundation)**
   - Run `gen-srs-scaling.md` to capture comprehensive enterprise NFRs
   - **Performance Requirements**: Response time budgets, throughput, scalability targets
   - **Security Specifications**: Enterprise security, compliance requirements, data protection
   - **Availability Standards**: Uptime targets, fault tolerance, disaster recovery
   - **Integration Constraints**: API performance, external system requirements
   - Generate `./srs.md` with measurable enterprise quality constraints within enterprise feature directory
   - **Human Gate**: Review and approve enterprise performance budgets and compliance requirements

5. **Artifact Upgrade Planning**
   - Map MVP artifacts to scaling equivalents based on design decisions and SRS requirements
   - Plan document enhancement timeline within enterprise feature directory structure
   - Identify missing documentation gaps and enterprise artifact requirements
   - Assess testing coverage and quality for enterprise compliance

6. **Risk Assessment**
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

## Enterprise Feature Directory Initialization Protocol

### **Automatic Enterprise Directory Creation**
```bash
# Auto-generate enterprise feature directory with OS timestamp
FEATURE_DATE=$(date +"%Y-%m-%d")
FEATURE_SLUG="[convert-project-name-to-kebab-case]"  
ENTERPRISE_FEATURE_DIR="/enterprise-features/${FEATURE_DATE}-${FEATURE_SLUG}"

# Create comprehensive enterprise directory structure
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/architecture-diagrams"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/api-contracts"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/design-system"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/performance-reports"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/security-audits"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/integration-tests"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/deployment-configs"
mkdir -p "${ENTERPRISE_FEATURE_DIR}/artifacts/monitoring-dashboards"

# Initialize enterprise feature manifest
cat > "${ENTERPRISE_FEATURE_DIR}/feature-manifest.json" << 'EOF'
{
  "feature_metadata": {
    "feature_name": "[Collected Project Name]",
    "feature_slug": "[kebab-case-slug]",
    "feature_directory": "[YYYY-MM-DD]-[kebab-case-slug]",
    "creation_date": "[ISO-8601-timestamp]",
    "creator": "scaling-transition-workflow",
    "project_context": "[Enterprise project context]",
    "enterprise_scope": "cross_team_coordination",
    "transition_from_mvp": true
  },
  "workflow_status": {
    "current_phase": "transition_initialization",
    "phases_completed": [],
    "phases_remaining": ["assessment", "foundation_enhancement", "implementation", "completion_summary"],
    "estimated_completion": null,
    "last_updated": "[ISO-8601-timestamp]"
  },
  "multi_team_coordination": {
    "coordination_mode": "enterprise_multi_team",
    "team_assignments": {},
    "coordination_lead": "to_be_determined",
    "review_board": [],
    "approval_gates": ["architecture_review", "security_review", "design_system_compliance"]
  },
  "enterprise_context": {
    "architecture_tier": "enterprise_distributed",
    "compliance_requirements": [],
    "performance_tier": "enterprise_scale",
    "integration_complexity": "high_cross_service"
  },
  "document_status": {
    "prd": {"status": "pending", "path": "./prd.md"},
    "srs": {"status": "pending", "path": "./srs.md"},
    "design_decisions_scaling": {"status": "pending", "path": "./design-decisions-scaling.md"},
    "design_analysis": {"status": "pending", "path": "./design-analysis.md"},
    "design_system_governance": {"status": "pending", "path": "./design-system-governance.md"},
    "tasks": {"status": "pending", "path": "./tasks.md"},
    "learning_notes_scaling": {"status": "pending", "path": "./learning-notes-scaling.md"},
    "completion_summary": {"status": "pending", "path": "./completion-summary.md"}
  }
}
EOF

# Set working directory for all subsequent scaling workflow steps
cd "${ENTERPRISE_FEATURE_DIR}"
```

### **MVP to Enterprise Migration Protocol**
```bash
# Migrate relevant MVP artifacts to enterprise feature directory
if [[ -d "/features/" ]]; then
  echo "Migrating relevant MVP artifacts to enterprise structure..."
  
  # Copy relevant MVP documents and enhance for enterprise
  find /features -name "*.md" -type f | while read mvp_file; do
    # Logic to determine relevance and copy/enhance for enterprise use
    # This preserves MVP learning while evolving to enterprise complexity
  done
fi
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
