# Lead Qualification Demo

This demo shows an end-to-end AI-agent workflow for qualifying an inbound sales lead.

The workflow demonstrates how a business request moves through:

1. Sample input
2. Agent routing
3. Tool call/schema validation
4. Final structured output

## Files

| File | Purpose |
|---|---|
| `sample_input.json` | Example inbound lead submitted by a user or form |
| `routing_trace.json` | Shows how the coordinator routes the request to the correct agent |
| `tool_schema.json` | Defines the expected tool/interface contract |
| `expected_output.json` | Shows the final structured result from the workflow |

## Workflow

```text
Inbound Lead
    ↓
Coordinator Agent
    ↓
Lead Qualification Agent
    ↓
Tool Schema Validation
    ↓
Lead Score + Recommendation
