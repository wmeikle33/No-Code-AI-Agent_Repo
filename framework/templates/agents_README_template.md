# {{AGENT_NAME}}

> **Status:** Draft | Production | Deprecated
>
> **Version:** 1.0
>
> **Category:** {{Customer Support | Research | Compliance | Sales | Analytics | Operations | etc.}}

---

# Overview

## Purpose

Briefly describe what this agent does.

Answer:

- Why does this agent exist?
- What business problem does it solve?
- Who benefits from it?

Example:

> The Customer Support Agent assists customers by answering product questions, troubleshooting issues, retrieving documentation, and escalating complex requests while maintaining a consistent support experience.

---

# Responsibilities

List everything this agent is expected to do.

Example:

- Retrieve relevant knowledge
- Answer user questions
- Use external tools
- Generate structured reports
- Summarize documents
- Escalate complex requests

---

# Non-Responsibilities

Clearly define what the agent should **not** do.

Example:

- Make legal decisions
- Execute financial transactions
- Approve contracts
- Invent missing information
- Ignore company policy

---

# Target Users

Who is this agent designed for?

Examples:

- Customers
- Employees
- Sales representatives
- Compliance officers
- Executives
- Developers

---

# Typical Use Cases

Describe the most common scenarios.

Example:

## Use Case 1

Description...

---

## Use Case 2

Description...

---

## Use Case 3

Description...

---

# Inputs

Describe the information the agent expects.

Typical inputs include:

- User request
- Uploaded files
- Customer profile
- Internal documents
- Knowledge base
- Database records

Example:

```json
{
  "user_request": "...",
  "context": "...",
  "documents": []
}
```

---

# Outputs

Describe the expected outputs.

Examples:

- Markdown report
- JSON response
- Executive summary
- Email draft
- Ticket
- Recommendation
- Checklist

Example:

```json
{
  "status": "...",
  "summary": "...",
  "confidence": "..."
}
```

---

# Required Knowledge

What information should this agent have access to?

Examples:

- Product documentation
- Company handbook
- Policies
- SOPs
- FAQs
- Knowledge Base
- Technical documentation
- Internal wiki

---

# Required Tools

List the tools the agent may use.

Examples:

- Web Search
- RAG
- Database Query
- CRM
- Email
- Calendar
- Calculator
- Code Interpreter
- Ticket System

---

# Workflow

Describe the overall workflow.

```
Receive Request
       │
       ▼
Validate Input
       │
       ▼
Retrieve Context
       │
       ▼
Reason
       │
       ▼
Use Tools
       │
       ▼
Generate Response
       │
       ▼
Validate Output
       │
       ▼
Return Result
```

---

# Decision Rules

Describe important business rules.

Examples:

- Always verify user identity before accessing records.
- Never answer using unsupported information.
- Escalate requests requiring human approval.
- Require citations for policy questions.

---

# Output Structure

Describe the preferred response format.

Example:

1. Summary
2. Analysis
3. Recommendations
4. Risks
5. References
6. Confidence Level

---

# Confidence Levels

Define confidence ratings.

| Level | Meaning |
|--------|----------|
| High | Strong supporting evidence |
| Medium | Some uncertainty |
| Low | Limited evidence |

---

# Risk Levels

(Optional)

| Level | Description |
|--------|-------------|
| Low | Minimal impact |
| Medium | Moderate impact |
| High | Significant business impact |
| Critical | Legal, financial, or safety risk |

---

# Human Review

Describe when human review is required.

Examples:

- Legal decisions
- Financial approval
- Customer complaints
- Policy exceptions
- Low-confidence responses
- High-risk recommendations

---

# Safety Considerations

Describe safety boundaries.

Examples:

- Never fabricate information.
- Protect confidential data.
- Respect access permissions.
- Follow company policy.
- Refuse unsafe requests.

---

# Design Principles

List the principles guiding this agent.

Example:

1. Accuracy over speed.
2. Transparency over certainty.
3. Evidence over assumptions.
4. Human review for critical decisions.
5. Clear communication.

---

# Performance Metrics

How is this agent evaluated?

Examples:

- Accuracy
- Response time
- Hallucination rate
- User satisfaction
- Citation accuracy
- Cost
- Escalation accuracy

---

# Evaluation

Evaluation cases are stored in:

```
evaluation_cases.json
```

Typical evaluation categories:

- Accuracy
- Tool usage
- Reasoning
- Hallucination resistance
- Output quality
- Safety
- Policy compliance

---

# Failure Modes

Common failure modes are documented in:

```
failure_modes.md
```

Examples:

- Hallucination
- Missing information
- Tool failures
- Incorrect reasoning
- Unsafe recommendations
- Policy violations

---

# Integration Points

This agent commonly integrates with:

- Knowledge Base
- Database
- Email
- CRM
- Ticket System
- Calendar
- APIs
- Internal Services

---

# Related Files

```
agent.json
system_prompt.md
evaluation_cases.json
failure_modes.md
```

---

# Future Improvements

Potential enhancements:

- Better retrieval
- Additional tools
- Improved evaluation
- Multi-agent collaboration
- Memory integration
- Workflow automation

---

# Dependencies

List any required dependencies.

Examples:

- Shared prompts
- Knowledge collections
- APIs
- External services
- Internal workflows

---

# Version History

| Version | Date | Changes |
|----------|------|----------|
| 1.0 | YYYY-MM-DD | Initial version |

---

# Maintainers

| Role | Owner |
|-------|-------|
| Product | |
| Engineering | |
| Prompt Engineering | |
| QA | |

---

# Notes

Additional implementation notes, assumptions, or limitations.
