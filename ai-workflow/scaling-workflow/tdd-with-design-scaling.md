# TDD with Design System Integration (Scaling)

## Objective
Follow strict TDD with comprehensive design system validation and accessibility compliance. Every coding step starts with failing tests that validate both functionality and design system adherence.

---

## Enhanced TDD Workflow (Design-Aware)

### 1. Pre-Implementation Analysis
- **Component Analysis**: Review existing design system components for reuse opportunities
- **Design Token Validation**: Ensure design tokens are available and correctly defined
- **Accessibility Requirements**: Define accessibility requirements (WCAG 2.1 AA compliance)
- **Performance Benchmarks**: Establish performance budgets for bundle size and render time

### 2. Test-First Development (RED Phase)
- **Write Failing Functional Tests**: Core functionality tests
- **Write Failing Design System Tests**: Validate design token usage and component API compliance
- **Write Failing Accessibility Tests**: WCAG compliance, keyboard navigation, screen reader support
- **Write Failing Visual Regression Tests**: Capture expected visual output and behavior
- **Write Failing Performance Tests**: Bundle size limits, render performance benchmarks

### 3. Minimal Implementation (GREEN Phase)
- **Implement Core Functionality**: Minimal code to pass functional tests
- **Apply Design System Compliance**: Use design tokens, follow component API patterns
- **Implement Accessibility Features**: ARIA labels, keyboard navigation, semantic HTML
- **Optimize for Performance**: Efficient rendering, proper prop usage, memoization where needed

### 4. Design-Aware Refactoring (REFACTOR Phase)
- **Code Quality**: Single Responsibility Principle, composability, maintainability
- **Design System Consistency**: Ensure all design tokens are used correctly
- **Accessibility Enhancement**: Improve accessibility beyond minimum requirements
- **Performance Optimization**: Bundle size optimization, render performance improvements
- **Component API Standardization**: Ensure props follow design system conventions

### 5. Comprehensive Validation
- **All Tests Passing**: Functional, design system, accessibility, visual, performance
- **Design System Compliance**: 100% design token usage, component API adherence
- **Accessibility Compliance**: WCAG 2.1 AA validation with automated and manual testing
- **Performance Validation**: Bundle size and render time within established budgets
- **Cross-Browser Testing**: Compatibility across target browsers and devices

---

## Design System Integration Principles

### Component Development
- **Reuse First**: Always check existing design system components before creating new ones
- **Token Usage**: Use design tokens for all colors, spacing, typography, shadows
- **API Consistency**: Follow established prop naming conventions and patterns
- **Composition Patterns**: Build components that compose well with existing components

### Accessibility Integration
- **Semantic HTML**: Use proper HTML elements for accessibility
- **ARIA Attributes**: Implement ARIA labels, roles, and properties correctly
- **Keyboard Navigation**: Ensure all interactive elements are keyboard accessible
- **Screen Reader Support**: Test with screen readers and provide proper descriptions
- **Color Contrast**: Validate color contrast ratios meet WCAG AA standards

### Performance Integration
- **Bundle Impact**: Monitor component bundle size impact
- **Render Performance**: Measure and optimize component render time
- **Memory Usage**: Avoid memory leaks and excessive re-renders
- **Lazy Loading**: Implement lazy loading for large components when appropriate

---

## Testing Strategy (Comprehensive)

### Functional Testing
```javascript
// Example functional test with design system validation
describe('Button Component', () => {
  it('should render with design system tokens', () => {
    render(<Button variant="primary">Click me</Button>);
    
    const button = screen.getByRole('button');
    expect(button).toHaveStyleRule('background-color', tokens.colors.primary[500]);
    expect(button).toHaveStyleRule('padding', tokens.spacing.md);
    expect(button).toHaveStyleRule('font-family', tokens.typography.fontFamily.sans);
  });
});
```

### Accessibility Testing
```javascript
// Example accessibility test
describe('Button Accessibility', () => {
  it('should be keyboard accessible', () => {
    render(<Button onClick={mockFn}>Click me</Button>);
    
    const button = screen.getByRole('button');
    button.focus();
    fireEvent.keyDown(button, { key: 'Enter' });
    
    expect(mockFn).toHaveBeenCalled();
  });

  it('should have proper ARIA attributes', () => {
    render(<Button aria-label="Close dialog">×</Button>);
    
    expect(screen.getByRole('button')).toHaveAttribute('aria-label', 'Close dialog');
  });
});
```

### Visual Regression Testing
```javascript
// Example visual test
describe('Button Visual Tests', () => {
  it('should match visual snapshot', () => {
    const component = render(<Button variant="primary">Click me</Button>);
    expect(component).toMatchSnapshot();
  });
});
```

### Performance Testing
```javascript
// Example performance test
describe('Button Performance', () => {
  it('should render within performance budget', () => {
    const start = performance.now();
    render(<Button>Click me</Button>);
    const end = performance.now();
    
    expect(end - start).toBeLessThan(16); // 60fps budget
  });
});
```

---

## Design System TDD Checklist

### Before Writing Tests
- [ ] Reviewed existing design system components for reuse opportunities
- [ ] Identified required design tokens (colors, spacing, typography)
- [ ] Defined accessibility requirements (WCAG 2.1 AA)
- [ ] Established performance benchmarks

### Test Implementation
- [ ] Functional tests cover all requirements
- [ ] Design system compliance tests validate token usage
- [ ] Accessibility tests cover keyboard navigation and ARIA
- [ ] Visual regression tests capture expected appearance
- [ ] Performance tests validate bundle size and render time

### Implementation Phase
- [ ] Uses design tokens for all styling
- [ ] Follows component API conventions
- [ ] Implements proper accessibility features
- [ ] Meets performance benchmarks
- [ ] Composes well with existing components

### Validation Phase
- [ ] All tests passing (functional, design, accessibility, visual, performance)
- [ ] Design system compliance verified
- [ ] Accessibility compliance validated (automated + manual)
- [ ] Performance benchmarks met
- [ ] Cross-browser compatibility confirmed

---

## AI Agent Directives
- Always validate design system compliance before writing implementation code
- Require comprehensive test coverage across all test types (functional, design, accessibility, visual, performance)
- Enforce design token usage and component API consistency
- Validate accessibility compliance with both automated and manual testing
- Monitor performance impact and enforce established budgets
- Ensure all components compose well with existing design system
Set reasoning_effort = high; design system TDD requires comprehensive validation

---

## Human Review Gate (Required)
- Confirm: design system analysis complete and reuse opportunities identified
- Confirm: comprehensive test suite covers functionality, design, accessibility, and performance
- Confirm: accessibility compliance validated with WCAG 2.1 AA standards
- Confirm: performance benchmarks met and validated
- Confirm: component integrates properly with existing design system
- Approve implementation with design system compliance

---

## Integration with Scaling Workflow
This TDD workflow integrates with other scaling documents:
- Builds upon component analysis from `gen-design-scaling.md`
- Implements design system standards from `gen-design-system-scaling.md`
- Supports recovery goals from `gen-design-recovery-scaling.md`
- Provides test validation for `test-suite-scaling.md`

---

## Success Criteria
- [ ] 100% design token usage for all styling
- [ ] Complete accessibility compliance (WCAG 2.1 AA)
- [ ] Performance benchmarks met (bundle size, render time)
- [ ] All test types passing (functional, design, accessibility, visual, performance)
- [ ] Component API follows design system conventions
- [ ] Proper composition with existing design system components  
