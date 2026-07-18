# 12. Multi-Agent Systems

## Purpose

A multi-agent system divides complex work among specialized AI agents
instead of relying on a single general-purpose assistant.

## Learning Objectives

-   Understand multi-agent architectures
-   Compare single and multi-agent systems
-   Design agent roles
-   Choose orchestration patterns
-   Handle routing, monitoring, and failures

------------------------------------------------------------------------

# Benefits

-   Specialization
-   Scalability
-   Better security
-   Parallel work
-   Easier maintenance
-   Reusable agents

# Single vs Multi-Agent

  Single Agent        Multi-Agent
  ------------------- ---------------------
  One prompt          Specialized prompts
  Broad permissions   Least privilege
  Simple              Modular

# Common Agent Roles

-   Coordinator
-   Research
-   Planner
-   Retriever
-   Customer Support
-   Reviewer
-   Compliance
-   Reporting

# Example

``` text
User
 │
 ▼
Coordinator
 ├─ Research
 ├─ Planner
 └─ Support
      │
      ▼
 Reviewer
      │
      ▼
 Final Response
```

# Communication

Prefer structured JSON messages between agents.

``` json
{"task":"summarize","priority":"high"}
```

# Orchestration

## Sequential

Research → Draft → Review

## Parallel

Coordinator → Multiple Specialists → Merge

## Hierarchical

Coordinator → Team Leads → Workers

## Event Driven

Agents react to workflow events.

# Routing

Coordinator responsibilities:

-   Select agent
-   Prevent loops
-   Track workflow state
-   Escalate when needed

# Memory

Options:

-   None
-   Shared knowledge
-   Shared state
-   Agent-specific memory

# Human Review

Review:

-   Financial actions
-   Legal outputs
-   External communications
-   Low-confidence responses

# Monitoring

Track:

-   Delegations
-   Routing accuracy
-   Latency
-   Completion rate
-   Retries
-   Human overrides

# Failure Modes

-   Routing loops
-   Conflicting outputs
-   Missing context
-   Tool failures
-   Infinite delegation

# Best Practices

-   One responsibility per agent
-   Least privilege
-   Structured communication
-   Evaluation per agent
-   Monitor coordination
-   Document escalation

# Common Mistakes

-   Too many agents
-   Overlapping responsibilities
-   Unlimited delegation
-   Shared unrestricted memory

# Related Chapters

  Chapter           Relationship
  ----------------- ------------------------
  02 Workflows      Workflow orchestration
  03 Memory         Shared memory
  05 Routing        Coordinator logic
  08 Human Review   Escalation
  10 Monitoring     Coordination metrics

# Summary

Multi-agent systems improve scalability and maintainability by dividing
work among specialized agents with clearly defined responsibilities,
communication protocols, permissions, and monitoring.
