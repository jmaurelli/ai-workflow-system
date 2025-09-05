# Workflow: Design System Creation & Management (Scaling)

## Objective
Create, maintain, and evolve design systems for scaling projects. Establish component libraries, design tokens, and governance processes that prevent design inconsistencies while enabling rapid development and consistent user experiences.

## When to Use
- **Design System Creation**: When establishing a new design system from existing components
- **Component Library Management**: When formalizing component reuse patterns
- **Cross-Team Coordination**: When multiple developers need shared design standards
- **Brand Evolution**: When updating or extending brand guidelines and design language
- **Design Debt Resolution**: When consolidating inconsistent design patterns
- **Platform Scaling**: When scaling across multiple products or platforms

---

## Design System Creation Workflow

### 1. Foundation Establishment
- **Design Token Definition**: Define foundational design tokens (colors, typography, spacing, etc.)
- **Component Hierarchy**: Establish component categorization and relationships
- **Brand Guidelines**: Document brand standards, voice, and visual identity
- **Accessibility Standards**: Define accessibility requirements and compliance levels
- **Browser Support**: Establish browser support matrix and testing requirements
- **Performance Budgets**: Define performance standards for components and systems

### 2. Component Library Architecture
- **Atomic Design Implementation**: Organize components using atomic design principles
- **Component API Design**: Establish consistent prop naming and behavior patterns
- **Composition Patterns**: Define how components should compose and interact
- **State Management**: Plan component state management and data flow patterns
- **Error Handling**: Establish error states and error handling patterns
- **Loading States**: Define loading patterns and skeleton implementations

### 3. Documentation & Governance
- **Component Documentation**: Create comprehensive component documentation with examples
- **Usage Guidelines**: Establish when and how to use each component
- **Contribution Guidelines**: Define processes for adding and modifying components
- **Review Processes**: Establish design and code review requirements
- **Versioning Strategy**: Define component versioning and release processes
- **Breaking Change Management**: Plan strategies for managing breaking changes

### 4. Quality Assurance & Testing
- **Testing Strategy**: Establish unit, integration, and visual testing approaches
- **Quality Metrics**: Define quality gates and success criteria
- **Performance Monitoring**: Implement performance tracking and optimization
- **Accessibility Testing**: Establish automated and manual accessibility testing
- **Cross-Browser Testing**: Define browser testing matrix and processes
- **Regression Testing**: Implement visual regression and behavior testing

---

## Design System Output Format

```markdown
# Design System Specification - [Project Name]

## Executive Summary
- **Purpose**: [design system objectives and scope]
- **Target Audience**: [developers, designers, stakeholders using the system]
- **Timeline**: [implementation and adoption timeline]
- **Success Metrics**: [how success will be measured]

## Design Foundations

### Design Tokens
```json
{
  "colors": {
    "primary": {
      "50": "#f0f9ff",
      "500": "#3b82f6",
      "900": "#1e3a8a"
    },
    "semantic": {
      "success": "#10b981",
      "warning": "#f59e0b",
      "error": "#ef4444",
      "info": "#3b82f6"
    }
  },
  "typography": {
    "fontFamily": {
      "sans": ["Inter", "system-ui", "sans-serif"],
      "mono": ["JetBrains Mono", "monospace"]
    },
    "fontSize": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "base": "1rem",
      "lg": "1.125rem",
      "xl": "1.25rem"
    }
  },
  "spacing": {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem"
  }
}
```

### Brand Guidelines
- **Visual Identity**: [logo usage, color usage, imagery guidelines]
- **Voice & Tone**: [writing style, messaging guidelines]
- **Accessibility**: [WCAG compliance level, inclusive design principles]
- **Performance**: [load time targets, bundle size limits]

## Component Library

### Component Hierarchy
```
Atoms (Foundational)
├── Button
├── Input
├── Text
├── Icon
└── Spacer

Molecules (Composite)
├── SearchInput (Input + Icon + Button)
├── FormField (Text + Input + ValidationMessage)
├── Card (Container + Text + Actions)
└── Navigation Item (Icon + Text + Badge)

Organisms (Complex)
├── Header (Navigation + Search + UserMenu)
├── DataTable (Headers + Rows + Pagination)
├── Form (FormFields + Validation + Submit)
└── Modal (Overlay + Header + Content + Actions)

Templates (Layout)
├── PageLayout (Header + Content + Footer)
├── DashboardLayout (Sidebar + Content + Toolbar)
└── AuthLayout (Centered + Branding + Form)
```

### Component Specifications

#### [ComponentName] Component
- **Purpose**: [what problem this component solves]
- **Usage**: [when and how to use this component]
- **API**: 
  ```typescript
  interface ComponentProps {
    variant?: 'primary' | 'secondary' | 'tertiary';
    size?: 'sm' | 'md' | 'lg';
    disabled?: boolean;
    children: React.ReactNode;
    onClick?: (event: MouseEvent) => void;
  }
  ```
- **States**: [default, hover, active, disabled, loading]
- **Accessibility**: [ARIA labels, keyboard navigation, screen reader support]
- **Examples**:
  ```jsx
  // Basic usage
  <Button variant="primary" size="md">
    Click me
  </Button>
  
  // With icon
  <Button variant="secondary" size="lg">
    <Icon name="download" />
    Download File
  </Button>
  ```

## Implementation Guidelines

### Development Standards
- **TypeScript Usage**: [strict typing requirements and patterns]
- **Testing Requirements**: [minimum test coverage and testing approaches]
- **Documentation Standards**: [required documentation for each component]
- **Performance Standards**: [bundle size limits, rendering performance]
- **Accessibility Requirements**: [compliance checklist and testing]

### Component Creation Process
1. **Design Review**: [design approval process and stakeholders]
2. **API Design**: [prop design and component interface planning]
3. **Implementation**: [coding standards and implementation guidelines]
4. **Testing**: [required testing approaches and coverage]
5. **Documentation**: [documentation requirements and examples]
6. **Review**: [code review process and approval requirements]

### Migration & Adoption
- **Migration Strategy**: [how to migrate from existing components]
- **Adoption Timeline**: [rollout plan and milestones]
- **Training Plan**: [team education and onboarding]
- **Support Process**: [how to get help and report issues]

## Governance & Maintenance

### Design System Team
- **Maintainers**: [who maintains the design system]
- **Contributors**: [who can contribute to the design system]
- **Stakeholders**: [who has input on design system decisions]
- **Decision Making**: [how design system decisions are made]

### Process & Workflows
- **RFC Process**: [how to propose new components or changes]
- **Review Process**: [design and code review requirements]
- **Release Process**: [how changes are released and communicated]
- **Support Process**: [how users get help and report issues]

### Quality Assurance
- **Testing Strategy**: [automated testing approaches and requirements]
- **Quality Gates**: [quality requirements and validation]
- **Performance Monitoring**: [performance tracking and optimization]
- **User Feedback**: [how user feedback is collected and addressed]

## Versioning & Evolution

### Versioning Strategy
- **Semantic Versioning**: [how versions are incremented]
- **Breaking Changes**: [how breaking changes are managed]
- **Deprecation Process**: [timeline and communication for deprecations]
- **Migration Support**: [tools and documentation for migrations]

### Evolution Planning
- **Roadmap**: [planned features and improvements]
- **Research & Innovation**: [how new patterns are researched and validated]
- **Community Input**: [how community feedback influences evolution]
- **Platform Expansion**: [plans for supporting additional platforms]

## Tools & Infrastructure

### Development Tools
- **Build System**: [build tools and configuration]
- **Testing Tools**: [testing frameworks and tools]
- **Documentation Tools**: [documentation generation and hosting]
- **Design Tools**: [design tool integration and workflows]

### Distribution & Consumption
- **Package Management**: [how components are packaged and distributed]
- **CDN Strategy**: [content delivery and caching strategy]
- **Installation Guide**: [how to install and configure the design system]
- **Update Strategy**: [how users stay updated with new versions]
```

---

## AI Agent Directives
- Always establish comprehensive design tokens before creating components
- Enforce consistent component API patterns across all components
- Validate accessibility compliance for all design system components
- Create comprehensive documentation with interactive examples
- Establish clear governance processes for design system evolution
- Save design system specification to `/design/design-system-[project-name].md`
- Maintain backward compatibility when evolving design system
Set reasoning_effort = high; design system decisions impact entire project

---

## Human Review Gate (Required)
- Confirm: design token system complete and brand-aligned
- Confirm: component hierarchy logical and comprehensive
- Confirm: governance processes practical and sustainable
- Confirm: accessibility standards meet compliance requirements
- Confirm: performance budgets realistic and measurable
- Confirm: migration strategy feasible and timeline realistic
- Approve proceeding with design system implementation

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "design_system",
  "project_name": "[project-name]",
  "design_system_path": "/design/design-system-[project-name].md",
  "design_tokens": {
    "colors_defined": true,
    "typography_defined": true,
    "spacing_defined": true,
    "elevation_defined": true
  },
  "component_library": {
    "atoms_count": 0,
    "molecules_count": 0,
    "organisms_count": 0,
    "templates_count": 0
  },
  "governance": {
    "processes_defined": true,
    "team_roles_defined": true,
    "quality_gates_defined": true
  },
  "implementation_ready": true|false
}
```

### Context Seed (for implementation)
Provide this block to development workflow:

```json
{
  "project_name": "[project-name]",
  "design_system_path": "/design/design-system-[project-name].md",
  "design_system_ready": true,
  "token_system_defined": true,
  "component_library_specified": true
}
```

---

## Human-in-the-Loop Rule
Pause for explicit approval before:
- Finalizing design token values and naming conventions
- Establishing component API patterns that will affect all components
- Making architectural decisions about component composition
- Defining governance processes that affect team workflows
- Otherwise proceed autonomously for documentation and specification

---

## Integration with Scaling Workflow
This design system workflow integrates with other scaling documents:
- Builds upon analysis from `gen-design-scaling.md`
- Provides foundation for `gen-design-recovery-scaling.md`
- Informs component standards for `create-prd-scaling.md`
- Establishes quality standards for `tasks-and-testing-scaling.md`

---

## Success Criteria
- [ ] Comprehensive design token system established
- [ ] Complete component hierarchy documented
- [ ] All components have clear APIs and documentation
- [ ] Governance processes defined and adopted
- [ ] Quality assurance processes implemented
- [ ] Migration strategy documented and validated
- [ ] Team training completed and support processes established

---

## Start Here
Use this workflow when establishing a design system for scaling projects or when formalizing design standards from MVP projects. Ensure design analysis is complete before beginning design system creation.
