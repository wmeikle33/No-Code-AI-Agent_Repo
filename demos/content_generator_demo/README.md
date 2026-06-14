# Content Generator Demo

## Overview

This demo demonstrates how the Content Generator workflow transforms a user request into structured content using predefined templates, tools, and routing logic.

The workflow is designed to generate high-quality content while maintaining consistency, formatting standards, and workflow transparency.

Examples of supported content include:

- Blog posts
- Product descriptions
- Marketing copy
- Social media content
- Email drafts
- Technical documentation
- Executive summaries

---

# Demo Objectives

This demo illustrates:

- Input validation
- Workflow routing
- Tool selection
- Content generation
- Output formatting
- Structured response generation

The goal is to provide a reproducible example of how the Content Generator workflow operates.

---

# Directory Structure

```text
content_generator_demo/
├── README.md
├── sample_input.json
├── expected_output.json
├── routing_trace.json
└── tool_schema.json
```

---

# Files

## sample_input.json

Contains a sample content generation request.

Typical fields include:

- Content type
- Topic
- Audience
- Tone
- Length requirements
- Formatting instructions

Example:

```json
{
  "content_type": "blog_post",
  "topic": "AI Agents in Customer Support",
  "audience": "Business Leaders",
  "tone": "Professional"
}
```

Purpose:

- Demonstrates expected workflow input
- Supports testing and validation
- Provides examples for developers

---

## expected_output.json

Contains the expected workflow response.

Typical fields include:

- Generated content
- Content metadata
- Formatting information
- Quality checks
- Workflow status

Purpose:

- Defines expected behavior
- Supports regression testing
- Enables output validation

---

## routing_trace.json

Captures workflow execution details.

Examples include:

- Routing decisions
- Selected tools
- Template selection
- Content generation path
- Validation checkpoints

Purpose:

- Improves workflow transparency
- Supports debugging
- Documents decision-making behavior

---

## tool_schema.json

Defines tools available to the workflow.

Examples:

- Content Generator
- Template Selector
- Grammar Checker
- Style Validator
- Fact Checker
- SEO Analyzer

Purpose:

- Standardize tool usage
- Support workflow validation
- Enable agent interoperability

---

# Example Workflow

```text
sample_input.json
        │
        ▼
Input Validation
        │
        ▼
Workflow Router
        │
        ▼
Template Selection
        │
        ▼
Content Generation
        │
        ▼
Quality Validation
        │
        ▼
Output Formatting
        │
        ▼
expected_output.json
```

---

# Validation Process

A successful workflow execution should:

1. Validate the request.
2. Select the appropriate content strategy.
3. Invoke required tools.
4. Generate content.
5. Perform quality checks.
6. Produce structured output.

---

# Testing

Example execution:

```bash
python run_demo.py \
    --input sample_input.json
```

Results should:

- Match the expected schema.
- Follow the documented routing path.
- Produce content similar to expected_output.json.

---

# Example Use Cases

## Marketing

Generate:

- Product descriptions
- Landing page copy
- Email campaigns

---

## Content Marketing

Generate:

- Blog articles
- Newsletters
- Thought leadership content

---

## Customer Support

Generate:

- Knowledge base articles
- FAQ content
- Help center documentation

---

## Internal Operations

Generate:

- Meeting summaries
- Status reports
- Executive briefings

---

# Success Criteria

The workflow is considered successful if:

- Input passes validation
- Routing behaves as expected
- Tool selection is correct
- Content quality requirements are met
- Output conforms to schema

---

# Related Components

- `agents/content_generator`
- `agents/marketing_assistant`
- `workflows/content_creation`
- `code_modules/templates`
- `code_modules/tools`
- `code_modules/routing`

---

# Future Enhancements

Potential improvements include:

- SEO optimization
- Multi-language generation
- Brand voice enforcement
- Citation generation
- Content scoring
- Human review workflows

---

# Version Information

| Field | Value |
|---------|---------|
| Demo | Content Generator |
| Version | 1.0 |
| Status | Draft |
| Purpose | Workflow Demonstration |
| Last Updated | YYYY-MM-DD |
