#!/bin/bash
# Activate AI Workflow Environment
echo "🚀 Activating AI Workflow Environment..."
cd /home/jmaurelli/Projects/ai-workflow-system/ai-workflow
source ai-workflow-env/bin/activate
echo "✅ Environment activated! You can now run:"
echo "  python3 ./mvp-initializer.py --ai-first --llm-api"
echo "  python3 ./workflow-runner.py --feature=your-feature --llm-api"
bash
