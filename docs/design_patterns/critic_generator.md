# Generator–Critic Pattern

## Overview

The **Generator–Critic pattern** separates content creation from evaluation.

A **generator** produces an initial answer, plan, draft, or solution. A **critic** then reviews that output against explicit criteria and identifies errors, omissions, risks, or opportunities for improvement.

The generator may revise its output based on the critique, creating an iterative improvement cycle.

```text
Task
  ↓
Generator
  ↓
Draft
  ↓
Critic
  ↓
Feedback
  ↓
Revision
  ↓
Final Output
```

This pattern is useful when producing a draft is relatively easy, but verifying its quality requires a different perspective or stricter criteria.

---

## Core Idea

Generation and evaluation are different responsibilities.

The generator asks:

> What is a good solution?

The critic asks:

> Does this solution satisfy the requirements?

Separating these roles can reduce confirmation bias and make evaluation more systematic.

---

## Components

### Generator

The generator creates the initial output.

It may produce:

- An answer
- A document
- A plan
- Code
- A summary
- A recommendation
- A structured report
- A tool-use strategy

The generator should focus on solving the task rather than repeatedly judging its own work while creating it.

### Critic

The critic evaluates the generated output.

It may check:

- Correctness
- Completeness
- Relevance
- Clarity
- Consistency
- Safety
- Factual grounding
- Formatting
- Compliance with instructions
- Use of supporting evidence

The critic should return specific, actionable feedback rather than vague judgments.

### Revision Step

The generator receives the critique and updates the original output.

A revision step may:

- Correct factual errors
- Add missing information
- Remove irrelevant content
- Improve structure
- Resolve contradictions
- Strengthen evidence
- Adjust tone or format

### Controller

A controller manages the workflow.

It decides:

- Whether critique is required
- How many revision cycles are allowed
- Whether the output passes
- When to stop
- When to escalate to human review

The controller may be deterministic workflow logic rather than another agent.

---

## Basic Workflow

```text
Receive Task
     ↓
Generate Draft
     ↓
Evaluate Draft
     ↓
Does It Pass?
 ├── Yes → Return Final Output
 └── No
       ↓
    Revise Draft
       ↓
    Re-evaluate
```

Every implementation should include a clear stopping condition.

---

## Example

A user asks an agent to prepare a market analysis.

### Generator Output

The generator creates:

- A market overview
- Major competitors
- Customer segments
- Trends
- Risks
- Recommendations

### Critic Review

The critic checks whether:

- Claims are supported by evidence
- Competitors are current
- Risks are adequately covered
- Recommendations follow from the analysis
- Important customer segments are missing
- The requested format was followed

### Revision

The generator corrects unsupported claims, adds missing competitors, and strengthens the recommendations.

---

## Critic Output Format

Criticism should be structured and actionable.

A useful format is:

```text
Verdict: Revise

Strengths:
- The structure is clear.
- The main recommendation is relevant.

Issues:
1. Two factual claims lack supporting evidence.
2. The requested risk section is incomplete.
3. The conclusion introduces a recommendation not discussed earlier.

Required Changes:
- Add evidence for claims 2 and 4.
- Expand the risk section.
- Align the conclusion with the analysis.
```

Avoid feedback such as:

```text
This could be better.
```

That feedback gives the generator little guidance.

---

## Evaluation Rubric

The critic should evaluate the output against explicit criteria.

| Criterion | Question |
|---|---|
| Correctness | Are the claims and conclusions accurate? |
| Completeness | Are all requested elements included? |
| Relevance | Does the output stay focused on the task? |
| Consistency | Do sections agree with one another? |
| Evidence | Are important claims adequately supported? |
| Clarity | Is the output easy to understand? |
| Safety | Does the output avoid unacceptable risks? |
| Format | Does it follow the requested structure? |
| Actionability | Can the user act on the result? |

The rubric should be adapted to the task rather than reused blindly.

---

## Generator Prompt Responsibilities

A generator prompt should define:

- The objective
- Relevant context
- Available tools
- Constraints
- Expected output
- Quality requirements

Example:

```text
Create a concise project proposal based on the supplied requirements.

Include:
- Problem statement
- Proposed solution
- Scope
- Milestones
- Risks
- Success metrics

Do not invent unsupported facts.
```

---

## Critic Prompt Responsibilities

A critic prompt should define:

- What it is reviewing
- The evaluation criteria
- The expected feedback format
- What counts as a blocking issue
- Whether it may recommend acceptance

Example:

```text
Review the proposal against the original requirements.

Evaluate:
- Completeness
- Internal consistency
- Feasibility
- Risk coverage
- Measurable success criteria

Return:
- Verdict: Pass or Revise
- Strengths
- Issues
- Required changes

Do not rewrite the proposal.
```

The critic should normally evaluate before rewriting. Combining criticism and revision too early can make failures harder to diagnose.

---

## Same Model or Different Models?

The generator and critic may use the same model or different models.

### Same Model

Advantages:

- Simpler architecture
- Easier configuration
- Consistent capabilities
- Lower operational overhead

Disadvantages:

- Similar blind spots
- Greater risk of agreeing with its own output
- Less diversity in evaluation

### Different Models

Advantages:

- More diverse perspectives
- Different strengths can be combined
- Reduced dependence on one model's behavior

Disadvantages:

- More configuration
- Potentially higher cost
- Different output conventions
- More difficult evaluation

Different models are not automatically better. The choice should be tested against quality, cost, and latency requirements.

---

## Independent Critic vs. Self-Critique

### Independent Critic

A separate critic receives:

- The original task
- The evaluation criteria
- The generated output

It should not automatically inherit the generator's assumptions or intermediate discussion.

This separation often produces more independent evaluation.

### Self-Critique

The generator reviews its own output.

This is simpler and may improve basic quality, but it can reproduce the same assumptions and errors that caused the original problem.

Self-critique is useful for low-risk tasks, while independent criticism is often better for high-value or complex outputs.

---

## When to Use This Pattern

The Generator–Critic pattern is useful when:

- Output quality matters more than minimum latency
- The task has clear evaluation criteria
- Errors can be detected through review
- Drafting and evaluation require different perspectives
- The result is difficult to validate with code alone
- A first draft is unlikely to be sufficient
- Human reviewers would otherwise perform repetitive checks

Common use cases include:

- Report generation
- Research synthesis
- Code review
- Policy drafting
- Contract analysis
- Marketing content
- Strategic planning
- Data analysis narratives
- Customer support quality review

---

## When Not to Use It

Avoid this pattern when:

- The task is simple and low risk
- Deterministic validation is available
- Latency requirements are strict
- Evaluation criteria are vague
- Critique adds little measurable value
- The output can be verified directly with code or tools
- The cost of another model call exceeds the likely benefit

For example, JSON syntax should normally be checked with a parser rather than an LLM critic.

---

## Deterministic Validation First

Use deterministic checks before model-based criticism whenever possible.

```text
Generated Output
       ↓
Schema Validation
       ↓
Rule Checks
       ↓
Critic Review
       ↓
Final Decision
```

Deterministic checks are usually:

- Faster
- Cheaper
- More consistent
- Easier to test

The critic should focus on qualities that cannot be reliably validated with rules alone.

---

## Stopping Conditions

Without limits, the Generator–Critic pattern can become an infinite revision loop.

Possible stopping conditions include:

- The critic returns `Pass`
- A minimum quality score is reached
- A maximum number of revisions is reached
- No new issues are identified
- The remaining issues are non-blocking
- A time or cost budget is reached
- Human review is required

Example:

```text
Maximum revisions: 2

If the output still fails after 2 revisions:
- Return the best available draft.
- Include unresolved issues.
- Escalate when appropriate.
```

---

## Common Failure Modes

### Vague Criticism

The critic says that the output needs improvement without identifying specific problems.

**Better approach:** Require issue locations, explanations, severity levels, and corrective actions.

### Endless Revision

The critic always finds another optional improvement.

**Better approach:** Separate blocking defects from optional enhancements and enforce a revision limit.

### Critic Rewrites Everything

The critic replaces the generator instead of evaluating it.

**Better approach:** Keep evaluation and revision as separate workflow stages.

### Shared Blind Spots

The generator and critic make the same assumptions or factual errors.

**Better approach:** Provide the critic with independent evidence, tools, or a different evaluation method.

### Critic Drift

The critic evaluates personal preferences rather than the original requirements.

**Better approach:** Include the original task and a concrete rubric in every review.

### Excessive Strictness

The critic rejects acceptable outputs because it seeks perfection.

**Better approach:** Define an explicit acceptance threshold and distinguish required fixes from optional improvements.

### Unsupported Criticism

The critic claims that something is wrong without evidence.

**Better approach:** Require supporting reasoning, references, or validation results.

---

## Severity Levels

Critic feedback may be classified by severity.

| Level | Meaning | Action |
|---|---|---|
| Critical | Makes the output unsafe or unusable | Must fix |
| Major | Substantially reduces correctness or completeness | Must fix |
| Minor | Reduces clarity or polish | Fix when worthwhile |
| Suggestion | Optional enhancement | May ignore |

Severity levels help prevent minor stylistic issues from causing unnecessary revision cycles.

---

## Scoring Approach

A critic may assign scores to each criterion.

| Criterion | Score |
|---|---:|
| Correctness | 4/5 |
| Completeness | 3/5 |
| Clarity | 5/5 |
| Evidence | 2/5 |
| Format | 5/5 |

Example acceptance rule:

```text
Pass when:
- No critical issues exist.
- Correctness is at least 4/5.
- Completeness is at least 4/5.
- Overall score is at least 80%.
```

Scores should support decisions, not replace clear written feedback.

---

## Multi-Critic Variation

Some systems use several critics with different responsibilities.

```text
Generator
   ↓
Draft
   ├── Factuality Critic
   ├── Safety Critic
   ├── Style Critic
   └── Requirements Critic
          ↓
     Consolidated Feedback
          ↓
       Revision
```

This approach may improve coverage, but it also increases:

- Cost
- Latency
- Conflicting feedback
- Orchestration complexity

Use multiple critics only when distinct evaluation domains justify them.

---

## Critic–Generator with Human Review

For high-impact tasks, human review may follow automated criticism.

```text
Generator
   ↓
Automated Critic
   ↓
Revision
   ↓
Human Reviewer
   ↓
Approve or Reject
```

The critic can reduce the human review burden, but it should not automatically replace required human oversight.

---

## Tool-Assisted Criticism

Critics may use tools to verify outputs.

Examples include:

- Search tools for factual verification
- Calculators for numerical checks
- Code execution for testing
- Schema validators
- Database queries
- Citation verification
- Policy lookup

```text
Draft
  ↓
Critic
  ├── Verify facts
  ├── Test calculations
  ├── Check requirements
  └── Inspect citations
  ↓
Evidence-Based Feedback
```

Tool-assisted criticism is generally more reliable than evaluation based only on model judgment.

---

## Observability

Record enough information to understand the improvement cycle.

Useful fields include:

- Original task
- Generator version
- Critic version
- Draft
- Evaluation rubric
- Critic feedback
- Revision count
- Final verdict
- Cost
- Latency
- Human override
- Unresolved issues

This information supports debugging, evaluation, and prompt improvement.

---

## Evaluation Metrics

The pattern should be evaluated as a complete workflow.

Useful metrics include:

- First-pass acceptance rate
- Final acceptance rate
- Average revision count
- Defect reduction
- Human approval rate
- False rejection rate
- Cost per accepted output
- End-to-end latency
- Frequency of repeated feedback
- User satisfaction

A critic that always requests revisions may appear thorough while providing little practical value.

---

## No-Code Implementation

In a no-code platform, the workflow may be configured as follows:

1. Receive the task.
2. Send the task to the generator block.
3. Store the generated draft.
4. Send the original task, draft, and rubric to the critic block.
5. Parse the critic's verdict.
6. Route `Pass` outputs to completion.
7. Route `Revise` outputs back to the generator.
8. Increment the revision counter.
9. Stop when the draft passes or the revision limit is reached.
10. Log the draft, feedback, and final decision.

Example routing logic:

```text
Critic Verdict
   ├── Pass → Return Output
   ├── Revise + Attempts Remaining → Generator
   └── Revise + Limit Reached → Escalate or Return Best Draft
```

---

## Design Checklist

Before implementing this pattern, confirm that:

- The generator has a clear objective.
- The critic has an explicit rubric.
- The critic receives the original requirements.
- Feedback is structured and actionable.
- Deterministic checks run where possible.
- Blocking issues are distinguished from suggestions.
- Revision limits are defined.
- Cost and latency are measured.
- The workflow records each decision.
- Human escalation exists for high-risk cases.

---

## Trade-Offs

| Advantage | Trade-Off |
|---|---|
| Improves output quality | Adds model calls |
| Detects missing requirements | Increases latency |
| Separates creation from evaluation | Requires orchestration |
| Produces structured feedback | May cause unnecessary revisions |
| Supports iterative improvement | Needs stopping conditions |
| Reduces some human review work | Does not guarantee correctness |

---

## Related Patterns

- Reflection
- Evaluator–Optimizer
- Draft–Review–Revise
- Human-in-the-Loop
- Supervisor–Worker
- Verification
- Debate
- Ensemble Review

---

## Related Anti-Patterns

- [Blind Retries](../anti_patterns/blind_retries.md)
- [Infinite Loops](../anti_patterns/infinite_loops.md)
- [Model Overkill](../anti_patterns/model_overkill.md)
- [Overplanning](../anti_patterns/overplanning.md)
- [Prompt Bloat](../anti_patterns/prompt_bloat.md)
- [Too Many Agents](../anti_patterns/too_many_agents.md)

---

## Pattern Summary

The Generator–Critic pattern improves output by separating creation from evaluation.

The generator produces a solution, while the critic checks that solution against explicit requirements and provides actionable feedback. The generator then revises the output until it meets the acceptance criteria or reaches a defined limit.

The pattern works best when criticism is evidence-based, evaluation criteria are clear, deterministic checks are used where possible, and revision cycles have explicit stopping conditions.
