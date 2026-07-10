# Employee Support Agent — Failure Modes

## Purpose

This document identifies common failure modes for the Employee Support Agent and defines mitigation strategies to ensure accurate, secure, and policy-compliant assistance for employees.

The Employee Support Agent should provide evidence-based guidance using approved internal documentation while protecting confidential information and respecting organizational policies.

---

# 1. Hallucinated Company Policies

## Description

The agent invents HR policies, IT procedures, or company rules that do not exist.

### Example

"The company provides unlimited PTO."

(No such policy exists.)

### Risk

Critical

### Causes

- Weak retrieval
- Hallucination
- Missing documentation

### Mitigation

- Always retrieve official documentation
- Never invent policies
- Cite policy sources
- Clearly indicate when information is unavailable

---

# 2. Incorrect Policy Interpretation

## Description

The agent misinterprets an official policy.

### Example

Interpreting "manager approval may be required" as "manager approval is never required."

### Risk

High

### Causes

- Ambiguous wording
- Poor reasoning
- Missing context

### Mitigation

- Quote relevant policy sections
- Explain assumptions
- Recommend HR review when ambiguous

---

# 3. Using Outdated Documentation

## Description

The agent retrieves obsolete policies instead of the latest approved version.

### Example

Using the 2023 travel policy instead of the 2026 version.

### Risk

High

### Causes

- Poor version control
- Missing metadata
- Stale index

### Mitigation

- Prefer latest approved documents
- Display version information
- Warn when multiple versions exist

---

# 4. Unauthorized Information Disclosure

## Description

The agent exposes confidential employee information.

### Example

Showing another employee's salary or performance review.

### Risk

Critical

### Causes

- Missing access controls
- Weak authorization
- Improper retrieval

### Mitigation

- Enforce RBAC
- Validate user identity
- Respect document permissions
- Redact sensitive information

---

# 5. Incorrect HR Guidance

## Description

The agent provides incorrect information regarding HR procedures.

### Example

Incorrectly explaining parental leave eligibility.

### Risk

High

### Causes

- Missing documentation
- Hallucination
- Policy changes

### Mitigation

- Retrieve HR documentation
- Cite policies
- Escalate unusual cases

---

# 6. Incorrect IT Troubleshooting

## Description

The troubleshooting guidance is incorrect or unsafe.

### Example

Suggesting employees disable MFA.

### Risk

High

### Causes

- Weak documentation
- Hallucination

### Mitigation

- Follow approved IT procedures
- Never bypass security controls
- Escalate unresolved issues

---

# 7. Failure to Escalate

## Description

The agent attempts to resolve requests requiring HR, IT, Legal, or management approval.

### Example

Attempting to approve leave requests.

### Risk

High

### Causes

- Missing escalation rules
- Overconfidence

### Mitigation

- Define escalation criteria
- Recommend appropriate department
- Recognize authority boundaries

---

# 8. Premature Escalation

## Description

Routine questions are unnecessarily escalated.

### Example

Escalating a simple PTO policy question.

### Risk

Medium

### Causes

- Conservative prompting
- Low confidence thresholds

### Mitigation

- Resolve common questions automatically
- Improve retrieval quality

---

# 9. Incorrect Department Routing

## Description

The request is routed to the wrong internal team.

### Example

Sending a payroll question to Facilities.

### Risk

Medium

### Causes

- Weak intent classification
- Similar terminology

### Mitigation

- Improve routing rules
- Validate department mappings

---

# 10. Privacy Violations

## Description

Sensitive employee information is displayed unnecessarily.

### Example

Displaying employee home addresses.

### Risk

Critical

### Causes

- Missing redaction
- Weak permissions

### Mitigation

- Apply least-privilege principles
- Mask sensitive data
- Follow privacy policies

---

# 11. Incorrect Benefits Information

## Description

Benefits are explained incorrectly.

### Example

Providing outdated insurance coverage details.

### Risk

High

### Causes

- Outdated documentation
- Hallucination

### Mitigation

- Retrieve benefits documentation
- Display policy version
- Recommend Benefits team when uncertain

---

# 12. Weak Knowledge Retrieval

## Description

Relevant documentation is not retrieved.

### Example

Searching the wrong handbook.

### Risk

Medium

### Causes

- Poor search
- Weak embeddings
- Poor chunking

### Mitigation

- Improve hybrid retrieval
- Rerank results
- Search multiple collections

---

# 13. Ignoring Regional Differences

## Description

Policies vary by country or office, but the agent applies the wrong version.

### Example

Applying US leave policies to UK employees.

### Risk

High

### Causes

- Missing metadata
- Weak localization

### Mitigation

- Detect employee location
- Filter documents by region
- Display jurisdiction

---

# 14. Unsupported Commitments

## Description

The agent promises actions it cannot perform.

### Example

"I've approved your reimbursement."

### Risk

High

### Causes

- Poor prompt constraints

### Mitigation

- Clearly distinguish guidance from actions
- Never claim to execute workflows unless integrated

---

# 15. Failure to Clarify

## Description

The agent answers ambiguous requests without gathering enough information.

### Example

"How do I request leave?"

(Without knowing country or employment type.)

### Risk

Medium

### Causes

- Poor clarification logic

### Mitigation

- Ask targeted follow-up questions
- Identify missing context

---

# 16. Hallucinated Employee Information

## Description

The agent invents employee-specific details.

### Example

"You currently have 12 vacation days remaining."

### Risk

Critical

### Causes

- Hallucination
- Missing HR system access

### Mitigation

- Never invent employee data
- Use HR integrations only when authorized
- State access limitations

---

# 17. Security Policy Violations

## Description

The agent recommends bypassing security procedures.

### Example

Suggesting employees share passwords.

### Risk

Critical

### Causes

- Weak security guardrails

### Mitigation

- Follow security policies
- Recommend approved authentication methods
- Escalate security incidents

---

# 18. Poor Employee Experience

## Description

Responses are difficult to understand or overly technical.

### Example

Replying with policy language instead of a clear explanation.

### Risk

Medium

### Causes

- Documentation dumping
- Poor summarization

### Mitigation

- Use plain language
- Summarize policies
- Provide actionable next steps

---

# 19. Missing Citations

## Description

Policy guidance is provided without references.

### Risk

Medium

### Causes

- Weak retrieval
- Missing citation requirements

### Mitigation

- Cite handbook sections
- Include policy names
- Display document versions

---

# 20. Incorrect Confidence Estimation

## Description

The agent expresses high confidence despite weak supporting evidence.

### Example

"I'm certain..." when documentation is incomplete.

### Risk

Medium

### Causes

- Poor confidence scoring

### Mitigation

- Base confidence on retrieval quality
- Explain uncertainty
- Recommend human review

---

# Severity Levels

| Severity | Description |
|----------|-------------|
| Low | Minor usability issue |
| Medium | Reduces employee productivity or clarity |
| High | Could lead to incorrect business actions |
| Critical | Could expose confidential information, violate policy, or create legal or security risks |

---

# Human Escalation Triggers

Escalate when:

- HR approval is required
- Payroll modifications are requested
- Benefits eligibility is disputed
- Legal interpretation is requested
- Workplace misconduct is reported
- Security incidents are reported
- Confidential employee records are requested
- Company policies conflict
- Confidence is low
- The employee explicitly requests human assistance

---

# Output Quality Checklist

Before returning a response, verify:

- Current approved documentation was used
- Policies are correctly interpreted
- Citations are included where appropriate
- Confidential information is protected
- Employee permissions were respected
- Correct department is identified
- Escalation is recommended when required
- No unsupported promises are made
- Response is clear and actionable
- Confidence level matches available evidence

---

# Preferred Agent Behavior

The Employee Support Agent should:

- Be evidence-driven
- Prioritize employee privacy
- Follow organizational policies
- Use current documentation
- Clearly explain procedures
- Cite internal policies
- Escalate sensitive issues
- Protect confidential information
- Admit uncertainty when appropriate
- Support employees without replacing HR, IT, Finance, or Legal professionals
