# 🚀 Python Workflow System - Complete User Guide

*The definitive guide to automated MVP creation and feature development with real LLM content generation*

---

## **🎯 What This System Does**

**Transform your development workflow from hours of planning to minutes of automation:**

- **🚀 Create complete MVP projects** with real PRD, SRS, tasks, and specifications
- **➕ Add features to existing projects** with full context awareness
- **🤖 Generate real content** using 5 different LLM providers
- **📁 Organize everything** in clean, structured project directories
- **⚡ Save 90%+ of planning time** with professional-quality output

---

## **🛠️ Quick Setup**

### **1. Choose Your LLM Provider**
Pick one (or try multiple):

```bash
# OpenAI (most reliable)
export OPENAI_API_KEY="sk-your-key-here"

# Anthropic Claude (advanced reasoning)  
export ANTHROPIC_API_KEY="your-claude-key"

# Google Gemini (fast & competitive)
export GOOGLE_API_KEY="your-gemini-key"

# Groq (ultra-fast)
export GROQ_API_KEY="your-groq-key"

# Local Ollama (free & private)
ollama serve
```

### **2. Install Dependencies**
```bash
pip install openai anthropic google-generativeai requests
```

### **3. Test Your Setup**
```bash
./test-complete-workflow.py --quick
```

**Ready!** ✅

---

## **🎯 The Two Workflows**

### **🚀 NEW MVP PROJECTS**
*Start here when creating a brand new product*

```bash
./mvp-initializer.py --project=my-amazing-app --mode=autonomous --llm-api
```

**Creates:**
- `/projects/my-amazing-app/` directory
- Complete MVP specification (PRD, SRS, tasks)
- Project manifest for tracking
- Organized subdirectories for development

### **➕ ADD FEATURES TO EXISTING PROJECTS**
*Use this to expand existing MVPs*

```bash
./workflow-runner.py --feature=user-authentication --existing-project=my-amazing-app --mode=autonomous --llm-api
```

**Adds:**
- Feature documentation to existing project
- Context-aware content generation
- Integration with existing project structure

---

## **⚙️ Automation Modes**

### **🚪 GUIDED Mode** (Recommended for first time)
*Maximum oversight - stops at every major decision*

```bash
./mvp-initializer.py --project=my-app --mode=guided --llm-api
```

**Best for:** First-time users, critical features, learning the system

### **⚡ AUTONOMOUS Mode** (Recommended for production)
*Minimal oversight - AI runs automatically with smart safety checks*

```bash
./mvp-initializer.py --project=my-app --mode=autonomous --llm-api
```

**Best for:** Experienced users, rapid development, trusted environments

### **🧠 LEARNING Mode** (Advanced)
*Adaptive oversight - learns from your approval patterns*

```bash
./mvp-initializer.py --project=my-app --mode=learning --llm-api
```

**Best for:** Long-term usage, personalized automation

---

## **🌟 LLM Provider Selection**

### **Choose Based on Your Needs:**

```bash
# Most reliable & popular
--llm-provider=openai

# Best reasoning & analysis
--llm-provider=anthropic

# Fast & cost-effective
--llm-provider=google

# Ultra-fast inference
--llm-provider=groq

# Free & private
--llm-provider=local_ollama
```

### **Advanced Configuration:**
```bash
# Custom model selection
./mvp-initializer.py --project=my-app --llm-api --llm-provider=openai --llm-model=gpt-4

# Cost management
./mvp-initializer.py --project=my-app --llm-api --cost-limit=15.0

# Custom configuration file
./mvp-initializer.py --project=my-app --llm-api --llm-config=my-llm-config.json
```

---

## **📁 Project Structure**

### **Generated Project Layout:**
```
/projects/my-amazing-app/
├── 📊 project-manifest.json     # Project tracking & metadata
├── 📁 features/                 # Feature-specific documentation
├── 📁 docs/                     # Project documentation
├── 📁 artifacts/                # Generated content & assets
└── 📄 Generated workflow files:
    ├── project-initialization.md
    ├── prd.md                   # Product Requirements
    ├── srs.md                   # Software Requirements  
    ├── design-decisions.md      # Technology choices
    ├── design-analysis.md       # UI/UX planning
    ├── tasks.md                 # Development roadmap
    ├── implementation-guide.md  # Development process
    ├── completion-summary.md    # Success criteria
    └── project-history.md       # Evolution tracking
```

### **What Each File Contains:**
- **📊 project-manifest.json**: Project metadata, tracking, status
- **📄 prd.md**: Complete product requirements with scope & constraints
- **📄 srs.md**: Technical requirements, performance standards, security
- **📄 design-decisions.md**: Technology stack choices with rationale
- **📄 tasks.md**: Detailed development tasks with acceptance criteria
- **📄 And more...** Complete development specification ready for implementation

---

## **🎯 Usage Examples**

### **🚀 Create Your First MVP**
```bash
# Test the system first
./test-complete-workflow.py

# Create a task management app
./mvp-initializer.py --project=task-manager --mode=guided --llm-api --llm-provider=openai

# Check what was created
ls projects/task-manager/
cat projects/task-manager/prd.md
```

### **➕ Add Authentication Feature**
```bash
./workflow-runner.py --feature=user-authentication --existing-project=task-manager --mode=autonomous --llm-api
```

### **➕ Add Dashboard Feature**
```bash
./workflow-runner.py --feature=admin-dashboard --existing-project=task-manager --mode=autonomous --llm-api --llm-provider=anthropic
```

### **🧪 Try Different Approaches**
```bash
# See what would happen (dry run)
./mvp-initializer.py --project=e-commerce-store --mode=autonomous --llm-api --dry-run

# Use local models (free)
./mvp-initializer.py --project=blog-platform --mode=autonomous --llm-api --llm-provider=local_ollama

# Cost-conscious approach
./mvp-initializer.py --project=fitness-tracker --mode=autonomous --llm-api --llm-provider=google --cost-limit=5.0
```

---

## **🔧 Advanced Features**

### **💰 Cost Management**
```bash
# Set daily cost limits
export LLM_COST_LIMIT=25.0

# Monitor usage
tail -f llm-usage.log

# Override limits per project
./mvp-initializer.py --project=big-project --llm-api --cost-limit=50.0
```

### **🎛️ Custom Configuration**
Create `my-llm-config.json`:
```json
{
  "default_provider": "anthropic",
  "providers": {
    "anthropic": {
      "model": "claude-3-5-sonnet-20241022",
      "temperature": 0.6,
      "cost_limit_usd": 20.0
    }
  }
}
```

Use it:
```bash
./mvp-initializer.py --project=my-app --llm-api --llm-config=my-llm-config.json
```

### **🧪 Testing & Validation**
```bash
# Quick system check
./test-complete-workflow.py --quick

# Full system test with LLM
./test-complete-workflow.py --test-llm

# Debug mode for troubleshooting
./test-complete-workflow.py --debug --no-cleanup
```

---

## **🎉 Success Metrics**

### **You'll Know It's Working When:**

✅ **Complete project created in minutes** (instead of hours/days)
✅ **Real, actionable content generated** (not generic templates)  
✅ **Organized project structure** ready for development
✅ **Tasks you can immediately start implementing**
✅ **Professional-quality specifications** ready to show stakeholders

### **Expected Results:**
- **Time savings**: 90%+ reduction in planning time
- **Quality**: Professional-grade specifications
- **Consistency**: Standardized project structure
- **Speed**: Complete MVP specification in 2-5 minutes
- **Cost**: $0.50-$5.00 per complete project (depending on provider)

---

## **🔍 Troubleshooting**

### **Common Issues:**

**❌ "No LLM providers available"**
```bash
# Solution: Set at least one API key
export OPENAI_API_KEY="your-key-here"
# OR start local Ollama
ollama serve
```

**❌ "Project already exists"**
```bash
# Solution: Use different project name or add features
./workflow-runner.py --feature=new-feature --existing-project=existing-name --llm-api
```

**❌ "Cost limit exceeded"**
```bash
# Solution: Increase limit or use cheaper provider
./mvp-initializer.py --project=my-app --llm-api --cost-limit=20.0
# OR use free local models
./mvp-initializer.py --project=my-app --llm-api --llm-provider=local_ollama
```

**❌ "Script not found"**
```bash
# Solution: Ensure you're in the correct directory
cd /path/to/dev-utils/dev_workflow
```

### **Getting Help:**
```bash
# Check script options
./mvp-initializer.py --help
./workflow-runner.py --help

# Run system diagnostics  
./test-complete-workflow.py --debug

# Check logs
tail -f workflow-execution.log
tail -f llm-usage.log
```

---

## **🎯 Next Steps**

### **🚀 Your First Project:**
1. **Choose a simple MVP idea** (task manager, blog, e-commerce)
2. **Test the system** with `./test-complete-workflow.py --quick`
3. **Create your MVP** with `./mvp-initializer.py --project=YOUR_IDEA --mode=guided --llm-api`
4. **Review the generated specifications** in `/projects/YOUR_IDEA/`
5. **Add features** with `./workflow-runner.py --feature=FEATURE_NAME --existing-project=YOUR_IDEA --llm-api`
6. **Start building** based on the generated tasks!

### **🌟 Pro Tips:**
- **Start with GUIDED mode** to learn the system
- **Use DRY RUN** to preview what will be created
- **Try different LLM providers** to find your favorite
- **Set cost limits** to manage expenses
- **Keep projects focused** - add features incrementally

---

## **💡 Real-World Examples**

### **Task Management App:**
```bash
./mvp-initializer.py --project=task-manager --mode=autonomous --llm-api
./workflow-runner.py --feature=user-authentication --existing-project=task-manager --llm-api
./workflow-runner.py --feature=team-collaboration --existing-project=task-manager --llm-api
```

### **E-commerce Store:**
```bash
./mvp-initializer.py --project=online-store --mode=guided --llm-api --llm-provider=anthropic
./workflow-runner.py --feature=payment-integration --existing-project=online-store --llm-api
./workflow-runner.py --feature=inventory-management --existing-project=online-store --llm-api
```

### **Content Management System:**
```bash
./mvp-initializer.py --project=cms-platform --mode=autonomous --llm-api --llm-provider=google
./workflow-runner.py --feature=rich-text-editor --existing-project=cms-platform --llm-api
./workflow-runner.py --feature=media-library --existing-project=cms-platform --llm-api
```

---

## **🎊 Ready to Build Amazing Things!**

**You now have the most advanced automated development workflow system available!**

**Start with:**
```bash
./test-complete-workflow.py --quick
./mvp-initializer.py --project=my-first-automated-mvp --mode=guided --llm-api
```

**🚀 Transform your development process from planning to building in minutes, not days!**

---

*Built with ❤️ for developers who want to focus on building, not planning.*
