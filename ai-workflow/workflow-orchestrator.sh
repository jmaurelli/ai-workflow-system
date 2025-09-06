#!/bin/bash

# 🚫 DEPRECATED: This script has been replaced by Python-based workflow
# 
# MIGRATION GUIDE:
# ================
# 
# OLD (Deprecated):
# ./workflow-orchestrator.sh --mode=autonomous --feature=user-auth --llm-api
# 
# NEW (Recommended):
# 
# For NEW MVP projects:
# ./mvp-initializer.py --project=my-app --mode=autonomous --llm-api
# 
# For FEATURES in existing projects:
# ./workflow-runner.py --feature=user-auth --existing-project=my-app --mode=autonomous --llm-api
# 
# For STANDALONE features:
# ./workflow-runner.py --feature=standalone-component --mode=autonomous --llm-api
# 
# BENEFITS OF NEW SYSTEM:
# =======================
# ✅ Clear distinction between MVP creation vs feature addition
# ✅ Organized project structure in /projects/ directory
# ✅ Better context awareness for existing projects
# ✅ Python-based for better portability and extensibility
# ✅ Consistent tooling (no more shell vs Python confusion)
# 
# Please update your workflows to use the new Python-based system!

echo "🚫 DEPRECATED: workflow-orchestrator.sh has been replaced"
echo ""
echo "📖 Please use the new Python-based workflow system:"
echo ""
echo "🚀 For NEW MVP projects:"
echo "   ./mvp-initializer.py --project=my-app --mode=autonomous --llm-api"
echo ""
echo "➕ For FEATURES in existing projects:"
echo "   ./workflow-runner.py --feature=user-auth --existing-project=my-app --mode=autonomous --llm-api"
echo ""
echo "🔧 For STANDALONE features:"
echo "   ./workflow-runner.py --feature=standalone-component --mode=autonomous --llm-api"
echo ""
echo "📖 See automation-quickstart.md for complete migration guide"

exit 1
