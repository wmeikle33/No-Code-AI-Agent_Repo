
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import re


@dataclass
class SummaryResult:
    summary: str
    key_points: list[str]
    original_length: int
    summary_length: int
    compression_ratio: float
    metadata: dict[str, Any] = field(default_factory=dict)


class Summarizer:
    """
    Generic summarization helper.

    This implementation uses extractive summarization.
    Later it can be replaced by an LLM-based summarizer.
    """

    def summarize(
        self,
        text: str,
        max_sentences: int = 5,
    ) -> SummaryResult:

        sentences = self._split_sentences(text)

        if not sentences:
            return SummaryResult(
                summary="",
                key_points=[],
                original_length=0,
                summary_length=0,
                compression_ratio=0.0,
            )

        selected = sentences[:max_sentences]

        summary = " ".join(selected)

        return SummaryResult(
            summary=summary,
            key_points=selected,
            original_length=len(text),
            summary_length=len(summary),
            compression_ratio=(
                len(summary) / len(text)
                if text
                else 0.0
            ),
        )

    def summarize_documents(
        self,
        documents: list[str],
        max_sentences: int = 10,
    ) -> SummaryResult:

        combined = "\n".join(documents)

        return self.summarize(
            combined,
            max_sentences=max_sentences,
        )

    def summarize_bullets(
        self,
        text: str,
        max_points: int = 5,
    ) -> list[str]:

        sentences = self._split_sentences(text)

        return sentences[:max_points]

    def executive_summary(
        self,
        text: str,
        max_points: int = 3,
    ) -> str:

        points = self.summarize_bullets(
            text,
            max_points=max_points,
        )

        return "\n".join(
            f"- {point}" for point in points
        )

    def _split_sentences(
        self,
        text: str,
    ) -> list[str]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text.strip(),
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]
