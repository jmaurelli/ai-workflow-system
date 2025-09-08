Developer: # Workflow: Bug Resolution (MVP-First & Context-Aware)

## Objective
Resolve bugs efficiently by leveraging existing feature context to provide AI agents with the same explicit instructions and references that make feature development successful. Reduce iteration cycles from 4-5 down to 1-2 by ensuring comprehensive context capture upfront.

---

## When to Use
- **Production bugs** in deployed features that impact users
- **Implementation bugs** discovered during feature development
- **Integration issues** between existing components
- **Performance regressions** that violate established SRS budgets
- **User experience issues** that affect core workflows

---

## Bug Resolution Strategy

### **Context Reuse First**
The key insight: Your feature development succeeds because AI agents get rich, explicit context. Bug resolution should leverage the **same context patterns** from the original feature where the bug exists.

### **Fast Bug Capture**
Capture bugs with minimal overhead while ensuring AI agents have sufficient context to resolve issues in 1-2 iterations instead of 4-5.

---

## Bug Context Checklist (Prevent Iteration Cycles)

Before engaging AI agents for bug resolution, ensure you have:

### **✅ Feature Context Reference**
- [ ] **Feature Directory**: Identify which feature directory contains the bug (`/features/[date]-[slug]/` or legacy structure)
- [ ] **Original PRD**: Reference specific requirements that are broken (`./prd.md` or `/prd/prd-[slug].md`)
- [ ] **SRS Violations**: Identify which NFRs are violated (`./srs.md` or `/srs/srs-[slug].md`)
- [ ] **Implementation Context**: Reference the original tasks that created this code (`./tasks.md` or `/tasks/tasks-[slug].md`)

### **✅ Bug-Specific Context**
- [ ] **Error Details**: Complete error messages, stack traces, console outputs
- [ ] **Reproduction Steps**: Exact steps that trigger the bug consistently
- [ ] **Environment Context**: Browser, device, OS, data state when bug occurs
- [ ] **Expected vs Actual**: What should happen vs what actually happens

### **✅ Code Context**
- [ ] **Affected Files**: Specific files where the bug manifests
- [ ] **Related Components**: Other components that interact with the buggy code
- [ ] **Recent Changes**: What was changed recently that might have introduced the bug

---

## Bug Resolution Workflow

### **1. Bug Capture & Context Assembly**

Use this template to capture bugs with rich context:

```markdown
# Bug Report: [Brief Description]

## Bug Context
**Feature Directory**: [/features/YYYY-MM-DD-feature-name/ or legacy path]
**Related PRD**: [./prd.md#section or /prd/prd-feature.md#section]
**Related SRS**: [./srs.md#NFR-X or /srs/srs-feature.md#NFR-X]  
**Related Tasks**: [./tasks.md#task-X.Y or /tasks/tasks-feature.md#task-X.Y]

## Executive Context (From Original Feature)
**Tech Stack**: [Copy from original feature's tasks.md Executive Context]
**Performance Budgets**: [Copy relevant budgets that are being violated]
**Security Baseline**: [Copy relevant security requirements if applicable]
**Component Strategy**: [Copy relevant component context]

## Bug Details
**Error Message**: 
```
[Complete error message/stack trace]
```

**Reproduction Steps**:
1. [Step 1]
2. [Step 2] 
3. [Step 3]

**Expected Behavior**: [What should happen]
**Actual Behavior**: [What actually happens]
**Environment**: [Browser/device/OS/data state]

## Affected Code
**Primary Files**: 
- [file1.ext] - [role in bug]
- [file2.ext] - [role in bug]

**Related Components**:
- [ComponentA] - [relationship to bug]
- [ComponentB] - [relationship to bug]

## Recent Changes
**Last Working State**: [When did this last work correctly?]
**Recent Modifications**: [What changed that might have caused this?]
**Git Reference**: [Commit hash or branch where bug was introduced]
```

### **2. Context-Aware Bug Analysis**

**AI Agent Instructions for Bug Resolution:**

```markdown
## Bug Resolution Protocol

### Context Loading (Priority 1)
1. **Read Original Feature Context**: Load Executive Context from the feature where this bug exists
2. **Apply Tech Stack Context**: Use the same technology patterns and decisions from original implementation  
3. **Reference Design Decisions**: Check if bug violates original design decisions or assumptions
4. **Check SRS Compliance**: Verify if bug violates established performance/security budgets

### Root Cause Analysis (Priority 2)
1. **Code Pattern Analysis**: Compare buggy code to working examples in the same feature
2. **Integration Point Review**: Check if bug occurs at component boundaries described in design analysis
3. **Performance Budget Violation**: If performance bug, compare to SRS performance budgets
4. **Security Compliance Check**: If security bug, compare to SRS security baseline

### Solution Planning (Priority 3)
1. **Follow Original Patterns**: Use the same implementation patterns from the original feature
2. **Maintain Design Consistency**: Ensure fix aligns with original design decisions
3. **Preserve Performance**: Ensure fix doesn't violate SRS performance budgets
4. **Update Documentation**: Update relevant sections of feature documentation if needed
```

### **3. TDD-Lite Bug Resolution**

Apply the same RED→GREEN→REFACTOR cycle that works for features:

```markdown
## Bug Fix Implementation (TDD-Lite)

### RED Phase: Failing Test for Bug
- [ ] **Write test that reproduces the bug** (should fail initially)
- [ ] **Test covers the exact reproduction steps** from bug report
- [ ] **Test validates the expected behavior** described in bug report
- [ ] **Test uses same testing patterns** as original feature

### GREEN Phase: Minimal Fix
- [ ] **Implement minimal code to make test pass**
- [ ] **Follow same tech stack patterns** as original feature implementation
- [ ] **Maintain performance budgets** from original SRS
- [ ] **Preserve security baseline** from original SRS

### REFACTOR Phase: Code Quality
- [ ] **Remove duplication** if fix introduces any
- [ ] **Improve naming** if bug was caused by unclear names
- [ ] **Enhance error handling** if bug was due to missing error cases
- [ ] **Update comments/documentation** to prevent similar bugs
```

### **4. Validation & Integration**

```markdown
## Bug Fix Validation

### Functional Validation
- [ ] **Original reproduction steps now work correctly**
- [ ] **All existing tests still pass**
- [ ] **No regressions in related functionality**
- [ ] **Performance budgets still met** (if performance-related)

### Context Integration
- [ ] **Fix aligns with original design decisions**
- [ ] **Implementation follows established patterns**
- [ ] **Documentation updated if assumptions changed**
- [ ] **Learning captured if new pattern discovered**

### Deployment Validation
- [ ] **Bug fix tested in same environment as bug report**
- [ ] **Edge cases tested** (different browsers/devices if applicable)
- [ ] **Performance measured** if SRS budgets were involved
- [ ] **Security validated** if security baseline was affected
```

---

## Bug Resolution Output Locations

### **Feature-Centric Bug Resolution**
```
/features/YYYY-MM-DD-feature-name/
├── prd.md                     # Original feature context
├── srs.md                     # Performance/security budgets  
├── tasks.md                   # Original implementation context
├── design-decisions.md        # Technology and pattern decisions
└── bugs/
    ├── bug-YYYY-MM-DD-001-brief-description.md    # Bug report with context
    ├── bug-fix-001-implementation.md               # Fix implementation notes
    └── bug-fix-001-validation.md                  # Fix validation results
```

### **Legacy Structure Bug Resolution**
```
/bugs/
├── YYYY-MM-DD-bug-001-brief-description.md       # Bug report with references
├── YYYY-MM-DD-bug-001-fix-implementation.md      # Fix implementation  
└── YYYY-MM-DD-bug-001-validation.md              # Fix validation
```

---

## Bug Fix Template (Implementation)

```markdown
# Bug Fix Implementation: [Brief Description]

## Context References
**Original Feature**: [Path to feature directory or legacy references]
**Bug Report**: [Path to bug report with reproduction steps]
**Related PRD**: [Specific PRD sections affected by this bug]
**Related SRS**: [Specific SRS sections violated by this bug]

## Root Cause Analysis
**Primary Cause**: [What caused this bug]
**Contributing Factors**: [What made this bug possible]
**Pattern Violation**: [If bug violates established patterns from design decisions]

## Fix Strategy
**Approach**: [How the fix addresses the root cause]
**Pattern Compliance**: [How fix maintains original design patterns] 
**Performance Impact**: [Impact on SRS performance budgets]
**Security Impact**: [Impact on SRS security baseline]

## Implementation Details
**Files Modified**:
- [file1.ext] - [nature of changes]
- [file2.ext] - [nature of changes]

**Tests Added**:
- [test1.test.ext] - [test for bug reproduction and fix validation]
- [test2.test.ext] - [test for edge cases if applicable]

## Validation Results
**Functional Testing**: [✅ Pass / ❌ Fail] - [Details]
**Performance Testing**: [✅ Pass / ❌ Fail] - [Actual vs budget]
**Security Testing**: [✅ Pass / ❌ Fail] - [Validation method]
**Regression Testing**: [✅ Pass / ❌ Fail] - [Scope of regression tests]

## Learning & Prevention
**Pattern Improvement**: [How to prevent similar bugs in the future]
**Documentation Update**: [What documentation should be updated]
**Design Decision Impact**: [If this affects future technology choices]
```

---

## AI Agent Directives (Context-Heavy Bug Resolution)

### **Context Loading Protocol**
- **Always start with feature context**: Load Executive Context from the feature directory where bug exists
- **Reference original documents**: Use PRD requirements, SRS budgets, design decisions, and task context
- **Apply established patterns**: Follow the same technology and implementation patterns from original feature
- **Maintain design consistency**: Ensure bug fixes align with documented design decisions

### **Bug Resolution Rules**
- **Use existing testing frameworks**: Follow same testing patterns as original feature
- **Preserve performance budgets**: Ensure bug fixes don't violate SRS performance requirements
- **Maintain security baseline**: Ensure bug fixes don't compromise SRS security requirements
- **Follow TDD-Lite**: Write failing test for bug, implement minimal fix, refactor for quality

### **Iteration Reduction Strategy**
- **Capture complete context upfront**: Use Bug Context Checklist to prevent missing information
- **Reference all related documents**: Provide links to PRD, SRS, design decisions, and implementation tasks
- **Include environment details**: Provide complete error messages, reproduction steps, and environment context
- **Apply proven patterns**: Use technology and implementation patterns that already work in this codebase

### **Documentation Integration**
- **Update feature documentation**: If bug reveals design assumption errors, update relevant documents
- **Capture learning insights**: Add bug prevention insights to design learning journal if applicable
- **Reference in changelog**: Update original feature's tasks.md changelog with bug fix reference

Set reasoning_effort = medium; bug resolution requires thorough analysis but should be efficient.

---

## Human Review Gate (Streamlined for Speed)

### **Pre-Resolution Review**
- Confirm: Bug report contains sufficient context for AI resolution (use Bug Context Checklist)
- Confirm: Bug is related to identifiable feature with existing documentation
- Confirm: Bug fix approach aligns with original design decisions and patterns

### **Post-Resolution Review**  
- Confirm: Bug fix resolves the reported issue without regressions
- Confirm: Fix maintains performance budgets and security baseline from SRS
- Confirm: Fix follows established patterns and technology choices
- Approve: Bug fix for deployment

---

## Integration with Existing Workflow

### **No Changes to Existing Documents**
This bug resolution workflow **supplements** your existing lean workflow without modifying any of the 01-09 documents. It leverages the context and patterns you've already established.

### **Context Reuse Strategy**
- **Feature-centric bugs**: Store in `/features/[date]-[slug]/bugs/` to maintain context proximity
- **Legacy structure bugs**: Store in `/bugs/` with explicit references to existing documentation
- **Cross-feature bugs**: Create standalone bug directory with references to multiple features

### **Learning Integration**
- **Bug patterns**: Feed insights back into `design-learning-journal.md` for future prevention
- **Design decision updates**: If bugs reveal design assumption errors, update design decision documentation
- **Quarterly rollups**: Include bug resolution metrics in project history summaries

---

## Success Metrics

### **Iteration Reduction**
- **Target**: Reduce bug resolution from 4-5 iterations to 1-2 iterations
- **Method**: Comprehensive context capture using Bug Context Checklist
- **Measurement**: Track actual iterations needed per bug fix

### **Context Effectiveness**
- **Measure**: How often AI agents need additional context requests during bug resolution
- **Target**: <20% of bug fixes require additional context beyond initial capture
- **Improvement**: Refine Bug Context Checklist based on actual context needs

### **Pattern Consistency**
- **Measure**: Bug fixes follow established technology and design patterns
- **Target**: 100% of bug fixes align with original feature design decisions
- **Quality**: Bug fixes don't introduce new inconsistencies or design debt

---

This bug resolution workflow leverages the same context-rich, pattern-based approach that makes your feature development successful, applied specifically to efficient bug resolution!
