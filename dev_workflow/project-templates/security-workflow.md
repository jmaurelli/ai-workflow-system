# 🔹 Security Workflow Protocol

This workflow enforces **basic security hygiene during MVP** while allowing for deeper security practices if the project grows beyond MVP.

---

## 1. Meta Rules
- During MVP: run **lightweight checks** → validate, then delete reports if passing.  
- Post-MVP: enable **persistent logs, advanced scans, and historical tracking**.  
- All security results must be written to `/security/` as JSON. The AI agent must **read files, not terminal output**.  

---

## 2. Secure Development Protocol

### MVP-Level Practices
- **Input Validation:** Validate all external inputs minimally, provide safe defaults.  
- **Output Sanitization:** Prevent obvious injection (HTML, SQL, logs).  
- **Secrets Management:** Never hardcode secrets; load from env variables or config.  
- **Dependencies:** Run quick vulnerability checks (`npm audit`, `pip-audit`, etc.).  

### Post-MVP Enhancements
- Add static analysis (e.g., `semgrep`, `bandit`).  
- Apply principle of least privilege for services and APIs.  
- Conduct threat modeling and penetration testing.  
- Store and review historical security logs.  

---

## 3. Security Testing Protocol

### Rules
- Run framework-appropriate security checks.  
- All results → JSON in `/security/<check_name>.json`.  
- AI agent must open and read JSON files.  
- If vulnerabilities are found → stop and report.  

### Framework-Specific Commands
| Framework | MVP Command | Post-MVP Command |
|-----------|-------------|------------------|
| **Node.js / Next.js** | `npm audit --json > security/npm-audit.json` | Add `npx semgrep --json > security/semgrep.json` |
| **Python** | `pip-audit -f json -o security/pip-audit.json` | Add `bandit -r . -f json -o security/bandit.json` |
| **Java (Maven)** | `mvn org.owasp:dependency-check-maven:check -Dformat=JSON -DoutputDirectory=security` | Add `spotbugs` or `semgrep` scans |
| **General** | — | Integrate static analysis, SAST/DAST tools |

---

## 4. Workflow Quick Checklist
1. **Plan**: Identify security-sensitive code and dependencies.  
2. **Run**: Execute MVP security scans → JSON output in `/security/`.  
3. **Validate**: Open and read JSON reports; confirm pass/fail.  
4. **Delete**: If all pass (MVP), delete JSON files. Retain only on failures.  
5. **Expand**: Post-MVP, retain logs + add deeper scans.  

---

## 5. Success Criteria

### MVP
- No high/critical dependency vulnerabilities.  
- No hardcoded secrets.  
- No obvious injection or unsafe inputs/outputs.  
- JSON reports deleted after successful runs.  

### Post-MVP
- Persistent logs retained.  
- Regular static and dynamic analysis.  
- Verified least-privilege and threat modeling completed.  
- Clear audit trail of security practices.  

---
