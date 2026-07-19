# Debate Pattern

## Overview

The **Debate pattern** improves reasoning by allowing multiple agents (or multiple reasoning paths) to independently develop and defend different solutions before a final decision is made.

Rather than relying on a single answer, the system compares competing arguments, identifies strengths and weaknesses, and synthesizes a better final result.

```text
            Task
              │
      ┌───────┴────────┐
      │                │
  Agent A          Agent B
      │                │
      └───────┬────────┘
              │
        Compare Arguments
              │
        Judge / Synthesizer
              │
        Final Decision
```

The Debate pattern is particularly useful for complex reasoning tasks where multiple valid approaches exist or where identifying weaknesses is as important as generating solutions.

---

## Core Idea

A single reasoning process may overlook assumptions or alternative solutions.

By generating multiple independent viewpoints, the system can:

- Discover alternative solutions
- Identify logical errors
- Reduce confirmation bias
- Compare trade-offs
- Produce more balanced decisions

The objective is not to "win" the debate but to improve the overall quality of the final answer.

---

## Components

### Participants

Each participant independently develops a solution.

Participants may:

- Use different prompts
- Use different reasoning strategies
- Use different models
- Access different tools
- Represent different perspectives

Each participant should reason independently before seeing another participant's answer.

---

### Judge

The judge reviews all arguments.

Responsibilities include:

- Comparing evidence
- Identifying weaknesses
- Resolving disagreements
- Synthesizing the strongest ideas
- Producing the final answer

The judge should not simply vote for the longest or most confident response.

---

### Controller

The controller manages the workflow.

Responsibilities include:

- Launching participants
- Collecting responses
- Managing debate rounds
- Invoking the judge
- Recording results
- Applying stopping conditions

---

## Basic Workflow

```text
Receive Task
      │
Create Independent Arguments
      │
Compare Arguments
      │
Judge Reviews Debate
      │
Return Final Answer
```

---

## Example

A user asks:

> Should our company build or buy an AI platform?

### Agent A

Arguments for building internally:

- Full customization
- Data ownership
- Long-term flexibility
- Competitive advantage

### Agent B

Arguments for buying:

- Faster deployment
- Lower upfront cost
- Vendor support
- Reduced engineering effort

### Judge

The judge concludes:

- Buy initially
- Build specialized components later
- Review after 12 months

The final recommendation combines strengths from both perspectives.

---

## Debate Styles

### Two-Agent Debate

```text
Agent A
    │
    ▼
Judge
    ▲
    │
Agent B
```

Simple and inexpensive.

---

### Multi-Agent Debate

```text
Agent A
Agent B
Agent C
Agent D
      │
      ▼
Judge
```

Provides more perspectives but increases cost and complexity.

---

### Round-Based Debate

```text
Round 1

Agent A
Agent B

↓

Exchange Arguments

↓

Round 2

Agent A Responds
Agent B Responds

↓

Judge
```

Allows participants to address weaknesses in opposing arguments.

---

## Independent Reasoning

Participants should develop their solutions independently before seeing other responses.

Poor workflow:

```text
Agent A

↓

Agent B Reads Agent A

↓

Copies Most Arguments
```

Better workflow:

```text
Agent A

Agent B

↓

Independent Solutions

↓

Comparison
```

Independence increases diversity and reduces shared blind spots.

---

## Judge Responsibilities

A judge should evaluate:

- Evidence quality
- Logical consistency
- Completeness
- Assumptions
- Risks
- Trade-offs
- Missing information
- Overall recommendation

The judge should explain *why* one argument is stronger rather than simply selecting a winner.

---

## Evaluation Rubric

| Criterion | Question |
|-----------|----------|
| Correctness | Are the arguments factually accurate? |
| Evidence | Are claims supported? |
| Logic | Is the reasoning sound? |
| Completeness | Are important aspects covered? |
| Trade-offs | Are advantages and disadvantages considered? |
| Practicality | Is the recommendation realistic? |
| Risk | Are potential risks identified? |

---

## Debate Prompt Example

Participant prompt:

```text
Develop the strongest possible solution to the problem.

Support your reasoning with evidence.

Do not consider other possible solutions.
```

Judge prompt:

```text
Compare all submitted arguments.

Identify:

- Strengths
- Weaknesses
- Missing information
- Incorrect assumptions
- Best overall recommendation

Produce a final synthesized answer.
```

---

## When to Use This Pattern

The Debate pattern works well for:

- Strategic planning
- Architecture decisions
- Research synthesis
- Business recommendations
- Policy analysis
- Scientific reasoning
- Complex design choices
- Risk assessment
- Multi-step planning

---

## When Not to Use It

Avoid this pattern when:

- The task has one deterministic answer
- Simple validation exists
- Latency is critical
- Cost must be minimized
- The task is straightforward

For example:

- JSON validation
- Arithmetic
- Unit conversion
- Schema validation

These are better handled using deterministic methods.

---

## Common Failure Modes

### Echo Chamber

Participants produce nearly identical answers.

**Solution**

Use different prompts, models, tools, or reasoning strategies.

---

### Weak Judge

The judge simply averages opinions.

**Solution**

Require explicit comparison and justification.

---

### Endless Debate

Participants continue arguing without improving the answer.

**Solution**

Limit the number of debate rounds.

---

### Confirmation Bias

All participants share similar assumptions.

**Solution**

Assign different roles or viewpoints.

---

### Overconfidence

The system chooses the most confident argument rather than the best-supported one.

**Solution**

Evaluate evidence instead of confidence.

---

## Stopping Conditions

Terminate the debate when:

- Maximum rounds are reached
- The judge reaches a decision
- No substantial new arguments appear
- Cost or latency limits are exceeded
- Human review is required

---

## Debate Variations

### Devil's Advocate

One participant intentionally challenges the dominant solution.

Useful for:

- Risk analysis
- Architecture review
- Decision validation

---

### Expert Panel

Each participant represents a specialist.

Example:

```text
Security Expert

Cost Expert

ML Expert

Legal Expert

↓

Judge
```

---

### Multi-Model Debate

Different foundation models generate competing arguments.

Example:

```text
Model A

Model B

Model C

↓

Judge
```

This can improve diversity but increases operational complexity.

---

## Human-in-the-Loop Debate

For high-impact decisions, a human reviewer may participate.

```text
Agents

↓

Judge

↓

Human Reviewer

↓

Final Decision
```

Human review is particularly valuable when decisions involve legal, financial, medical, or safety implications.

---

## No-Code Implementation

Typical workflow:

1. Receive the task.
2. Send the task to multiple participants simultaneously.
3. Collect responses.
4. Send responses to the judge.
5. Generate the final recommendation.
6. Store debate logs and reasoning.
7. Return the final answer.

---

## Observability

Track:

- Participant outputs
- Judge decision
- Debate rounds
- Cost
- Latency
- Agreement rate
- Final confidence
- Human overrides

This information supports debugging and continuous improvement.

---

## Evaluation Metrics

Measure:

- Final answer quality
- Human preference rate
- Error reduction
- Decision accuracy
- Average debate rounds
- Cost per task
- Latency
- Agreement between participants
- Judge consistency

Debate should provide measurable improvements over simpler approaches.

---

## Design Checklist

Before implementing the Debate pattern, ensure that:

- Participants reason independently.
- Debate objectives are clearly defined.
- The judge has explicit evaluation criteria.
- Maximum debate rounds are configured.
- Costs and latency are monitored.
- Participant outputs are logged.
- Human review exists for high-risk workflows.
- Final decisions explain why they were chosen.

---

## Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Produces higher-quality reasoning | Higher cost |
| Identifies hidden assumptions | Increased latency |
| Explores multiple solutions | More orchestration |
| Encourages balanced decisions | Requires a reliable judge |
| Reduces confirmation bias | More complex implementation |

---

## Related Patterns

- Generator–Critic
- Reflection
- Evaluator–Optimizer
- Supervisor–Worker
- Consensus
- Human-in-the-Loop

---

## Related Anti-Patterns

- Too Many Agents
- Overplanning
- Blind Retries
- Infinite Loops
- Prompt Bloat

---

## Pattern Summary

The Debate pattern improves decision quality by comparing multiple independent solutions before selecting or synthesizing a final answer.

Rather than trusting the first solution, the system evaluates competing perspectives, identifies strengths and weaknesses, and produces a more robust final recommendation.

Like all multi-agent patterns, Debate should be used only when the expected improvement in quality justifies the additional cost, latency, and orchestration complexity.
