from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Iterable


class CompetitorSignalType(str, Enum):
    PRICING_CHANGE = "pricing_change"
    PRODUCT_UPDATE = "product_update"
    NEWS = "news"
    FUNDING = "funding"
    HIRING = "hiring"
    POSITIONING_CHANGE = "positioning_change"
    CONTENT_MARKETING = "content_marketing"
    PARTNERSHIP = "partnership"
    UNKNOWN = "unknown"


@dataclass
class Competitor:
    name: str
    website: str | None = None
    pricing_url: str | None = None
    changelog_url: str | None = None
    careers_url: str | None = None
    notes: str | None = None


@dataclass
class CompetitorSignal:
    competitor_name: str
    signal_type: CompetitorSignalType
    title: str
    summary: str
    source_url: str | None = None
    detected_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    confidence: float = 0.5
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class CompetitorSnapshot:
    competitor_name: str
    captured_at: datetime
    pricing_text: str | None = None
    product_text: str | None = None
    positioning_text: str | None = None
    careers_text: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class CompetitorMonitor:
    """
    Monitors competitors and extracts business-relevant signals.

    This class is intentionally provider-agnostic. You can connect it later
    to a scraper, web search provider, RSS reader, or vector database.
    """

    def __init__(self, competitors: Iterable[Competitor] | None = None):
        self.competitors: list[Competitor] = list(competitors or [])
        self.signals: list[CompetitorSignal] = []

    def add_competitor(self, competitor: Competitor) -> None:
        self.competitors.append(competitor)

    def list_competitors(self) -> list[Competitor]:
        return self.competitors

    def monitor_text(
        self,
        competitor_name: str,
        text: str,
        source_url: str | None = None,
    ) -> list[CompetitorSignal]:
        """
        Extract competitor signals from raw text.
        """

        signals: list[CompetitorSignal] = []

        checks = [
            (
                CompetitorSignalType.PRICING_CHANGE,
                ["price", "pricing", "plan", "subscription", "discount"],
            ),
            (
                CompetitorSignalType.PRODUCT_UPDATE,
                ["launch", "released", "new feature", "update", "beta"],
            ),
            (
                CompetitorSignalType.FUNDING,
                ["funding", "raised", "series a", "series b", "investment"],
            ),
            (
                CompetitorSignalType.HIRING,
                ["hiring", "job opening", "careers", "recruiting"],
            ),
            (
                CompetitorSignalType.PARTNERSHIP,
                ["partner", "partnership", "integration", "collaboration"],
            ),
            (
                CompetitorSignalType.POSITIONING_CHANGE,
                ["now for", "built for", "designed for", "rebrand"],
            ),
        ]

        lowered = text.lower()

        for signal_type, keywords in checks:
            matched = [keyword for keyword in keywords if keyword in lowered]

            if matched:
                signals.append(
                    CompetitorSignal(
                        competitor_name=competitor_name,
                        signal_type=signal_type,
                        title=f"{competitor_name}: {signal_type.value}",
                        summary=self._make_summary(text, matched),
                        source_url=source_url,
                        confidence=min(0.95, 0.45 + 0.1 * len(matched)),
                        metadata={"matched_keywords": matched},
                    )
                )

        self.signals.extend(signals)
        return signals

    def compare_snapshots(
        self,
        previous: CompetitorSnapshot,
        current: CompetitorSnapshot,
    ) -> list[CompetitorSignal]:
        """
        Compare two saved snapshots and create signals for changed sections.
        """

        if previous.competitor_name != current.competitor_name:
            raise ValueError("Snapshots must belong to the same competitor.")

        signals: list[CompetitorSignal] = []

        fields = {
            "pricing_text": CompetitorSignalType.PRICING_CHANGE,
            "product_text": CompetitorSignalType.PRODUCT_UPDATE,
            "positioning_text": CompetitorSignalType.POSITIONING_CHANGE,
            "careers_text": CompetitorSignalType.HIRING,
        }

        for field_name, signal_type in fields.items():
            old_value = getattr(previous, field_name)
            new_value = getattr(current, field_name)

            if self._has_meaningful_change(old_value, new_value):
                signals.append(
                    CompetitorSignal(
                        competitor_name=current.competitor_name,
                        signal_type=signal_type,
                        title=f"{current.competitor_name}: changed {field_name}",
                        summary=f"Detected a change in {field_name}.",
                        confidence=0.8,
                        metadata={
                            "field": field_name,
                            "previous_excerpt": self._excerpt(old_value),
                            "current_excerpt": self._excerpt(new_value),
                        },
                    )
                )

        self.signals.extend(signals)
        return signals

    def get_signals(
        self,
        signal_type: CompetitorSignalType | None = None,
        min_confidence: float = 0.0,
    ) -> list[CompetitorSignal]:
        results = self.signals

        if signal_type is not None:
            results = [
                signal for signal in results
                if signal.signal_type == signal_type
            ]

        return [
            signal for signal in results
            if signal.confidence >= min_confidence
        ]

    def generate_digest(self, signals: list[CompetitorSignal] | None = None) -> str:
        signals = signals or self.signals

        if not signals:
            return "No competitor signals detected."

        lines = ["# Competitor Monitoring Digest", ""]

        for signal in signals:
            lines.append(f"## {signal.title}")
            lines.append(f"- Competitor: {signal.competitor_name}")
            lines.append(f"- Type: {signal.signal_type.value}")
            lines.append(f"- Confidence: {signal.confidence:.2f}")
            if signal.source_url:
                lines.append(f"- Source: {signal.source_url}")
            lines.append(f"- Summary: {signal.summary}")
            lines.append("")

        return "\n".join(lines)

    def _make_summary(self, text: str, matched_keywords: list[str]) -> str:
        excerpt = self._excerpt(text, max_length=220)
        return (
            f"Matched keywords: {', '.join(matched_keywords)}. "
            f"Excerpt: {excerpt}"
        )

    def _has_meaningful_change(
        self,
        old_value: str | None,
        new_value: str | None,
    ) -> bool:
        if not old_value and not new_value:
            return False

        return self._normalize(old_value) != self._normalize(new_value)

    def _normalize(self, value: str | None) -> str:
        return " ".join((value or "").lower().split())

    def _excerpt(self, value: str | None, max_length: int = 160) -> str:
        if not value:
            return ""

        cleaned = " ".join(value.split())
        if len(cleaned) <= max_length:
            return cleaned
