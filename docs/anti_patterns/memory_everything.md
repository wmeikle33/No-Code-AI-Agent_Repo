# Memory Everything

## Overview

The **Memory Everything** anti-pattern occurs when an AI agent stores nearly every interaction, observation, tool result, and intermediate output in long-term memory.

This approach assumes that retaining more information will always improve future performance. In practice, excessive memory often makes an agent slower, more expensive, less predictable, and more likely to use irrelevant or outdated information.

Good memory systems are selective. They preserve information that is useful later and discard information that is temporary, redundant, sensitive, or low value.

---

## Why It Happens

Common causes include:

- Assuming more context always improves performance
- Treating conversation history as permanent memory
- Lacking rules for what should be stored
- Avoiding difficult memory-selection decisions
- Storing data "just in case"
- Confusing logs with agent memory
- Failing to define retention or deletion policies

---

## Example

Poor memory strategy:

```text
Every user message
        ↓
Every agent response
        ↓
Every tool result
        ↓
Every intermediate draft
        ↓
Every failed attempt
        ↓
Permanent memory
```

Over time, the memory store fills with duplicated, outdated, and irrelevant information.

---

## Why It's a Problem

Storing everything can lead to:

- Higher storage and retrieval costs
- Larger context windows
- Increased latency
- Irrelevant memories influencing responses
- Outdated information overriding newer facts
- Conflicting user preferences
- Privacy and compliance risks
- Difficult debugging
- Poor retrieval quality

A larger memory store can make useful information harder to find.

---

## Common Examples

### Example 1: Saving Temporary Requests

A user says:

> Use a formal tone for this email.

The agent stores this as a permanent preference and continues using a formal tone in unrelated conversations.

This instruction was temporary and should have applied only to the current task.

---

### Example 2: Saving Outdated Information

A customer changes their delivery address.

The memory system stores the new address but does not remove or supersede the old one.

Later, the agent retrieves both addresses and cannot determine which is correct.

---

### Example 3: Saving Tool Noise

An agent permanently stores:

- API status messages
- Temporary search results
- Failed tool responses
- Debugging information
- Intermediate calculations

These records rarely improve future tasks and may reduce retrieval quality.

---

### Example 4: Saving Intermediate Drafts

A writing agent creates five drafts before producing a final answer.

All five drafts are stored in memory.

Later retrieval may return an incomplete draft instead of the approved final version.

---

## Memory Is Not the Same as Logging

Logs and memory serve different purposes.

| System | Purpose |
|---------|---------|
| Memory | Improve future agent behavior |
| Logs | Support monitoring, auditing, and debugging |
| Conversation history | Preserve short-term context |
| Database | Store authoritative application data |
| Cache | Reuse temporary results |

Operational logs should not automatically become agent memory.

Similarly, authoritative customer or business data should usually remain in a structured database rather than being copied into an unstructured memory store.

---

## Better Architecture

Instead of storing everything:

```text
New Information
       ↓
Is it useful later?
   ├── No → Discard
   └── Yes
         ↓
Is it already stored?
   ├── Yes → Update or merge
   └── No
         ↓
Is it safe and appropriate to retain?
   ├── No → Do not store
   └── Yes → Save with metadata
```

Memory should pass through a selection process before it is retained.

---

## What Should Usually Be Stored

Long-term memory may be appropriate for:

- Stable user preferences
- Confirmed long-term goals
- Important decisions
- Ongoing project context
- Reusable facts
- Approved summaries
- Unresolved commitments
- Information the user explicitly asks the system to remember

---

## What Should Usually Not Be Stored

Avoid storing:

- Temporary instructions
- One-time requests
- Failed tool outputs
- Intermediate reasoning
- Duplicate information
- Unverified assumptions
- Sensitive information without a clear need
- Data that already exists in an authoritative system
- Short-lived search results
- Casual conversation with no future value

---

## Memory Selection Framework

Before storing information, ask:

1. Will this information likely be useful in a future interaction?
2. Is it expected to remain valid?
3. Is it already stored elsewhere?
4. Is the information verified?
5. Is it safe and appropriate to retain?
6. Can the user inspect, update, or delete it?
7. Does storing it justify the added cost and complexity?

If the answer to several of these questions is no, the information probably should not become long-term memory.

---

## Memory Quality Dimensions

A useful memory system should evaluate information across several dimensions.

| Dimension | Question |
|-----------|----------|
| Relevance | Will this help with future tasks? |
| Stability | Is it likely to remain true? |
| Confidence | Has the information been verified? |
| Uniqueness | Is it already stored? |
| Sensitivity | Is it appropriate to retain? |
| Recency | Has newer information replaced it? |
| Importance | Would forgetting it meaningfully reduce quality? |

---

## Warning Signs

Your system may be storing too much if:

- Memory grows continuously without pruning.
- Retrieval returns irrelevant results.
- Old information frequently conflicts with new information.
- Identical facts appear multiple times.
- Context windows are dominated by memory.
- Users are surprised by what the system remembers.
- Memory costs increase faster than usage.
- Developers cannot explain why a memory was stored.

---

## Better Alternatives

Use a combination of:

- Short-term conversation context
- Selective long-term memory
- Structured user profiles
- Summarization
- Memory expiration
- Deduplication
- Confidence scoring
- Versioning
- User-controlled memory
- External databases for authoritative records

Not every piece of information belongs in the same storage system.

---

## Memory Lifecycle

Memory should be managed throughout its lifecycle.

```text
Capture
   ↓
Validate
   ↓
Classify
   ↓
Store
   ↓
Retrieve
   ↓
Update
   ↓
Expire or Delete
```

A memory system that only stores information but never updates or removes it will become less reliable over time.

---

## Memory Expiration

Some information should automatically expire.

Examples include:

- Temporary preferences
- Current travel plans
- Short-term project status
- Time-sensitive search results
- Session-specific instructions
- Temporary access details

Expiration can be based on:

- Time
- Task completion
- Project completion
- Replacement by newer information
- User request

---

## Handling Conflicting Memories

When new information conflicts with existing memory, the system should not simply store both versions without explanation.

A better process is:

```text
New Information
       ↓
Conflict Detected
       ↓
Determine Authority and Recency
       ↓
Update, Supersede, or Ask for Confirmation
```

Important memories should include timestamps, sources, confidence levels, and version history.

---

## Best Practices

- Store only information with clear future value.
- Separate short-term context from long-term memory.
- Keep authoritative data in structured systems.
- Deduplicate similar memories.
- Add timestamps and source metadata.
- Expire temporary information.
- Replace outdated facts instead of accumulating conflicts.
- Give users control over stored memory.
- Review memory quality regularly.
- Retrieve only the minimum relevant context.

---

## Related Anti-patterns

- Hidden State
- God Agent
- Infinite Loops
- Blind Retries

---

## Related Concepts

- Context engineering
- Memory retrieval
- Memory pruning
- Summarization
- Data retention
- Privacy
- Observability
- Agent economics

---

## Anti-pattern Summary

The goal of agent memory is not to remember everything.

The goal is to preserve the smallest amount of reliable, relevant, and useful information needed to improve future behavior.

Selective memory produces better retrieval, lower costs, clearer behavior, and safer AI systems.
