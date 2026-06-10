# Token Management Policy

## Purpose

This document defines how OAuth access tokens, refresh tokens, and related authentication credentials should be stored, refreshed, rotated, and revoked inside the No-Code AI Agent framework.

## Scope

This policy applies to all agents, tools, workflows, connectors, and integrations that use OAuth, API tokens, service account tokens, or other bearer credentials.

## Core Principles

1. Tokens must never be committed to the repository.
2. Tokens must be encrypted at rest.
3. Tokens must only be available to agents that explicitly need them.
4. Tokens must be refreshed automatically when supported.
5. Tokens must be revoked when no longer needed.
6. Token access should follow the principle of least privilege.

## Token Storage

Production tokens should be stored in a secure storage backend, such as:

- Cloud secret manager
- Encrypted database
- Vault service
- Managed identity provider

Local `.env` files may only be used for development and must never contain production credentials.

## Access Tokens

Access tokens should be treated as sensitive secrets.

Access tokens should:

- Be short-lived when possible
- Be refreshed before expiration
- Never be printed in logs
- Never be exposed in API responses
- Never be included in error messages

## Refresh Tokens

Refresh tokens are higher risk than access tokens because they may allow long-term access.

Refresh tokens must:

- Be encrypted at rest
- Be stored separately from non-sensitive metadata
- Be rotated when supported by the provider
- Be revoked if compromise is suspected
- Be removed when a user disconnects an integration

## Expiration Handling

The system should refresh tokens before they expire.

Recommended refresh window:

```text
5 minutes before expiration
