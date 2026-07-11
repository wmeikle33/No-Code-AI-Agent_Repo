# Lead Qualification Agent Failure Modes

## Purpose

This document describes the known failure modes of the Lead Qualification Agent, their potential impact, methods for detection, and recommended mitigation strategies.

Understanding these failure modes helps improve qualification accuracy, reduce business risk, and ensure that important sales opportunities are neither missed nor incorrectly prioritized.

---

# Failure Severity Levels

| Level | Description |
|--------|-------------|
| Low | Minor qualification issue with little effect on sales operations. |
| Medium | Incorrect recommendation requiring manual review. |
| High | Significant qualification error that may affect sales pipeline quality. |
| Critical | Failure that could cause the loss of valuable opportunities, customer dissatisfaction, or compliance issues. |

---

# Failure Modes

## FM-001 — False Positive Qualification

### Description

The agent incorrectly identifies a low-quality prospect as a highly qualified lead.

### Example

A student downloading a free whitepaper is classified as a high-priority enterprise lead.

### Potential Causes

- Poor qualification criteria
- Overreliance on a single signal
- Incomplete lead information
- Weak scoring thresholds

### Impact

**High**

### Detection

- Sales representative review
- CRM conversion analysis
- Qualification audits

### Mitigation

- Require multiple qualification signals
- Use weighted scoring models
- Lower confidence when information is incomplete

---

## FM-002 — False Negative Qualification

### Description

The agent incorrectly rejects or deprioritizes a valuable lead.

### Example

A Fortune 500 company inquiry is marked as "low priority" because budget information was unavailable.

### Potential Causes

- Missing company information
- Overly strict qualification rules
- Missing contextual signals

### Impact

**Critical**

### Detection

- CRM opportunity review
- Lost opportunity analysis
- Sales manager audits

### Mitigation

- Escalate uncertain leads
- Treat missing information as unknown rather than negative
- Allow manual review of borderline cases

---

## FM-003 — Hallucinated Customer Information

### Description

The agent invents facts about a company or contact.

### Example

Claiming that a company has 5,000 employees when no evidence was provided.

### Potential Causes

- Model hallucination
- Missing CRM data
- Prompt ambiguity

### Impact

**Critical**

### Detection

- CRM verification
- Human review
- Data validation

### Mitigation

- Require evidence for all factual claims
- Clearly distinguish assumptions from verified information
- Leave unknown fields blank

---

## FM-004 — Incorrect Lead Score

### Description

The agent assigns an inaccurate qualification score.

### Example

A highly engaged prospect receives a score of 20/100.

### Potential Causes

- Incorrect weighting
- Missing data
- Calculation errors
- Poor prompt instructions

### Impact

**High**

### Detection

- Score distribution analysis
- Historical comparison
- Human review

### Mitigation

- Validate scoring rules
- Review weighting periodically
- Include explanation for each score

---

## FM-005 — Missing Required Information

### Description

The agent proceeds despite lacking critical qualification information.

### Example

Budget, company size, and purchasing timeline are all missing.

### Potential Causes

- Incomplete lead forms
- Missing CRM records
- Poor extraction

### Impact

**Medium**

### Detection

- Output validation
- Required-field checks

### Mitigation

- Explicitly identify missing fields
- Recommend follow-up questions
- Reduce confidence

---

## FM-006 — Poor Prioritization

### Description

The agent recommends an inappropriate follow-up priority.

### Example

A strategic enterprise opportunity is placed behind small one-time purchases.

### Potential Causes

- Weak prioritization rules
- Missing engagement data
- Incorrect weighting

### Impact

**High**

### Detection

- Pipeline review
- Sales performance analysis

### Mitigation

- Combine qualification score with business impact
- Periodically review prioritization logic

---

## FM-007 — Incorrect Routing

### Description

The lead is assigned to the wrong team or salesperson.

### Example

An enterprise healthcare lead is routed to a small-business sales representative.

### Potential Causes

- Missing routing rules
- Incorrect territory mapping
- Missing industry classification

### Impact

**High**

### Detection

- CRM routing audits
- Sales operations review

### Mitigation

- Validate routing rules
- Escalate uncertain assignments
- Review routing exceptions

---

## FM-008 — Overconfidence

### Description

The agent reports high confidence despite limited information.

### Example

"98% qualified."

Only a name and email address are available.

### Potential Causes

- Weak confidence calibration
- Sparse data

### Impact

**Medium**

### Detection

- Confidence calibration review
- Human evaluation

### Mitigation

- Lower confidence when important information is missing
- Explain confidence using supporting evidence

---

## FM-009 — Bias in Qualification

### Description

The agent systematically favors or disadvantages certain organizations or industries without business justification.

### Example

Large companies consistently receive higher scores regardless of engagement.

### Potential Causes

- Biased training data
- Poor scoring rules
- Historical sales bias

### Impact

**Critical**

### Detection

- Fairness audits
- Statistical analysis
- Human review

### Mitigation

- Regular bias evaluations
- Diverse evaluation datasets
- Transparent scoring explanations

---

## FM-010 — Policy Violation

### Description

The agent violates sales, privacy, or compliance policies.

### Example

Recommending contact with a lead that has opted out of communications.

### Potential Causes

- Missing compliance checks
- Outdated CRM information
- Incomplete policies

### Impact

**Critical**

### Detection

- CRM validation
- Compliance review
- Audit logs

### Mitigation

- Check communication preferences
- Validate against current policies
- Escalate uncertain compliance situations

---

## General Mitigation Strategies

The following practices reduce qualification failures:

- Verify factual claims using authoritative data.
- Clearly distinguish verified information from assumptions.
- Lower confidence when information is incomplete.
- Route uncertain cases for human review.
- Explain qualification decisions.
- Validate CRM data before recommendations.
- Respect privacy and communication preferences.
- Avoid unsupported assumptions.
- Periodically review scoring rules.

---

# Evaluation Recommendations

The Lead Qualification Agent should be evaluated using scenarios that include:

- Enterprise prospects
- Small-business prospects
- Returning customers
- Existing customers requesting upgrades
- Leads with incomplete information
- Conflicting CRM data
- Duplicate leads
- High-value opportunities
- Low-quality inquiries
- Opt-out contacts
- International prospects

Each evaluation should measure:

- Qualification accuracy
- Lead score accuracy
- Routing accuracy
- Hallucination rate
- Bias and fairness
- Policy compliance
- Recommendation quality
- Confidence calibration
- CRM field completeness
- Human reviewer agreement

---

# Revision History

| Version | Date | Changes |
|----------|------|---------|
| 1.0.0 | YYYY-MM-DD | Initial version |
