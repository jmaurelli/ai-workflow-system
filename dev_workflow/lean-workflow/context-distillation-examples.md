# Context Distillation Examples for AI Agents

## Objective
Provide concrete examples of how to distill complex workflow context into actionable, concise task file content that enables effective AI implementation without context window exhaustion.

---

## Example 1: User Authentication Feature

### **Raw Context Sources (Before Distillation)**
- **PRD**: 3 pages covering user stories, workflows, requirements
- **SRS**: 2 pages with 15 NFRs covering performance, security, compliance
- **Design Decisions**: 4 pages covering Python/FastAPI choice, JWT strategy, database selection
- **Design Analysis**: 2 pages covering existing user management component reuse
- **Learning Notes**: Growing document with team confidence levels

**Total Context**: ~11 pages / ~8KB of context

### **Distilled Executive Context (After Distillation)**
```markdown
## Executive Context (Distilled for AI Agents)
**Tech Stack**: FastAPI + Python (rapid dev + team learning), PostgreSQL (relational data), React + TypeScript (component reuse)
**Performance Budgets**: Auth response <500ms (SRS-PERF-003), Login flow <2sec (SRS-PERF-001), JWT validation <50ms (SRS-PERF-005)
**Security Baseline**: OAuth 2.0 + JWT with HMAC-SHA256, 1hr token expiry, password hashing with bcrypt (SRS-SEC-002, SRS-SEC-004)
**Component Strategy**: Reuse existing UserService.get_user(), create new AuthMiddleware, enhance existing LoginForm component
**Learning Context**: Team FastAPI confidence 3/5→4/5, JWT patterns new to team, PostgreSQL familiar 4/5
```

### **Context References (Just-in-Time Loading)**
```markdown
## Context References (Just-in-Time Loading)
**Requirements**: `/prd/prd-auth.md` sections 2.1-2.3 (user flows), 3.1-3.2 (security requirements)
**NFR Specifications**: `/srs/srs-auth.md` REQ-PERF-003, REQ-SEC-002, REQ-SEC-004 (auth performance + security)
**Design Decisions**: `/decisions/design-decisions-auth.md` backend rationale, security pattern choice
**Component Integration**: `/design/design-auth.md` section 2.2 (UserService integration), 3.1 (frontend component reuse)
**Learning Notes**: `/decisions/learning-notes-auth.md` FastAPI + JWT confidence tracking
```

### **Task Context Example**
```markdown
## Tasks (Context-Embedded)
- [ ] 1.0 Implement JWT Authentication Service
  - **Context**: FastAPI service, HMAC-SHA256 signing, 1hr expiry, <50ms validation target, integrate with existing UserService
  - [ ] 1.1 Create JWT token generation - FastAPI dependency injection pattern, bcrypt password verification
  - [ ] 1.2 Implement JWT validation middleware - Request validation, user lookup via UserService.get_user()
  - [ ] 1.3 Add token refresh endpoint - Security: validate existing token, performance: <200ms refresh time
```

---

## Example 2: Real-Time Dashboard Feature

### **Distilled Executive Context**
```markdown
## Executive Context (Distilled for AI Agents)
**Tech Stack**: Node.js + Express (WebSocket support), Redis (real-time caching), React + WebSocket API (chosen for real-time UX)
**Performance Budgets**: Real-time updates <100ms latency (SRS-PERF-001), Dashboard load <3sec (SRS-PERF-002), 1000+ concurrent connections (SRS-SCALE-001)
**Security Baseline**: WebSocket auth via JWT, CORS whitelist, rate limiting 100 updates/sec/user (SRS-SEC-001, SRS-SEC-003)
**Component Strategy**: Create new DashboardWidget components, reuse existing Chart library, enhance DataGrid component
**Learning Context**: Team WebSocket confidence 2/5→3/5, Redis new to team 1/5, React advanced 4/5
```

### **Context References**
```markdown
## Context References (Just-in-Time Loading)
**Requirements**: `/prd/prd-dashboard.md` sections 1.2 (real-time requirements), 2.1-2.4 (widget specifications)
**NFR Specifications**: `/srs/srs-dashboard.md` REQ-PERF-001, REQ-SCALE-001, REQ-SEC-003 (real-time performance + scaling)
**Design Decisions**: `/decisions/design-decisions-dashboard.md` WebSocket vs SSE choice, Redis caching strategy
**Component Integration**: `/design/design-dashboard.md` section 1.3 (Chart library reuse), 2.1 (DataGrid enhancement)
**Learning Notes**: `/decisions/learning-notes-dashboard.md` WebSocket + Redis learning plan
```

### **Task Context Example**
```markdown
## Tasks (Context-Embedded)
- [ ] 2.0 Implement Real-Time WebSocket Service
  - **Context**: Node.js + socket.io, JWT auth for connections, Redis pub/sub for scaling, <100ms update latency target
  - [ ] 2.1 Setup WebSocket server - Express + socket.io integration, JWT middleware for connection auth
  - [ ] 2.2 Implement Redis pub/sub - Message broadcasting pattern, connection scaling across instances
  - [ ] 2.3 Add rate limiting - 100 updates/sec/user limit, graceful degradation for overload
```

---

## Context Distillation Patterns

### **Tech Stack Distillation Pattern**
```
Raw: "We chose Python with FastAPI because the team is familiar with Python from previous projects, and FastAPI provides excellent performance for API development while maintaining Python's readability. The async capabilities align well with our performance requirements..."

Distilled: "FastAPI + Python (team familiar + async performance), PostgreSQL (relational data needs)"
```

### **Performance Budgets Pattern**
```
Raw: "The system must respond to authentication requests within 500 milliseconds 95% of the time. Login flow should complete within 2 seconds including database lookup and token generation..."

Distilled: "Auth response <500ms (SRS-PERF-003), Login flow <2sec (SRS-PERF-001), JWT validation <50ms"
```

### **Security Baseline Pattern**
```
Raw: "Authentication shall use OAuth 2.0 flow with JWT tokens. Tokens must be signed using HMAC-SHA256 algorithm. Token expiry should be set to 1 hour for security. Password storage must use bcrypt hashing..."

Distilled: "OAuth 2.0 + JWT with HMAC-SHA256, 1hr expiry, bcrypt password hashing (SRS-SEC-002, SRS-SEC-004)"
```

### **Component Strategy Pattern**
```
Raw: "Based on the design analysis, we can reuse the existing UserService for user data retrieval. The current LoginForm component needs enhancement for JWT handling. A new AuthMiddleware component will be required..."

Distilled: "Reuse existing UserService.get_user(), create new AuthMiddleware, enhance existing LoginForm component"
```

### **Learning Context Pattern**
```
Raw: "The team has moderate experience with FastAPI (3 out of 5 confidence level) but wants to improve to level 4. JWT implementation patterns are new to the team. PostgreSQL experience is strong at 4 out of 5..."

Distilled: "Team FastAPI confidence 3/5→4/5, JWT patterns new to team, PostgreSQL familiar 4/5"
```

---

## Context Reference Mapping Patterns

### **Specific Section References**
```
Good: `/prd/prd-auth.md` sections 2.1-2.3 (user flows), 3.1-3.2 (security requirements)
Avoid: `/prd/prd-auth.md` (too broad - entire document)
```

### **Requirement ID References**
```
Good: `/srs/srs-auth.md` REQ-PERF-003, REQ-SEC-002, REQ-SEC-004
Avoid: `/srs/srs-auth.md` performance and security (too vague)
```

### **Decision Area References**
```
Good: `/decisions/design-decisions-auth.md` backend rationale, security pattern choice
Avoid: `/decisions/design-decisions-auth.md` all decisions (too broad)
```

---

## Task Context Embedding Guidelines

### **Parent Task Context - Essential Information**
Include:
- **Technology pattern** (FastAPI service, React component, etc.)
- **Key constraints** (performance targets, security requirements)
- **Integration points** (existing services, components to reuse)

Example:
```
- [ ] 1.0 Implement JWT Authentication Service
  - **Context**: FastAPI service, HMAC-SHA256 signing, 1hr expiry, <50ms validation target, integrate with existing UserService
```

### **Subtask Context - Minimal Specific Information**
Include:
- **Specific tech pattern** (middleware pattern, dependency injection)
- **Performance/security target** (specific timing or security requirement)
- **Integration approach** (specific service method, component prop)

Example:
```
- [ ] 1.1 Create JWT token generation - FastAPI dependency injection pattern, bcrypt password verification
- [ ] 1.2 Implement JWT validation middleware - Request validation, user lookup via UserService.get_user()
```

---

## Context Window Management Strategy

### **What Goes in Executive Context (Always Loaded)**
- **Tech stack choices** with brief rationale
- **Critical performance budgets** that affect implementation decisions
- **Essential security requirements** that guide all development
- **Component integration strategy** that affects architecture
- **Learning context** that affects implementation approach

### **What Goes in Context References (Load as Needed)**
- **Detailed requirements** from PRD sections
- **Specific NFRs** with full specification details
- **Design decision rationale** for complex architectural choices
- **Component integration details** for specific reuse patterns
- **Learning progress tracking** for skill development

### **What Goes in Task Context (Minimal per Task)**
- **Technology pattern** for the specific task
- **Performance/security target** that affects implementation
- **Integration approach** for connecting with existing code

This approach ensures AI agents have enough context to implement effectively while managing context window limits efficiently.
