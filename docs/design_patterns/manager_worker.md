# Manager–Worker Pattern

## Overview

The **Manager–Worker pattern** divides work between a central coordinator (the manager) and one or more workers.

The manager is responsible for planning, assigning tasks, monitoring progress, and combining results. Workers focus on completing individual tasks without needing to understand the entire workflow.

This separation improves scalability, modularity, and specialization.

```text
          Task
            │
            ▼
        Manager
      ┌────┼────┐
      ▼    ▼    ▼
 Worker A Worker B Worker C
      └────┼────┘
           ▼
      Combined Result
```

The manager coordinates work but does not necessarily perform it.

---

# Core Idea

Separate **coordination** from **execution**.

The manager decides:

- What work needs to be done
- Which worker should perform it
- When work is complete
- How outputs should be combined

Workers simply complete assigned tasks.

---

# Components

## Manager

The manager is responsible for:

- Planning
- Task decomposition
- Worker selection
- Delegation
- Progress monitoring
- Validation
- Result aggregation
- Error handling

The manager should minimize direct execution and focus on orchestration.

---

## Worker

Workers perform specialized tasks.

Examples:

- Research
- Coding
- Retrieval
- Summarization
- Translation
- Image analysis
- Tool execution

Workers should remain independent whenever possible.

---

## Shared Context

Workers often require:

- Task instructions
- Relevant documents
- Tool access
- Constraints
- Success criteria

Only provide workers with the information they need.

---

# Basic Workflow

```text
Receive Task
      │
Manager Plans
      │
Assign Tasks
      │
Workers Execute
      │
Collect Results
      │
Validate Results
      │
Return Final Output
```

---

# Example

User request:

> Analyze our competitors.

Manager creates three tasks.

```text
Worker A

Research Competitors

Worker B

Analyze Pricing

Worker C

Identify Market Trends
```

The manager combines all three reports into a single recommendation.

---

# Task Decomposition

Large tasks should be divided into meaningful subtasks.

Poor:

```text
Worker 1

Write One Paragraph
```

Better:

```text
Worker A

Research

Worker B

Analysis

Worker C

Recommendations
```

Tasks should be independent whenever possible.

---

# Parallel Execution

Independent tasks can execute simultaneously.

```text
Manager

├── Worker A

├── Worker B

├── Worker C

└── Worker D

↓

Merge Results
```

Parallel execution can reduce total latency.

---

# Sequential Delegation

Some work must occur in order.

```text
Research

↓

Analysis

↓

Report Writing
```

Not every workflow benefits from parallelism.

---

# Validation

Managers should verify worker outputs.

Validation may include:

- Completeness
- Correctness
- Formatting
- Policy compliance
- Tool success
- Confidence

Poor-quality outputs should be revised or reassigned.

---

# Worker Specialization

Workers should have clear responsibilities.

Examples:

| Worker | Responsibility |
|---------|----------------|
| Research Worker | Gather information |
| Coding Worker | Write code |
| Retrieval Worker | Search documents |
| Translation Worker | Translate text |
| Planning Worker | Create execution plans |

Avoid overlapping responsibilities.

---

# Load Balancing

When multiple workers share the same capability, managers may distribute work evenly.

Example:

```text
Manager

↓

Available Worker?

├── Worker A

├── Worker B

└── Worker C
```

This improves throughput.

---

# Dynamic Worker Selection

Managers may choose workers based on:

- Expertise
- Availability
- Cost
- Latency
- Confidence
- Required tools

Not every task requires every worker.

---

# Error Handling

If a worker fails:

```text
Worker Failure

↓

Retry

↓

Alternative Worker

↓

Escalate
```

Managers should detect failures rather than silently ignoring them.

---

# Aggregation

Managers combine worker outputs.

Methods include:

- Concatenation
- Ranking
- Voting
- Scoring
- Synthesis
- Majority decision

Aggregation should preserve useful information while resolving conflicts.

---

# When to Use This Pattern

Use the Manager–Worker pattern when:

- Tasks can be decomposed
- Multiple specialists exist
- Parallel execution is valuable
- Large workflows require coordination
- Specialized tools are available

Typical applications include:

- Research assistants
- Document analysis
- Multi-step planning
- Data pipelines
- Code generation
- Enterprise workflows

---

# When Not to Use It

Avoid this pattern when:

- Tasks are very small
- One agent is sufficient
- Coordination exceeds useful work
- Worker specialization adds little value

Simple tasks rarely benefit from delegation.

---

# Common Failure Modes

## Micromanagement

The manager controls every small step.

**Solution**

Delegate meaningful responsibilities.

---

## Poor Task Decomposition

Tasks overlap or depend heavily on one another.

**Solution**

Design independent subtasks.

---

## Idle Workers

Many workers exist but are rarely used.

**Solution**

Reduce unnecessary specialization.

---

## Weak Validation

The manager accepts poor-quality outputs.

**Solution**

Implement explicit validation.

---

## Communication Overhead

Workers spend more time exchanging information than completing tasks.

**Solution**

Minimize unnecessary communication.

---

# Human-in-the-Loop

Managers may escalate difficult tasks.

```text
Manager

↓

Human Reviewer

↓

Continue Workflow
```

Human intervention is useful for high-risk decisions.

---

# No-Code Implementation

Typical workflow:

1. Receive a task.
2. Manager decomposes the task.
3. Route subtasks to workers.
4. Workers execute independently.
5. Collect results.
6. Validate outputs.
7. Merge responses.
8. Return the final answer.

---

# Observability

Track:

- Number of workers
- Task completion time
- Worker utilization
- Failure rate
- Retry count
- Queue length
- Manager decisions
- Aggregation quality

Monitoring helps optimize delegation.

---

# Evaluation Metrics

Useful metrics include:

- Worker accuracy
- Parallel speedup
- Task completion time
- Manager overhead
- Aggregation quality
- Cost per workflow
- Worker utilization
- Success rate

The objective is to improve throughput and quality without introducing unnecessary coordination.

---

# Design Checklist

Before implementing the Manager–Worker pattern, ensure that:

- Workers have clear responsibilities.
- Tasks are independent where possible.
- The manager validates outputs.
- Parallel execution is used appropriately.
- Failure handling exists.
- Aggregation is well defined.
- Worker performance is monitored.
- Human escalation exists for exceptional cases.

---

# Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Clear separation of responsibilities | More orchestration |
| Parallel execution | Coordination overhead |
| Better specialization | Higher operational complexity |
| Easier scaling | More communication |
| Modular architecture | Increased latency for small tasks |

---

# Related Patterns

- Router
- Pipeline
- Generator–Critic
- Debate
- Human-in-the-Loop

---

# Related Anti-Patterns

- God Agent
- Too Many Agents
- Tool Explosion
- Overplanning
- Everything Is an Agent

---

# Pattern Summary

The Manager–Worker pattern separates coordination from execution.

A central manager plans, delegates, validates, and combines work performed by specialized workers. This enables scalable and modular AI systems while allowing workers to focus on well-defined responsibilities. The pattern is most effective when tasks can be decomposed cleanly and the benefits of specialization outweigh the additional coordination overhead.
