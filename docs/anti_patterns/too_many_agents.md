# Too Many Agents

## Overview

The **Too Many Agents** anti-pattern occurs when an AI system contains more specialized agents than are necessary to solve the problem effectively.

While dividing responsibilities can improve modularity, excessive specialization increases communication, orchestration, debugging, and maintenance complexity.

Every additional agent should provide measurable value to the overall system.

---

## Why It Happens

Common causes include:

- Excessive specialization
- Splitting simple tasks into separate agents
- Constantly creating new agents instead of improving existing ones
- Poor architectural boundaries
- Optimizing for modularity instead of simplicity
- Copying large multi-agent architectures without understanding their purpose

---

## Example

Poor architecture:

```text
User
   ↓
Router

   ├── Greeting Agent
   ├── Formatting Agent
   ├── Grammar Agent
   ├── Citation Agent
   ├── Tone Agent
   ├── Emoji Agent
   ├── Signature Agent
   ├── Validation Agent
   ├── Summary Agent
   └── Output Agent
```

Most of these tasks could be handled by a single agent or deterministic code.

---

## Why It's a Problem

Using too many agents can lead to:

- Higher API costs
- Increased latency
- Larger context transfers
- Communication overhead
- More orchestration logic
- Difficult debugging
- More failure points
- Lower reliability

As the number of agents grows, the complexity of coordinating them grows as well.

---

## Common Examples

### Example 1

Creating separate agents for:

- Grammar
- Tone
- Formatting
- Style

A single writing agent could perform all four tasks.

---

### Example 2

Building five research agents that repeatedly search the same sources.

---

### Example 3

Creating separate agents for:

- Date formatting
- Number formatting
- JSON validation

These tasks are better handled by code.

---

## Better Architecture

Instead of:

```text
One Task
     ↓
Many Tiny Agents
```

Use:

```text
One Responsibility
        ↓
One Agent
```

Agents should own meaningful responsibilities rather than tiny operations.

---

## Agent Granularity

Poor granularity:

```
Greeting Agent

↓

Question Agent

↓

Grammar Agent

↓

Formatting Agent
```

Better granularity:

```
Customer Support Agent

↓

Tool Calling

↓

Response
```

Each agent should perform a complete, coherent responsibility.

---

## Decision Framework

Before adding another agent, ask:

1. Does this responsibility already belong to an existing agent?
2. Would a tool or function be simpler?
3. Is the new agent solving a real architectural problem?
4. Can this task be grouped with similar responsibilities?
5. Will the additional complexity improve quality?

If not, another agent is probably unnecessary.

---

## Warning Signs

Your architecture may contain too many agents if:

- Several agents perform very similar tasks.
- Communication exceeds useful work.
- Most agents are rarely used.
- Debugging requires tracing long chains of agents.
- Small changes require modifying many agents.
- API costs grow faster than functionality.

---

## Better Alternatives

Instead of creating another agent, consider:

- Improving prompts
- Better routing
- Tool calling
- Conventional code
- Workflow orchestration
- Refactoring existing agents

---

## Agent Economics

Every additional agent introduces costs:

- API requests
- Context transfer
- Latency
- Monitoring
- Testing
- Maintenance

An agent should exist only if its benefits outweigh these costs.

---

## Best Practices

- Give every agent a clear responsibility.
- Avoid unnecessary specialization.
- Combine closely related tasks.
- Use code for deterministic operations.
- Measure the value of each agent.
- Review architectures regularly as systems grow.

---

## Related Anti-patterns

- Premature Multi-Agent
- Everything Is an Agent
- God Agent
- Model Overkill

---

## Related Concepts

- Agent specialization
- Routing
- Workflow orchestration
- Single Responsibility Principle
- Agent economics

---

## Anti-pattern Summary

Adding more agents does not automatically create a better AI system.

Well-designed architectures use the smallest number of agents needed to provide clear, meaningful separation of responsibilities while keeping coordination simple.
