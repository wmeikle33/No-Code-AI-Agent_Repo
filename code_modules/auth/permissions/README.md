# Permissions

This folder defines permission rules for agents, tools, workflows, and connected services.

The goal is to make sure each agent only has access to the resources it actually needs.

## Folder Purpose

Use this folder to document and configure:

- agent-level permissions
- workflow-level permissions
- tool access rules
- OAuth scope requirements
- API key usage permissions
- deny-by-default policies
- approval requirements for sensitive actions

## Recommended Structure

```text
auth/permissions/
├── README.md
├── agent_permissions.json
├── workflow_permissions.json
├── tool_permissions.json
├── role_permissions.json
└── permission_policy.md
