# Service Accounts

## Purpose

This directory contains templates, examples, and policies related to service account authentication.

Service accounts are non-human identities used by applications, agents, workflows, and automated systems.

Examples include:

- Google Cloud Service Accounts
- AWS IAM Roles
- Azure Managed Identities
- Kubernetes Service Accounts
- CI/CD Deployment Accounts

## Why Use Service Accounts?

Service accounts allow agents and workflows to:

- Access cloud resources
- Read and write storage buckets
- Query databases
- Invoke APIs
- Execute background jobs
- Authenticate without human intervention

## Structure

```text
service_accounts/
├── README.md
├── google_service_account.example.json
├── aws_iam_role_policy.example.json
└── service_account_policy.md
```

## Important Rules

- Never commit real service account credentials.
- Use example files only.
- Follow least privilege principles.
- Rotate credentials regularly.
- Store credentials in approved secret managers.

## Examples

### Google Cloud

```text
AI Agent
   ↓
Google Service Account
   ↓
Vertex AI
Cloud Storage
BigQuery
```

### AWS

```text
AI Agent
   ↓
IAM Role
   ↓
S3
Lambda
RDS
Secrets Manager
```

## Related Documents

- ../secrets/secret_storage_policy.md
- ../oauth/token_management/token_policy.md
- ../permissions/least_privilege.md
