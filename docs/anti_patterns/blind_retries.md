# Blind Retries

## Overview

Blind retries occur when an AI agent repeats the same action after a failure without understanding why the failure happened.

Instead of diagnosing the root cause, the agent repeatedly issues the same request, often producing identical failures while wasting time, API calls, and compute resources.

A retry should only occur when there is a reasonable chance that the next attempt will succeed.

---

## Why It Happens

Common causes include:

- Assuming every failure is temporary
- Missing error classification
- No retry policy
- Ignoring tool error messages
- Treating all failures the same

---

## Example

Bad workflow:

```
Call API
    ↓
Fails
    ↓
Retry
    ↓
Fails
    ↓
Retry
    ↓
Fails
    ↓
Retry...
```

Nothing changes between attempts.

---

## Why It's a Problem

Blind retries can cause:

- Increased latency
- Higher API costs
- Infinite retry loops
- Rate limiting
- Duplicate actions
- Poor user experience
- Excessive token consumption

---

## Common Examples

### Example 1

A weather API returns:

```
401 Unauthorized
```

The agent retries five more times.

The API key is invalid.

Retries will never succeed.

---

### Example 2

The model receives incomplete customer information.

Instead of requesting the missing fields, it repeatedly attempts the same database lookup.

---

### Example 3

A calculator tool rejects invalid input.

Instead of correcting the expression, the agent calls the calculator again.

---

## Better Approach

Before retrying, classify the failure.

```
Failure
    ↓
Can this succeed if repeated?

Yes
    ↓
Retry

No
    ↓
Fix the problem first
```

---

## Retry Decision Framework

| Failure | Retry? |
|----------|---------|
| Network timeout | ✅ Yes |
| Temporary server error | ✅ Yes |
| Rate limit | ✅ After waiting |
| Invalid API key | ❌ No |
| Invalid user input | ❌ No |
| Missing required field | ❌ No |
| Permission denied | ❌ No |
| Tool not installed | ❌ No |

---

## Better Retry Strategy

Instead of:

```
Retry
Retry
Retry
Retry
```

Use:

```
Attempt
    ↓
Identify failure
    ↓
Classify error
    ↓
Retry if appropriate
    ↓
Otherwise recover
```

---

## Best Practices

- Retry only transient failures.
- Set a maximum retry count.
- Use exponential backoff.
- Add random jitter to avoid synchronized retries.
- Log every retry attempt.
- Surface persistent failures to users or operators.
- Avoid retrying permanent errors.

---

## Related Patterns

- Reflection
- Self-correction
- Human review
- Tool validation
- Error handling
- Monitoring

---

## Anti-pattern Summary

Blind retries assume that repeating the same action will eventually produce a different outcome.

Robust AI agents first determine *why* an action failed before deciding whether a retry is appropriate.
