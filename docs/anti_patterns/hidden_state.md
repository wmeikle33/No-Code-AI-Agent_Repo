# Hidden State

## Overview

The "Hidden State" anti-pattern occurs when an AI agent's behavior depends on information that is not obvious, visible, or easy to inspect.

Instead of producing results solely from the current inputs, the agent is influenced by hidden context such as conversation history, memory, cached data, previous tool calls, or external systems.

Hidden state makes systems difficult to understand, debug, reproduce, and test.

---

## Why It Happens

Common causes include:

- Long conversation histories
- Persistent memory
- Cached tool results
- Session variables
- External databases
- Environment configuration
- Implicit assumptions between agents

---

## Example

```
User Request
      ↓
Current Prompt
      ↓
Conversation History
      ↓
Memory Store
      ↓
Cached Results
      ↓
Previous Tool Calls
      ↓
External State
      ↓
Final Response
```

Although the user only sees the current request, the response may depend on several hidden sources of information.

---

## Why It's a Problem

Hidden state can cause:

- Inconsistent responses
- Difficult debugging
- Non-reproducible behavior
- Unexpected side effects
- Incorrect assumptions
- Fragile workflows
- Poor testability

Small changes to hidden state can produce completely different outputs.

---

## Common Examples

### Example 1

An agent answers differently because an old conversation remains in context.

The current prompt is identical, but the hidden conversation history changes the result.

---

### Example 2

A memory store contains outdated customer information.

The agent continues using the stale data even after the user provides updated details.

---

### Example 3

A cached API response is returned after the underlying data has changed.

The user receives outdated information without realizing it.

---

### Example 4

A downstream agent assumes that another agent has already validated user input.

The validation never occurred, leading to incorrect behavior.

---

## Better Architecture

Instead of relying on hidden state:

```
Input
    ↓
Explicit Context
    ↓
Visible Memory
    ↓
Visible Tool Results
    ↓
Response
```

Every important piece of information should be traceable.

---

## Warning Signs

Your system may have hidden state if:

- Bugs cannot be reproduced consistently.
- Restarting the application fixes problems.
- Different users receive different results from identical inputs.
- Developers cannot explain why an agent made a decision.
- Testing requires recreating long conversations.
- State exists outside the visible workflow.

---

## Better Alternatives

Reduce hidden state by:

- Passing required context explicitly.
- Logging important decisions.
- Versioning memory.
- Keeping workflows deterministic where possible.
- Making tool outputs visible.
- Resetting temporary state when appropriate.
- Clearly documenting state dependencies.

---

## Best Practices

- Make state explicit whenever possible.
- Keep memory transparent.
- Avoid unnecessary global state.
- Separate temporary and persistent memory.
- Record important tool outputs.
- Ensure workflows can be reproduced.

---

## Related Patterns

- Memory
- Context Engineering
- Monitoring
- Evaluation
- Tool Calling
- Workflow Orchestration

---

## Anti-pattern Summary

Hidden state occurs when an AI agent depends on information that is not obvious or visible.

Making important state explicit improves reliability, debugging, reproducibility, and maintainability.
