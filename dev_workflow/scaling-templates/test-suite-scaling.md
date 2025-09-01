# Test Suite Workflow (Scaling)

## Objective
Maintain a complete, standardized test result schema for traceability.  

---

## Schema
```json
{
  "test": "string",
  "status": "pass|fail|skip",
  "duration_ms": 120,
  "coverage": "lines:85, branches:70",
  "timestamp": "2025-08-24T12:00:00Z",
  "logs": "stdout/stderr output"
}
```

---

## Workflow
1. Run all tests.  
2. Record results in `/tests/results/`.  
3. Commit results with build.  

---

## AI Agent Instructions
- Enforce full schema always.  
- Reject incomplete test entries.  
- Aggregate results per feature and per release.  
