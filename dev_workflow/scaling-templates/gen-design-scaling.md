# Workflow: Design Analysis & Integration (Scaling)

## Objective
Perform comprehensive design analysis for scaling projects with focus on component library management, design system integration, and cross-project consistency. Prevents design debt accumulation and ensures maintainable component architecture.

## When to Use
- **Scaling Projects**: When transitioning from MVP to scaling workflow
- **Large Features**: Features with >5 parent tasks or complex UI requirements
- **Component Libraries**: When building or maintaining shared component systems
- **Multi-Team Projects**: When multiple developers will work on the same codebase
- **Design System Evolution**: When evolving or migrating design systems
- **Legacy Code Integration**: When integrating with existing large codebases

---

## Enhanced Workflow Steps

### 1. Comprehensive Codebase Analysis
- **Component Inventory**: Catalog all existing UI components with usage patterns
- **Pattern Analysis**: Identify design patterns, anti-patterns, and inconsistencies
- **Dependency Mapping**: Document component dependencies and relationships
- **Performance Analysis**: Assess component performance and bundle impact
- **Accessibility Audit**: Evaluate accessibility compliance across components
- **Design Token Usage**: Analyze design token consistency and coverage

### 2. Design System Integration Planning
- **Component Library Alignment**: Map existing components to design system standards
- **Token Migration**: Plan design token implementation and migration
- **Pattern Consolidation**: Identify opportunities to consolidate similar components
- **API Standardization**: Design consistent component APIs and props
- **Documentation Strategy**: Plan component documentation and examples
- **Versioning Strategy**: Design component versioning and deprecation processes

### 3. Scalability Design Decisions
- **Component Architecture**: Design for reusability, composability, and maintainability
- **State Management**: Plan component state management strategies
- **Performance Optimization**: Design for optimal rendering and bundle size
- **Testing Strategy**: Plan component testing approaches and coverage
- **Internationalization**: Design for multiple languages and locales
- **Theming Strategy**: Plan theme and brand customization approaches

### 4. Cross-Project Consistency
- **Style Guide Creation**: Establish comprehensive style guide standards
- **Component Governance**: Define component approval and review processes
- **Breaking Change Management**: Plan strategies for managing breaking changes
- **Migration Pathways**: Design clear migration paths for component updates
- **Quality Assurance**: Establish quality metrics and validation processes
- **Team Coordination**: Plan design review and collaboration processes

---

## Enhanced Output Format

```markdown
# Design Analysis (Scaling) - [Feature Name]

## Executive Summary
- **Component Count**: [total existing components]
- **Design Debt Score**: [low|medium|high] 
- **Recommended Actions**: [top 3 priority items]
- **Timeline Estimate**: [weeks for implementation]

## Component Inventory
### Existing Components
- **ComponentName**: 
  - **Location**: [file path]
  - **Usage**: [X instances across Y files]
  - **Props API**: [prop count and complexity]
  - **Dependencies**: [component dependencies]
  - **Performance**: [bundle size, render complexity]
  - **Accessibility**: [compliance level]
  - **Design System Alignment**: [aligned|needs-migration|deprecated]

### Component Categories
- **Foundational**: [buttons, inputs, layout components]
- **Composite**: [forms, cards, complex interactions]
- **Page-Level**: [headers, footers, navigation]
- **Utility**: [helpers, wrappers, providers]

## Design System Integration

### Design Token Analysis
- **Colors**: [token coverage and consistency]
- **Typography**: [font usage and hierarchy]
- **Spacing**: [spacing system adherence]
- **Elevation**: [shadow and layering consistency]
- **Motion**: [animation and transition patterns]

### Component Mapping
| Existing Component | Design System Equivalent | Migration Action |
|-------------------|--------------------------|------------------|
| CustomButton | Button | Migrate props, update usage |
| SearchInput | Input[type=search] | Consolidate with Input |
| UserCard | Card + Avatar | Refactor composition |

### Integration Strategy
- **Primary Approach**: [migrate-in-place|create-parallel|hybrid]
- **Timeline**: [migration phases and deadlines]
- **Breaking Changes**: [list of breaking changes needed]
- **Backward Compatibility**: [compatibility strategy]

## Scalability Recommendations

### Architecture Decisions
- **Component Structure**: [atomic design|feature-based|hybrid]
- **State Management**: [local|context|external store]
- **Styling Approach**: [CSS modules|styled-components|CSS-in-JS]
- **Bundle Strategy**: [monolithic|code-splitting|micro-frontends]

### Performance Optimizations
- **Lazy Loading**: [components suitable for lazy loading]
- **Code Splitting**: [split points and bundle analysis]
- **Memoization**: [components needing React.memo or useMemo]
- **Bundle Analysis**: [current bundle size and optimization opportunities]

### Testing Strategy
- **Unit Testing**: [component testing coverage and tools]
- **Integration Testing**: [component interaction testing]
- **Visual Testing**: [screenshot testing and visual regression]
- **Accessibility Testing**: [automated and manual accessibility testing]

## Cross-Project Consistency

### Style Guide Standards
- **Component API Guidelines**: [prop naming, event handling patterns]
- **Documentation Standards**: [required documentation for each component]
- **Code Quality Standards**: [TypeScript usage, testing requirements]
- **Accessibility Standards**: [WCAG compliance requirements]

### Governance Process
- **Component Review Process**: [design review, code review, testing requirements]
- **Approval Workflow**: [who approves new components and changes]
- **Breaking Change Process**: [how to introduce and communicate breaking changes]
- **Deprecation Process**: [timeline and communication for deprecating components]

## Implementation Guidance

### Migration Plan
- **Phase 1**: [foundational components and design tokens]
- **Phase 2**: [composite components and patterns]
- **Phase 3**: [page-level components and optimization]
- **Phase 4**: [cleanup and documentation]

### Development Guidelines
- **Component Creation**: [when to create new vs. extend existing]
- **Prop Design**: [prop naming conventions and patterns]
- **State Management**: [when to use local vs. global state]
- **Performance Considerations**: [optimization guidelines and metrics]

### Quality Assurance
- **Testing Requirements**: [minimum test coverage and types]
- **Documentation Requirements**: [required documentation sections]
- **Performance Benchmarks**: [performance targets and monitoring]
- **Accessibility Requirements**: [compliance checklist and testing]

## Risk Assessment

### High-Risk Areas
- **Component**: [component name] - **Risk**: [specific risk] - **Mitigation**: [mitigation strategy]
- **Migration**: [migration risk] - **Impact**: [user/business impact] - **Mitigation**: [fallback plan]

### Technical Debt
- **Design Debt Score**: [calculated score based on inconsistencies]
- **Priority Issues**: [top issues requiring immediate attention]
- **Long-term Issues**: [issues that can be addressed over time]

## Inconsistency Detection & Recovery

### Duplicate Components Identified
- **Similar Components**: [list of components serving similar purposes]
- **Consolidation Opportunities**: [specific consolidation recommendations]
- **Migration Strategy**: [how to consolidate without breaking existing usage]

### Pattern Inconsistencies
- **Inconsistent Patterns**: [patterns that differ across components]
- **Standardization Recommendations**: [how to standardize patterns]
- **Impact Assessment**: [effort required for standardization]

### Recovery Recommendations
- **Immediate Actions**: [critical issues requiring immediate attention]
- **Suggested Recovery Workflow**: [run gen-design-recovery-scaling.md if needed]
- **Timeline**: [recommended timeline for recovery actions]
```

---

## AI Agent Directives
- Always perform comprehensive component analysis before scaling implementation
- Enforce design system compliance for all new and modified components
- Flag any duplicate or inconsistent components for consolidation
- Validate component APIs follow established patterns and conventions
- Ensure accessibility compliance is maintained throughout scaling
- Save comprehensive design analysis to `/design/design-[feature-name]-scaling.md`
- Reference design system documentation and enforce compliance
Set reasoning_effort = high; thorough analysis critical for scaling success

---

## Human Review Gate (Required)
- Confirm: component inventory complete and accurate
- Confirm: design system integration strategy approved
- Confirm: migration timeline and breaking changes acceptable
- Confirm: performance and accessibility requirements met
- Confirm: governance and quality processes established
- Confirm: risk assessment and mitigation strategies approved
- Approve proceeding to implementation with design guidance

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "design_scaling",
  "feature_slug": "[feature-name]",
  "design_path": "/design/design-[feature-name]-scaling.md",
  "component_inventory": {
    "total_components": 0,
    "foundational": 0,
    "composite": 0,
    "page_level": 0,
    "utility": 0
  },
  "design_system_integration": {
    "token_coverage": "0%",
    "component_alignment": "0%",
    "migration_required": true
  },
  "design_debt_score": "low|medium|high",
  "inconsistencies_found": ["..."],
  "recovery_recommended": true|false,
  "performance_issues": ["..."],
  "accessibility_issues": ["..."]
}
```

### Context Seed (for next stage)
Provide this block to the next stage:

```json
{
  "feature_slug": "[feature-name]",
  "design_path": "/design/design-[feature-name]-scaling.md",
  "design_system_ready": true|false,
  "component_library_required": true|false,
  "recovery_required": true|false
}
```

---

## Human-in-the-Loop Rule
Pause for explicit approval before:
- Implementing breaking changes to component APIs
- Deprecating widely-used components
- Making design system architecture decisions
- Otherwise proceed autonomously for analysis and documentation

---

## Integration with MVP Workflow
This scaling design analysis builds upon and enhances the MVP design analysis:
- Preserves all component decisions from MVP workflow
- Extends component analysis for larger scale requirements
- Maintains backward compatibility with MVP design artifacts
- Provides upgrade path from MVP design context to scaling design system

---

## Start Here
Run this analysis after completing MVP-to-scaling transition or when beginning any scaling project. Ensure design system foundation is established before proceeding to task generation.
