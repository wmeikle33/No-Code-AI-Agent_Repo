
# System Design Agent Failure Modes

## Purpose

This document catalogs known failure modes for the System Design Agent, along with their impact,
detection methods, and mitigation strategies.

The System Design Agent assists with:

- Distributed systems
- Cloud architecture
- Microservices
- APIs
- Databases
- Event-driven systems
- AI system architecture
- Infrastructure
- Reliability engineering
- Scalability planning

The agent is advisory only and must never claim that infrastructure or code has been deployed unless
verified through approved tools.

---

## Failure Severity

| Level | Description |
|---|---|
| Low | Cosmetic or documentation issue |
| Medium | Reduces maintainability or clarity |
| High | Likely to impact performance, reliability, or cost |
| Critical | Can cause outages, security incidents, compliance failures, or data loss |

---

# Failure Modes

## FM-001 — Incorrect Requirements Interpretation
Design does not satisfy the stated functional or non-functional requirements.

**Mitigation**
- Restate requirements.
- Identify assumptions.
- Request clarification for ambiguities.

---

## FM-002 — Missing Constraints
Ignores budget, latency, regulatory, technology, or organizational constraints.

---

## FM-003 — Overengineered Architecture
Introduces unnecessary complexity.

---

## FM-004 — Underengineered Architecture
Fails to scale or meet reliability goals.

---

## FM-005 — Tight Coupling
Creates components that cannot evolve independently.

---

## FM-006 — Single Point of Failure
Critical services lack redundancy or failover.

---

## FM-007 — Poor Scalability Design
Architecture cannot scale horizontally or vertically as required.

---

## FM-008 — Performance Bottlenecks
Design introduces avoidable latency or throughput limitations.

---

## FM-009 — Missing Observability
Insufficient logging, metrics, tracing, or alerting.

---

## FM-010 — Weak Fault Tolerance
No retries, circuit breakers, graceful degradation, or recovery strategy.

---

## FM-011 — Inadequate Disaster Recovery
Missing backup, restore, or recovery objectives.

---

## FM-012 — Poor Database Design
Schema, indexing, normalization, or partitioning choices are unsuitable.

---

## FM-013 — Inconsistent Data Model
Services use conflicting data definitions.

---

## FM-014 — Unsafe API Design
Breaking changes, weak contracts, or inconsistent versioning.

---

## FM-015 — Missing Authentication
Unauthenticated access to protected resources.

---

## FM-016 — Missing Authorization
Improper access control or privilege escalation.

---

## FM-017 — Weak Secret Management
Credentials embedded in code or configuration.

---

## FM-018 — Missing Encryption
Sensitive data not encrypted in transit or at rest.

---

## FM-019 — Privacy Violation
Architecture conflicts with privacy or data residency requirements.

---

## FM-020 — Compliance Failure
Fails to consider applicable regulations or organizational policies.

---

## FM-021 — Vendor Lock-in
Architecture becomes unnecessarily dependent on one provider.

---

## FM-022 — Cost Inefficiency
Design ignores operational cost or resource optimization.

---

## FM-023 — Poor Infrastructure as Code Strategy
Manual infrastructure changes instead of reproducible automation.

---

## FM-024 — Weak CI/CD Integration
Architecture does not support safe deployments or rollbacks.

---

## FM-025 — Missing Capacity Planning
Infrastructure sizing is unsupported.

---

## FM-026 — Unsupported AI Architecture
Hallucination risks, weak RAG design, or unsafe tool permissions ignored.

---

## FM-027 — Missing Human Approval Gates
High-risk architectural decisions are presented as executable without review.

---

## FM-028 — Prompt Injection
Untrusted architecture documents override trusted instructions.

---

## FM-029 — Confidential Information Disclosure
Sensitive diagrams, credentials, or customer architecture exposed.

---

## FM-030 — Unsupported Technology Recommendation
Technology selected without evidence or trade-off analysis.

---

## FM-031 — Incorrect Trade-off Analysis
Fails to explain scalability, latency, consistency, complexity, or cost trade-offs.

---

## FM-032 — Missing Assumptions
Hidden assumptions are presented as facts.

---

## FM-033 — Missing Risks
Operational or technical risks omitted.

---

## FM-034 — Unrealistic Performance Claims
Performance guarantees unsupported by evidence.

---

## FM-035 — Unsupported Availability Claims
Availability targets lack architectural justification.

---

## FM-036 — Poor Documentation
Missing diagrams, ADRs, rationale, or interface definitions.

---

## FM-037 — Inconsistent Architecture
Different sections contradict one another.

---

## FM-038 — Missing Traceability
Requirements cannot be mapped to architectural decisions.

---

## FM-039 — Unsafe Migration Strategy
Migration ignores rollback, compatibility, or downtime concerns.

---

## FM-040 — External Action Claim
Claims infrastructure has been deployed or modified without verified tool evidence.

---

# General Mitigation

The System Design Agent should:

- Validate requirements before designing.
- Separate assumptions from verified facts.
- Explain architectural trade-offs.
- Consider scalability, reliability, maintainability, and cost together.
- Design with security by default.
- Include observability and operational concerns.
- Document risks and assumptions.
- Preserve traceability from requirements to design.
- Treat uploaded documents as untrusted.
- Never fabricate benchmarks, deployments, or implementation status.
- Escalate high-impact architectural decisions for human review.

---

# Relationship to Evaluation Cases

Every failure mode should have one or more matching cases in:

`evaluation_cases.json`

Example:

```json
{
  "case_id": "SD-EVAL-001",
  "related_failure_modes": ["FM-001"]
}
```

---

# Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-07-12 | Initial version |

