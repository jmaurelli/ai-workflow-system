# AI Execution Status: 02-gen-prd.md

```json
{
  "workflow_step": {
    "document": "02-gen-prd.md",
    "step_number": "02",
    "phase": "foundation",
    "timestamp": "2025-09-06T21:34:05.487313"
  },
  "execution_status": "ready_for_ai_agent",
  "ai_prompt_file": "/tmp/tmpazdzjchd.md",
  "feature_directory": "/home/jmaurelli/Projects/ai-workflow-system/ai-workflow/features/2025-09-06-standalone-20250906-213402",
  "expected_outputs": [
    "  ```bash\n  if [[ \"$PWD\" == */features/*-* ]]; then\n    PRD_PATH=\"./prd.md\"\n    UPDATE_MANIFEST=true\n  else\n    mkdir -p \"/prd\"\n    PRD_PATH=\"/prd/prd-[feature-name].md\"\n    UPDATE_MANIFEST=false\n  fi\n  ```\n- Limit Lean PRDs to one page and \u2264 400 words\n- Validate that the file exists, is accessible, and that all template sections appear in the specified order. If validation fails, self-correct before completion\n- Include the optional Linkages section with appropriate paths (feature-centric vs legacy)\nSet reasoning_effort = minimal; keep outputs concise and focused.\n",
    "/prd/prd-[feature-name].md",
    "- The feature is cross-functional,\n- It has a significant impact on architecture or design,\n- Or additional collaborators will be involved.\n\nIf added complexity or NFRs are material to MVP execution, generate a Lean SRS using `gen-srs.md` before creating tasks.\n",
    "```json\n{\n  \"feature_slug\": \"[feature-name]\",\n  \"prd_path\": \"/prd/prd-[feature-name].md\",\n  \"requirement_ids\": [\"REQ-1\", \"REQ-2\"]\n}\n```\n",
    "./prd.md"
  ],
  "validation_criteria": [
    "- The feature is cross-functional,\n- It has a significant impact on architecture or design,\n- Or additional collaborators will be involved.\n\nIf added complexity or NFRs are material to MVP execution, generate a Lean SRS using `gen-srs.md` before creating tasks.",
    "```bash\n  if [[ \"$PWD\" == */features/*-* ]]; then\n    PRD_PATH=\"./prd.md\"\n    UPDATE_MANIFEST=true\n  else\n    mkdir -p \"/prd\"\n    PRD_PATH=\"/prd/prd-[feature-name].md\"\n    UPDATE_MANIFEST=false\n  fi\n  ```\n- Limit Lean PRDs to one page and \u2264 400 words\n- Validate that the file exists, is accessible, and that all template sections appear in the specified order. If validation fails, self-correct before completion\n- Include the optional Linkages section with appropriate paths (feature-centric vs legacy)\nSet reasoning_effort = minimal; keep outputs concise and focused.",
    "be lightweight, actionable, and quick to produce, with the flexibility to be expanded into a Full PRD if needed."
  ],
  "completion_status": {
    "started": false,
    "completed": false,
    "validated": false,
    "errors": []
  }
}
```

## Instructions for AI Agent

Execute the workflow document `02-gen-prd.md` using the context and data provided.

### Next Steps
1. Read the workflow document
2. Execute the instructions
3. Generate required outputs
4. Validate results
5. Update completion status
