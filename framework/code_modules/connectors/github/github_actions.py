from __future__ import annotations

from typing import Any

import requests


class GitHubConnector:
    """Connector for interacting with the GitHub REST API."""

    def __init__(
        self,
        access_token: str,
        base_url: str = "https://api.github.com",
    ):
        if not access_token:
            raise ValueError("GitHub access token is required")

        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> dict[str, Any] | list[dict[str, Any]]:
        url = f"{self.base_url}{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            timeout=10,
            **kwargs,
        )

        response.raise_for_status()

        if response.status_code == 204:
            return {}

        return response.json()

    def health_check(self) -> dict[str, Any]:
        user = self._request("GET", "/user")

        return {
            "status": "healthy",
            "connector": "github",
            "user": user.get("login"),
        }

    def get_repository(
        self,
        owner: str,
        repo: str,
    ) -> dict[str, Any]:
        return self._request(
            "GET",
            f"/repos/{owner}/{repo}",
        )

    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 30,
    ) -> list[dict[str, Any]]:
        return self._request(
            "GET",
            f"/repos/{owner}/{repo}/issues",
            params={
                "state": state,
                "per_page": per_page,
            },
        )

    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: str,
        labels: list[str] | None = None,
    ) -> dict[str, Any]:
        if not title:
            raise ValueError("Issue title is required")

        payload: dict[str, Any] = {
            "title": title,
            "body": body,
        }

        if labels:
            payload["labels"] = labels

        return self._request(
            "POST",
            f"/repos/{owner}/{repo}/issues",
            json=payload,
        )

    def close_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
    ) -> dict[str, Any]:
        return self._request(
            "PATCH",
            f"/repos/{owner}/{repo}/issues/{issue_number}",
            json={"state": "closed"},
        )

    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 30,
    ) -> list[dict[str, Any]]:
        return self._request(
            "GET",
            f"/repos/{owner}/{repo}/pulls",
            params={
                "state": state,
                "per_page": per_page,
            },
        )

    def get_file(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: str = "main",
    ) -> dict[str, Any]:
        return self._request(
            "GET",
            f"/repos/{owner}/{repo}/contents/{path}",
            params={"ref": ref},
        )

    def list_workflows(
        self,
        owner: str,
        repo: str,
    ) -> list[dict[str, Any]]:
        result = self._request(
            "GET",
            f"/repos/{owner}/{repo}/actions/workflows",
        )

        return result.get("workflows", [])

    def trigger_workflow(
        self,
        owner: str,
        repo: str,
        workflow_id: str,
        ref: str = "main",
        inputs: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "ref": ref,
        }

        if inputs:
            payload["inputs"] = inputs

        self._request(
            "POST",
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
            json=payload,
        )

        return {
            "status": "triggered",
            "connector": "github",
            "workflow_id": workflow_id,
            "ref": ref,
