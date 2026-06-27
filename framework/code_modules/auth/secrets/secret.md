# Secrets Overview

## Purpose

This document explains what counts as a secret in the No-Code AI Agent framework and how secrets should be handled during development, testing, and production deployment.

## What Is a Secret?

A secret is any value that grants access to a system, service, account, database, model provider, or private resource.

Examples include:

- API keys
- OAuth client secrets
- OAuth access tokens
- OAuth refresh tokens
- JWT signing keys
- Session signing keys
- Database passwords
- Cloud provider credentials
- Service account private keys
- Webhook signing secrets
- Encryption keys
- SSH private keys

## What Is Not a Secret?

The following values are usually not secrets by themselves:

- Public client IDs
- Public redirect URIs
- Provider names
- API base URLs
- Model names
- Environment names
- Non-sensitive feature flags

However, non-secret values can still become sensitive when combined with other information.

## Rules

1. Never commit real secrets to the repository.
2. Never paste secrets into issues, pull requests, comments, logs, or documentation.
3. Never print secrets in terminal output or application logs.
4. Never expose secrets to agents unless explicitly required.
5. Never store production secrets in local `.env` files.
6. Always use placeholders in examples.
7. Rotate secrets immediately if exposure is suspected.

## Safe Example

```env
OPENAI_API_KEY=replace_with_openai_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/database
