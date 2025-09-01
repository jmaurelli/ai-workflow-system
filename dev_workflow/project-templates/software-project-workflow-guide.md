Developer: Follow this Software Project Workflow Guide (MVP-First).

Main Instruction:
Use **MVP Mode** by default for all software project workflows unless otherwise specified.

Context:
'''
## Modes
- 🚀 **MVP Mode (default):** Lean documentation, minimal tests, fast coding.
- 🛠️ **Enhancement Mode:** Full documentation, TDD, expanded test suite.

---

## MVP Mode Workflow
1. Start with an idea, create `create-prd.md` for a lean PRD.
2. Use `generate-tasks.md` to produce the task file from the PRD.
3. Complete tasks with code and minimal smoke tests.
4. Deploy quickly.

---

## Enhancement Mode Workflow
1. Expand lean PRD into a full PRD.
2. Expand tasks into full TDD tasks.
3. Run a complete test suite.
4. Perform formal deployment and monitoring.

---

## AI Agent Instructions
- Always default to MVP Mode.
- Switch to Enhancement Mode only if explicitly requested.
'''
Output formats:
- Use bullet points for workflow steps.
- Clearly distinguish between MVP and Enhancement modes.