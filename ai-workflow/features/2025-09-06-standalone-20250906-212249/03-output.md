# AI Execution Status: 03-gen-srs.md

```json
{
  "workflow_step": {
    "document": "03-gen-srs.md",
    "step_number": "03",
    "phase": "foundation",
    "timestamp": "2025-09-06T21:22:50.489941"
  },
  "execution_status": "ready_for_ai_agent",
  "ai_prompt_file": "/tmp/tmp0pzi24pr.md",
  "feature_directory": "/home/jmaurelli/Projects/ai-workflow-system/ai-workflow/features/2025-09-06-standalone-20250906-212249",
  "expected_outputs": [
    "```json\n{\n  \"stage\": \"srs\",\n  \"feature_slug\": \"[feature_slug]\",\n  \"srs_path\": \"/srs/srs-[feature_slug].md\",\n  \"nfr_ids\": [\"NFR-1\", \"NFR-2\"],\n  \"budgets\": {\"latency_p50_ms\": 300, \"latency_p95_ms\": 800}\n}\n```\n",
    "./srs.md",
    "/srs/srs-[feature_slug].md",
    "```json\n{\n  \"feature_slug\": \"[feature_slug]\",\n  \"srs_path\": \"/srs/srs-[feature_slug].md\",\n  \"nfr_ids\": [\"NFR-1\", \"NFR-2\"]\n}\n```\n"
  ],
  "validation_criteria": [
    "- **Feature-centric**: Review `./prd.md` to understand functional requirements\n   - **Legacy**: Review `/prd/prd-[feature_slug].md` to understand functional requirements\n2. **Identify NFRs**: List critical constraints and NFRs that affect design/implementation and testing\n3. **Define Budgets**: Set measurable budgets (e.g., p50/p95 latency, error rates, uptime)\n4. **Prioritize**: Keep to \u2264 1 page; prioritize only what must be enforced during MVP\n5. **Save & Validate**: \n   - **Feature-centric**: Save to `./srs.md` and update `./feature-manifest.json`\n   - **Legacy**: Save to `/srs/srs-[feature_slug].md` and validate section order",
    "```json\n{\n  \"stage\": \"srs\",\n  \"feature_slug\": \"[feature_slug]\",\n  \"srs_path\": \"/srs/srs-[feature_slug].md\",\n  \"nfr_ids\": [\"NFR-1\", \"NFR-2\"],\n  \"budgets\": {\"latency_p50_ms\": 300, \"latency_p95_ms\": 800}\n}\n```",
    "be enforced during MVP"
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

Execute the workflow document `03-gen-srs.md` using the context and data provided.

### Next Steps
1. Read the workflow document
2. Execute the instructions
3. Generate required outputs
4. Validate results
5. Update completion status
