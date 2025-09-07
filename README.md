# 🚀 AI Workflow System

**Revolutionary automated development workflow system with real LLM content generation**

Transform your development process from hours of planning to minutes of automation with professional-quality MVP specifications, feature documentation, and development roadmaps.

## 🎯 What This System Does

- **🚀 Create complete MVP projects** with real PRD, SRS, tasks, and specifications
- **➕ Add features to existing projects** with full context awareness  
- **🤖 Generate real content** using 5 different LLM providers (OpenAI, Anthropic, Google, Groq, Ollama)
- **📁 Organize everything** in clean, structured project directories
- **⚡ Save 90%+ of planning time** with professional-quality output

## 🎊 Revolutionary Results

**Before:** Hours/days of manual planning and documentation
**After:** Complete MVP specification in 2-5 minutes with real, actionable content

## 🚀 Quick Start

### 1. Setup
```bash
# Install dependencies  
pip install openai anthropic google-generativeai requests

# Test the system
cd ai-workflow
./test-complete-workflow.py --quick
```

### 2. Create Your First MVP
```bash
# Create a complete MVP project (will prompt for API key)
./workflow-runner.py create-mvp task-manager-app

# Check what was created
ls ~/Projects/task-manager-app/
cat ~/Projects/task-manager-app/features/*/prd.md
```

### 3. Add Features
```bash
# Add features to existing project
./workflow-runner.py add-feature user-authentication --to task-manager-app
```

## 📖 Complete Documentation

**📚 [Python Workflow User Guide](ai-workflow/python-workflow-user-guide.md)** - Complete documentation
**⚡ [Automation Quickstart](ai-workflow/automation-quickstart.md)** - Quick reference
**🔧 [LLM API Setup Guide](ai-workflow/llm-api-setup-guide.md)** - Provider configuration

## 🎯 Core Components

### 🚀 Unified Interface
- **`workflow-runner.py`** - Single tool for all operations
- **Subcommand interface** - `create-mvp`, `add-feature`, `list-projects`, `status`
- **Always-on AI** - Automatic API key prompting and LLM integration

### 📁 Project Management
- **Standard structure** - README, src/, docs/, tests/, features/
- **Context-aware** - Understands existing project structure

### 🤖 LLM Integration
- **5 LLM providers supported** - OpenAI, Anthropic, Google, Groq, Ollama
- **Real content generation** - Not templates, actual specifications
- **Cost management** - Usage tracking and limits

### 🧪 Testing & Validation
- **`test-complete-workflow.py`** - Comprehensive system testing
- **End-to-end validation** - MVP creation, feature addition, error handling

## 📁 Generated Project Structure

```
~/Projects/your-project/
├── 📄 README.md                # Project overview  
├── 📊 project-manifest.json     # Project tracking & metadata
├── 📁 src/                     # Source code
├── 📁 docs/                    # Project documentation
├── 📁 tests/                   # Test files
└── 📁 features/                # AI-generated specifications
    └── 2025-XX-XX-your-project-mvp-initialization/
        ├── 📄 prd.md           # Product Requirements
        ├── 📄 srs.md           # Software Requirements  
        ├── 📄 design-decisions.md  # Technology choices
        ├── 📄 tasks.md         # Development roadmap
        └── 📄 implementation-guide.md  # Development process
```

## 🌟 LLM Providers

The system supports multiple LLM providers and will prompt you to choose:

- **OpenAI** - Most reliable (GPT-4o, GPT-4o-mini, GPT-4-turbo)
- **Anthropic Claude** - Advanced reasoning (Claude 3.5 Sonnet, Haiku, Opus)
- **Google Gemini** - Fast & competitive (Gemini 2.0 Flash, 1.5 Pro, 1.5 Flash)

Advanced users can specify provider/model:
```bash
./workflow-runner.py create-mvp my-project --llm-provider=anthropic --llm-model=claude-3-5-sonnet-20241022
```

## 💡 Real-World Examples

### Task Management App
```bash
./workflow-runner.py create-mvp task-manager --mode=autonomous
./workflow-runner.py add-feature user-authentication --to task-manager
./workflow-runner.py add-feature team-collaboration --to task-manager
```

### E-commerce Store
```bash
./workflow-runner.py create-mvp online-store --mode=guided --llm-provider=anthropic
./workflow-runner.py add-feature payment-integration --to online-store
./workflow-runner.py add-feature inventory-management --to online-store
```

### Project Management Commands
```bash
# List all your projects
./workflow-runner.py list-projects

# Check project status
./workflow-runner.py status task-manager

# See execution plan without running
./workflow-runner.py create-mvp my-app --dry-run
```

## 🔧 Advanced Features

- **Cost Management** - Track and limit LLM usage costs
- **Custom Configuration** - Tailor LLM settings per workflow
- **Multiple Automation Modes** - Guided, autonomous, learning
- **Comprehensive Testing** - Validate entire system functionality
- **Professional Documentation** - Export-ready specifications

## 🎊 Success Metrics

✅ **90%+ time savings** compared to manual planning
✅ **Professional-quality specifications** ready for stakeholders
✅ **Immediate actionability** - tasks ready for development
✅ **Consistent structure** - standardized across all projects
✅ **Cost-effective** - $0.50-$5.00 per complete project specification

## 🚀 Ready to Transform Your Development Workflow?

```bash
cd ai-workflow
./test-complete-workflow.py --quick
./workflow-runner.py create-mvp my-amazing-app --mode=guided
```

**Welcome to the future of automated software development!** 🤖✨

---

*Built with ❤️ for developers who want to focus on building, not planning.*