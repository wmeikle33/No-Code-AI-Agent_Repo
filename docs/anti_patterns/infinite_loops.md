# Infinite Loops

## Overview

The "Infinite Loops" anti-pattern occurs when an AI agent repeatedly performs the same actions without making meaningful progress toward completing a task.

Unlike traditional software bugs, AI agent loops often arise from reasoning failures, poor stopping conditions, or workflows that continually generate new tasks for themselves.

Every autonomous workflow should have clear termination conditions.

---

## Why It Happens

Common causes include:

- Missing stopping conditions
- Blind retries
- Recursive planning
- Reflection without limits
- Tool failures
- Circular workflows
- Poor success detection

---

## Example

Bad workflow:

```
Plan
   ↓
Execute
   ↓
Review
   ↓
Needs Improvement
   ↓
Plan Again
   ↓
Execute
   ↓
Review
   ↓
Needs Improvement
   ↓
...
```

The workflow never reaches completion.

---

## Why It's a Problem

Infinite loops can lead to:

- High API costs
- Increased latency
- Excessive token usage
- Rate limiting
- Duplicate tool calls
- Poor user experience
- Resource exhaustion

In severe cases, an agent may never return a response.

---

## Common Examples

### Example 1

An agent repeatedly retries an API request after receiving a permanent authentication error.

---

### Example 2

A planning agent continually creates new subtasks instead of completing existing ones.

---

### Example 3

A self-review agent keeps deciding that its answer "could be improved" and rewrites it indefinitely.

---

### Example 4

Two agents repeatedly hand a task back and forth because each believes the other should handle it.

```
Agent A
    ↓
Agent B
    ↓
Agent A
    ↓
Agent B
```

---

## Better Architecture

Instead of:

```
Repeat
    ↓
Repeat
    ↓
Repeat
```

Use:

```
Attempt
    ↓
Evaluate Progress
    ↓
Complete?
 ├── Yes → Finish
 └── No
       ↓
Retry Limit Reached?
 ├── Yes → Escalate
 └── No → Retry
```

---

## Warning Signs

Your system may contain infinite loops if:

- The same tool is repeatedly called.
- Identical prompts appear multiple times.
- Costs continue increasing without progress.
- Logs show repeated execution paths.
- Responses never complete.
- Planning repeatedly generates similar tasks.

---

## Better Alternatives

Prevent loops by:

- Setting maximum retry counts.
- Limiting planning depth.
- Limiting reflection cycles.
- Detecting repeated actions.
- Tracking workflow progress.
- Escalating persistent failures.
- Using timeouts.

---

## Best Practices

- Define clear stopping conditions.
- Monitor execution progress.
- Detect repeated states.
- Set maximum execution time.
- Limit recursive workflows.
- Log every iteration.
- Return partial results when appropriate.

---

## Related Patterns

- Blind Retries
- God Agent
- Reflection
- Workflow Orchestration
- Monitoring
- Human Review

---

## Anti-pattern Summary

Infinite loops occur when an AI agent continues executing without making meaningful progress.

Well-designed AI systems include explicit stopping conditions, retry limits, and progress checks to ensure workflows eventually terminate.
