# API Key Management

This folder defines how API keys and provider credentials are documented, validated, and rotated for the no-code AI agent system.

No real API keys should ever be stored in this folder.

## Folder Structure

```text
auth/api_keys/
├── providers/      # Provider metadata such as env var names and supported models
├── templates/      # Safe example .env files for local, Docker, and CI setup
├── validation/     # Rules and scripts for checking provider key configuration
├── rotation/       # Key rotation, incident response, and compromise procedures
└── README.md
```
