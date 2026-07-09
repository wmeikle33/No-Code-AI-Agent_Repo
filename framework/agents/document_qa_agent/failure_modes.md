# Document Q&A Agent — Failure Modes

## Purpose

This document identifies common failure modes for the Document Q&A Agent and defines mitigation strategies to ensure accurate, evidence-based, and trustworthy responses.

The Document Q&A Agent answers questions using one or more provided documents. It should ground every response in retrieved content and clearly distinguish between documented facts, reasonable inferences, and unknown information.

The agent should **never fabricate document contents**.

---

# 1. Hallucinated Information

## Description

The agent provides information that does not exist in any supplied document.

### Example

The user asks:

> "What is the company's vacation policy?"

The document contains no vacation policy, but the agent invents one.

### Risk

Critical

### Causes

- Weak retrieval
- LLM hallucination
- Pressure to answer every question

### Mitigation

- Only answer using retrieved evidence
- Respond with "The document does not contain this information."
- Clearly distinguish unknown information

---

# 2. Incorrect Document Retrieval

## Description

The retrieval system selects irrelevant sections.

### Example

The user asks about payroll, but the retrieval returns cybersecurity documentation.

### Risk

High

### Causes

- Poor embeddings
- Weak chunking
- Similar terminology

### Mitigation

- Improve retrieval ranking
- Retrieve multiple candidate chunks
- Use reranking models
- Validate retrieval confidence

---

# 3. Missing Relevant Information

## Description

The correct answer exists but is not retrieved.

### Example

The answer is in Appendix B but only Chapter 1 was searched.

### Risk

High

### Causes

- Small retrieval window
- Poor chunking
- Missing indexing

### Mitigation

- Search multiple chunks
- Increase recall
- Improve document indexing

---

# 4. Incorrect Citation

## Description

The agent cites the wrong page, section, or paragraph.

### Example

References Section 4.2 when the answer is actually in Section 7.1.

### Risk

High

### Causes

- Citation mapping errors
- Incorrect chunk metadata

### Mitigation

- Preserve source metadata
- Verify citations before responding
- Include page and section references when available

---

# 5. Misinterpreting Document Content

## Description

The agent misunderstands what the document actually says.

### Example

Interpreting "recommended" as "required."

### Risk

High

### Causes

- Ambiguous wording
- Poor reasoning
- Missing context

### Mitigation

- Quote supporting passages
- Explain reasoning
- Indicate uncertainty when interpretation is ambiguous

---

# 6. Outdated Document Usage

## Description

The agent answers using obsolete versions of documents.

### Example

Using the 2022 employee handbook instead of the 2025 edition.

### Risk

High

### Causes

- Missing version control
- Poor indexing

### Mitigation

- Prefer latest approved documents
- Display document version
- Warn when multiple versions exist

---

# 7. Mixing Multiple Documents Incorrectly

## Description

The agent combines information from unrelated documents.

### Example

Combining HR policy with engineering procedures.

### Risk

Medium

### Causes

- Weak document boundaries
- Similar terminology

### Mitigation

- Keep document sources separate
- Identify source document for every claim
- Explain conflicts

---

# 8. Ignoring Conflicting Information

## Description

The agent fails to identify contradictory documents.

### Example

One policy allows remote work while another prohibits it.

### Risk

High

### Causes

- Multiple document versions
- No conflict detection

### Mitigation

- Highlight conflicts
- Recommend human review
- Cite both sources

---

# 9. Answering Beyond the Documents

## Description

The agent supplements answers using general knowledge without clearly indicating it.

### Example

Adding legal advice not contained in the document.

### Risk

High

### Causes

- Default LLM behavior
- Weak prompt constraints

### Mitigation

- Separate document evidence from external knowledge
- Label external information explicitly
- Allow grounding-only mode

---

# 10. Poor Context Handling

## Description

The agent loses context across multiple questions.

### Example

Follow-up questions are answered using unrelated sections.

### Risk

Medium

### Causes

- Context window limitations
- Conversation state errors

### Mitigation

- Maintain conversation history
- Re-run retrieval for follow-up questions
- Track referenced documents

---

# 11. Weak Summarization

## Description

Summaries omit key information or distort the original meaning.

### Risk

Medium

### Causes

- Aggressive compression
- Long documents

### Mitigation

- Preserve key findings
- Highlight omitted sections
- Validate summaries against source text

---

# 12. Incorrect Table Interpretation

## Description

The agent misunderstands tabular data.

### Example

Misreading rows or columns.

### Risk

Medium

### Causes

- Poor OCR
- Table parsing issues

### Mitigation

- Preserve table structure
- Validate extracted values
- Reference row and column labels

---

# 13. OCR Errors

## Description

Scanned documents are interpreted incorrectly.

### Example

"$10,000" becomes "$100,000."

### Risk

High

### Causes

- Poor scan quality
- OCR limitations

### Mitigation

- Detect OCR confidence
- Flag uncertain text
- Recommend manual verification

---

# 14. Confidential Information Exposure

## Description

The agent reveals information beyond the user's permissions.

### Example

Displaying confidential contract clauses.

### Risk

Critical

### Causes

- Missing access controls
- Weak authorization

### Mitigation

- Enforce document permissions
- Respect access levels
- Redact restricted sections

---

# 15. Ignoring Document Scope

## Description

The user asks about Document A but the agent answers using Document B.

### Risk

Medium

### Causes

- Retrieval ambiguity

### Mitigation

- Confirm document scope
- Restrict retrieval to selected documents

---

# 16. Unsupported Inference

## Description

The agent draws conclusions not supported by the documents.

### Example

"This policy exists because management wanted..."

### Risk

Medium

### Causes

- Speculation
- Overinterpretation

### Mitigation

- Distinguish facts from inference
- Label assumptions
- Avoid unsupported conclusions

---

# 17. Poor Multi-Document Comparison

## Description

The agent compares documents incorrectly.

### Example

Missing differences between two contract versions.

### Risk

Medium

### Causes

- Weak comparison logic

### Mitigation

- Compare section-by-section
- Highlight additions, removals, and modifications

---

# 18. Large Document Context Loss

## Description

Information from earlier sections is forgotten.

### Risk

Medium

### Causes

- Context window limitations

### Mitigation

- Chunk intelligently
- Retrieve multiple relevant sections
- Maintain document hierarchy

---

# 19. Failure to Admit Unknowns

## Description

The agent answers confidently despite insufficient evidence.

### Example

"I believe..." when the document is silent.

### Risk

High

### Causes

- Overconfidence

### Mitigation

- Clearly state when information is unavailable
- Encourage further document review
- Report retrieval confidence

---

# 20. Low Retrieval Confidence Ignored

## Description

The agent answers despite poor retrieval quality.

### Risk

Medium

### Causes

- No confidence threshold

### Mitigation

- Calculate retrieval confidence
- Warn users when confidence is low
- Recommend manual verification

---

# Severity Levels

| Severity | Description |
|----------|-------------|
| Low | Minor quality issue |
| Medium | May reduce answer quality |
| High | Could mislead users |
| Critical | Could expose confidential information or fabricate document content |

---

# Human Review Triggers

Human review is recommended when:

- Multiple documents conflict
- Legal or contractual interpretation is required
- OCR confidence is low
- Confidential information is involved
- Retrieval confidence is low
- Documents appear incomplete
- Regulatory or compliance questions arise

---

# Output Quality Checklist

Before returning an answer, verify:

- Answer is supported by retrieved evidence
- Citations are accurate
- No unsupported claims are included
- Conflicting information is identified
- Document version is correct
- Sensitive information is protected
- Confidence level is included
- Unknown information is acknowledged
- Sources are clearly identified
- Response remains within document scope

---

# Preferred Agent Behavior

The Document Q&A Agent should:

- Be evidence-driven
- Prioritize retrieval over memory
- Never fabricate document content
- Cite supporting passages
- Explain uncertainty
- Respect document permissions
- Distinguish facts from inferences
- Admit when information is unavailable
- Escalate ambiguous interpretations
- Produce transparent, traceable answers
