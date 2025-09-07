# AI Execution Status: 07-process-tasks.md

```json
{
  "workflow_step": {
    "document": "07-process-tasks.md",
    "step_number": "07",
    "phase": "implementation",
    "timestamp": "2025-09-06T21:34:05.988028"
  },
  "execution_status": "ready_for_ai_agent",
  "ai_prompt_file": "/tmp/tmp55g_5cjj.md",
  "feature_directory": "/home/jmaurelli/Projects/ai-workflow-system/ai-workflow/features/2025-09-06-standalone-20250906-213402",
  "expected_outputs": [
    "  ```bash\n  npx ajv validate -s dev-utils/test/schema.json -d \"test/*.json\" --strict=false\n  ```\n- Example (Python, jsonschema):\n  ```bash\n  python -c 'import json,glob,jsonschema,sys;\\\nfor f in glob.glob(\"test/*.json\"):\\\n  jsonschema.validate(json.load(open(f)), json.load(open(\"dev-utils/test/schema.json\"))) or print(f, \"ok\")' || echo \"validation failed\"\n  ```\n",
    "  - `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'`\n  - Fallback order if unavailable: `main` \u2192 `master`.\n",
    "```json\n{\n  \"feature_slug\": \"[feature-name]\",\n  \"changed_files\": [\"src/...\"],\n  \"last_status\": \"passed|failed|partial\"\n}\n```\n",
    "```json\n{\n  \"stage\": \"process\",\n  \"feature_slug\": \"[feature-name]\",\n  \"default_branch\": \"[detected]\",\n  \"changed_files\": [\"src/...\"],\n  \"targeted_tests\": [\"src/.../__tests__/...test.ts\"],\n  \"json_result_paths\": [\"test/<test_name>.json\"],\n  \"status_summary\": \"passed|failed|partial\",\n  \"dependency_status\": \"blocked|unblocked|complete\",\n  \"risk_status\": \"normal|high_risk|contingency_active\",\n  \"quality_gate_status\": \"week1_complete|week2_complete|week3_complete|week4_complete\"\n}\n```\n",
    "- **Jest:**\n  ```bash\n  jest --runInBand --watch=false --watchAll=false --json --outputFile=test/<test_name>.json <files>\n  ```\n- **Mocha:**\n  ```bash\n  mocha --reporter json <files> > test/<test_name>.json\n  ```\n- **Pytest:**\n  ```bash\n  pytest <files> --json-report --json-report-file=test/<test_name>.json\n  ```\n- **Java (JUnit):**\n  ```bash\n  mvn test -DjsonReportOutput=test/<test_name>.json\n  ```\n- **Next.js:** Same as Jest.\n"
  ],
  "validation_criteria": [
    "- `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'`\n  - Fallback order if unavailable: `main` \u2192 `master`.",
    "- Use task-embedded context for 80% of implementation decisions\n  - Load specific requirement sections only for complex edge cases\n  - Reference design decisions only when implementation approach is unclear\n  - Access learning materials only when encountering new patterns",
    "- **Jest:**\n  ```bash\n  jest --runInBand --watch=false --watchAll=false --json --outputFile=test/<test_name>.json <files>\n  ```\n- **Mocha:**\n  ```bash\n  mocha --reporter json <files> > test/<test_name>.json\n  ```\n- **Pytest:**\n  ```bash\n  pytest <files> --json-report --json-report-file=test/<test_name>.json\n  ```\n- **Java (JUnit):**\n  ```bash\n  mvn test -DjsonReportOutput=test/<test_name>.json\n  ```\n- **Next.js:** Same as Jest.",
    "```bash\n  npx ajv validate -s dev-utils/test/schema.json -d \"test/*.json\" --strict=false\n  ```\n- Example (Python, jsonschema):\n  ```bash\n  python -c 'import json,glob,jsonschema,sys;\\\nfor f in glob.glob(\"test/*.json\"):\\\n  jsonschema.validate(json.load(open(f)), json.load(open(\"dev-utils/test/schema.json\"))) or print(f, \"ok\")' || echo \"validation failed\"\n  ```",
    "```json\n{\n  \"stage\": \"process\",\n  \"feature_slug\": \"[feature-name]\",\n  \"default_branch\": \"[detected]\",\n  \"changed_files\": [\"src/...\"],\n  \"targeted_tests\": [\"src/.../__tests__/...test.ts\"],\n  \"json_result_paths\": [\"test/<test_name>.json\"],\n  \"status_summary\": \"passed|failed|partial\",\n  \"dependency_status\": \"blocked|unblocked|complete\",\n  \"risk_status\": \"normal|high_risk|contingency_active\",\n  \"quality_gate_status\": \"week1_complete|week2_complete|week3_complete|week4_complete\"\n}\n```",
    "be written to `/test/<test_name>.json` and validated directly.",
    "use the precise, non-interactive JSON-producing command for each framework:",
    "contain:",
    "validate and report solely based on JSON file contents."
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

Execute the workflow document `07-process-tasks.md` using the context and data provided.

### Next Steps
1. Read the workflow document
2. Execute the instructions
3. Generate required outputs
4. Validate results
5. Update completion status
