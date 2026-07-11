# Incident Response Agent Failure Modes

## Purpose

This document describes the known failure modes of the Incident Response Agent, their potential impact, methods for detecting them, and recommended mitigation strategies.

Understanding these failure modes helps improve system reliability, guide evaluation, and determine when human review is required.

---

# Failure Severity Levels

| Level | Description |
|--------|-------------|
| Low | Minor issue with little operational impact. |
| Medium | Incorrect or incomplete response requiring manual correction. |
| High | Significant error that could delay incident response or mislead responders. |
| Critical | Failure that could contribute to unsafe decisions, security risks, or major business disruption. |

---

# Failure Modes

## FM-001 — Incorrect Severity Classification

### Description

The agent assigns the wrong incident severity.

### Example

A production outage is classified as **Medium** instead of **Critical**.

### Potential Causes

- Incomplete incident description
- Ambiguous user input
- Missing monitoring data
- Poorly defined severity criteria

### Impact

**High**

### Detection

- Comparison with organizational severity matrix
- Human review
- Automated validation rules

### Mitigation

- Request additional information
- Reference severity policy before responding
- Escalate when confidence is low

---

## FM-002 — Missing Escalation

### Description

The agent fails to recommend escalation for a serious incident.

### Example

A suspected customer data breach is handled without notifying the security team.

### Potential Causes

- Missing context
- Failure to recognize security indicators
- Incomplete escalation policy

### Impact

**Critical**

### Detection

- Human review
- Evaluation test cases
- Audit log analysis

### Mitigation

- Always escalate possible security incidents
- Apply policy-based escalation rules
- Require human review for Critical incidents

---

## FM-003 — Hallucinated Information

### Description

The agent invents facts that are not supported by the provided evidence.

### Example

Claiming that a database server failed when no logs indicate this.

### Potential Causes

- Missing evidence
- Prompt over-generalization
- Model uncertainty

### Impact

**Critical**

### Detection

- Evidence verification
- Citation checks
- Human review

### Mitigation

- Require evidence for factual claims
- Clearly label assumptions
- State when information is unknown

---

## FM-004 — Unsafe Recommendations

### Description

The agent recommends actions that could worsen the incident.

### Example

Suggesting that production databases be deleted to recover storage.

### Potential Causes

- Missing operational context
- Weak safety constraints
- Misinterpreted request

### Impact

**Critical**

### Detection

- Human approval
- Policy validation

### Mitigation

- Never recommend destructive actions without approval
- Prefer containment before recovery
- Follow organizational runbooks

---

## FM-005 — Incomplete Incident Summary

### Description

Important details are omitted from the response.

### Example

The affected systems are not listed.

### Potential Causes

- Poor extraction
- Long input context
- Missing structured fields

### Impact

**Medium**

### Detection

- Output schema validation
- Human review

### Mitigation

- Use structured response templates
- Validate required fields before completion

---

## FM-006 — Incorrect Root Cause Assumption

### Description

The agent presents speculation as confirmed fact.

### Example

"The outage was caused by a firewall update."

No supporting evidence exists.

### Potential Causes

- Pattern matching
- Insufficient evidence
- Ambiguous logs

### Impact

**High**

### Detection

- Evidence review
- Root cause verification

### Mitigation

- Clearly distinguish observations from hypotheses
- Recommend further investigation

---

## FM-007 — Failure to Identify Missing Information

### Description

The agent proceeds despite lacking critical diagnostic data.

### Example

No request is made for logs or timestamps.

### Potential Causes

- Overconfidence
- Incomplete checklist

### Impact

**High**

### Detection

- Evaluation datasets
- Human review

### Mitigation

- Always include a "Missing Information" section
- Use required-information checklists

---

## FM-008 — Poor Communication

### Description

The response is difficult to understand during a time-sensitive incident.

### Example

Large unstructured paragraphs instead of concise action items.

### Potential Causes

- Unstructured output
- Missing formatting instructions

### Impact

**Medium**

### Detection

- Human review
- Readability evaluation

### Mitigation

- Use standardized response templates
- Prioritize actionable recommendations

---

## FM-009 — Policy Violation

### Description

The response conflicts with organizational incident response policies.

### Example

Skipping mandatory approval before recommending production recovery.

### Potential Causes

- Outdated knowledge
- Missing policy documents

### Impact

**High**

### Detection

- Policy compliance checks
- Human review

### Mitigation

- Reference current policies
- Escalate when policies are unavailable or conflicting

---

## FM-010 — Overconfidence

### Description

The agent reports high confidence despite limited evidence.

### Example

"95% confident this is a network issue."

Only one log entry was provided.

### Potential Causes

- Weak confidence estimation
- Sparse input

### Impact

**Medium**

### Detection

- Confidence calibration evaluation
- Human review

### Mitigation

- Lower confidence when evidence is incomplete
- Explain confidence using available observations

---

# General Mitigation Strategies

The following practices reduce the likelihood and impact of failures:

- Follow organizational incident response policies.
- Preserve evidence before recommending recovery actions.
- Escalate uncertain or high-risk incidents.
- Require human approval for Critical incidents.
- Distinguish facts from assumptions.
- Use structured response templates.
- Validate required output fields.
- Clearly communicate uncertainty.
- Never fabricate missing information.

---

# Evaluation Recommendations

The Incident Response Agent should be evaluated using scenarios that include:

- Production outages
- Cybersecurity incidents
- Customer data exposure
- Infrastructure failures
- Incomplete incident reports
- Conflicting evidence
- False-positive alerts
- False-negative alerts
- Ambiguous incident descriptions
- Missing monitoring data

Each evaluation should measure:

- Severity classification accuracy
- Escalation accuracy
- Policy compliance
- Hallucination rate
- Completeness of documentation
- Recommendation quality
- Output schema compliance
- Human reviewer agreement

---

# Revision History

| Version | Date | Changes |
|----------|------|---------|
| 1.0.0 | YYYY-MM-DD | Initial version |
