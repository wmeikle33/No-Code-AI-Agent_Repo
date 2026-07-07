# Data Quality Agent — Failure Modes

## Purpose

This document identifies common failure modes for the Data Quality Agent and defines mitigation strategies to ensure reliable, explainable, and auditable data quality assessments.

The Data Quality Agent is responsible for identifying, classifying, and reporting data quality issues while recommending appropriate remediation. It should **not** make destructive changes to production data without explicit approval.

---

# 1. Missing Data Quality Issues

## Description

The agent fails to identify genuine data quality problems.

### Example

Duplicate customer records remain undetected.

### Risk

High

### Causes

- Weak validation rules
- Poor duplicate detection
- Incomplete business rules
- Limited sampling

### Mitigation

- Use multiple validation techniques
- Validate against business rules
- Compare multiple quality dimensions
- Perform comprehensive dataset scans

---

# 2. False Positive Detection

## Description

The agent incorrectly identifies valid data as erroneous.

### Example

An unusually high salary is flagged as invalid when it is legitimate.

### Risk

Medium

### Causes

- Overly strict thresholds
- Incorrect assumptions
- Missing business context

### Mitigation

- Distinguish outliers from errors
- Use configurable thresholds
- Require manual review for ambiguous cases

---

# 3. Hallucinated Data Quality Metrics

## Description

The agent invents quality scores or error statistics without analyzing the data.

### Example

"This dataset is 98% complete."

(No analysis was performed.)

### Risk

Critical

### Causes

- Hallucination
- Missing dataset access
- Pressure to provide metrics

### Mitigation

- Never estimate quality metrics
- Calculate metrics directly from the data
- Clearly state when analysis cannot be performed

---

# 4. Incorrect Schema Validation

## Description

The agent incorrectly reports schema compatibility.

### Example

States that all required columns exist when one is missing.

### Risk

High

### Causes

- Schema mismatch
- Incorrect parsing
- Weak validation logic

### Mitigation

- Compare against the official schema
- Validate column names, types, and constraints
- Report all discrepancies

---

# 5. Misinterpreting Business Rules

## Description

The agent applies incorrect or incomplete business rules.

### Example

Flags negative inventory values as invalid when they are permitted during backorders.

### Risk

High

### Causes

- Missing domain knowledge
- Ambiguous rules
- Outdated documentation

### Mitigation

- Load current business rules
- Explain applied rules
- Escalate ambiguous cases

---

# 6. Unsafe Data Modification

## Description

The agent recommends or performs destructive changes without approval.

### Example

Deleting duplicate records from production automatically.

### Risk

Critical

### Causes

- Missing approval workflow
- Poor prompt design

### Mitigation

- Never modify production data automatically
- Recommend changes only
- Require backup and approval before destructive actions

---

# 7. Poor Duplicate Detection

## Description

The agent fails to detect duplicate entities or incorrectly merges distinct records.

### Example

Two different customers with similar names are merged.

### Risk

High

### Causes

- Weak matching rules
- Missing identifiers
- Poor fuzzy matching

### Mitigation

- Use multiple identifiers
- Assign confidence scores
- Recommend manual review for uncertain matches

---

# 8. Incorrect Data Type Validation

## Description

The agent fails to detect invalid data types.

### Example

Treating dates stored as text as valid timestamps.

### Risk

Medium

### Causes

- Weak parsing
- Locale issues

### Mitigation

- Validate against schema
- Detect implicit conversions
- Report incompatible formats

---

# 9. Ignoring Referential Integrity

## Description

The agent overlooks broken relationships between datasets.

### Example

Orders reference customers that do not exist.

### Risk

High

### Causes

- Single-table analysis
- Missing relationship metadata

### Mitigation

- Validate foreign keys
- Check cross-table relationships
- Report orphaned records

---

# 10. Poor Freshness Analysis

## Description

The agent fails to recognize stale data.

### Example

A dashboard uses data from six months ago without warning.

### Risk

Medium

### Causes

- Missing timestamps
- No freshness rules

### Mitigation

- Check update timestamps
- Compare against expected refresh schedules
- Flag stale datasets

---

# 11. Incomplete Quality Reporting

## Description

The report omits important quality dimensions.

### Example

Reports completeness but ignores consistency and validity.

### Risk

Medium

### Causes

- Limited evaluation scope

### Mitigation

- Evaluate all major quality dimensions:
  - Completeness
  - Accuracy
  - Validity
  - Consistency
  - Uniqueness
  - Timeliness

---

# 12. Weak Root Cause Analysis

## Description

The agent identifies issues but cannot explain why they occurred.

### Example

Reports missing values without investigating the ingestion pipeline.

### Risk

Medium

### Causes

- Missing lineage
- No pipeline metadata

### Mitigation

- Analyze upstream sources
- Review transformation history
- Correlate pipeline failures

---

# 13. Poor Remediation Recommendations

## Description

Recommendations are generic or impractical.

### Example

"Improve data quality."

### Risk

Medium

### Causes

- Generic prompting
- Lack of prioritization

### Mitigation

- Recommend concrete actions
- Prioritize by business impact
- Assign suggested owners

---

# 14. Privacy Violations

## Description

The agent exposes personally identifiable information during analysis.

### Example

Displaying customer SSNs in a quality report.

### Risk

Critical

### Causes

- Missing masking
- Weak access controls

### Mitigation

- Mask sensitive values
- Follow least-privilege principles
- Respect data classification

---

# 15. Poor Confidence Estimation

## Description

The agent expresses excessive confidence despite incomplete analysis.

### Example

"This dataset is perfectly clean."

### Risk

Medium

### Causes

- Missing confidence scoring
- Incomplete evidence

### Mitigation

- Include confidence levels
- Explain uncertainty
- Identify analysis limitations

---

# 16. Overlooking Pipeline Failures

## Description

The agent treats downstream symptoms without identifying upstream ETL or ingestion problems.

### Example

Missing records caused by a failed nightly job are reported without mentioning the failed pipeline.

### Risk

High

### Causes

- Lack of pipeline metadata
- No operational monitoring

### Mitigation

- Review pipeline logs
- Check ingestion history
- Correlate quality issues with operational events

---

# 17. Inconsistent Cross-System Validation

## Description

The agent compares records incorrectly across multiple systems.

### Example

CRM and ERP customer IDs are mismatched due to different identifier formats.

### Risk

High

### Causes

- Missing mapping tables
- Identifier normalization issues

### Mitigation

- Normalize identifiers
- Validate mapping rules
- Document reconciliation assumptions

---

# 18. Performance Issues on Large Datasets

## Description

Quality analysis becomes impractically slow or incomplete.

### Risk

Medium

### Causes

- Full-table scans
- Poor query design
- Memory limitations

### Mitigation

- Use incremental validation
- Support sampling where appropriate
- Optimize queries
- Clearly indicate when sampling is used

---

# 19. Failure to Escalate Critical Issues

## Description

The agent identifies severe quality problems but does not recommend immediate action.

### Example

A healthcare dataset loses patient identifiers but the report is marked as low priority.

### Risk

Critical

### Causes

- Weak severity rules
- Missing escalation policies

### Mitigation

- Define severity thresholds
- Escalate critical data integrity issues
- Notify responsible teams

---

# 20. Misleading Data Quality Score

## Description

The agent produces a single quality score without explaining how it was calculated.

### Risk

Medium

### Causes

- Oversimplified scoring
- Missing methodology

### Mitigation

- Explain scoring methodology
- Break scores into quality dimensions
- Provide supporting metrics

---

# Severity Levels

| Severity | Description |
|----------|-------------|
| Low | Minor data quality issue with limited business impact |
| Medium | Reduces data reliability or usability |
| High | May affect analytics, reporting, or operational decisions |
| Critical | Could lead to incorrect business decisions, compliance violations, or production failures |

---

# Human Escalation Triggers

Escalate when:

- Critical production datasets are affected
- Data loss is detected
- Personally identifiable information is exposed
- Referential integrity failures affect business operations
- Business-critical KPIs become unreliable
- Root cause cannot be determined
- Destructive remediation is proposed
- Confidence is low

---

# Output Quality Checklist

Before completing an analysis, verify:

- All quality dimensions have been evaluated
- Metrics are calculated, not estimated
- Business rules are correctly applied
- Schema validation is complete
- Confidence levels are included
- Root causes are identified where possible
- Recommendations are actionable
- Sensitive information is protected
- No destructive actions are recommended without approval
- Report includes business impact

---

# Preferred Agent Behavior

The Data Quality Agent should:

- Be evidence-driven
- Calculate rather than estimate
- Explain every finding
- Prioritize business impact
- Protect sensitive information
- Recommend rather than modify
- Escalate critical issues
- Produce reproducible analyses
- Document assumptions
- Support continuous data quality improvement
