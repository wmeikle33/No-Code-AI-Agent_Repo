# Architecture

## Overview

The No-Code AI Agent Repository is organized as a modular AI-agent platform. The system separates agent behavior, workflow orchestration, tool execution, external integrations, authentication, permissions, and deployment infrastructure into independent layers.

This separation makes the platform easier to extend, test, secure, and deploy.

---

## High-Level Architecture

```text
User / Application
        ↓
API or CLI Entry Point
        ↓
Workflow Router
        ↓
Workflow Orchestration Layer
        ↓
Agent Layer
        ↓
Tool Layer
        ↓
Connector Layer
        ↓
External Systems
```

---

## Core Layers

### 1. Entry Point Layer

The entry point layer receives user requests from interfaces such as:

- CLI commands
- API endpoints
- Web applications
- Scheduled jobs
- Webhook events

Example files:

```text
run_demo.py
api/
app/
```

---

### 2. Workflow Routing Layer

The workflow router determines which workflow should handle an incoming request.

Responsibilities:

- Classify requests
- Select workflows
- Route inputs
- Handle fallback behavior

Example files:

```text
workflows/router.py
workflows/workflow_registry.py
```

---

### 3. Workflow Orchestration Layer

Workflows define the sequence of steps required to complete a task.

A workflow may use one agent or multiple agents.

Example:

```text
Support Request
      ↓
Customer Support Agent
      ↓
Lead Qualification Agent
      ↓
CRM Tool
      ↓
Final Response
```

Example files:

```text
workflows/customer_support_workflow.py
workflows/support_to_lead_workflow.py
workflows/document_qa_workflow.py
```

---

### 4. Agent Layer

Agents contain task-specific behavior.

Each agent usually includes:

```text
agent.json
system_prompt.md
examples/
tests/
```

Example agents:

```text
agents/customer_support_agent/
agents/lead_qualification_agent/
agents/document_qa_agent/
agents/pipeline_orchestration_agent/
```

Agents should not directly access external systems. They should request actions through approved tools.

---

### 5. Tool Layer

Tools are safe, reusable actions that agents are allowed to call.

Examples:

```text
tools/crm/create_lead.py
tools/email/draft_email.py
tools/search/knowledge_search.py
tools/documents/summarize_document.py
tools/webhooks/send_webhook.py
```

Tools should:

- Validate inputs
- Check permissions
- Call connectors when needed
- Return structured outputs
- Log execution results

---

### 6. Connector Layer

Connectors handle communication with external systems.

Examples:

```text
connectors/google/
connectors/microsoft/
connectors/slack/
connectors/github/
connectors/salesforce/
```

Connectors are responsible for:

- API authentication
- Request formatting
- Response normalization
- Token refresh
- Rate-limit handling

---

### 7. Authentication and Permission Layer

The authentication layer controls identity, authorization, OAuth flows, and agent permissions.

Example files:

```text
code_modules/auth/oauth/
code_modules/auth/permissions/
```

Permissions follow the principle of least privilege.

Agents should only receive the minimum access required to perform their task.

---

### 8. Knowledge and RAG Layer

The knowledge layer supports retrieval-augmented generation.

Responsibilities:

- Document ingestion
- Chunking
- Embedding generation
- Vector search
- Citation tracking
- Knowledge-base querying

Example files:

```text
code_modules/knowledge/
code_modules/retrieval/
code_modules/embeddings/
```

---

### 9. Data and Persistence Layer

The persistence layer stores workflow state, logs, agent metadata, OAuth connections, documents, embeddings, and audit records.

Possible storage systems:

```text
PostgreSQL
SQLite
Vector database
Object storage
```

Example files:

```text
code_modules/database/
code_modules/storage/
migrations/
```

---

### 10. Monitoring and Governance Layer

This layer tracks system health, workflow outcomes, tool usage, agent failures, and security events.

Example capabilities:

- Audit logs
- Error reporting
- Workflow traces
- Human approval checkpoints
- Incident response

Example files:

```text
docs/security/
docs/governance/
code_modules/monitoring/
```

---

## Repository Structure

```text
No-Code-AI-Agent_Repo/
├── agents/
├── workflows/
├── code_modules/
│   ├── auth/
│   ├── tools/
│   ├── connectors/
│   ├── knowledge/
│   ├── database/
│   └── utils/
├── docs/
├── examples/
├── tests/
├── infra/
└── run_demo.py
```

---

## Agent Lifecycle

```text
Create agent folder
      ↓
Define agent.json
      ↓
Write system_prompt.md
      ↓
Assign permissions
      ↓
Register agent
      ↓
Connect tools
      ↓
Add tests
      ↓
Use in workflow
```

---

## Workflow Lifecycle

```text
Request received
      ↓
Router selects workflow
      ↓
Workflow validates input
      ↓
Workflow selects agent(s)
      ↓
Agents call approved tools
      ↓
Tools call connectors
      ↓
Results are aggregated
      ↓
Logs and audit records are saved
      ↓
Response is returned
```

---

## Security Model

The platform uses a layered security model:

```text
User authentication
        ↓
Agent permissions
        ↓
Tool authorization
        ↓
Connector scopes
        ↓
Audit logging
```

Key principles:

- Deny by default
- Least privilege
- Explicit tool grants
- Scoped OAuth access
- No direct secret exposure to agents
- Human approval for sensitive actions

---

## Example End-to-End Flow

### Support-to-Lead Workflow

```text
1. User submits a customer support request.
2. Router selects support_to_lead_workflow.
3. Customer Support Agent analyzes the issue.
4. Lead Qualification Agent checks buying intent.
5. CRM tool creates or updates a lead.
6. Notification tool alerts the sales team.
7. Workflow summary is logged.
8. Final response is returned.
```

---

## Extensibility

The system is designed so new components can be added independently.

To add a new agent:

```text
agents/new_agent/
├── agent.json
├── system_prompt.md
└── examples/
```

To add a new tool:

```text
code_modules/tools/new_tool.py
```

To add a new connector:

```text
code_modules/connectors/new_service/
```

To add a new workflow:

```text
workflows/new_workflow.py
```

---

## Design Principles

- Modular architecture
- Configuration-driven agents
- Reusable tools
- Secure connectors
- Workflow-based orchestration
- Explicit permissions
- Auditable execution
- Human-in-the-loop support
- Easy local development
- Production deployment readiness

---

## Future Architecture Goals

Planned improvements may include:

- Web-based workflow builder
- Visual agent designer
- Hosted API service
- Multi-tenant permission model
- Advanced observability dashboard
- Agent evaluation framework
- Automated regression testing
- Human approval queue
- Connector marketplace
