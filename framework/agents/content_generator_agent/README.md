# Content Generator Agent

## Overview

The Content Generator Agent creates, rewrites, edits, and improves written content for different audiences, formats, channels, and business goals.

It is designed to produce clear, original, audience-aware content while following brand guidelines, factual accuracy requirements, formatting constraints, and human review rules.

This agent can support marketing, education, sales, internal communication, product documentation, social media, newsletters, blog posts, landing pages, scripts, and executive communications.

---

# Purpose

The purpose of this agent is to help teams create high-quality content faster while maintaining consistency, accuracy, originality, and brand alignment.

---

# Primary Responsibilities

The Content Generator Agent is responsible for:

- Drafting original content
- Rewriting and polishing existing text
- Adapting tone and style
- Matching content to a target audience
- Creating outlines and content briefs
- Generating blog posts, emails, ads, captions, and landing page copy
- Improving clarity, grammar, and structure
- Producing SEO-aware content
- Creating summaries and repurposed content
- Suggesting headlines, hooks, and calls to action
- Following brand voice and formatting requirements
- Flagging unsupported factual claims

---

# Non-Responsibilities

The agent should not:

- Invent facts, statistics, quotes, or sources
- Copy copyrighted material
- Publish content without human approval
- Reveal confidential information
- Make legal, medical, financial, or regulatory claims without review
- Create misleading, deceptive, or manipulative content
- Ignore brand guidelines
- Generate harmful, discriminatory, or unsafe content

---

# Target Users

This agent is intended for:

- Marketing teams
- Content writers
- Founders
- Product marketers
- Social media managers
- Sales teams
- Educators
- Internal communications teams
- Executives
- Customer success teams

---

# Typical Use Cases

## Blog Content

Create outlines, introductions, full drafts, summaries, and SEO-friendly blog sections.

## Marketing Copy

Generate landing page sections, ad copy, email campaigns, product descriptions, and calls to action.

## Social Media

Create LinkedIn posts, X/Twitter posts, Instagram captions, short-form hooks, and content variations.

## Editing and Rewriting

Improve clarity, grammar, tone, structure, concision, and readability.

## Content Repurposing

Turn long-form content into emails, posts, summaries, scripts, or newsletters.

## Executive Communication

Draft polished updates, announcements, memos, and internal messages.

## Educational Content

Create explanations, lesson materials, examples, worksheets, and simplified summaries.

---

# Inputs

Typical inputs include:

- User request
- Target audience
- Content format
- Desired tone
- Brand guidelines
- Source material
- Product information
- Keywords
- Length requirements
- Channel or platform
- Call to action
- Publication goal

Example:

```json
{
  "request": "Write a LinkedIn post about no-code AI agents.",
  "audience": "small business owners",
  "tone": "friendly and professional",
  "format": "social_post",
  "length": "under 150 words",
  "cta": "invite readers to request a demo"
}
```

---

# Outputs

The agent may produce:

- Blog posts
- Article outlines
- Social media posts
- Email drafts
- Landing page copy
- Product descriptions
- Ad copy
- Video scripts
- Newsletter sections
- Executive updates
- Educational explanations
- Rewritten or edited text
- Content briefs
- Headline variations
- CTA options

---

# Required Knowledge

The agent benefits from access to:

- Brand voice guidelines
- Style guides
- Product documentation
- Customer personas
- Marketing strategy
- SEO keyword research
- Existing content examples
- Messaging frameworks
- Approved claims
- Company glossary
- Content approval rules

---

# Required Tools

The agent may use:

- Knowledge Base Retrieval
- Document Search
- Web Search
- Citation Generator
- Grammar Checker
- SEO Analyzer
- Plagiarism Checker
- Readability Analyzer
- Content Calendar
- CMS Integration

---

# Workflow

```text
Receive Request
      │
      ▼
Identify Content Goal
      │
      ▼
Determine Audience and Channel
      │
      ▼
Retrieve Brand and Source Context
      │
      ▼
Generate Outline or Draft
      │
      ▼
Check Facts and Claims
      │
      ▼
Adjust Tone and Structure
      │
      ▼
Validate Against Requirements
      │
      ▼
Recommend Human Review if Needed
      │
      ▼
Return Final Content
```

---

# Output Structure

A typical output may include:

1. Final content
2. Optional headline alternatives
3. Optional CTA alternatives
4. Notes on assumptions
5. Confidence level
6. Review warnings, if needed

For long-form content:

1. Title
2. Introduction
3. Main sections
4. Examples
5. Conclusion
6. Call to action
7. Sources, if factual claims are included

---

# Content Categories

The agent may classify requests into:

- Blog/article
- Social post
- Email
- Landing page
- Advertisement
- Product copy
- Educational content
- Internal communication
- Executive communication
- Script
- Rewrite/edit
- Summary
- Content brief

---

# Tone Options

Common supported tones include:

- Professional
- Friendly
- Conversational
- Persuasive
- Executive
- Educational
- Concise
- Warm
- Formal
- Playful
- Technical
- Neutral

---

# Quality Standards

Generated content should be:

- Clear
- Original
- Accurate
- Audience-appropriate
- Brand-aligned
- Well-structured
- Grammatically correct
- Easy to read
- Purpose-driven
- Safe to publish after review

---

# Evaluation

The Content Generator Agent is evaluated on:

- Audience fit
- Brand voice alignment
- Factual accuracy
- Originality
- Formatting compliance
- Tone control
- Clarity
- Grammar quality
- SEO quality, when relevant
- CTA effectiveness
- Safety
- Confidentiality protection

Evaluation cases are defined in:

```text
evaluation_cases.json
```

---

# Failure Modes

Common failure modes include:

- Hallucinated facts
- Unsupported statistics
- Brand voice mismatch
- Poor audience targeting
- Copyright issues
- Generic writing
- Weak structure
- Missing CTA
- SEO keyword stuffing
- Tone mismatch
- Confidentiality leakage
- Unsafe or insensitive content

See:

```text
failure_modes.md
```

---

# Human Review Requirements

Human review is required when content:

- Will be published externally
- Discusses legal, medical, financial, or regulatory topics
- Uses customer data or confidential information
- Represents official company policy
- Discusses incidents, layoffs, breaches, or crises
- Makes performance, revenue, safety, or compliance claims
- Uses statistics or research claims
- Is part of a paid marketing campaign
- Is being sent to executives, investors, press, or customers

---

# Safety Principles

The Content Generator Agent should:

- Never fabricate facts or sources
- Avoid misleading claims
- Protect confidential information
- Avoid copying copyrighted material
- Respect brand and editorial guidelines
- Flag uncertain or unsupported claims
- Avoid harmful or discriminatory language
- Recommend review for high-impact content
- Clearly distinguish draft content from approved content

---

# Design Principles

This agent follows these principles:

1. Clarity over complexity.
2. Originality over imitation.
3. Audience fit over generic writing.
4. Accuracy over persuasion.
5. Brand consistency over novelty.
6. Human review before publication.
7. Useful content over filler.

---

# Performance Metrics

Typical evaluation metrics include:

- Content acceptance rate
- Revision rate
- Factual error rate
- Brand voice match score
- Readability score
- SEO quality score
- Plagiarism/similarity score
- User satisfaction
- CTA effectiveness
- Time saved
- Human review pass rate

---

# Integration Points

This agent commonly integrates with:

- CMS platforms
- Marketing automation tools
- CRM systems
- SEO platforms
- Brand asset libraries
- Knowledge bases
- Content calendars
- Social media schedulers
- Email marketing platforms
- Document repositories

---

# Related Files

```text
agent.json
system_prompt.md
evaluation_cases.json
failure_modes.md
```

---

# Future Improvements

Potential future enhancements include:

- Brand voice scoring
- Automated SEO recommendations
- Content calendar generation
- A/B test variant generation
- Readability scoring
- Plagiarism detection
- Multi-language localization
- Persona-specific writing
- Approval workflow integration
- Performance feedback loops
- Content refresh recommendations

---

# Version

Current Version: 1.0

Status: Production Template
