# 🚀 AI Workflow System

**Intelligent MVP development with enhanced questioning framework and conversational AI guidance**

Transform your development process from hours of planning to 10 minutes of comprehensive automation with professional-quality MVP specifications, feature documentation, and development roadmaps powered by conversational AI.

## 🎯 What This System Does

- **🚀 Create complete MVP projects** with enhanced questioning framework for rich context
- **👥 Collect user stories** through conversational Q&A with pain point analysis
- **💼 Capture business context** with value propositions and success metrics
- **🤖 AI-guided tech stack selection** with pros/cons analysis and assumption challenges
- **➕ Add features to existing projects** with full context awareness  
- **📁 Generate professional documentation** (PRD, SRS, tasks, architecture) in structured project directories
- **⚡ Save 90%+ of planning time** with 10-minute comprehensive project initialization

## 🧠 Enhanced Questioning Framework

### 👥 User Context Collection (3-4 minutes)
- **Primary user identification** and pain point analysis
- **User success journey** mapping (2-3 step ideal scenarios)
- **Access pattern assessment** with conditional device/platform specifics

### 💼 Business Context Gathering (2-3 minutes)
- **Value proposition** definition (free tool, paid service, efficiency gain)
- **Key success metrics** for measurable validation
- **3-month success criteria** for MVP validation

### 🏗️ Technical Guidance with AI (4-5 minutes)
- **Complexity assessment** (simple/medium/complex) with immediate AI guidance
- **Team skills and constraints** analysis
- **Conversational AI tech stack consultation** with 2-3 recommendations
- **AI challenges assumptions** and suggests alternatives with reasoning capture

## 🚀 Quick Start

### 1. Setup
```bash
# Install dependencies  
pip install openai anthropic google-generativeai requests

# Test the system
cd ai-workflow
./test-complete-workflow.py --quick
```

### 2. Create Your First Enhanced MVP
```bash
# Create a complete MVP project with enhanced questioning
./workflow-runner.py create-mvp task-manager-app

# The system will guide you through:
# - User story collection (who, pain points, success journey)
# - Business model and success metrics
# - AI-guided tech stack selection with pros/cons
# - Final confirmation with complete decision summary

# Check what was created
ls ~/Projects/task-manager-app/
cat ~/Projects/task-manager-app/features/*/prd.md
```

### 3. Add Features
```bash
# Add features to existing project
./workflow-runner.py add-feature user-authentication task-manager-app
```

## 📖 Complete Documentation

**📚 [Python Workflow User Guide](ai-workflow/python-workflow-user-guide.md)** - Complete documentation
**⚡ [Automation Quickstart](ai-workflow/automation-quickstart.md)** - Quick reference
**🔧 [LLM API Setup Guide](ai-workflow/llm-api-setup-guide.md)** - Provider configuration

## 🎯 Core Components

### 🚀 Unified CLI Interface
- **`workflow-runner.py`** - Single entry point for all operations
- **Intuitive subcommands** - `create-mvp PROJECT_NAME`, `add-feature FEATURE_NAME PROJECT_NAME`
- **Enhanced help documentation** - Comprehensive `--help` with examples and use cases
- **Always-on AI** - Automatic API key prompting and LLM integration

### 🧠 Enhanced Interactive Collection
- **EnhancedInteractiveDataCollector** - 10+ comprehensive data fields
- **Conversational AI tech stack guidance** - Real-time recommendations with reasoning
- **Human gates** - Prompted conditional questions for optional details
- **Mental flow optimization** - Questions grouped by concern (User → Business → Technical)

### 📁 Project Management
- **Standard structure** - README, src/, docs/, tests/, features/
- **Rich metadata capture** - Business model, user stories, technical reasoning
- **Context-aware** - Understands existing project structure

### 🤖 LLM Integration
- **5 LLM providers supported** - OpenAI, Anthropic, Google, Groq, Ollama
- **Consistent model usage** - User selection respected across all workflow steps
- **Real content generation** - Rich context produces detailed, actionable specifications
- **Cost management** - Usage tracking and limits

## 📁 Generated Project Structure

```
~/Projects/your-project/
├── 📄 README.md                # Project overview  
├── 📊 project-manifest.json     # Project tracking & metadata
├── 📁 src/                     # Source code
├── 📁 docs/                    # Project documentation
├── 📁 tests/                   # Test files
└── 📁 features/                # AI-generated specifications with rich context
    └── 2025-XX-XX-your-project-mvp-initialization/
        ├── 📄 project-initialization.md  # Enhanced initialization document
        ├── 📄 collected-project-data.json  # Structured collected data
        ├── 📄 prd.md           # Product Requirements with user stories
        ├── 📄 srs.md           # Software Requirements with business context
        ├── 📄 design-decisions.md  # AI-guided technology choices with reasoning
        ├── 📄 tasks.md         # Development roadmap with rich context
        └── 📄 implementation-guide.md  # Development process
```

## 🌟 LLM Providers

The system supports multiple LLM providers with consistent model usage:

- **OpenAI** - Most reliable (GPT-4o, GPT-4o-mini, GPT-4-turbo)
- **Anthropic Claude** - Advanced reasoning (Claude 3.5 Sonnet, Haiku, Opus)
- **Google Gemini** - Fast & competitive (Gemini 2.0 Flash, 1.5 Pro, 1.5 Flash)

Advanced users can specify provider/model:
```bash
./workflow-runner.py create-mvp my-project --llm-provider=anthropic --llm-model=claude-3-5-sonnet-20241022
```

## 💡 Real-World Examples

### Task Management App with Enhanced Context
```bash
./workflow-runner.py create-mvp task-manager --mode=guided
# System asks: Who are your users? (Small team leads managing project deadlines)
# System asks: What's their pain point? (Losing track of tasks in scattered tools)  
# System asks: Success journey? (1. Add task quickly, 2. See team progress, 3. Hit deadlines)
# AI recommends: Simple web app with real-time updates
```

### E-commerce Store with AI Guidance
```bash
./workflow-runner.py create-mvp online-store --mode=autonomous
# System collects business model, complexity assessment
# AI challenges: "You said complex e-commerce but have a solo team - consider starting simpler?"
# AI recommends tech stack with reasoning captured in documentation
```

### Project Management Commands
```bash
# List all your projects with enhanced metadata
./workflow-runner.py list-projects

# Check project status with collected context
./workflow-runner.py status task-manager

# See enhanced execution plan
./workflow-runner.py create-mvp my-app --dry-run
```

## 🔧 Advanced Features

- **Enhanced Questioning Framework** - 10+ data fields vs basic 9 questions
- **Conversational AI Guidance** - Real-time tech stack recommendations with pros/cons
- **AI Reasoning Capture** - All AI decisions and rationale included in documentation
- **Human Gates** - Optional conditional questions for additional context
- **Cost Management** - Track and limit LLM usage costs
- **Custom Configuration** - Tailor LLM settings per workflow
- **Multiple Automation Modes** - Guided (recommended), autonomous, learning
- **Comprehensive Testing** - Validate entire enhanced system functionality

## 🎊 Success Metrics

✅ **90%+ time savings** with 10-minute comprehensive initialization
✅ **Rich context collection** - User stories, business model, technical reasoning
✅ **AI-guided decisions** - Tech stack recommendations with captured rationale
✅ **Professional-quality specifications** ready for stakeholders
✅ **Immediate actionability** - Tasks with business and user context
✅ **Consistent structure** - Standardized across all projects
✅ **Cost-effective** - $0.50-$5.00 per complete project specification

## 🚀 Ready to Transform Your Development Workflow?

```bash
cd ai-workflow
./test-complete-workflow.py --quick
./workflow-runner.py create-mvp my-amazing-app --mode=guided
```

Experience the power of **conversational AI guidance** and **enhanced context collection** for comprehensive MVP development in just 10 minutes!

**Welcome to the future of intelligent software development!** 🤖✨

---

*Built with ❤️ for developers who want rich context and AI guidance without the time investment.*