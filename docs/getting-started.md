# Getting Started with No-Code AI Agents at Greenscale INc

## What Is an AI Agent?

An AI agent is a digital worker that can:

- Receive information
- Make decisions using rules or AI
- Use tools
- Take actions
- Return results

Think of an AI agent as a team member with a clearly defined job.

### Human Example

A sales coordinator might:

1. Read an email
2. Determine if it is a sales inquiry
3. Check company information
4. Route the lead to the sales team

An AI agent can perform the same workflow automatically.

---

## Core Building Blocks

This repository is organized around four simple concepts:

### 1. Trigger

A trigger starts the workflow.

Examples:

- New email arrives
- Form submission received
- Slack message posted
- CRM record created

Example:

```text
Customer submits:
"I would like pricing for my company."
```

The submission triggers the agent.

---

### 2. Agent

The agent analyzes the information and decides what to do next.

Example:

```text
Input:
"We need pricing for 200 employees."
```

Agent reasoning:

- Pricing request detected
- Business context detected
- High-value lead identified

Decision:

```text
Route to Sales
```

---

### 3. Tools

Tools allow the agent to perform tasks.

Examples:

- Search a knowledge base
- Query a CRM
- Read documents
- Call an API
- Generate a report

Think of tools as the agent's toolbox.

Without tools:

```text
Agent can think
```

With tools:

```text
Agent can act
```

---

### 4. Actions

Actions are the final outputs.

Examples:

- Create a ticket
- Send an email
- Update a CRM record
- Notify a team
- Generate a report

Example:

```text
Action:
Create Sales Opportunity
```

---

## How Everything Fits Together

```text
Trigger
   ↓
Agent
   ↓
Tools
   ↓
Decision
   ↓
Action
```

Example:

```text
Customer Form Submitted
          ↓
Lead Qualification Agent
          ↓
CRM Lookup Tool
          ↓
Lead Score Calculated
          ↓
Route to Sales Team
```

---

## Repository Structure

### `agents/`

Defines agent behavior and responsibilities.

Examples:

- Lead Qualification Agent
- Support Triage Agent
- HR Assistant Agent

### `workflows/`

Defines the sequence of steps.

Examples:

- Lead Routing Workflow
- Ticket Escalation Workflow

### `tools/`

Reusable capabilities available to agents.

Examples:

- CRM Search
- Document Search
- API Connector

### `knowledge/`

Reference information used by agents.

Examples:

- Policies
- FAQs
- Product Documentation

### `demos/`

Runnable examples showing the system in action.

---

## How to Customize a Workflow

### Step 1: Identify the Trigger

Example:

```text
New Customer Inquiry
```

### Step 2: Define the Decision Logic

Questions:

- Is this sales?
- Is this support?
- Is this urgent?

### Step 3: Select Required Tools

Example:

```text
CRM Lookup
Knowledge Search
Email Sender
```

### Step 4: Define Actions

Example:

```text
If Sales:
    Create Opportunity

If Support:
    Create Support Ticket
```

---

## Example Workflow

Customer submits:

```text
"We need pricing for 150 users."
```

Workflow:

```text
Trigger:
Customer Form Submitted

↓

Agent:
Lead Qualification Agent

↓

Tool:
CRM Lookup

↓

Decision:
High-Value Lead

↓

Action:
Send to Sales Team
```

Output:

```json
{
  "route": "sales",
  "lead_score": 85,
  "recommended_next_step": "Send to sales for follow-up"
}
```

---

## Beginner Checklist

Before creating a new workflow:

- [ ] Define the trigger
- [ ] Define the agent's goal
- [ ] Define required tools
- [ ] Define decision rules
- [ ] Define final actions
- [ ] Test with sample inputs
- [ ] Document expected outputs

---

## Visual Workflow Diagram

```text
┌─────────────┐
│   Trigger   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Agent    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Tools    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Decision   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Action    │
└─────────────┘
```

## Next Steps

1. Run the Lead Qualification Demo.
2. Review the workflow definitions in `workflows/`.
3. Explore the agent configurations in `agents/`.
4. Customize an existing workflow.
5. Create a new demo workflow based on your own use case.

For a runnable example, see `quickstart.md`.
