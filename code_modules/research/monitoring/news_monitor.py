from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Iterable


class NewsCategory(str, Enum):
    FUNDING = "funding"
    ACQUISITION = "acquisition"
    PRODUCT_LAUNCH = "product_launch"
    PARTNERSHIP = "partnership"
    REGULATION = "regulation"
    MARKET_TREND = "market_trend"
    EXECUTIVE_CHANGE = "executive_change"
    SECURITY = "security"
    LEGAL = "legal"
    EARNINGS = "earnings"
    GENERAL = "general"


@dataclass
class NewsItem:
    title: str
    summary: str
    url: str | None = None
    source: str | None = None
    published_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class NewsSignal:
    item: NewsItem
    category: NewsCategory
    relevance_score: float
    importance_score: float
    matched_keywords: list[str] = field(default_factory=list)
    detected_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class NewsMonitor:
    KEYWORDS: dict[NewsCategory, list[str]] = {
        NewsCategory.FUNDING: [
            "funding", "raised", "series a", "series b", "investment"
        ],
        NewsCategory.ACQUISITION: [
            "acquired", "acquisition", "merger", "bought"
        ],
        NewsCategory.PRODUCT_LAUNCH: [
            "launch", "released", "new product", "new feature", "beta"
        ],
        NewsCategory.PARTNERSHIP: [
            "partner", "partnership", "integration", "collaboration"
        ],
        NewsCategory.REGULATION: [
            "regulation", "law", "policy", "compliance", "regulator"
        ],
        NewsCategory.MARKET_TREND: [
            "trend", "market", "growth", "adoption", "demand"
        ],
        NewsCategory.EXECUTIVE_CHANGE: [
            "ceo", "cfo", "cto", "appointed", "resigned", "steps down"
        ],
        NewsCategory.SECURITY: [
            "breach", "hack", "cyberattack", "vulnerability", "leak"
        ],
        NewsCategory.LEGAL: [
            "lawsuit", "sued", "settlement", "court", "investigation"
        ],
        NewsCategory.EARNINGS: [
            "earnings", "revenue", "profit", "quarterly results"
        ],
    }

    IMPORTANT_CATEGORIES = {
        NewsCategory.ACQUISITION,
        NewsCategory.REGULATION,
        NewsCategory.SECURITY,
        NewsCategory.LEGAL,
    }

    def __init__(self, watch_terms: Iterable[str] | None = None):
        self.watch_terms = [term.lower().strip() for term in watch_terms or []]
        self.signals: list[NewsSignal] = []

    def add_watch_term(self, term: str) -> None:
        normalized = term.lower().strip()
        if normalized and normalized not in self.watch_terms:
            self.watch_terms.append(normalized)

    def monitor_items(self, items: Iterable[NewsItem]) -> list[NewsSignal]:
        return [self.classify_item(item) for item in items]

    def classify_item(self, item: NewsItem) -> NewsSignal:
        text = f"{item.title} {item.summary}".lower()

        category = NewsCategory.GENERAL
        matched_keywords: list[str] = []

        for possible_category, keywords in self.KEYWORDS.items():
            matches = [keyword for keyword in keywords if keyword in text]

            if len(matches) > len(matched_keywords):
                category = possible_category
                matched_keywords = matches

        signal = NewsSignal(
            item=item,
            category=category,
            relevance_score=self._score_relevance(text),
            importance_score=self._score_importance(category, matched_keywords, text),
            matched_keywords=matched_keywords,
        )

        self.signals.append(signal)
        return signal

    def get_relevant_signals(
        self,
        min_relevance: float = 0.3,
        min_importance: float = 0.3,
    ) -> list[NewsSignal]:
        return [
            signal
            for signal in self.signals
            if signal.relevance_score >= min_relevance
            and signal.importance_score >= min_importance
        ]

    def generate_digest(
        self,
        signals: list[NewsSignal] | None = None,
        max_items: int = 10,
    ) -> str:
        selected_signals = signals or self.get_relevant_signals()

        selected_signals = sorted(
            selected_signals,
            key=lambda signal: (
                signal.importance_score,
                signal.relevance_score,
                signal.item.published_at or datetime.min.replace(tzinfo=timezone.utc),
            ),
            reverse=True,
        )[:max_items]

        if not selected_signals:
            return "No relevant news signals detected."

        lines = ["# News Monitoring Digest", ""]

        for signal in selected_signals:
            item = signal.item

            lines.append(f"## {item.title}")
            lines.append(f"- Category: {signal.category.value}")
            lines.append(f"- Relevance: {signal.relevance_score:.2f}")
            lines.append(f"- Importance: {signal.importance_score:.2f}")

            if item.source:
                lines.append(f"- Source: {item.source}")

            if item.published_at:
                lines.append(f"- Published: {item.published_at.isoformat()}")

            if item.url:
                lines.append(f"- URL: {item.url}")

            lines.append(f"- Summary: {item.summary}")
            lines.append("")

        return "\n".join(lines)

    def clear(self) -> None:
        self.signals.clear()

    def _score_relevance(self, text: str) -> float:
        if not self.watch_terms:
            return 0.5

        matches = sum(1 for term in self.watch_terms if term in text)
        return min(1.0, matches / len(self.watch_terms))

    def _score_importance(
        self,
        category: NewsCategory,
        matches: list[str],
        text: str,
    ) -> float:
        score = 0.35

        if category in self.IMPORTANT_CATEGORIES:
            score += 0.35
        elif category != NewsCategory.GENERAL:
            score += 0.2

        score += min(0.2, len(matches) * 0.05)

        urgent_terms = [
            "breaking",
            "major",
            "confirmed",
            "urgent",
            "record",
        ]

        if any(term in text for term in urgent_terms):
            score += 0.1

        return min(1.0, score)
