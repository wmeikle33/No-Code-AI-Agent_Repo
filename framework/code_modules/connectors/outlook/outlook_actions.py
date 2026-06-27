from typing import Any

import requests


class TeamsConnector:
    def __init__(self, access_token: str):
        if not access_token:
            raise ValueError("Microsoft Graph access token is required")

        self.base_url = "https://graph.microsoft.com/v1.0"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def health_check(self) -> dict:
        response = requests.get(
            f"{self.base_url}/me",
            headers=self.headers,
            timeout=10,
        )
        response.raise_for_status()

        profile = response.json()

        return {
            "status": "healthy",
            "connector": "teams",
            "user": profile.get("userPrincipalName"),
        }

    def list_joined_teams(self) -> list[dict[str, Any]]:
        response = requests.get(
            f"{self.base_url}/me/joinedTeams",
            headers=self.headers,
            timeout=10,
        )
        response.raise_for_status()

        return response.json().get("value", [])

    def list_channels(self, team_id: str) -> list[dict[str, Any]]:
        response = requests.get(
            f"{self.base_url}/teams/{team_id}/channels",
            headers=self.headers,
            timeout=10,
        )
        response.raise_for_status()

        return response.json().get("value", [])

    def get_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        max_results: int = 20,
    ) -> list[dict[str, Any]]:
        response = requests.get(
            f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages",
            headers=self.headers,
            params={"$top": max_results},
            timeout=10,
        )
        response.raise_for_status()

        return response.json().get("value", [])

    def send_channel_message(
        self,
        team_id: str,
        channel_id: str,
        content: str,
    ) -> dict:
        payload = {
            "body": {
                "contentType": "html",
                "content": content,
            }
        }

        response = requests.post(
            f"{self.base_url}/teams/{team_id}/channels/{channel_id}/messages",
            headers=self.headers,
            json=payload,
            timeout=10,
        )
        response.raise_for_status()

        return {
            "status": "sent",
            "connector": "teams",
            "team_id": team_id,
            "channel_id": channel_id,
        }

    def send_chat_message(
        self,
        chat_id: str,
        content: str,
    ) -> dict:
        payload = {
            "body": {
                "content": content,
            }
        }

        response = requests.post(
            f"{self.base_url}/chats/{chat_id}/messages",
            headers=self.headers,
            json=payload,
            timeout=10,
        )
        response.raise_for_status()

        return {
            "status": "sent",
            "connector": "teams",
            "chat_id": chat_id,
        }
