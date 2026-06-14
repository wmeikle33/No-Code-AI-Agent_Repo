from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class MarketResearchWorkflow:
    """Creates a simple market research report from structured input."""

    def run(self, data: dict[str, Any]) -> dict[str, Any]:
        topic = data.get("topic") or data.get("industry") or "Unknown market"
        competitors = data.get("competitors", [])
        target_customers = data.get("target_customers", [])
        region = data.get("region", "global")

        return {
            "workflow": "market_research",
            "topic": topic,
            "region": region,
            "summary": f"Initial market research report for {topic}.",
            "competitors_analyzed": competitors,
            "target_customers": target_customers,
            "recommended_next_steps": [
                "Collect competitor pricing data.",
                "Identify customer pain points.",
                "Compare positioning and feature gaps.",
                "Generate final research report.",
            ],
            "human_review_required": True,
        }
