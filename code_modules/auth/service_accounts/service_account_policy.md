# Service Account Policy

## Purpose

This document defines how service accounts are created, managed, secured, and monitored within the No-Code AI Agent Framework.

## Definition

A service account is a non-human identity used by software systems, agents, workflows, and automation.

Examples:

- Google Cloud Service Accounts
- AWS IAM Roles
- Azure Managed Identities
- Kubernetes Service Accounts

## Security Principles

### Least Privilege

Service accounts should receive only the permissions required to perform their tasks.

Good:

```text
Document Q&A Agent
↓
Read access to vector database
```

Bad:

```text
Document Q&A Agent
↓
Administrator permissions
```

### Separation of Duties

Different agents should use different service accounts.

Example:

```text
Customer Support Agent
  ↓
support-service-account

Market Research Agent
  ↓
research-service-account
```

Avoid:

```text
all-agents-admin-account
```

## Credential Storage

Service account credentials must:

- Be stored in approved secret managers
- Be encrypted at rest
- Be encrypted in transit
- Never be committed to source control

Approved storage:

- AWS Secrets Manager
- Google Secret Manager
- Azure Key Vault
- HashiCorp Vault

## Key Management

### Preferred

Use workload identity or role-based authentication.

Examples:

```text
AWS IAM Roles
Google Workload Identity
Azure Managed Identity
```

### Less Preferred

Long-lived JSON key files.

If key files must be used:

- Encrypt them
- Rotate regularly
- Limit access
- Monitor usage

## Rotation Schedule

Recommended:

| Credential Type | Rotation |
|---------------|----------|
| Service Account Keys | 90 days |
| High-Risk Accounts | 30 days |
| Temporary Credentials | Automatic |

## Monitoring

All service account activity should be logged.

Monitor:

- Failed authentication
- Privilege escalation
- Unexpected geographic access
- Excessive API requests
- Secret access attempts

## Agent Mapping

Example:

| Agent | Service Account |
|---------|---------|
| Customer Support Agent | support-agent-sa |
| Document QA Agent | document-qa-sa |
| Executive Assistant Agent | executive-assistant-sa |
| Market Research Agent | research-agent-sa |

## Revocation

Service accounts should be disabled when:

- An integration is retired
- A workflow is removed
- Suspicious activity occurs
- Credentials are exposed

## CI/CD Usage

CI/CD pipelines should use dedicated service accounts.

Example:

```text
github-actions-deploy-sa
```

Never use:

```text
organization-admin-sa
```

for routine deployments.

## Auditing

Review service accounts quarterly:

- Remove unused accounts
- Remove excessive permissions
- Rotate credentials
- Review logs

## Summary

Service accounts should be isolated, minimally privileged, securely stored, regularly rotated, and continuously monitored.
