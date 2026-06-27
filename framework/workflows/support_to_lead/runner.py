from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SupportToLeadWorkflow:
    """Turns a support conversation into a qualified lead decision."""

    min_score: int = 60

    def run(self, data: dict[str, Any]) -> dict[str, Any]:
        customer_message = data.get("customer_message", "")
        customer_email = data.get("customer_email")
        company = data.get("company")
        issue_type = data.get("issue_type", "unknown")

        score = self._score_lead(customer_message, company)

        status = "qualified_lead" if score >= self.min_score else "support_only"

        return {
            "workflow": "support_to_lead",
            "status": status,
            "lead_score": score,
            "customer_email": customer_email,
            "company": company,
            "issue_type": issue_type,
            "recommended_action": self._recommended_action(status),
            "human_review_required": score >= 80,
        }

    def _score_lead(self, message: str, company: str | None) -> int:
        score = 0
        text = message.lower()

        buying_signals = [
            "pricing",
            "demo",
            "quote",
            "upgrade",
            "enterprise",
            "subscription",
            "sales",
            "contract",
        ]

        for signal in buying_signals:
            if signal in text:
                score += 15

        if company:
            score += 20

        return min(score, 100)

    def _recommended_action(self, status: str) -> str:
        if status == "qualified_lead":
            return "Route to sales team for follow-up."
        return "Continue normal support workflow."
