# OAuth 2.0 Authorization Code Flow

## Purpose

The Authorization Code flow is used when an agent or connector needs to access a third-party service on behalf of a user.

Examples:

- Google Drive connector
- Gmail connector
- Slack connector
- Notion connector
- GitHub connector
- CRM connector

This flow is appropriate when the application has a backend server that can securely exchange an authorization code for tokens.

---

## When to Use This Flow

Use the Authorization Code flow when:

- A user must explicitly grant access
- The app needs access to private user data
- The app has a backend service
- Refresh tokens may be needed
- The integration requires scoped permissions

Do not use this flow for:

- Server-to-server access without a user
- Public frontend-only apps without PKCE
- Static API-key integrations

---

## High-Level Flow

```text
User
  ↓
App redirects user to provider authorization URL
  ↓
User logs in and grants permissions
  ↓
Provider redirects back with authorization code
  ↓
Backend exchanges code for access token
  ↓
Backend stores token securely
  ↓
Agent uses token to call provider API
