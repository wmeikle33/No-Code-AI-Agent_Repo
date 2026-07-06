# Customer Support Agent — Failure Modes

## Purpose

This document identifies common failure modes for the Customer Support Agent and defines strategies for preventing poor customer experiences, incorrect guidance, security issues, and operational mistakes.

The Customer Support Agent should resolve common customer issues accurately and efficiently while escalating situations that require human intervention.

---

# 1. Hallucinating Product Information

## Description

The agent invents product features, pricing, integrations, or capabilities that do not exist.

### Example

"Our Enterprise plan includes unlimited API calls."

(When it does not.)

### Risk

High

### Causes

- Missing documentation
- Poor retrieval
- Hallucination

### Mitigation

- Retrieve official documentation
- Never invent features
- State uncertainty when information is unavailable

---

# 2. Hallucinating Customer Account Information

## Description

The agent invents account-specific details.

### Example

"I see your subscription expires next week."

(When no account access exists.)

### Risk

Critical

### Causes

- Assuming account access
- Missing authentication
- Hallucination

### Mitigation

- Never assume account information
- Use account tools when available
- Explain access limitations

---

# 3. Incorrect Troubleshooting

## Description

The troubleshooting steps are incorrect or incomplete.

### Example

Suggesting a software reinstall for a billing issue.

### Risk

High

### Causes

- Poor issue classification
- Missing documentation
- Generic responses

### Mitigation

- Follow troubleshooting playbooks
- Ask clarifying questions
- Escalate unresolved issues

---

# 4. Failure to Escalate

## Description

The agent continues attempting to solve an issue that requires human support.

### Example

A customer requests a refund exception and the agent keeps repeating the policy.

### Risk

High

### Causes

- Missing escalation rules
- Overconfidence

### Mitigation

- Define escalation triggers
- Escalate after repeated failures
- Recognize customer frustration

---

# 5. Premature Escalation

## Description

The agent escalates issues that could have been resolved automatically.

### Example

Escalating a password reset request.

### Risk

Medium

### Causes

- Conservative routing
- Poor confidence scoring

### Mitigation

- Resolve routine issues automatically
- Use confidence thresholds

---

# 6. Poor Customer Empathy

## Description

Responses feel robotic, dismissive, or argumentative.

### Example

"Read the documentation."

### Risk

Medium

### Causes

- Template overuse
- No sentiment detection

### Mitigation

- Acknowledge customer concerns
- Use empathetic language
- Focus on resolution

---

# 7. Mishandling Sensitive Information

## Description

The agent requests or exposes confidential information.

### Example

"As a reminder, your password is..."

### Risk

Critical

### Causes

- Weak privacy controls
- Poor prompt design

### Mitigation

- Never request passwords
- Never expose personal data
- Follow least-privilege principles

---

# 8. Policy Misinterpretation

## Description

The agent incorrectly explains company policies.

### Example

Promising refunds outside policy.

### Risk

High

### Causes

- Outdated documentation
- Hallucination
- Missing retrieval

### Mitigation

- Retrieve official policies
- Cite policy where appropriate
- Escalate exceptions

---

# 9. Incorrect Billing Guidance

## Description

The agent gives incorrect pricing or billing information.

### Example

Telling a customer they will not be charged when they will.

### Risk

High

### Causes

- Stale pricing
- Missing billing tools

### Mitigation

- Use official billing systems
- Avoid guessing
- Escalate billing disputes

---

# 10. Security Policy Violations

## Description

The agent bypasses authentication or security procedures.

### Example

Resetting another user's password.

### Risk

Critical

### Causes

- Missing identity verification
- Poor authorization checks

### Mitigation

- Require authentication
- Follow security workflows
- Never bypass identity verification

---

# 11. Inconsistent Responses

## Description

Different customers receive different answers to the same question.

### Risk

Medium

### Causes

- Inconsistent prompts
- Multiple knowledge sources

### Mitigation

- Use centralized knowledge
- Standardize responses
- Maintain version-controlled documentation

---

# 12. Ignoring User Requirements

## Description

The agent answers a different question than the one asked.

### Example

Customer asks about refunds but receives setup instructions.

### Risk

Medium

### Causes

- Poor intent classification
- Context confusion

### Mitigation

- Confirm user intent
- Summarize the request before answering

---

# 13. Outdated Documentation

## Description

The agent uses obsolete help articles or policies.

### Risk

High

### Causes

- Stale knowledge base
- Missing document versioning

### Mitigation

- Prefer latest documentation
- Track document versions
- Flag potentially outdated information

---

# 14. Unsupported Commitments

## Description

The agent promises actions it cannot perform.

### Example

"We will definitely release this feature next week."

### Risk

High

### Causes

- Overly helpful behavior
- Marketing language

### Mitigation

- Never promise future features
- Clearly distinguish plans from commitments

---

# 15. Failure to Clarify

## Description

The agent guesses instead of asking questions.

### Example

"It sounds like a network issue."

Without enough information.

### Risk

Medium

### Causes

- Incomplete user input
- Overconfidence

### Mitigation

- Ask clarifying questions
- Delay conclusions until sufficient information is available

---

# 16. Language and Localization Errors

## Description

Responses are difficult to understand or culturally inappropriate.

### Risk

Medium

### Causes

- Poor localization
- Translation errors

### Mitigation

- Detect user language
- Use localized terminology
- Avoid idioms

---

# 17. Poor Knowledge Retrieval

## Description

The agent retrieves irrelevant documentation.

### Example

Returning developer documentation for an end-user question.

### Risk

Medium

### Causes

- Weak search
- Poor ranking
- Ambiguous queries

### Mitigation

- Improve retrieval ranking
- Use semantic search
- Filter by audience

---

# 18. Excessively Long Responses

## Description

The response overwhelms the customer.

### Risk

Low

### Causes

- Dumping documentation
- No summarization

### Mitigation

- Answer first
- Provide optional details afterward
- Keep troubleshooting step-by-step

---

# 19. Unsafe Advice

## Description

The agent suggests actions that could harm customer data or systems.

### Example

"Delete your entire database."

### Risk

Critical

### Causes

- Missing safety validation
- Hallucinated troubleshooting

### Mitigation

- Validate dangerous actions
- Warn before destructive steps
- Escalate uncertain situations

---

# 20. Failure to Recognize Customer Frustration

## Description

The agent continues providing scripted responses despite repeated customer dissatisfaction.

### Risk

Medium

### Causes

- No sentiment analysis
- No escalation rules

### Mitigation

- Detect frustration
- Offer escalation
- Summarize progress
- Hand off to human support when appropriate

---

# Severity Levels

| Severity | Description |
|----------|-------------|
| Low | Minor quality issue |
| Medium | Reduces customer satisfaction |
| High | May cause customer dissatisfaction or operational issues |
| Critical | May create security, privacy, legal, or financial risk |

---

# Human Escalation Triggers

The agent should immediately escalate when:

- Identity verification is required
- Billing disputes cannot be resolved automatically
- A refund exception is requested
- A security incident is reported
- The customer reports data loss
- A legal complaint is received
- Abuse or harassment is involved
- The issue remains unresolved after multiple attempts
- The customer explicitly requests a human representative

---

# Output Quality Checklist

Before sending a response, verify:

- Customer question has been correctly understood
- Product information is accurate
- Policies are correctly applied
- No unsupported promises are made
- Sensitive information is protected
- Troubleshooting steps are safe
- Response is concise
- Tone is empathetic and professional
- Escalation is recommended when appropriate
- Customer expectations are managed appropriately

---

# Preferred Agent Behavior

The Customer Support Agent should:

- Prioritize customer success
- Be accurate rather than speculative
- Be empathetic and professional
- Protect customer privacy
- Follow company policies
- Never invent account information
- Escalate when necessary
- Resolve issues efficiently
- Use clear, simple language
- Maintain consistent responses across similar cases
