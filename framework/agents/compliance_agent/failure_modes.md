# Compliance Agent — Failure Modes

## Purpose

This document identifies common ways the Compliance Agent can fail and defines safeguards for reducing legal, regulatory, operational, and reputational risk.

The Compliance Agent should support policy interpretation, compliance review, risk classification, audit preparation, and escalation, but it should not replace qualified legal, compliance, security, or privacy professionals.

---

## 1. Providing Legal Advice

### Description
The agent may make definitive legal judgments instead of providing compliance support.

### Example
“This contract is legally enforceable.”

### Risk
Critical

### Causes
- User asks for a legal conclusion
- Agent oversteps its advisory role
- Missing escalation rules

### Mitigation
- Clearly state that legal determinations require qualified counsel
- Provide general compliance considerations only
- Escalate legal-risk decisions to humans

---

## 2. Hallucinating Policies or Regulations

### Description
The agent may invent policy sections, regulatory clauses, requirements, or compliance standards.

### Example
“According to Section 8.4 of the company policy...” when no such section exists.

### Risk
Critical

### Causes
- Missing source documents
- Overconfidence
- Poor retrieval grounding
- Pressure to provide a complete answer

### Mitigation
- Require citations for policy-based claims
- Say when a policy cannot be found
- Use “unknown” instead of guessing
- Never fabricate exact clause numbers or quotes

---

## 3. Using Outdated Regulations

### Description
The agent may rely on old legal or regulatory requirements.

### Example
The agent applies an outdated privacy requirement after a regulation has changed.

### Risk
High

### Causes
- Stale knowledge base
- No freshness checks
- Old internal documents
- Missing effective dates

### Mitigation
- Track regulation and policy effective dates
- Require recent sources for current-law questions
- Flag potentially outdated guidance
- Escalate time-sensitive regulatory questions

---

## 4. Misinterpreting Internal Policy

### Description
The agent may apply the wrong internal policy or misunderstand policy language.

### Example
The agent approves an expense under a travel policy when the finance policy actually prohibits it.

### Risk
High

### Causes
- Ambiguous policy language
- Multiple overlapping policies
- Poor document retrieval
- Missing business context

### Mitigation
- Retrieve all relevant policies
- Identify uncertainty
- Explain reasoning step by step
- Escalate ambiguous cases

---

## 5. Missing Required Information

### Description
The agent may make a compliance decision without enough facts.

### Example
Approving a vendor without knowing whether they process personal data.

### Risk
High

### Causes
- Incomplete user input
- No required-information checklist
- Over-eagerness to answer

### Mitigation
- Ask for missing facts
- Use intake checklists
- Refuse to classify risk when required fields are absent
- Mark conclusions as provisional

---

## 6. False Compliance Approval

### Description
The agent may incorrectly determine that an action, vendor, policy, or process is compliant.

### Example
“This vendor is approved,” despite missing security documentation.

### Risk
Critical

### Causes
- Weak validation
- Missing evidence
- Misapplied criteria
- Overreliance on user statements

### Mitigation
- Require evidence for approval
- Use policy-defined approval criteria
- Distinguish “appears compliant” from “approved”
- Require human approval for high-risk decisions

---

## 7. False Compliance Rejection

### Description
The agent may incorrectly flag a compliant activity as non-compliant.

### Example
Rejecting a permitted data transfer because the agent misunderstands the company’s data handling policy.

### Risk
Medium to High

### Causes
- Overly conservative interpretation
- Missing exceptions
- Incomplete policy retrieval
- Poor contextual understanding

### Mitigation
- Check for policy exceptions
- Provide reasoning and confidence level
- Escalate instead of issuing final rejection when uncertain
- Allow human override

---

## 8. Failure to Escalate High-Risk Issues

### Description
The agent may continue answering when human review is required.

### Example
The user asks whether to self-report a regulatory violation, and the agent provides a direct recommendation.

### Risk
Critical

### Causes
- Missing escalation triggers
- No severity classification
- Lack of compliance boundaries

### Mitigation
- Define mandatory escalation scenarios
- Escalate legal, regulatory, privacy, security, and financial-risk issues
- Refuse to make final decisions in critical cases

---

## 9. Poor Citation Quality

### Description
The agent may cite irrelevant, outdated, or incorrect policies and regulations.

### Example
Citing a general security policy for a question about employee expense reimbursement.

### Risk
High

### Causes
- Weak retrieval
- Similar document names
- No source verification
- Citation hallucination

### Mitigation
- Verify citations match the claim
- Cite specific policy sections where possible
- Avoid citations if the source does not support the statement
- Prefer authoritative internal documents

---

## 10. Ignoring Policy Conflicts

### Description
The agent may fail to notice that two policies provide conflicting guidance.

### Example
A data retention policy requires deletion after 12 months, while a legal hold policy requires preservation.

### Risk
High

### Causes
- Single-document retrieval
- No conflict detection
- Lack of precedence rules

### Mitigation
- Search for related policies
- Identify conflicts explicitly
- Apply documented precedence rules only when available
- Escalate unresolved conflicts

---

## 11. Mishandling Sensitive Data

### Description
The agent may expose, summarize, or process sensitive personal, financial, legal, or confidential information incorrectly.

### Example
Including employee medical information in a compliance summary.

### Risk
Critical

### Causes
- No data classification
- Poor redaction
- Excessive detail in output
- Lack of access controls

### Mitigation
- Redact sensitive data when possible
- Use least-privilege access
- Avoid including unnecessary personal data
- Label outputs by sensitivity level

---

## 12. Weak Audit Trail

### Description
The agent may produce compliance recommendations without preserving enough evidence or reasoning for audit review.

### Example
The agent says a vendor was approved but does not record the criteria used.

### Risk
High

### Causes
- No structured output
- Missing timestamps
- Missing source references
- No decision log

### Mitigation
- Include decision rationale
- Record sources and dates
- Preserve reviewer and approval status
- Use structured compliance records

---

## 13. Overconfidence in Risk Classification

### Description
The agent may assign risk levels too confidently despite limited evidence.

### Example
Classifying a vendor as “low risk” based only on their website.

### Risk
High

### Causes
- Missing evidence thresholds
- No confidence scoring
- Incomplete vendor intake

### Mitigation
- Add confidence levels
- Require minimum evidence for risk classification
- Use “insufficient information” when appropriate
- Escalate high-impact classifications

---

## 14. Misclassifying Regulatory Scope

### Description
The agent may apply the wrong regulatory framework or fail to identify applicable rules.

### Example
Applying GDPR analysis to a scenario governed primarily by HIPAA or local employment law.

### Risk
High

### Causes
- Missing jurisdiction
- Missing industry context
- Ambiguous data types
- User-provided assumptions

### Mitigation
- Require jurisdiction, industry, and data type
- Identify applicable frameworks before analysis
- Flag uncertain regulatory scope
- Escalate cross-border or multi-regime issues

---

## 15. Treating Draft Policies as Approved Policies

### Description
The agent may rely on draft, archived, or superseded policy documents.

### Example
Using an old acceptable-use policy instead of the current approved version.

### Risk
High

### Causes
- Poor document versioning
- Missing status metadata
- Retrieval from outdated files

### Mitigation
- Check document status and version
- Prefer approved and current policies
- Flag draft or archived sources
- Require policy effective dates

---

## 16. Making Final Approval Decisions

### Description
The agent may approve contracts, vendors, expenses, data transfers, or policy exceptions without proper authority.

### Example
“This vendor is approved for production use.”

### Risk
Critical

### Causes
- Unclear authority boundaries
- Missing human-in-the-loop workflow
- User pressure

### Mitigation
- Use “recommendation” language
- Require human approval for final decisions
- Route approvals to the correct owner
- Track approval status separately from agent analysis

---

## 17. Producing Generic Compliance Output

### Description
The agent may generate vague compliance language that is not tied to the user’s actual policies or risk environment.

### Example
“Follow best practices and ensure compliance with regulations.”

### Risk
Medium

### Causes
- No policy retrieval
- Weak prompt instructions
- Missing business context

### Mitigation
- Require policy-grounded analysis
- Use specific controls and requirements
- Include actionable next steps
- Avoid generic compliance filler

---

## 18. Unsafe External Sharing

### Description
The agent may generate compliance summaries that expose internal risks, incidents, audits, or weaknesses to external parties.

### Example
Sending a vendor a detailed description of internal security gaps.

### Risk
High

### Causes
- No audience classification
- Missing redaction rules
- Confusion between internal and external outputs

### Mitigation
- Label output audience: internal, external, legal, executive
- Redact sensitive details
- Require review before external sharing
- Use separate external-safe templates

---

## 19. Poor Handling of Exceptions

### Description
The agent may fail to identify whether a policy exception is allowed, documented, expired, or requires approval.

### Example
Allowing an exception without checking whether it was approved by the compliance team.

### Risk
High

### Causes
- Missing exception registry
- No approval workflow
- No expiration tracking

### Mitigation
- Check exception records
- Require approver, date, scope, and expiration
- Flag undocumented exceptions
- Escalate expired or unclear exceptions

---

## 20. Confusing Compliance With Security

### Description
The agent may treat security controls as equivalent to compliance approval.

### Example
“SOC 2 certified” is treated as full approval for all data processing use cases.

### Risk
Medium to High

### Causes
- Overreliance on certifications
- Missing policy mapping
- Shallow risk analysis

### Mitigation
- Distinguish certifications from internal approval
- Map controls to specific requirements
- Identify gaps between external attestations and company policy
- Require additional review for sensitive use cases

---

# Severity Levels

| Severity | Description |
|---|---|
| Low | Minor issue with limited operational impact |
| Medium | May reduce usefulness or create confusion |
| High | Could cause incorrect compliance handling or business risk |
| Critical | Could create legal, regulatory, privacy, financial, or reputational harm |

---

# Mandatory Escalation Triggers

The agent must escalate to human review when:

- A legal interpretation or legal conclusion is requested
- A potential regulatory violation is involved
- A user asks whether to self-report an issue
- Personal, financial, health, employee, or confidential data is involved
- A contract, vendor, or data transfer requires approval
- Policies conflict or are ambiguous
- Source documents are missing or outdated
- The output will be shared externally
- The decision could create material business, legal, or reputational risk

---

# Output Quality Checklist

Before finalizing a compliance response, verify:

- The relevant policy or regulation was identified
- The source is current and authoritative
- Citations support the claims
- Missing information is clearly listed
- Assumptions are labeled
- Risk level is stated
- Confidence level is included
- Human escalation is recommended where appropriate
- No final legal decision is made
- Sensitive data is protected
- The response is actionable and auditable

---

# Preferred Agent Behavior

The Compliance Agent should:

- Be cautious
- Be policy-grounded
- Avoid legal conclusions
- Clearly identify uncertainty
- Ask for missing information
- Cite relevant sources
- Escalate high-risk decisions
- Preserve auditability
- Protect sensitive information
- Distinguish recommendations from approvals
