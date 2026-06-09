# OAuth Flows

## Overview

This folder contains reusable OAuth configuration, provider definitions, scope mappings, and token management patterns used by AI agents, workflow automations, and API integrations.

The goal is to provide a cloud-agnostic and provider-agnostic reference implementation for secure authentication.

---

## Folder Structure

```text
oauth_flows/
├── flows/
├── providers/
├── scopes/
└── token_management/
```

---

## flows/

Contains OAuth flow definitions and examples.

Examples:

- Authorization Code Flow
- Authorization Code with PKCE
- Client Credentials Flow
- Device Code Flow

Purpose:

```text
User or Application
        ↓
OAuth Flow
        ↓
Access Token
```

The flow determines how authentication occurs and how tokens are obtained.

---

## providers/

Contains provider-specific OAuth configurations.

Examples:

```text
google.json
microsoft.json
salesforce.json
hubspot.json
```

Provider files typically define:

- Authorization endpoint
- Token endpoint
- User information endpoint
- Supported OAuth flows
- Default scopes

Example:

```json
{
  "provider": "google",
  "authorization_url": "https://accounts.google.com/o/oauth2/v2/auth",
  "token_url": "https://oauth2.googleapis.com/token",
  "supported_flows": [
    "authorization_code",
    "pkce"
  ]
}
```

---

## scopes/

Contains scope definitions for supported providers.

Scopes define what permissions an agent receives.

Example:

```text
google_scopes.json
```

Common permissions:

```text
Read Email
Send Email
Read Calendar
Manage Contacts
Read Drive Files
```

Example:

```json
{
  "gmail.readonly": {
    "description": "Read Gmail messages"
  }
}
```

Principle:

```text
Minimum Required Permissions
```

Agents should request only the scopes they actually need.

---

## token_management/

Contains token lifecycle patterns and examples.

Responsibilities:

- Access token storage
- Refresh token handling
- Token expiration checks
- Token rotation
- Secure credential storage

Typical workflow:

```text
Access Token Issued
        ↓
Stored Securely
        ↓
Used For API Requests
        ↓
Expiration Detected
        ↓
Refresh Token Used
        ↓
New Access Token Issued
```

Security recommendations:

- Never commit tokens to source control
- Encrypt secrets at rest
- Use secure secret stores
- Rotate credentials regularly

---
