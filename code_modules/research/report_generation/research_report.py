from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ResearchFinding:
    title: str
    summary: str
    evidence: list[str] = field(default_factory=list)
    confidence: float = 0.5
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ResearchSource:
    title: str
    url: str | None = None
    publisher: str | None = None
    published_at: datetime | None = None
    reliability_score: float = 0.5


@dataclass
class ResearchReport:
    query: str
    title: str
    executive_summary: str
    findings: list[ResearchFinding] = field(default_factory=list)
    sources: list[ResearchSource] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    generated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    metadata: dict[str, Any] = field(default_factory=dict)


class ResearchReportGenerator:
    def generate_markdown(self, report: ResearchReport) -> str:
        lines: list[str] = []

        lines.append(f"# {report.title}")
        lines.append("")
        lines.append(f"**Query:** {report.query}")
        lines.append(f"**Generated at:** {report.generated_at.isoformat()}")
        lines.append("")

        lines.append("## Executive Summary")
        lines.append(report.executive_summary)
        lines.append("")

        if report.findings:
            lines.append("## Key Findings")
            lines.append("")

            for index, finding in enumerate(report.findings, start=1):
                lines.append(f"### {index}. {finding.title}")
                lines.append(finding.summary)
                lines.append("")
                lines.append(f"**Confidence:** {finding.confidence:.2f}")
                lines.append("")

                if finding.evidence:
                    lines.append("**Evidence:**")
                    for item in finding.evidence:
                        lines.append(f"- {item}")
                    lines.append("")

        if report.recommendations:
            lines.append("## Recommendations")
            lines.append("")

            for recommendation in report.recommendations:
                lines.append(f"- {recommendation}")

            lines.append("")

        if report.limitations:
            lines.append("## Limitations")
            lines.append("")

            for limitation in report.limitations:
                lines.append(f"- {limitation}")

            lines.append("")

        if report.sources:
            lines.append("## Sources")
            lines.append("")

            for index, source in enumerate(report.sources, start=1):
                source_line = f"{index}. {source.title}"

                if source.publisher:
                    source_line += f" — {source.publisher}"

                if source.published_at:
                    source_line += f" ({source.published_at.date().isoformat()})"

                if source.url:
                    source_line += f" — {source.url}"

                source_line += f" [Reliability: {source.reliability_score:.2f}]"

                lines.append(source_line)

            lines.append("")

        return "\n".join(lines)

    def generate_brief(self, report: ResearchReport) -> str:
        lines = [
            f"# {report.title}",
            "",
            "## Summary",
            report.executive_summary,
            "",
        ]

        if report.findings:
            lines.append("## Top Findings")
            for finding in report.findings[:3]:
                lines.append(f"- **{finding.title}:** {finding.summary}")

        return "\n".join(lines)

    def generate_source_summary(self, report: ResearchReport) -> str:
        if not report.sources:
            return "No sources available."

        lines = ["# Source Summary", ""]

        for source in report.sources:
            lines.append(f"- **{source.title}**")
            if source.publisher:
                lines.append(f"  - Publisher: {source.publisher}")
            if source.published_at:
                lines.append(f"  - Published: {source.published_at.date().isoformat()}")
            if source.url:
                lines.append(f"  - URL: {source.url}")
            lines.append(f"  - Reliability: {source.reliability_score:.2f}")

        return "\n".join(lines)
