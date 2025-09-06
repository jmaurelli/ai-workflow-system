# 🚀 Workflow Automation Quickstart Guide

## **🎯 Three Ways to Run Your MVP Workflow**

### **🚪 Option 1: GUIDED Mode (Traditional)**
*Maximum human oversight - stops at every major decision point*

```bash
# Run complete workflow with human approval gates
./workflow-orchestrator.sh --mode=guided --feature=user-auth

# Show what gates will be required
./ai-workflow-runner.py --mode=guided --feature=user-auth --dry-run
```

**Best for**: First-time users, critical features, learning the workflow

---

### **⚡ Option 2: AUTONOMOUS Mode (AI-Driven)**  
*Minimal human oversight - AI agent runs automatically with smart safety checks*

```bash
# Run workflow automatically with minimal gates
./workflow-orchestrator.sh --mode=autonomous --feature=dashboard

# AI-powered execution with risk assessment
./ai-workflow-runner.py --mode=autonomous --feature=api-v2
```

**Best for**: Experienced users, incremental features, rapid prototyping

---

### **🧠 Option 3: LEARNING Mode (Adaptive)**
*Learns from your approval patterns and reduces gates over time*

```bash
# Adaptive workflow that learns your preferences
./ai-workflow-runner.py --mode=learning --feature=search-engine

# See how the learning algorithm plans your workflow
./ai-workflow-runner.py --mode=learning --feature=payments --dry-run
```

**Best for**: Power users, consistent workflow patterns, organizational learning

---

## **🎛️ Custom Gate Configuration**

### **Skip Specific Gates**
```bash
# Skip design analysis and completion summary gates
./workflow-orchestrator.sh --mode=autonomous --feature=notifications \
    --skip-gates=design_analysis,completion_summary
```

### **Force Specific Gates**
```bash
# Always require human approval for task implementation and design decisions
./workflow-orchestrator.sh --mode=autonomous --feature=payments \
    --require-gates=task_implementation,design_decisions
```

### **Dry Run Any Configuration**
```bash
# See execution plan without running anything
./ai-workflow-runner.py --mode=autonomous --feature=test-feature \
    --dry-run --verbose
```

---

## **📋 Numbered Workflow Sequence**

### **What Each Step Does**
```
PHASE 1: FOUNDATION
01-mvp-entrypoint.md              ← Collect project requirements
02-gen-prd.md                     ← Generate Product Requirements
03-gen-srs.md                     ← Generate Software Requirements (NFRs)

PHASE 2: DESIGN
04-gen-design-decisions-lite.md   ← Make technology/UX decisions
05-gen-design.md                  ← Analyze existing components

PHASE 3: IMPLEMENTATION  
06-gen-tasks-and-testing.md       ← Generate implementation tasks
07-process-tasks.md               ← Execute tasks with TDD-Lite

PHASE 4: COMPLETION
08-gen-completion-summary.md      ← Generate executive summary
09-gen-project-history.md         ← Update organizational learning
```

### **Gate Locations by Mode**

#### **🚪 GUIDED Mode Gates**
```
01 → 🚪 → 02 → 🚪 → 03 → 🚪 → 04 → 🚪 → 05 → 06 → 🚪 → 07 → 🚪 → 08 → 09
```

#### **⚡ AUTONOMOUS Mode Gates**  
```
01 → 02 → 03 → 04 → 05 → 06 → 07 → 🚪 → 08 → 09
```
*Only stops for destructive/high-risk actions*

#### **🧠 LEARNING Mode Gates**
```
01 → 🧠 → 02 → 🧠 → 03 → 🧠 → 04 → 🧠 → 05 → 06 → 🧠 → 07 → 🚪 → 08 → 09
```
*Adaptive gates based on approval history*

---

## **🔧 Configuration Files**

### **Main Configuration**
- `automation-config.json` - Gate behavior, risk assessment, workflow sequence
- Customize automation modes, risk thresholds, and gate requirements

### **Execution Logs**
- `workflow-execution.log` - Shell orchestrator logs  
- `ai-workflow-execution.log` - Python orchestrator logs
- Track automation decisions and approval patterns

---

## **⚡ Quick Examples**

### **🎯 Most Common Use Cases**

```bash
# New feature development (balanced approach)
./ai-workflow-runner.py --mode=guided --feature=user-profile

# Rapid prototyping (minimal gates)  
./ai-workflow-runner.py --mode=autonomous --feature=quick-prototype

# Production feature (with safety gates)
./ai-workflow-runner.py --mode=autonomous --feature=billing-system \
    --require-gates=design_decisions,task_implementation

# Incremental enhancement (learning mode)
./ai-workflow-runner.py --mode=learning --feature=ui-improvements

# See execution plan for any workflow
./ai-workflow-runner.py --mode=autonomous --feature=any-feature --dry-run
```

### **🚀 Advanced Automation**

```bash
# Custom risk tolerance
./ai-workflow-runner.py --mode=autonomous --feature=api-integration \
    --config=./custom-automation-config.json

# Verbose logging for debugging
./ai-workflow-runner.py --mode=learning --feature=complex-feature \
    --verbose --dry-run

# Traditional bash orchestrator with custom gates
./workflow-orchestrator.sh --mode=autonomous --feature=simple-feature \
    --skip-gates=design_analysis,completion_summary \
    --require-gates=task_implementation
```

---

## **🎓 Learning Your Workflow**

### **📊 The Learning Mode Evolution**
1. **Initial Runs**: Requires all gates (like guided mode)
2. **Pattern Recognition**: Tracks your approval/rejection patterns  
3. **Confidence Building**: Gradually reduces gates for trusted patterns
4. **Adaptive Execution**: Automatically skips gates you always approve
5. **Smart Safety**: Always maintains gates for high-risk operations

### **🧠 What Learning Mode Learns**
- Technology stack preferences and approval patterns
- Feature scope comfort levels and automatic approvals
- Design decision confidence and gate requirements  
- Task implementation trust levels and safety requirements
- Performance budget acceptance and NFR patterns

---

## **🚦 When to Use Each Mode**

### **🚪 Use GUIDED Mode When:**
- Learning the MVP workflow for the first time
- Working on critical/high-stakes features
- Teaching the workflow to new team members
- Debugging workflow issues or process problems
- Maximum oversight and control desired

### **⚡ Use AUTONOMOUS Mode When:**
- Experienced with the workflow process
- Rapid prototyping or iteration cycles  
- Incremental features with familiar patterns
- Time pressure with acceptable risk tolerance
- Trust in automation with safety nets

### **🧠 Use LEARNING Mode When:**
- Building organizational workflow intelligence
- Consistent development patterns emerging
- Want adaptive automation over time
- Balancing speed with appropriate oversight
- Long-term workflow optimization goals

---

## **🎯 Getting Started**

### **1. First Run (Recommended)**
```bash
# Start with guided mode to learn the workflow
./ai-workflow-runner.py --mode=guided --feature=hello-world --dry-run
```

### **2. Gradual Automation**
```bash
# Move to autonomous for simple features
./ai-workflow-runner.py --mode=autonomous --feature=simple-ui
```

### **3. Full Intelligence**
```bash  
# Enable learning for adaptive automation
./ai-workflow-runner.py --mode=learning --feature=complex-system
```

---

## **📚 Additional Resources**

- **📋 Complete Workflow**: See `workflow-sequence-guide.md`
- **🏗️ Architecture**: See `feature-centric-architecture.md`  
- **🤖 Multi-Agent**: See `multi-agent/` directory for parallel execution
- **📖 Scaling**: See `../scaling-workflow/` for enterprise workflows

**The future of development is here - automated, intelligent, and adaptive workflows!** 🚀✨
