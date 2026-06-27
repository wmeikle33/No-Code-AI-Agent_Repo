# Competitive Intelligence Agent — System Design

## Purpose

The Competitive Intelligence Agent monitors public competitor, market, product, funding, hiring, and industry signals and turns them into structured intelligence briefs.

It is designed for reusable competitive monitoring workflows while also supporting the Greenscale reference implementation.

## Responsibilities

The agent is responsible for:

- Tracking known competitors
- Discovering relevant market signals
- Summarizing public news and announcements
- Comparing competitors across defined criteria
- Identifying risks, opportunities, and strategic changes
- Producing cited competitive intelligence briefs
- Flagging uncertain or high-impact findings for human review

## Non-Responsibilities

This agent should not:

- Access private or unauthorized competitor information
- Scrape restricted systems
- Use leaked documents
- Collect unnecessary personal data
- Make final business decisions without human review
- Present uncertain claims as facts

## Inputs

Required inputs:

- `competitor_list`
- `research_goal`

Optional inputs:

- `industry`
- `target_market`
- `time_range`
- `trusted_sources`
- `excluded_sources`
- `keywords`
- `comparison_criteria`
- `output_format`

## Outputs

Typical outputs include:

- Competitive intelligence brief
- Competitor profile
- Market movement summary
- Risk and opportunity report
- Pricing comparison
- Product comparison table
- Weekly monitoring digest

## High-Level Architecture

```text
User Request
    ↓
Routing Layer
    ↓
Competitive Intelligence Agent
    ↓
Source Collection
    ↓
Signal Extraction
    ↓
Relevance Scoring
    ↓
Synthesis
    ↓
Human Review Check
    ↓
Final Intelligence Brief
