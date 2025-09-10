# 🔍 AI Workflow Validation Guide

**Ensuring consistency and quality across all workflow artifacts**

## 📋 **Validation Checklist**

### **1. JSON Schema Validation**

**Feature Manifest Validation:**
```bash
# Install JSON schema validator (one-time setup)
npm install -g ajv-cli

# Validate feature manifest structure
ajv validate -s feature-manifest.schema.json -d features/*/feature-manifest.json

# Example successful validation
✅ features/2024-01-15-user-auth/feature-manifest.json valid

# Example failed validation  
❌ features/2024-01-15-user-auth/feature-manifest.json invalid
   data/workflow_tracking/current_phase should be equal to one of the allowed values
```

**Integration in Workflow:**
- Automatic validation runs during feature directory creation
- Manual validation available via command line
- IDE integration possible with JSON schema support

### **2. Cross-Document Link Validation**

**Checking Document References:**
```bash
# Find all markdown links in workflow documents
grep -r '\]\(' ai-workflow/lean-workflow/*.md

# Verify link targets exist
find ai-workflow/lean-workflow -name "*.md" -exec grep -l '\]\(' {} \; | \
while read file; do
  echo "Checking links in: $file"
  # Extract and validate each link target
done
```

**Common Link Patterns:**
```markdown
# ✅ Correct relative linking
[02-gen-prd.md](./02-gen-prd.md)
[feature-manifest.json](./feature-manifest.json)
[SRS Performance Requirements](./03-gen-srs.md#performance-requirements)

# ❌ Incorrect linking  
[02-gen-prd.md](02-gen-prd.md)           # Missing ./
[other-doc.md](../other-doc.md)          # Incorrect path
[broken-link](./nonexistent.md)          # Target doesn't exist
```

### **3. Workflow State Consistency**

**Feature Manifest State Validation:**
```json
// ✅ Consistent state
{
  "workflow_tracking": {
    "current_phase": "implementation",
    "phases_completed": ["discovery", "prd", "srs", "design_decisions"]
  },
  "document_status": {
    "prd": {"status": "completed", "path": "./prd.md"},
    "srs": {"status": "completed", "path": "./srs.md"},
    "design_decisions": {"status": "completed", "path": "./design-decisions.md"},
    "tasks": {"status": "in_progress", "path": "./tasks.md"}
  }
}

// ❌ Inconsistent state
{
  "workflow_tracking": {
    "current_phase": "prd",                    // Says we're at PRD phase
    "phases_completed": ["discovery", "prd"]   // But PRD is marked complete
  },
  "document_status": {
    "prd": {"status": "completed"}             // Status matches phases_completed
  }
  // Inconsistency: current_phase should be "srs" not "prd"
}
```

### **4. Document Template Compliance**

**Required Sections Check:**
```markdown
# PRD Template Compliance
## Required Sections:
- [x] # PRD - [Feature Name]
- [x] ## Overview  
- [x] ## Goals
- [x] ## User Stories
- [x] ## Functional Requirements
- [x] ## Success Metrics
- [x] ## Workflow Transition Protocol

# SRS Template Compliance  
## Required Sections:
- [x] # Software Requirements Specification
- [x] ## Performance Requirements
- [x] ## Security Requirements
- [x] ## Quality Standards
- [x] ## Technical Constraints
```

## 🤖 **AI Agent Validation Instructions**

### **Pre-Processing Validation:**
```markdown
**AI Agent Protocol: Document Processing Validation**

1. **Schema Validation First:**
   - Validate feature-manifest.json against schema
   - Halt processing if validation fails
   - Request user to fix schema violations

2. **Document Existence Check:**
   - Verify all referenced documents exist
   - Check ai_navigation paths are valid
   - Confirm artifact directories are present

3. **State Consistency Verification:**
   - current_phase matches document_status
   - phases_completed aligns with completed documents
   - No orphaned or inconsistent state markers
```

### **Post-Processing Validation:**
```markdown
**AI Agent Protocol: Document Generation Validation**

1. **Template Compliance:**
   - Generated document includes all required sections
   - Follows established naming conventions
   - Contains proper cross-document references

2. **Metadata Updates:**
   - Update feature-manifest.json document_status
   - Increment phases_completed appropriately  
   - Set current_phase to next workflow step

3. **Link Validation:**
   - All generated links point to valid targets
   - Cross-references use correct anchor syntax
   - Navigation sections are complete and accurate
```

## 🔧 **Automated Validation Setup**

### **Git Pre-Commit Hook:**
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "🔍 Validating AI workflow artifacts..."

# Validate all feature manifests
find features -name "feature-manifest.json" | while read manifest; do
  if command -v ajv >/dev/null 2>&1; then
    ajv validate -s ai-workflow/lean-workflow/feature-manifest.schema.json -d "$manifest"
    if [ $? -ne 0 ]; then
      echo "❌ Validation failed for: $manifest"
      exit 1
    fi
  fi
done

# Check for broken links in markdown
find ai-workflow -name "*.md" -exec grep -l '\]\(' {} \; | \
while read file; do
  # Extract and validate markdown links
  echo "Checking links in: $file"
done

echo "✅ All validations passed"
```

### **IDE Integration (VS Code):**
```json
// .vscode/settings.json
{
  "json.schemas": [
    {
      "fileMatch": ["**/feature-manifest.json"],
      "url": "./ai-workflow/lean-workflow/feature-manifest.schema.json"
    }
  ],
  "markdown.validate.enabled": true,
  "markdown.validate.fileLinks.enabled": true
}
```

## 📊 **Validation Metrics**

### **Quality Indicators:**
| Metric | Target | Description |
|--------|--------|-------------|
| **Schema Compliance** | 100% | All feature manifests pass validation |
| **Link Integrity** | 100% | All cross-document links resolve |
| **State Consistency** | 100% | Workflow phases match document status |
| **Template Compliance** | 95%+ | Documents follow required structure |

### **Common Issues & Fixes:**

| Issue | Symptoms | Fix |
|-------|----------|-----|
| **Invalid Phase** | `current_phase` not in allowed enum | Update to valid phase name |
| **Broken Links** | 404 on link navigation | Fix relative path or create missing document |
| **Missing Sections** | Template sections absent | Add required sections to document |
| **State Mismatch** | Completed phases don't match status | Sync phases_completed with document_status |

## 🎯 **Best Practices**

### **For Human Developers:**
1. **Validate early**: Run schema validation after each document creation
2. **Check links**: Verify cross-references before committing
3. **State awareness**: Keep workflow phases synchronized
4. **Template compliance**: Use provided templates as guides

### **For AI Agents:**
1. **Schema-first**: Always validate JSON before processing
2. **Link verification**: Check all generated links resolve
3. **State updates**: Maintain consistent workflow state
4. **Error handling**: Gracefully handle validation failures

---

**🔍 Remember**: Validation ensures consistency, improves AI agent reliability, and maintains professional documentation quality across all workflow artifacts.
