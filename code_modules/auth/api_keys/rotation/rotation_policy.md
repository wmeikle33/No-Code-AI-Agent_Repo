## Credential Rotation Policy

Purpose
```bash

This document defines how API keys, OAuth tokens, service account credentials, database passwords, and other secrets should be rotated in this repository.
The goal is to reduce security risk if credentials are exposed, outdated, over-permissioned, or no longer needed.

```
Credentials Covered

```bash

This policy applies to:
API keys
OAuth client secrets
OAuth refresh tokens
Service account keys
Database passwords
JWT secrets
Encryption keys
Webhook signing secrets
Third-party integration tokens

```

## Rotation Schedule

| Key Type | Rotation Frequency |
|-----------|------------------|
| OpenAI | Every 90 days |
| Anthropic | Every 90 days |
| Internal Services | Every 60 days |

## Process

1. Generate new key
2. Update secret manager
3. Validate service functionality
4. Revoke old key
5. Log rotation event

## Emergency Rotation

Immediately rotate if:
- Key is exposed in source control
- Unauthorized access is suspected
- Vendor reports compromise
