# Everything Is an Agent

## Overview

The "Everything Is an Agent" anti-pattern occurs when every task in a system is implemented as a separate AI agent, even when a simple function, workflow, or rule-based process would be more appropriate.

Not every problem requires autonomous reasoning. Many tasks are deterministic and can be solved more reliably with conventional software.

A good AI system combines traditional software engineering with AI reasoning, using each where it provides the greatest value.

---

## Why It Happens

Common causes include:

- Excitement about multi-agent systems
- Assuming more agents always improve performance
- Confusing workflows with autonomous reasoning
- Overengineering simple tasks
- Lack of clear architectural boundaries

---

## Example

Poor architecture:

```
User
  ↓
Greeting Agent
  ↓
Validation Agent
  ↓
Formatting Agent
  ↓
Date Conversion Agent
  ↓
Math Agent
  ↓
Response Agent
```

Most of these tasks could be handled with simple code instead of LLM calls.

---

## Why It's a Problem

Using agents for every task can lead to:

- Higher API costs
- Increased latency
- More complex debugging
- Larger context windows
- Harder maintenance
- More points of failure
- Unpredictable behavior

---

## Common Examples

### Example 1

Creating an "Agent" to convert temperatures.

Better:

```
temperature = celsius_to_fahrenheit(c)
```

---

### Example 2

Using an LLM to validate email addresses.

Better:

```
Regular expression
```

---

### Example 3

Creating a "Math Agent" for arithmetic.

Better:

```
Calculator function
```

---

### Example 4

Using an LLM to sort a list.

Better:

```
Built-in sort()
```

---

## Better Architecture

Instead of:

```
Everything
    ↓
Agent
```

Use:

```
Simple task
    ↓
Code

Complex reasoning
    ↓
LLM

Multiple reasoning domains
    ↓
Multi-agent
```

---

## Decision Framework

Ask the following questions:

1. Does this task require reasoning?
2. Is the output deterministic?
3. Can conventional code solve it reliably?
4. Does an LLM provide meaningful additional value?
5. Does the task require planning or judgment?

If the answer to most of these is **no**, an agent is probably unnecessary.

---

## When an Agent Makes Sense

Agents are useful when tasks involve:

- Planning
- Decision making
- Open-ended reasoning
- Tool selection
- Multi-step problem solving
- Working with ambiguous instructions
- Interacting with users

---

## When Code Is Better

Traditional software is often better for:

- Validation
- Calculations
- Parsing
- Data transformation
- Sorting
- Filtering
- File handling
- Authentication
- Database operations
- API requests
- Business rules

---

## Best Practices

- Start with the simplest solution.
- Use code whenever the logic is deterministic.
- Introduce agents only where reasoning adds value.
- Minimize unnecessary LLM calls.
- Separate reasoning from execution.
- Keep architectures as simple as possible.

---

## Related Patterns

- Single Responsibility Principle
- Tool Calling
- Workflow Orchestration
- Routing
- Agent Economics
- Human Review

---

## Anti-pattern Summary

Not every task requires an AI agent.

Use traditional software for deterministic operations and reserve AI agents for problems that require reasoning, planning, or decision making. A well-designed system combines conventional software engineering with AI capabilities rather than replacing everything with agents.
