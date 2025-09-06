# 🚀 LLM API Setup Guide - Revolutionary Automation

*Transform your workflow from planning to REAL content generation!*

## 🎯 **WHAT THIS ENABLES**

### **❌ BEFORE: Planning Only**
```bash
./workflow-orchestrator.sh --mode=autonomous --feature=user-auth
# ✅ Creates: Feature directory structure
# ✅ Creates: AI execution instructions  
# ❌ BUT: No actual content generated - requires external AI agent
```

### **🚀 AFTER: Complete Automation**
```bash
./workflow-orchestrator.sh --mode=autonomous --feature=user-auth --llm-api
# ✅ Creates: Feature directory structure
# ✅ Creates: AI execution instructions
# ✅ GENERATES: Real PRD content via LLM API
# ✅ GENERATES: Real SRS content via LLM API
# ✅ GENERATES: Real tasks content via LLM API
# ✅ RESULT: Complete project ready for development!
```

---

## 🔧 **API PROVIDER SETUP**

### **🤖 Option 1: OpenAI (GPT-3.5/GPT-4)**

**1. Get API Key:**
- Visit: https://platform.openai.com/api-keys
- Create new secret key
- Copy the key (starts with `sk-`)

**2. Set Environment Variable:**
```bash
export OPENAI_API_KEY="sk-your-actual-key-here"

# Add to your shell profile for persistence:
echo 'export OPENAI_API_KEY="sk-your-actual-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**3. Test Integration:**
```bash
./test-llm-automation.sh
```

### **🧠 Option 2: Anthropic Claude**

**1. Get API Key:**
- Visit: https://console.anthropic.com/
- Create new API key
- Copy the key

**2. Set Environment Variable:**
```bash
export ANTHROPIC_API_KEY="your-claude-key-here"

# Add to your shell profile:
echo 'export ANTHROPIC_API_KEY="your-claude-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**3. Test Integration:**
```bash
./test-llm-automation.sh
```

### **⚡ Option 3: Groq (Ultra-Fast)**

**1. Get API Key:**
- Visit: https://console.groq.com/keys
- Create new API key
- Copy the key

**2. Set Environment Variable:**
```bash
export GROQ_API_KEY="your-groq-key-here"

# Add to your shell profile:
echo 'export GROQ_API_KEY="your-groq-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### **🏠 Option 4: Local Ollama (Free!)**

**1. Install Ollama:**
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model (e.g., Llama 3.1)
ollama pull llama3.1:8b
```

**2. Start Ollama Server:**
```bash
ollama serve
```

**3. Test Integration:**
```bash
./test-llm-automation.sh
```

---

## 🎯 **USAGE EXAMPLES**

### **🚀 Basic LLM Automation**
```bash
# OpenAI GPT-3.5 automation
./workflow-orchestrator.sh --mode=autonomous --feature=user-auth --llm-api --llm-provider=openai

# Anthropic Claude automation  
./ai-workflow-runner.py --mode=autonomous --feature=dashboard --llm-api --llm-provider=anthropic

# Local Ollama automation (free!)
./workflow-orchestrator.sh --mode=guided --feature=api-v2 --llm-api --llm-provider=local_ollama
```

### **🎛️ Advanced Configuration**
```bash
# Custom model and cost limits
./ai-workflow-runner.py --mode=autonomous --feature=e-commerce \
    --llm-api --llm-provider=openai --llm-model=gpt-4 --cost-limit=25.0

# Custom LLM configuration file
./workflow-orchestrator.sh --mode=learning --feature=chat-system \
    --llm-api --llm-config=custom-llm-config.json
```

### **🧪 Testing and Validation**
```bash
# Test all LLM integrations
./test-llm-automation.sh

# Test specific content generation
python3 content-generation-engine.py --workflow-document=02-gen-prd.md \
    --feature-name="Payment Gateway" --feature-dir=./test-feature \
    --content-type=prd --output-file=prd.md
```

---

## ⚙️ **CONFIGURATION OPTIONS**

### **LLM Configuration File (`llm-config.json`)**
```json
{
  "default_provider": "openai",
  "providers": {
    "openai": {
      "provider": "openai",
      "model": "gpt-3.5-turbo",
      "max_tokens": 4000,
      "temperature": 0.7,
      "cost_limit_usd": 10.0
    },
    "anthropic": {
      "provider": "anthropic", 
      "model": "claude-3-5-sonnet-20241022",
      "max_tokens": 4000,
      "temperature": 0.7,
      "cost_limit_usd": 15.0
    }
  },
  "workflow_specific_configs": {
    "gen_prd": {
      "provider": "openai",
      "model": "gpt-3.5-turbo",
      "temperature": 0.6,
      "system_prompt": "You are an expert product manager..."
    }
  }
}
```

### **Cost Management**
```bash
# Set daily cost limits
export LLM_COST_LIMIT=50.0

# Monitor usage
tail -f llm-usage.log

# Override cost limits per run
./workflow-orchestrator.sh --mode=autonomous --feature=big-project \
    --llm-api --cost-limit=100.0
```

---

## 🎯 **WORKFLOW COMPARISON**

### **Traditional Workflow (Manual)**
```bash
# 1. Manual execution of each step
./workflow-orchestrator.sh --mode=guided --feature=user-auth
# → Creates instructions, requires human to read and execute

# 2. Human reads 01-output.md and manually creates content
# 3. Human reads 02-output.md and manually creates PRD  
# 4. Human reads 03-output.md and manually creates SRS
# 5. Continue manually through all 9 steps...

# Result: Takes hours/days, requires constant human intervention
```

### **🚀 LLM Automated Workflow (Revolutionary)**
```bash
# 1. Single command with LLM automation
./workflow-orchestrator.sh --mode=autonomous --feature=user-auth --llm-api

# → Automatically executes ALL 9 workflow steps
# → Generates REAL content for each step
# → Creates complete project structure
# → Ready for development in minutes!

# Result: Complete automation in minutes, minimal human intervention
```

---

## 🔍 **TROUBLESHOOTING**

### **Common Issues:**

**❌ "No LLM providers available"**
```bash
# Solution: Set at least one API key
export OPENAI_API_KEY="your-key-here"
# OR
ollama serve  # Start local Ollama
```

**❌ "ImportError: No module named 'openai'"**
```bash
# Solution: Install required packages
pip install openai anthropic requests
```

**❌ "Cost limit exceeded"**
```bash
# Solution: Increase cost limit or use cheaper provider
./workflow-orchestrator.sh --feature=test --llm-api --cost-limit=20.0
# OR
./workflow-orchestrator.sh --feature=test --llm-api --llm-provider=local_ollama
```

**❌ "API key invalid"**
```bash
# Solution: Verify API key is correct
echo $OPENAI_API_KEY  # Should show your key
# Re-export if needed
export OPENAI_API_KEY="sk-correct-key-here"
```

### **Debugging:**
```bash
# Enable debug mode
./workflow-orchestrator.sh --feature=test --llm-api --verbose

# Test individual components
python3 llm-api-integration.py --provider=openai --prompt="Test prompt"

# Check logs
tail -f workflow-execution.log
tail -f llm-usage.log
```

---

## 🎉 **SUCCESS VALIDATION**

### **✅ You'll Know It's Working When:**

1. **Test Suite Passes:**
```bash
./test-llm-automation.sh
# Should show: "🎉 ALL TESTS PASSED! LLM API automation is WORKING!"
```

2. **Real Content Generated:**
```bash
ls features/YYYY-MM-DD-your-feature/
# Should contain: prd.md, srs.md, tasks.md, etc. with REAL content
```

3. **Complete Automation:**
```bash
./workflow-orchestrator.sh --mode=autonomous --feature=test-feature --llm-api
# Should run through all 9 steps automatically and generate complete project
```

### **🚀 Expected Results:**
- **Feature directory created** with date prefix
- **Real PRD content** (not templates) generated
- **Real SRS content** with specific requirements  
- **Real task breakdown** with acceptance criteria
- **Complete project structure** ready for development
- **All within minutes** instead of hours/days

---

## 🌟 **WHAT'S DIFFERENT NOW**

### **Before LLM Integration:**
- ❌ Created planning documents only
- ❌ Required external AI agent in IDE
- ❌ Manual content creation for each step
- ❌ Hours/days to complete workflow
- ❌ Inconsistent output quality

### **After LLM Integration:**
- ✅ **Generates real content automatically**
- ✅ **Complete CLI independence** 
- ✅ **End-to-end automation**
- ✅ **Minutes to complete full workflow**
- ✅ **Consistent, high-quality output**
- ✅ **Multiple LLM provider support**
- ✅ **Cost management and monitoring**
- ✅ **Revolutionary productivity boost**

---

## 🎯 **NEXT STEPS**

1. **Choose your LLM provider** (OpenAI recommended for beginners)
2. **Set up API keys** using the instructions above
3. **Run the test suite** to validate everything works
4. **Try your first automated workflow:**
   ```bash
   ./workflow-orchestrator.sh --mode=autonomous --feature=my-first-llm-project --llm-api
   ```
5. **Watch the magic happen** as real content gets generated automatically!

**🚀 Welcome to the future of automated software development workflows!**
