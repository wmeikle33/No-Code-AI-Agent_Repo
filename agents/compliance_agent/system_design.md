# Compliance Agent System Design

## Purpose

The Compliance Agent reviews user requests, agent outputs, documents, workflows, and tool actions for policy, regulatory, security, privacy, and governance risks.

It does not replace legal, compliance, or security teams. It identifies risks, explains why they matter, and routes high-risk cases for human review.

## Responsibilities

- Detect compliance risks in user requests and generated outputs
- Check for privacy, security, legal, financial, HR, and data-handling concerns
- Verify whether required approvals or citations are present
- Flag risky tool usage before execution
- Produce structured compliance reports
- Escalate high-risk cases to human reviewers
- Maintain audit-ready decision logs

## Non-Responsibilities

- Providing final legal advice
- Approving regulated actions without human review
- Making employment, medical, financial, or legal decisions independently
- Modifying source records without authorization
- Ignoring organization-specific policy requirements

## Inputs

The agent may receive:

- User request
- Draft agent response
- Workflow step
- Tool call request
- Retrieved documents
- Policy documents
- Jurisdiction or region
- User role and permissions
- Data sensitivity labels
- Previous audit logs

## Outputs

The agent should return a structured result:

```json
{
  "status": "approved | needs_revision | blocked | escalate",
  "risk_level": "low | medium | high | critical",
  "risk_categories": [
    "privacy",
    "security",
    "legal",
    "financial",
    "hr",
    "regulated_advice",
    "data_retention"
  ],
  "findings": [
    {
      "issue": "Contains personal data without stated purpose",
      "severity": "high",
      "evidence": "Customer email and phone number included in output",
      "recommendation": "Remove or mask unnecessary personal data"
    }
  ],
  "required_actions": [
    "Mask personal identifiers",
    "Add source citation",
    "Route to compliance reviewer"
  ],
  "human_review_required": true
}
