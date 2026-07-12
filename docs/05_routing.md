# 05. Routing

## Overview

Routing is the process of determining how a request moves through an AI system. It decides **which workflow, agent, tool, or execution path** should handle a request based on its content, context, risk, and business rules.

Effective routing improves efficiency, reduces costs, increases accuracy, and ensures requests are handled by the most appropriate components.

Routing is one of the core responsibilities of an AI orchestration layer.

---

# Objectives

A routing system should:

- Select the appropriate workflow
- Choose the correct agent
- Determine when tools are required
- Minimize unnecessary LLM calls
- Apply business rules consistently
- Support human escalation
- Improve reliability and scalability
- Remain observable and explainable

---

# Routing Architecture

```text
                   User Request
                         │
                         ▼
                Input Validation
                         │
                         ▼
                 Request Classification
                         │
                         ▼
               Routing Decision Engine
                         │
      ┌──────────────┬───────────────┬──────────────┐
      ▼              ▼               ▼              ▼
 Workflow A     Workflow B     Workflow C     Human Review
      │              │               │
      ▼              ▼               ▼
   Agent A       Agent B        Agent C
      │              │               │
      └──────────────┴───────────────┘
                     ▼
              Generate Response
```

---

# Why Routing Matters

Without routing:

- Every request is handled by the same agent.
- Specialized capabilities are underutilized.
- Costs increase.
- Latency increases.
- Responses become less accurate.

With effective routing:

- Requests reach the best agent.
- Resources are used efficiently.
- Complex systems remain maintainable.
- New agents can be added without redesigning the entire architecture.

---

# Types of Routing

## Rule-Based Routing

Routing decisions are made using predefined rules.

Example:

```text
If request contains:

"refund"

↓

Customer Support Agent
```

Advantages:

- Predictable
- Fast
- Easy to audit

Disadvantages:

- Difficult to scale
- Limited flexibility

Best suited for:

- Simple business rules
- Compliance requirements
- Deterministic workflows

---

## Classification-Based Routing

A classification model determines the request category.

Example:

```text
Incoming Request

↓

Intent Classification

↓

Billing

↓

Billing Agent
```

Advantages:

- More flexible
- Handles varied language
- Easy to expand

---

## LLM-Based Routing

An LLM reasons about the request and selects the most appropriate path.

Example:

```text
User Request

↓

Routing Prompt

↓

Selected Agent
```

Useful when:

- Requests are complex
- Categories overlap
- Context matters

Risks:

- Higher cost
- Increased latency
- Potential inconsistency

---

## Hybrid Routing

Combines multiple routing methods.

Example:

```text
Security Request

↓

Rule-Based Validation

↓

LLM Classification

↓

Workflow Selection
```

Hybrid routing often provides the best balance between reliability and flexibility.

---

# Routing Levels

Large AI systems may route at multiple levels.

## Workflow Routing

Determine which workflow should execute.

Example:

- Customer Support
- Research
- Scheduling
- Analytics

---

## Agent Routing

Select the most appropriate agent.

Example:

```text
Research Request

↓

Market Research Agent
```

---

## Tool Routing

Determine whether external tools are required.

Example:

```text
Calendar Question

↓

Calendar Tool
```

---

## Knowledge Routing

Select the correct knowledge source.

Examples:

- Internal documentation
- Product catalog
- Policy database
- External search

---

## Human Routing

Escalate requests requiring human review.

Examples:

- Legal decisions
- Financial approvals
- Security incidents
- Low-confidence responses

---

# Routing Criteria

Routing decisions may consider:

- User intent
- Conversation history
- User role
- Risk level
- Confidence score
- Available tools
- Cost constraints
- Latency requirements
- Business policies
- Agent availability

---

# Routing Workflow

```text
Receive Request
        │
        ▼
Validate Input
        │
        ▼
Classify Intent
        │
        ▼
Determine Risk
        │
        ▼
Select Workflow
        │
        ▼
Select Agent
        │
        ▼
Determine Tool Usage
        │
        ▼
Execute
```

---

# Confidence-Based Routing

Confidence scores may influence routing decisions.

Example:

```text
Confidence ≥ 0.90

↓

Return Response

------------------

Confidence 0.60–0.89

↓

Additional Verification

------------------

Confidence < 0.60

↓

Human Review
```

Thresholds should be defined according to organizational policies.

---

# Multi-Agent Routing

Some requests require multiple agents.

Example:

```text
Executive Request

↓

Planner

↓

Research Agent

↓

Financial Agent

↓

Reviewer

↓

Final Response
```

The coordinator manages communication between agents.

---

# Dynamic Routing

Routing decisions may change during execution.

Example:

```text
Customer Support Agent

↓

Unable to Answer

↓

Knowledge Search

↓

Still Unresolved

↓

Human Escalation
```

Dynamic routing improves resilience.

---

# Fallback Routing

Every routing strategy should define fallback behavior.

Example:

```text
Primary Agent

↓

Failure

↓

Secondary Agent

↓

Failure

↓

Human Review
```

Fallback paths reduce system downtime.

---

# Routing Governance

Routing policies should specify:

- Allowed workflows
- Approved agents
- Escalation rules
- Confidence thresholds
- Cost limits
- Latency targets
- Human approval requirements

Routing decisions should be reproducible and auditable.

---

# Routing Evaluation

Useful metrics include:

| Metric | Description |
|----------|-------------|
| Routing Accuracy | Correct destination selected |
| Escalation Rate | Percentage requiring human review |
| Average Latency | Time before execution begins |
| Misrouting Rate | Incorrect routing decisions |
| Workflow Success Rate | Successful workflow completion |
| Cost per Request | Average routing cost |

---

# Common Routing Patterns

## Single Agent

```text
User

↓

One Agent

↓

Response
```

Best for:

- Small applications
- Low complexity

---

## Router Pattern

```text
User

↓

Router

↓

Specialized Agent
```

Best for:

- Multiple business domains

---

## Planner–Executor

```text
Planner

↓

Task List

↓

Executor
```

Best for:

- Complex reasoning
- Long-running tasks

---

## Coordinator Pattern

```text
Coordinator

↓

Multiple Agents

↓

Merged Response
```

Best for:

- Enterprise AI systems
- Multi-domain requests

---

# Common Challenges

Typical routing issues include:

- Ambiguous requests
- Incorrect classification
- Conflicting business rules
- Excessive routing layers
- High latency
- Expensive LLM routing
- Poor fallback behavior
- Inconsistent routing decisions

These can often be reduced through hybrid routing strategies and continuous evaluation.

---

# Relationship to Other Components

| Component | Relationship |
|------------|--------------|
| `framework/workflows/` | Routing selects workflows |
| `framework/agents/` | Routing selects agents |
| `framework/tools/` | Routing determines tool usage |
| `framework/knowledge/` | Routing chooses knowledge sources |
| `framework/patterns/` | Implements routing strategies |
| `docs/02_workflows.md` | Defines execution order |
| `docs/04_tools.md` | Explains tool selection |
| `docs/07_patterns.md` | Describes orchestration patterns |

---

# Best Practices

- Keep routing logic separate from agent logic.
- Prefer deterministic routing when appropriate.
- Use LLM routing only when additional reasoning is beneficial.
- Define clear fallback paths.
- Minimize unnecessary routing steps.
- Log every routing decision.
- Evaluate routing performance regularly.
- Make routing decisions explainable.
- Review routing policies as new agents are added.
- Continuously improve routing based on production metrics.

---

# Key Takeaways

- Routing determines how requests move through an AI system.
- Effective routing improves scalability, efficiency, and response quality.
- Routing may occur at the workflow, agent, tool, knowledge, and human-review levels.
- Hybrid routing strategies often provide the best balance of flexibility and reliability.
- Well-governed routing systems are observable, explainable, and continuously evaluated.
