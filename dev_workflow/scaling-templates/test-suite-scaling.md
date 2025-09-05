# Test Suite Workflow (Scaling)

## Objective
Maintain a complete, standardized test result schema for traceability.  

---

## Schema
```json
{
  "test": "string",
  "status": "pass|fail|skip",
  "duration_ms": 120,
  "coverage": "lines:85, branches:70",
  "timestamp": "2025-08-24T12:00:00Z",
  "logs": "stdout/stderr output"
}
```

---

## Workflow
1. Run all tests.  
2. Record results in `/tests/results/`.  
3. Commit results with build.  

---

---

## Enhanced Schema (Design-Aware)
```json
{
  "test_suite": "string",
  "feature_slug": "string",
  "test_type": "unit|integration|visual|accessibility|performance",
  "component_name": "string",
  "status": "pass|fail|skip",
  "duration_ms": 120,
  "coverage": {
    "lines": 85,
    "branches": 70,
    "functions": 90,
    "statements": 88
  },
  "design_system_compliance": {
    "tokens_usage_validated": true,
    "accessibility_validated": true,
    "performance_validated": true
  },
  "performance_metrics": {
    "bundle_size_kb": 12.5,
    "render_time_ms": 16.7,
    "first_paint_ms": 45.2
  },
  "accessibility_metrics": {
    "wcag_aa_compliant": true,
    "keyboard_navigation": true,
    "screen_reader_compatible": true,
    "color_contrast_ratio": 4.8
  },
  "timestamp": "2025-08-24T12:00:00Z",
  "logs": "stdout/stderr output",
  "screenshots": [
    "path/to/visual-test-baseline.png",
    "path/to/visual-test-result.png"
  ]
}
```

---

## Enhanced Workflow
1. **Run Comprehensive Test Suites**
   - Unit tests with coverage requirements (>90%)
   - Integration tests with real component interactions
   - Visual regression tests with baseline comparisons
   - Accessibility tests with WCAG compliance validation
   - Performance tests with bundle size and render time monitoring

2. **Design System Validation**
   - Validate design token usage consistency
   - Check component API compliance with design system standards
   - Verify accessibility implementation matches design system requirements
   - Validate performance meets design system benchmarks

3. **Record Enhanced Results**
   - Save comprehensive results to `/tests/results/[feature-name]-[timestamp].json`
   - Include design system compliance metrics
   - Track performance regression against baselines
   - Document accessibility validation results

4. **Aggregate and Report**
   - Generate feature-level reports with design system compliance
   - Create release-level reports with performance trends
   - Track design debt and compliance over time
   - Monitor accessibility and performance regression

---

## AI Agent Directives
- Enforce enhanced schema with design system and accessibility metrics
- Require comprehensive test coverage across all test types
- Validate design system compliance for all component tests
- Monitor performance regression against established baselines
- Reject test results that don't meet accessibility compliance standards
- Aggregate results per feature, component, and release with trend analysis
- Save results to `/tests/results/[feature-name]-scaling-[timestamp].json`
Set reasoning_effort = high; scaling tests require comprehensive validation and monitoring

---

## Human Review Gate (Required)
- Confirm: comprehensive test coverage meets scaling requirements (>90% unit, >80% integration)
- Confirm: design system compliance validation included in all relevant tests
- Confirm: accessibility testing covers all WCAG 2.1 AA requirements
- Confirm: performance monitoring includes bundle size and render time tracking
- Confirm: visual regression testing configured with proper baselines
- Approve test results and proceed with deployment validation

---

## Handoff + Memory Sync
Update agent memory with the following minimal context:

```json
{
  "stage": "test_suite_scaling",
  "feature_slug": "[feature-name]",
  "test_results_path": "/tests/results/[feature-name]-scaling-[timestamp].json",
  "test_coverage": {
    "unit_coverage": 0,
    "integration_coverage": 0,
    "visual_tests_count": 0,
    "accessibility_tests_count": 0,
    "performance_tests_count": 0
  },
  "design_system_compliance": {
    "tokens_compliance": "pass|fail",
    "api_compliance": "pass|fail",
    "accessibility_compliance": "pass|fail",
    "performance_compliance": "pass|fail"
  },
  "quality_gates": {
    "coverage_threshold_met": true|false,
    "performance_benchmarks_met": true|false,
    "accessibility_requirements_met": true|false,
    "visual_regression_passed": true|false
  }
}
```

### Context Seed (for deployment)
Provide this block to deployment workflow:

```json
{
  "feature_slug": "[feature-name]",
  "test_results_path": "/tests/results/[feature-name]-scaling-[timestamp].json",
  "all_tests_passed": true|false,
  "design_system_compliant": true|false,
  "ready_for_deployment": true|false
}
```

---

## Human-in-the-Loop Rule
Pause for explicit approval before:
- Proceeding with deployment if any accessibility tests fail
- Accepting performance regression beyond established thresholds
- Deploying with design system compliance violations
- Otherwise proceed autonomously for test result recording and aggregation  
