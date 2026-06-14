# Employee FAQ Demo

## Overview

This demo demonstrates how the Employee FAQ workflow answers common employee questions using approved company knowledge sources.

The workflow is designed to provide accurate, consistent, and policy-compliant responses to employee inquiries while reducing the workload on HR, IT, and operations teams.

Typical topics include:

- Benefits
- Leave policies
- Payroll
- Remote work guidelines
- IT support
- Company policies
- Employee onboarding

This demo serves as a reference implementation for internal employee support workflows.

---

# Demo Objectives

The workflow is designed to:

- Understand employee questions
- Retrieve relevant policy information
- Generate compliant responses
- Escalate complex cases when necessary
- Provide supporting references
- Maintain consistent communication

---

# Directory Structure

```text
employee_faq_demo/
├── README.md
├── sample_input.json
├── expected_output.json
├── routing_trace.json
└── tool_schema.json
```

---

# Files

## sample_input.json

Contains a sample employee question submitted to the workflow.

Example:

```json
{
  "employee_id": "EMP12345",
  "question": "How many vacation days do I receive each year?",
  "department": "Engineering"
}
```

Purpose:

- Demonstrates expected input format
- Supports testing and validation
- Provides example employee inquiries

---

## expected_output.json

Contains the expected workflow response.

Example:

```json
{
  "status": "success",
  "answer": "Full-time employees receive 20 vacation days annually.",
  "source": "Employee Handbook"
}
```

Typical outputs include:

- Answer text
- Confidence score
- Supporting references
- Escalation status

---

## routing_trace.json

Documents workflow execution decisions.

Examples include:

- Question classification
- Knowledge retrieval steps
- Escalation decisions
- Tool invocations
- Response generation path

Purpose:

- Improve transparency
- Support debugging
- Validate workflow behavior

---

## tool_schema.json

Defines tools available to the workflow.

Examples:

- Policy Search Tool
- Employee Handbook Retriever
- Benefits Lookup Tool
- Payroll Information Tool
- Escalation Manager
- FAQ Classifier

Purpose:

- Standardize tool invocation
- Support validation
- Enable workflow interoperability

---

# Example Workflow

```text
sample_input.json
        │
        ▼
Question Classification
        │
        ▼
Knowledge Retrieval
        │
        ▼
Policy Validation
        │
        ▼
Response Generation
        │
        ▼
Compliance Review
        │
        ▼
expected_output.json
```

---

# Supported Question Categories

## Human Resources

Examples:

- Vacation policies
- Sick leave
- Paid time off
- Holidays
- Benefits

---

## Payroll

Examples:

- Pay schedules
- Tax documents
- Reimbursements
- Overtime policies

---

## Information Technology

Examples:

- Password resets
- VPN access
- Software requests
- Device support

---

## Company Policies

Examples:

- Code of conduct
- Travel policies
- Security requirements
- Remote work guidelines

---

## Onboarding

Examples:

- New hire procedures
- Required training
- Account setup
- Documentation requirements

---

# Escalation Rules

The workflow should escalate questions when:

- Information is unavailable
- Policy ambiguity exists
- Manager approval is required
- Sensitive employee information is involved
- Legal or compliance review is needed

Example escalation targets:

- HR Team
- Payroll Team
- IT Help Desk
- Compliance Team

---

# Validation Process

A successful workflow execution should:

1. Validate the question.
2. Classify the request category.
3. Retrieve relevant information.
4. Verify response compliance.
5. Determine whether escalation is required.
6. Generate a structured response.

---

# Testing

Example execution:

```bash
python run_demo.py \
    --input sample_input.json
```

Output should:

- Match the expected schema.
- Follow the documented routing path.
- Produce results consistent with expected_output.json.

---

# Example Use Cases

## HR Self-Service

Allow employees to answer common HR questions without opening tickets.

---

## IT Help Desk

Reduce repetitive support requests.

---

## Employee Onboarding

Provide immediate answers for new employees.

---

## Policy Assistance

Help employees locate and understand company policies.

---

# Success Criteria

The workflow is considered successful if:

- Question classification is correct.
- Relevant knowledge is retrieved.
- Responses comply with company policy.
- Escalations occur when appropriate.
- Output conforms to schema.

---

# Related Components

- `agents/employee_support`
- `agents/customer_support`
- `workflows/employee_faq`
- `code_modules/connectors/email`
- `code_modules/connectors/hr_systems`
- `code_modules/tools/knowledge_search`

---

# Future Enhancements

Potential improvements include:

- Multi-language support
- Personalized employee responses
- Benefits eligibility calculations
- Integration with HR platforms
- Conversational follow-up support
- Employee satisfaction tracking

---

# Version Information

| Field | Value |
|---------|---------|
| Demo | Employee FAQ |
| Version | 1.0 |
| Status | Draft |
| Purpose | Workflow Demonstration |
| Last Updated | YYYY-MM-DD |
