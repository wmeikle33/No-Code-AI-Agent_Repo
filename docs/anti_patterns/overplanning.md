# Overplanning

## Overview

The **Overplanning** anti-pattern occurs when an AI agent spends excessive time creating, refining, or expanding plans instead of executing meaningful work.

While planning is an important capability, excessive planning increases latency, cost, and complexity without improving the final outcome. In many cases, the agent repeatedly generates new plans rather than acting on the existing one.

Effective AI systems balance planning with execution.

---

## Why It Happens

Common causes include:

- Assuming more planning always produces better results
- Recursive planning loops
- Lack of execution confidence
- Poor stopping conditions
- Complex planning prompts
- Missing execution triggers
- Unlimited planning depth

---

## Example

Poor workflow:

```text
Create Plan
      ↓
Review Plan
      ↓
Improve Plan
      ↓
Review Again
      ↓
Expand Plan
      ↓
Review Again
      ↓
...
```

The agent never begins executing the task.

---

## Why It's a Problem

Overplanning can lead to:

- Increased latency
- Higher API costs
- Excessive token usage
- Decision paralysis
- Infinite planning loops
- Delayed task completion
- Poor user experience

Users typically value completed work over increasingly detailed plans.

---

## Common Examples

### Example 1: Research Agent

The agent repeatedly refines a research strategy instead of gathering information.

---

### Example 2: Coding Assistant

The agent generates increasingly detailed implementation plans but never starts writing code.

---

### Example 3: Travel Planner

The agent continues evaluating destinations, hotels, and transportation options without producing a final itinerary.

---

### Example 4: Multi-Agent Planning

A planner repeatedly sends tasks back for additional refinement instead of assigning them for execution.

---

## Better Architecture

Instead of:

```text
Plan
   ↓
Improve Plan
   ↓
Improve Plan
   ↓
Improve Plan
```

Use:

```text
Plan
   ↓
Execute
   ↓
Evaluate
   ↓
Revise if Necessary
```

Planning should support execution, not replace it.

---

## Decision Framework

Before creating a more detailed plan, ask:

1. Is the current plan sufficient to begin execution?
2. Will additional planning significantly improve the outcome?
3. Is new information required before proceeding?
4. Has planning exceeded its time or iteration budget?
5. Would execution provide better feedback than further planning?

If the answer to most of these questions is **no**, begin execution.

---

## Warning Signs

Your system may be overplanning if:

- Planning consumes more time than execution.
- The agent repeatedly rewrites plans.
- New subtasks continue to appear without being completed.
- Execution is continually postponed.
- Costs increase before any useful work is performed.
- Users receive plans instead of results.

---

## Better Alternatives

Reduce unnecessary planning by:

- Limiting planning iterations.
- Setting planning time budgets.
- Breaking work into smaller executable tasks.
- Executing after a minimum viable plan.
- Revising plans only when new information becomes available.
- Measuring progress based on completed work.

---

## Planning Levels

Different tasks require different amounts of planning.

| Task | Recommended Planning |
|------|-----------------------|
| Arithmetic | None |
| Email drafting | Minimal |
| Document summarization | Minimal |
| Data analysis | Moderate |
| Research | Moderate |
| Software design | High |
| Multi-agent coordination | High |

Not every task benefits from extensive planning.

---

## Plan-Execute Cycle

A balanced workflow follows a simple cycle:

```text
Goal
   ↓
Plan
   ↓
Execute
   ↓
Evaluate
   ↓
Finished?
   ├── Yes → Complete
   └── No → Update Plan
```

Execution should provide feedback that improves future planning.

---

## Agent Economics

Overplanning increases:

- API costs
- Token consumption
- Response latency
- Compute usage

In many cases, a shorter plan followed by execution is both cheaper and more effective than repeatedly refining the plan.

---

## Best Practices

- Plan only as much as necessary.
- Set limits on planning iterations.
- Execute early and refine later.
- Measure progress using completed work.
- Use planning to reduce uncertainty, not eliminate it entirely.
- Allow execution to inform future planning.
- Prefer iterative improvement over exhaustive upfront planning.

---

## Related Anti-patterns

- Infinite Loops
- Blind Retries
- God Agent
- Model Overkill

---

## Related Concepts

- Planning agents
- Workflow orchestration
- Reflection
- Task decomposition
- Agent economics
- Iterative development

---

## Anti-pattern Summary

Planning is valuable only when it leads to execution.

Well-designed AI systems create plans that are sufficient to begin meaningful work, then improve those plans through execution and feedback rather than endless refinement.
