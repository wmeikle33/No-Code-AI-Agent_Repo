# Session Timeout Policy

## Purpose

This document defines session expiration rules.

## Recommended Timeouts

| Session Type | Timeout |
|-------------|----------|
| User Session | 60 minutes |
| Agent Session | 120 minutes |
| Workflow Session | 240 minutes |
| OAuth Flow | 10 minutes |

## Idle Timeout

A session may expire after a period of inactivity.

Example:

```text
Last Activity
↓
60 Minutes Pass
↓
Session Expires
```

## Absolute Timeout

Sessions should also have a maximum lifetime.

Example:

```text
Session Created
↓
24 Hours Pass
↓
Forced Logout
```

## Sliding Expiration

If enabled:

```text
User Activity
↓
Timeout Reset
↓
Session Continues
```

If disabled:

```text
Session Created
↓
Fixed Lifetime
↓
Session Ends
```

## High-Risk Operations

Require re-authentication after:

- Admin actions
- Permission changes
- Secret access
- Service account creation
- OAuth scope modifications

Recommended timeout:

```text
15 minutes
```

## Workflow Timeouts

Long-running workflows should:

- Save state periodically
- Resume safely
- Terminate after maximum runtime

Recommended maximum:

```text
24 hours
```

## Expired Sessions

Expired sessions must:

1. Be rejected.
2. Be removed from active storage.
3. Require re-authentication if needed.

## Monitoring

Track:

- Session duration
- Session expirations
- Session renewals
- Failed validations
- Revocations

## Summary

Sessions should expire automatically, be renewed only when appropriate, and be removed promptly when no longer needed.
