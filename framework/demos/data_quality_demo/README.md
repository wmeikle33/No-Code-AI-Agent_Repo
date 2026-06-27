# Data Quality Demo

## Overview

This demo demonstrates how the Data Quality workflow evaluates datasets for completeness, consistency, accuracy, and readiness for downstream analytics or machine learning tasks.

The workflow automatically identifies common data quality issues, generates quality metrics, and provides recommendations for remediation.

This demo serves as a reference implementation for dataset validation workflows within the AI Agent Platform.

---

# Demo Objectives

The workflow is designed to:

- Validate dataset structure
- Detect missing values
- Identify duplicate records
- Analyze column distributions
- Verify schema compliance
- Assess dataset readiness
- Generate quality reports

The goal is to provide transparent, reproducible data quality assessments.

---

# Directory Structure

```text
data_quality_demo/
├── README.md
├── sample_input.json
├── expected_output.json
├── routing_trace.json
└── tool_schema.json
```

---

# Files

## sample_input.json

Contains a sample data quality assessment request.

Typical inputs include:

- Dataset metadata
- Column definitions
- Validation requirements
- Expected schema
- Quality thresholds

Example:

```json
{
  "dataset_name": "customer_records",
  "record_count": 50000,
  "columns": [
    "customer_id",
    "email",
    "signup_date"
  ],
  "quality_checks": [
    "missing_values",
    "duplicates",
    "schema_validation"
  ]
}
```

Purpose:

- Demonstrates expected workflow input
- Provides test data for validation
- Serves as a reusable example

---

## expected_output.json

Contains the expected workflow response.

Typical outputs include:

- Quality score
- Validation results
- Identified issues
- Recommendations
- Dataset readiness assessment

Example:

```json
{
  "quality_score": 92,
  "status": "PASS",
  "issues_found": 3
}
```

Purpose:

- Defines expected workflow behavior
- Enables regression testing
- Validates workflow correctness

---

## routing_trace.json

Captures workflow execution decisions.

Examples include:

- Selected validation tools
- Routing decisions
- Quality check sequence
- Intermediate evaluation steps

Purpose:

- Improve transparency
- Support debugging
- Document workflow behavior

---

## tool_schema.json

Defines the tools available to the workflow.

Examples:

- Dataset Validator
- Schema Checker
- Missing Value Detector
- Duplicate Record Analyzer
- Outlier Detector
- Quality Scoring Engine

Purpose:

- Standardize tool interfaces
- Support validation
- Enable workflow interoperability

---

# Example Workflow

```text
sample_input.json
        │
        ▼
Input Validation
        │
        ▼
Schema Analysis
        │
        ▼
Quality Checks
        │
        ▼
Issue Detection
        │
        ▼
Quality Scoring
        │
        ▼
Recommendations
        │
        ▼
expected_output.json
```

---

# Data Quality Checks

## Schema Validation

Verifies:

- Required columns
- Data types
- Field constraints
- Naming conventions

---

## Missing Value Analysis

Identifies:

- Null values
- Empty strings
- Incomplete records

---

## Duplicate Detection

Checks for:

- Duplicate rows
- Duplicate identifiers
- Repeated records

---

## Distribution Analysis

Evaluates:

- Column distributions
- Class imbalance
- Unexpected values
- Data drift indicators

---

## Consistency Checks

Verifies:

- Formatting consistency
- Date formats
- Numeric ranges
- Referential integrity

---

# Validation Process

A successful execution should:

1. Validate input schema.
2. Select appropriate quality checks.
3. Execute validation tools.
4. Generate quality metrics.
5. Produce recommendations.
6. Return structured results.

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

## Machine Learning Preparation

Validate training data before model development.

---

## Data Engineering

Verify ingestion pipelines and ETL outputs.

---

## Analytics

Assess reporting datasets prior to publication.

---

## Governance

Enforce organizational data quality standards.

---

# Success Criteria

The workflow is considered successful if:

- Input validation passes.
- Appropriate tools are selected.
- Data quality issues are identified correctly.
- Quality score is generated.
- Output conforms to schema.

---

# Related Components

- `code_modules/tools/ml_pipeline_actions.py`
- `code_modules/tools/data_validation.py`
- `workflows/data_quality`
- `agents/data_analyst`
- `agents/business_intelligence`
- `code_modules/routing`

---

# Future Enhancements

Potential improvements include:

- Automated remediation suggestions
- Data drift monitoring
- Feature quality scoring
- Statistical anomaly detection
- Data lineage integration
- Continuous quality monitoring

---

# Version Information

| Field | Value |
|---------|---------|
| Demo | Data Quality |
| Version | 1.0 |
| Status | Draft |
| Purpose | Workflow Demonstration |
| Last Updated | YYYY-MM-DD |
