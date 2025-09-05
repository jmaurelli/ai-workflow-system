# Enhanced Scaling Workflow Cheat Sheet (Design-Aware)

## 🛠️ Goal
Scale from MVP to production-ready development with **design consistency**, **higher rigor**, and **quality**.  
Ensure documentation, testing, and design systems are thorough enough for scaling and long-term maintainability while preventing design debt accumulation.

---

## Enhanced Workflow Overview

### Phase 1: MVP-to-Scaling Transition
0. **MVP Assessment → Scaling Readiness**
   - Use `mvp-to-scaling-transition.md`
   - Assess component inventory and design debt
   - Plan transition strategy and timeline

### Phase 2: Design-Aware Development
1. **Idea → Full PRD (Design-Aware)**  
   - Use `create-prd-scaling.md`  
   - Include comprehensive design context and component analysis
   - Generate complete PRD with design system integration requirements

2. **PRD → Design Analysis**
   - Use `gen-design-scaling.md`
   - Comprehensive component inventory and design system analysis
   - Identify reuse opportunities and consistency requirements

3. **Design System Foundation** (if needed)
   - Use `gen-design-system-scaling.md`
   - Establish design tokens, component library, and governance
   - Create comprehensive design standards and documentation

4. **Design Recovery** (if needed)
   - Use `gen-design-recovery-scaling.md`
   - Address design inconsistencies and component duplication
   - Implement systematic consolidation and cleanup

### Phase 3: Implementation with Design Compliance
5. **Design Analysis → Detailed Tasks + TDD**  
   - Use `tasks-and-testing-scaling.md`  
   - Each coding task includes design system compliance validation
   - Comprehensive testing (unit, integration, visual, accessibility)
   - Tests written **before code** with design validation

6. **Tasks → Code (Design System Compliant)**  
   - Follow strict TDD with design system validation
   - Refactor for design consistency and performance
   - Maintain links: PRD → Design → Tasks → Tests → Components

### Phase 4: Quality Assurance & Deployment
7. **Comprehensive Testing**
   - Use `test-suite-scaling.md`
   - Include design system compliance, accessibility, and performance testing
   - Visual regression testing and component validation

8. **Deploy with Monitoring**  
   - Use `project-templates-scaling.md` → Full Deployment Plan
   - Monitor design consistency, performance, and accessibility
   - Define rollback, monitoring, and design system metrics

9. **Maintain + Monitor + Evolve**  
   - Record comprehensive results including design system compliance
   - Track design debt and component consistency over time
   - Evolve design system based on usage patterns and feedback

---

## Enhanced Document Roles (Design-Aware)

### Transition & Foundation
- `mvp-to-scaling-transition.md` → Assess and plan transition from MVP to scaling workflow
- `gen-design-scaling.md` → Comprehensive design analysis and component inventory
- `gen-design-system-scaling.md` → Design system creation and governance
- `gen-design-recovery-scaling.md` → Design debt resolution and component consolidation

### Core Workflow Documents  
- `create-prd-scaling.md` → Full PRD with comprehensive design context
- `tasks-and-testing-scaling.md` → Tasks with design system compliance and comprehensive TDD
- `tdd-with-design-scaling.md` → Strict TDD with design system validation
- `test-suite-scaling.md` → Enhanced schema with design compliance and accessibility metrics

### Supporting Templates
- `project-templates-scaling.md` → Full templates for architecture, deployment, monitoring
- `software-project-workflow-guide-scaling.md` → Defines strict workflow for scaling
- `scaling-workflow-diagram.md` → Visual workflow representation

---

## Enhanced AI Agent Rules (Scaling Mode)
- Always generate **Full versions** of documents with comprehensive design analysis
- **Design System First**: Validate design system compliance before implementation
- **Accessibility Mandatory**: Ensure WCAG 2.1 AA compliance for all components
- **Performance Monitoring**: Track bundle size and render performance continuously
- **Component Reuse**: Prioritize existing component reuse over new component creation
- Link every task → design compliance → test → PRD requirement
- Reject incomplete test results or design system violations
- Expand documentation without compression while maintaining design consistency

---

## Enhanced Example Flow (Design-Aware)
1. **Transition Assessment** → Run `mvp-to-scaling-transition.md` assessment
2. **Feature Capture** → Full PRD with design context (`prd-user-login-scaling.md`)
3. **Design Analysis** → Component analysis (`design-user-login-scaling.md`)
4. **Design System** → Establish/update design system if needed
5. **Design Recovery** → Address any inconsistencies found
6. **Detailed Tasks** → Generate tasks with design compliance (`tasks-user-login-scaling.md`)
7. **Implementation** → Strict TDD with design system validation
8. **Comprehensive Testing** → Unit, integration, visual, accessibility testing
9. **Deploy** → With design system monitoring and rollback plan
10. **Monitor & Evolve** → Track design debt and component usage patterns

---

## Design-Aware Success Metrics
- **Component Reuse Rate**: >80% of UI elements use existing design system components
- **Design Consistency Score**: >95% compliance with design token usage
- **Accessibility Compliance**: 100% WCAG 2.1 AA compliance
- **Performance Benchmarks**: Bundle size and render time within established budgets
- **Design Debt Score**: Low design debt with systematic reduction over time
- **Test Coverage**: >90% unit, >80% integration, 100% accessibility coverage

---

## Common Pitfalls & Solutions
- **Design Drift**: Use automated linting and design system validation
- **Component Duplication**: Regular design analysis and recovery workflows
- **Accessibility Debt**: Mandatory accessibility testing in CI/CD pipeline
- **Performance Regression**: Continuous performance monitoring and budgets
- **Documentation Lag**: Automated documentation generation and validation  
