Developer: # Workflow: Bug Resolution (MVP-First & Context-Aware)

## Objective
Resolve bugs efficiently by leveraging existing feature context to provide AI agents with the same explicit instructions and references that make feature development successful. Reduce iteration cycles from 4-5 down to 1-2 by ensuring comprehensive context capture upfront.

---

## When to Use
- **Implementation bugs** discovered during your dev server testing
- **Production bugs** in deployed features that impact users
- **Integration issues** between existing components
- **Performance regressions** that violate established SRS budgets
- **User experience issues** that affect core workflows

---

## Quick Start (For Solo Developers)

### **Simple Invocation**
When you encounter a bug during your fast-moving development and testing:

```
I found a bug during testing. Please use the guided bug resolution workflow 
in ai-workflow/lean-workflow/bug-resolution-lite.md to help me resolve this.

Start with the Recent Task Analysis to understand what I just implemented, 
then walk me through the guided questions to capture the bug properly.

[Brief description of what seems wrong]
```

The AI will:
1. **Find your recent work** automatically (no infinite scanning)
2. **Ask guided questions** to help you describe the bug effectively  
3. **Explain technical concepts** as we go (educational approach)
4. **Suggest specific testing** based on what you just implemented
5. **Walk through validation** before and after the fix

---

## Bug Resolution Strategy

### **Context Reuse First**
The key insight: Your feature development succeeds because AI agents get rich, explicit context. Bug resolution should leverage the **same context patterns** from the original feature where the bug exists.

### **Fast Bug Capture**
Capture bugs with minimal overhead while ensuring AI agents have sufficient context to resolve issues in 1-2 iterations instead of 4-5.

---

## Guided Bug Discovery (For Solo Developers)

### **Phase 1: Recent Task Analysis (Auto-Discovery)**

**AI Agent Instructions**: Start here to understand what was recently implemented.

```markdown
## Recent Task Analysis Protocol

### Step 1: Find Most Recent Feature Work
1. **Scan for recently modified tasks.md files**:
   ```bash
   find /features -name "tasks.md" -exec ls -lt {} + | head -5
   # OR if using legacy structure:
   find /tasks -name "tasks-*.md" -exec ls -lt {} + | head -5
   ```

2. **Identify the most recently modified tasks file**
3. **Read the last 5-10 completed tasks** (marked with `[x]`)
4. **Extract what was just implemented**:
   - Which components were created/modified?
   - Which features were added?
   - Which integrations were completed?

### Step 2: Present Recent Work Summary
**AI presents to user**: "Based on your recent task completions, I see you just implemented:
- [Task X]: [Brief description]
- [Task Y]: [Brief description]  
- [Task Z]: [Brief description]

Is the bug you're experiencing related to any of these recent implementations?"
```

### **Phase 2: Guided Bug Capture (Educational Approach)**

**AI Agent Instructions**: Walk the user through bug discovery with educational support.

```markdown
## Progressive Bug Discovery Questions

### Question Set A: Basic Bug Understanding
**AI asks**: "Let's start simple. When you were testing your application:

1. **What were you trying to do?** (e.g., 'I was trying to log in', 'I was trying to view the dashboard')
2. **What did you expect to happen?** (e.g., 'I expected to see the dashboard page')  
3. **What actually happened instead?** (e.g., 'I got a blank page', 'I saw an error message')

Don't worry about technical details yet - just describe what you experienced as a user."

### Question Set B: Error Details (If Applicable)
**AI asks**: "Now let's gather some technical details:

1. **Do you see any error messages?** 
   - In the browser window itself?
   - In the browser console? (Press F12, click 'Console' tab)
   - In your development server terminal?

2. **Can you copy and paste any error messages you see?** 
   (AI explains: 'Error messages contain valuable clues about what's wrong')

If you're not sure where to look for errors, I can guide you through checking each location."

### Question Set C: Environment Context  
**AI asks**: "Let's understand your testing environment:

1. **Which browser are you using?** (Chrome, Firefox, Safari, etc.)
2. **Are you testing on the same computer where you're developing?**
3. **What's the URL you're trying to access?** (e.g., localhost:3000, localhost:8000)

This helps me understand if it's a general bug or specific to your setup."

### Question Set D: Reproduction Steps
**AI asks**: "Let's figure out how to trigger this bug consistently:

1. **Can you make the bug happen again?** Try the same steps you just did.
2. **What are the exact steps?** I'll help you break it down:
   - Step 1: 'I opened the browser and went to...'
   - Step 2: 'I clicked on...'
   - Step 3: 'I entered...'
   - Step 4: 'Then the bug appeared...'

3. **Does it happen every time, or sometimes?**

Being able to reproduce a bug consistently makes it much easier to fix."

### Question Set E: Recent Changes Connection
**AI asks**: "Based on what you recently implemented, let's connect this to your recent work:

1. **Is this bug in functionality that was working before?** (regression)
2. **Or is this a new feature that never worked?** (implementation issue)  
3. **When did you last see this functionality working correctly?**

Looking at your recent tasks, this might be related to [specific recent task]. Does that seem right?"
```

### **Phase 3: Automatic Testing Suggestions**

**AI Agent Instructions**: Based on completed tasks, suggest specific things to test.

```markdown
## Smart Testing Suggestions Protocol

### Step 1: Parse Recent Tasks for Testing Hints
**AI analyzes recent completed tasks** and extracts:
- **UI components** that were created/modified
- **API endpoints** that were implemented  
- **Database operations** that were added
- **Authentication flows** that were touched
- **Integrations** that were established

### Step 2: Generate Targeted Testing Steps
**AI suggests**: "Based on what you recently implemented, let's test these specific areas:

**If recent tasks included UI components:**
- 'Let's check if [ComponentName] loads correctly'
- 'Try clicking [button/link name] to see if it works'
- 'Check if [form name] submits properly'

**If recent tasks included API work:**
- 'Let's verify the [endpoint name] is responding'
- 'Check if data is being saved/retrieved correctly'
- 'Test if authentication is working with the API'

**If recent tasks included database changes:**
- 'Let's verify data is being stored correctly'
- 'Check if existing data is still accessible'
- 'Test if new database fields are working'

Would you like me to walk you through testing any of these areas?"

### Step 3: Progressive Validation
**AI guides**: "Let's test one thing at a time:

1. **First, let's verify the basics work**: 'Can you load the main page without errors?'
2. **Then, let's test the core functionality**: 'Can you [main user action] successfully?'  
3. **Finally, let's test what you just implemented**: 'Can you [recently implemented feature] without issues?'

This helps us narrow down where the problem is occurring."
```

---

## Enhanced Bug Resolution Workflow (Educational Focus)

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

### **4. Pre-Fix Validation Checkpoint**

```markdown
## Pre-Fix Validation (Confirm Bug Reproduction)

**AI guides user through validation**: "Before we implement a fix, let's make sure we can consistently reproduce the bug:

### Step 1: Controlled Bug Reproduction
1. **Follow the exact reproduction steps** we documented together
2. **Confirm the bug happens consistently** (try 2-3 times)
3. **Document the exact error state**: 
   - Screenshot of what's wrong (if visual)
   - Copy error messages (if any)
   - Note what's missing or broken

### Step 2: Environment Baseline Check
1. **Verify development server is running** without startup errors
2. **Check that other core functionality works** (quick smoke test)
3. **Confirm this is an isolated issue** and not system-wide problem

### Step 3: Scope Understanding  
1. **Identify what's working vs. broken**: 'The login form loads, but submission fails'
2. **Understand impact scope**: 'This affects all users' vs 'This only happens with certain data'
3. **Connect to recent changes**: 'This started after implementing [specific task]'

**Checkpoint**: AI confirms with user - 'I understand the bug. We can reproduce it consistently. Ready to implement fix?'"
```

### **5. Bug Fix Implementation (Same TDD-Lite Process)**

[Previous TDD-Lite content remains the same]

### **6. Post-Fix Validation Checkpoint**

```markdown
## Post-Fix Validation (Comprehensive Verification)

**AI guides user through post-fix validation**: "Now let's thoroughly verify the fix works and didn't break anything:

### Step 1: Primary Fix Validation
1. **Test the original reproduction steps**: 'Try the exact steps that caused the bug'
2. **Confirm expected behavior**: 'Verify you now see what you expected to see'
3. **Test edge cases**: 'Try variations of the same action to ensure robustness'

**AI explains**: 'This ensures our fix actually solves the problem you experienced.'

### Step 2: Regression Testing (No New Bugs)
1. **Test core application functions**: 
   - 'Can you still log in?' (if authentication exists)
   - 'Can you still navigate between main pages?'
   - 'Do the main features still work?'

2. **Test recently implemented features**:
   Based on recent task analysis, AI suggests: 'Let's test [recently implemented features] to make sure our fix didn't break them'

3. **Browser console check**: 'Press F12 and check if there are any new error messages'

**AI explains**: 'This ensures our fix didn't accidentally break something else.'

### Step 3: Performance & Quality Check
1. **Startup speed check**: 'Does the app still start up quickly?'
2. **Page load check**: 'Do pages still load at normal speed?'  
3. **User experience check**: 'Does everything still feel responsive?'

**AI explains**: 'This ensures our fix maintains the quality standards from your SRS requirements.'

### Step 4: Documentation Update Check
1. **Review if assumptions changed**: 'Did fixing this bug reveal any incorrect assumptions in our documentation?'
2. **Update learning notes**: 'What did we learn about [technology/pattern] from fixing this bug?'
3. **Consider prevention**: 'How can we avoid similar bugs in the future?'

**AI explains**: 'This captures learning to improve future development.'

**Final Checkpoint**: AI confirms with user - 'Bug is fixed, no regressions detected, quality maintained. Ready to move forward?'"
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
