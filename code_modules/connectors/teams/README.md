# Microsoft Teams Connector

This folder contains connector utilities for integrating workflow agents with Microsoft Teams.

The Teams connector is responsible for sending messages, reading channel activity, posting workflow updates, and supporting collaboration-related automations.

---

## Purpose

The Teams connector allows agents and workflows to interact with Microsoft Teams in a consistent way.

Typical use cases include:

- Sending workflow status updates to Teams channels
- Posting escalation alerts
- Notifying managers or support teams
- Creating summaries from Teams conversations
- Routing employee-support requests
- Delivering KPI or incident reports
- Triggering workflows from Teams messages

---

##  Folder Structure

```text
teams/
├── README.md
├── __init__.py
├── teams_actions.py

```

---

## Main Components

### `teams_actions.py`

Low-level Microsoft Teams or Microsoft Graph API client.

Responsibilities:

- Authenticate requests
- Send HTTP requests
- Handle API errors
- Parse API responses
- Provide a simple interface for workflows
- Wrap Teams-specific API logic
- Normalize inputs and outputs
- Return consistent connector results
- Send a direct message
- Send a channel message
- Send workflow alerts
- Send formatted Markdown messages
- Fetch recent channel messages
- Search messages by keyword
- Extract conversation context
- Prepare messages for summarization


## Example Usage

```python
from code_modules.connectors.teams.teams_actions import TeamsConnector

connector = TeamsConnector()

result = connector.send_channel_message(
    channel_id="general",
    message="Support escalation detected. Please review."
)

print(result)
```

---

## Example Workflow Integration

```python
from code_modules.connectors.teams.teams_connector import TeamsConnector


class EscalationWorkflow:
    def __init__(self):
        self.teams = TeamsConnector()

    def run(self, data):
        if data["priority"] == "high":
            self.teams.send_channel_message(
                channel_id=data["channel_id"],
                message=f"High-priority escalation: {data['summary']}"
            )

        return {
            "status": "completed",
            "notification_sent": True
        }
```

---

## Expected Connector Output

All Teams connector methods should return a consistent dictionary.

Success example:

```json
{
  "success": true,
  "connector": "teams",
  "action": "send_channel_message",
  "message_id": "abc123",
  "channel_id": "general",
  "error": null
}
```

Failure example:

```json
{
  "success": false,
  "connector": "teams",
  "action": "send_channel_message",
  "message_id": null,
  "channel_id": "general",
  "error": "Missing Teams access token."
}
```

---

## Security Notes

Do not hardcode credentials in this folder.

Use environment variables or a secrets manager for:

- Client IDs
- Client Secrets
- Tenant IDs
- Access Tokens
- Webhook URLs

Never commit `.env` files or real Microsoft Teams credentials.

---

## Testing

Recommended tests:

```text
tests/
├── test_message_sender.py
├── test_channel_reader.py
├── test_auth.py
└── test_webhook_handler.py
```

Tests should cover:

- Missing credentials
- Successful message formatting
- Failed API response handling
- Empty channel results
- Webhook event parsing
- Connector output structure

---

## Related Workflows

This connector may be used by:

- Customer Support Escalation Workflows
- Employee Support Workflows
- Executive Assistant Workflows
- KPI Monitoring Workflows
- Incident Response Workflows
- Meeting Summary Workflows

---

## Development Notes

Start with stubbed methods before adding real Microsoft Graph API calls.

Recommended development order:

1. Define schemas
2. Add connector result format
3. Implement message sending
4. Add authentication
5. Add channel reading
6. Add webhook support
7. Add tests

---

## Future Enhancements

Potential future features:

- Adaptive Cards support
- Team creation and management
- Channel creation
- Meeting scheduling
- Teams bot integration
- File uploads and downloads
- Conversation analytics
- AI-generated channel summaries
- Workflow approvals through Teams
