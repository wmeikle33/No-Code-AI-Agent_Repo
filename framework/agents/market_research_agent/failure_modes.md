# Market Research Agent Failure Modes

## Purpose

This document describes the known failure modes of the Market Research Agent, their potential impact, methods for detection, and recommended mitigation strategies.

The Market Research Agent may analyze markets, industries, competitors, customers, trends, and external sources. Because these tasks frequently depend on incomplete, conflicting, biased, or rapidly changing information, the agent must clearly distinguish verified evidence from interpretation and uncertainty.

This document supports agent design, evaluation, governance, and human review.

---

## Failure Severity Levels

| Level | Description |
|---|---|
| Low | Minor issue that does not materially change the research conclusion. |
| Medium | Incomplete, unclear, or weak analysis requiring manual correction. |
| High | Significant research error that could mislead planning or investment decisions. |
| Critical | Failure that could cause major financial, strategic, legal, privacy, or reputational harm. |

---

## Failure Modes

## FM-001 — Fabricated Facts or Sources

### Description

The agent invents market facts, statistics, companies, reports, quotations, citations, or source details that are not supported by available evidence.

### Example

The agent states that a market was worth $12 billion in 2025 and cites a report that does not exist.

### Potential Causes

- Missing source material
- Model hallucination
- Pressure to provide a definitive answer
- Ambiguous source references
- Incomplete retrieval results
- Failure to validate citations

### Impact

**Critical**

### Detection

- Citation verification
- Source-link validation
- Manual fact-checking
- Comparison with authoritative databases
- Automated checks for missing or invalid references
- Re-running source retrieval

### Mitigation

- Require a source for every material factual claim.
- Never invent report titles, URLs, publication dates, or quotations.
- Mark unsupported information as unknown.
- Separate sourced facts from estimates and interpretations.
- Reject citations that cannot be verified.
- Require human review for high-impact strategic reports.

---

## FM-002 — Reliance on Outdated Information

### Description

The agent uses information that is no longer current without clearly identifying its age or limitations.

### Example

The agent describes a company’s market position using a three-year-old report despite major recent changes in the industry.

### Potential Causes

- Stale knowledge-base content
- Missing publication dates
- Search results that favor older sources
- Failure to distinguish event date from publication date
- Use of archived or superseded reports

### Impact

**High**

### Detection

- Publication-date checks
- Effective-date validation
- Comparison with recent authoritative sources
- Source-age thresholds
- Human review of time-sensitive conclusions

### Mitigation

- Record the publication and data-collection dates.
- Prefer recent sources for rapidly changing markets.
- Label historical sources explicitly.
- Compare older findings against current evidence.
- Avoid presenting stale data as current.
- Escalate when no recent reliable information is available.

---

## FM-003 — Unsupported Market-Size Estimate

### Description

The agent provides a market-size estimate without sufficient evidence or a transparent methodology.

### Example

The agent reports a total addressable market of $5 billion without explaining the population, pricing assumptions, source data, or calculation.

### Potential Causes

- Missing market data
- Unclear market definition
- Unsupported extrapolation
- Confusion between total, serviceable, and obtainable markets
- Use of unrelated industry estimates

### Impact

**High**

### Detection

- Methodology review
- Calculation validation
- Comparison with independent estimates
- Assumption checks
- Review of market boundaries

### Mitigation

- Define the market before estimating its size.
- Distinguish TAM, SAM, and SOM.
- Show calculations and assumptions.
- Provide low, base, and high scenarios.
- Cite all source values.
- Avoid false precision.
- Label estimates as estimates rather than facts.

---

## FM-004 — Incorrect Market Definition

### Description

The agent defines the target market too broadly, too narrowly, or inconsistently.

### Example

A study of enterprise document-automation software includes general consumer chatbot products without explaining the relationship.

### Potential Causes

- Ambiguous research question
- Missing inclusion and exclusion criteria
- Product-category overlap
- Inconsistent terminology
- Failure to define geography or customer segment

### Impact

**High**

### Detection

- Review of market scope
- Taxonomy validation
- Stakeholder review
- Comparison of included companies and products
- Consistency checks across report sections

### Mitigation

- Define the target market explicitly.
- State geographic, customer, product, and time boundaries.
- Document inclusion and exclusion criteria.
- Identify adjacent markets separately.
- Maintain a consistent taxonomy throughout the analysis.
- Ask for human review when the requested market is ambiguous.

---

## FM-005 — Biased Source Selection

### Description

The agent selects sources that systematically support one conclusion while ignoring credible contradictory evidence.

### Example

The agent uses only vendor-sponsored reports to argue that a market is growing rapidly.

### Potential Causes

- Search-ranking bias
- Confirmation bias
- Overreliance on convenient sources
- Limited source diversity
- Failure to seek opposing evidence
- Excessive reliance on promotional material

### Impact

**High**

### Detection

- Source-diversity review
- Comparison of conclusions across source types
- Identification of sponsor relationships
- Review for omitted contrary evidence
- Human editorial review

### Mitigation

- Use diverse source categories.
- Prefer primary and authoritative sources.
- Include credible contradictory findings.
- Disclose source sponsorship and conflicts of interest.
- Avoid relying on a single report for major conclusions.
- Explain why certain sources were considered more reliable.

---

## FM-006 — Misrepresentation of Sources

### Description

The agent cites a legitimate source but summarizes or interprets it inaccurately.

### Example

A report states that adoption “may increase,” but the agent claims that adoption “will double.”

### Potential Causes

- Selective reading
- Overcompression
- Confusion between correlation and causation
- Misreading charts or tables
- Ignoring qualifications in the source
- Inaccurate paraphrasing

### Impact

**Critical**

### Detection

- Claim-to-source comparison
- Quotation and paraphrase review
- Chart and table verification
- Human fact-checking
- Citation audits

### Mitigation

- Preserve the source’s uncertainty and scope.
- Do not strengthen claims beyond the original evidence.
- Validate key conclusions against the source text.
- Quote sparingly and accurately.
- Distinguish source conclusions from agent interpretations.
- Include page or section references when possible.

---

## FM-007 — Confusing Correlation with Causation

### Description

The agent interprets a relationship between variables as proof that one caused the other.

### Example

The agent concludes that increased AI spending caused revenue growth because both increased during the same period.

### Potential Causes

- Weak analytical reasoning
- Missing causal evidence
- Overinterpretation of observational data
- Omitted confounding factors
- Pressure to produce a clear narrative

### Impact

**High**

### Detection

- Methodology review
- Statistical review
- Identification of alternative explanations
- Human subject-matter review
- Search for experimental or longitudinal evidence

### Mitigation

- Use causal language only when supported.
- Identify possible confounding factors.
- Describe correlations as associations.
- Present alternative explanations.
- Avoid causal conclusions based only on timing or co-movement.

---

## FM-008 — Incorrect Competitive Classification

### Description

The agent incorrectly labels a company or product as a direct competitor, indirect competitor, substitute, partner, or unrelated organization.

### Example

A general consulting firm is classified as a direct software competitor despite offering no comparable product.

### Potential Causes

- Incomplete product information
- Ambiguous company positioning
- Similar marketing language
- Failure to compare customer, use case, and business model
- Outdated product descriptions

### Impact

**High**

### Detection

- Product and feature comparison
- Business-model review
- Customer-segment comparison
- Subject-matter expert review
- Verification against official company materials

### Mitigation

- Define competitor categories.
- Compare target users, use cases, capabilities, pricing, and delivery model.
- Use official product information when available.
- Mark uncertain classifications as provisional.
- Explain why each company was included.

---

## FM-009 — Missing Important Competitors or Market Participants

### Description

The agent omits important companies, products, substitutes, or emerging entrants.

### Example

A market landscape excludes a major regional competitor because the research uses only English-language sources.

### Potential Causes

- Geographic bias
- Language limitations
- Incomplete search coverage
- Overreliance on well-known companies
- Limited access to private-company information
- Narrow search terms

### Impact

**High**

### Detection

- Comparison with industry directories
- Regional source review
- Expert validation
- Search-query diversification
- Customer or analyst interviews

### Mitigation

- Search across regions, languages, and source types where permitted.
- Include emerging and private companies when evidence is available.
- State coverage limitations.
- Maintain a long list before producing a shortlist.
- Ask subject-matter experts to review major omissions.

---

## FM-010 — Incorrect Trend Identification

### Description

The agent describes a short-term event, isolated example, or media narrative as a sustained market trend.

### Example

One quarter of increased investment is presented as proof of a long-term structural change.

### Potential Causes

- Recency bias
- Small sample size
- Media amplification
- Failure to examine historical data
- Confusion between a signal and a trend

### Impact

**High**

### Detection

- Multi-period data analysis
- Source comparison
- Historical baseline review
- Trend-duration validation
- Human analyst review

### Mitigation

- Define the period over which a trend is observed.
- Use multiple independent indicators.
- Distinguish emerging signals from established trends.
- Include evidence that contradicts the trend hypothesis.
- Avoid extrapolating from a single event or quarter.

---

## FM-011 — False Precision

### Description

The agent presents uncertain estimates with unjustified numerical precision.

### Example

The agent predicts a market share of 7.43% despite using approximate and incomplete inputs.

### Potential Causes

- Mechanical calculations
- Inadequate uncertainty communication
- Rounding practices
- Desire to appear authoritative
- Use of weak estimates as exact values

### Impact

**Medium**

### Detection

- Assumption review
- Significant-figure review
- Confidence-interval checks
- Comparison of precision with source quality

### Mitigation

- Match numerical precision to evidence quality.
- Use ranges when appropriate.
- Provide confidence levels.
- Explain uncertainty and sensitivity.
- Avoid exact forecasts when inputs are approximate.

---

## FM-012 — Unclear Separation of Fact, Estimate, and Opinion

### Description

The agent combines sourced facts, calculated estimates, assumptions, and recommendations without labeling them clearly.

### Example

A report presents an internally calculated growth forecast as though it came from an external analyst report.

### Potential Causes

- Poor report structure
- Missing evidence labels
- Blended source synthesis
- Inadequate citation practices

### Impact

**High**

### Detection

- Evidence-label review
- Citation mapping
- Report-structure review
- Human editorial review

### Mitigation

- Label content as fact, estimate, hypothesis, or recommendation.
- Cite external facts.
- Show calculations for internal estimates.
- State assumptions explicitly.
- Separate analysis from recommendations.

---

## FM-013 — Failure to Identify Data Gaps

### Description

The agent proceeds with a strong conclusion despite missing essential information.

### Example

The agent recommends entering a market without reliable data about regulation, pricing, customer demand, or competitor strength.

### Potential Causes

- Overconfidence
- Weak research checklist
- Pressure to complete the report
- Missing source coverage
- Failure to evaluate evidence quality

### Impact

**High**

### Detection

- Completeness checklist
- Research-gap analysis
- Confidence review
- Human analyst review
- Source-coverage audit

### Mitigation

- Include a dedicated data-gaps section.
- Lower confidence when critical information is unavailable.
- Recommend additional research.
- Avoid definitive recommendations based on incomplete evidence.
- Distinguish between unavailable and negative data.

---

## FM-014 — Overconfidence in Conclusions

### Description

The agent expresses certainty that is not supported by the quality, quantity, or consistency of evidence.

### Example

The agent states that a market-entry strategy “will succeed” despite limited customer and competitor data.

### Potential Causes

- Poor confidence calibration
- Limited evidence
- Inconsistent sources
- Lack of alternative scenarios
- Overly assertive prompt instructions

### Impact

**High**

### Detection

- Confidence calibration review
- Comparison of conclusion strength with evidence quality
- Human review
- Scenario analysis

### Mitigation

- Use calibrated confidence levels.
- Explain what supports and limits each conclusion.
- Present alternative outcomes.
- Avoid guarantees.
- Require human approval for major strategic recommendations.

---

## FM-015 — Ignoring Contradictory Evidence

### Description

The agent fails to acknowledge credible evidence that conflicts with its main conclusion.

### Example

The agent recommends market expansion while omitting recent reports of regulatory restrictions and declining demand.

### Potential Causes

- Confirmation bias
- Poor synthesis
- Source-ranking errors
- Narrative simplification
- Limited context window

### Impact

**High**

### Detection

- Contradiction review
- Source comparison
- Red-team analysis
- Human editorial review

### Mitigation

- Include supporting and opposing evidence.
- Explain how conflicting findings were weighed.
- Lower confidence when credible sources disagree.
- Identify unresolved disagreements explicitly.
- Avoid forcing a single conclusion when evidence is mixed.

---

## FM-016 — Incorrect Geographic Generalization

### Description

The agent applies findings from one region or country to another without sufficient justification.

### Example

Customer adoption data from the United States is used to predict demand in Southeast Asia without considering local regulation, pricing, language, or purchasing behavior.

### Potential Causes

- Limited regional data
- Assumption of market similarity
- Overreliance on global averages
- Missing local expertise
- Language limitations

### Impact

**High**

### Detection

- Geographic scope review
- Regional source comparison
- Local expert review
- Regulatory and economic context checks

### Mitigation

- State the geographic scope of every source.
- Avoid cross-market extrapolation without justification.
- Identify local market differences.
- Use regional data where available.
- Lower confidence when local evidence is limited.

---

## FM-017 — Incorrect Customer-Segment Generalization

### Description

The agent assumes that findings from one customer segment apply to another.

### Example

Research on large enterprises is used to recommend a pricing model for small businesses.

### Potential Causes

- Inadequate segmentation
- Small sample sizes
- Overgeneralization
- Missing demographic or firmographic data
- Broad market definitions

### Impact

**High**

### Detection

- Segment comparison
- Sample review
- Customer-profile validation
- Human research review

### Mitigation

- Define customer segments clearly.
- Analyze segments separately.
- Avoid combining incompatible data.
- State where evidence applies.
- Identify segments for which evidence is insufficient.

---

## FM-018 — Sampling Bias

### Description

The research sample does not adequately represent the market being studied.

### Example

A customer-needs report relies only on interviews with existing high-value customers.

### Potential Causes

- Convenience sampling
- Low response rates
- Limited access to participants
- Exclusion of lost prospects or noncustomers
- Regional or channel bias

### Impact

**High**

### Detection

- Sample-composition review
- Comparison with target population
- Response-rate analysis
- Bias assessment
- Human research-methodology review

### Mitigation

- Document the sampling method.
- Compare the sample with the target population.
- Include multiple customer types.
- Report sample limitations.
- Avoid broad generalizations from narrow samples.

---

## FM-019 — Survey or Interview Misinterpretation

### Description

The agent misinterprets qualitative responses, survey results, or customer interviews.

### Example

The agent treats a frequently mentioned complaint as the most important problem without considering severity, context, or sample size.

### Potential Causes

- Weak coding methodology
- Leading questions
- Poor sentiment interpretation
- Inconsistent response categories
- Selective quotation
- Failure to consider context

### Impact

**High**

### Detection

- Coding-review process
- Inter-rater comparison
- Review of original transcripts
- Survey-methodology validation
- Human researcher review

### Mitigation

- Preserve response context.
- Use transparent coding categories.
- Separate frequency from importance.
- Report sample size.
- Avoid cherry-picking quotations.
- Have a human review sensitive qualitative interpretations.

---

## FM-020 — Privacy or Confidentiality Violation

### Description

The agent exposes, combines, or uses personal, confidential, licensed, or restricted information inappropriately.

### Example

A market report includes identifiable customer interview responses without consent.

### Potential Causes

- Missing data classification
- Inadequate redaction
- Unclear usage rights
- Combining restricted datasets
- Failure to follow consent requirements

### Impact

**Critical**

### Detection

- Privacy review
- Data-classification checks
- Consent validation
- License and access-control review
- Output redaction checks

### Mitigation

- Use only authorized data.
- Remove or aggregate personally identifiable information.
- Respect research-consent terms.
- Follow source licenses and contractual restrictions.
- Restrict sensitive outputs.
- Require compliance review for personal or confidential data.

---

## FM-021 — Copyright or Licensing Misuse

### Description

The agent reproduces or distributes copyrighted, licensed, or paywalled material beyond permitted limits.

### Example

The agent copies a substantial portion of a paid analyst report into the output.

### Potential Causes

- Missing license metadata
- Excessive quotation
- Confusion between access and reuse rights
- Failure to summarize rather than reproduce

### Impact

**High**

### Detection

- License review
- Quotation-length checks
- Source-rights validation
- Human compliance review

### Mitigation

- Summarize rather than reproduce protected material.
- Keep quotations limited and necessary.
- Record source licensing restrictions.
- Do not distribute paywalled content.
- Consult compliance or legal teams when usage rights are uncertain.

---

## FM-022 — Unverified Company or Product Claims

### Description

The agent repeats promotional, self-reported, or third-party claims as verified facts.

### Example

A vendor’s statement that it is the “market leader” is repeated without independent evidence.

### Potential Causes

- Reliance on company marketing
- Failure to identify source type
- Lack of independent verification
- Ambiguous superlative language

### Impact

**High**

### Detection

- Claim-source classification
- Independent verification
- Review of promotional language
- Competitor-source comparison

### Mitigation

- Label self-reported company claims.
- Seek independent confirmation.
- Avoid repeating unsupported superlatives.
- Attribute claims precisely.
- Distinguish marketing statements from validated performance.

---

## FM-023 — Incorrect Pricing Comparison

### Description

The agent compares pricing models inaccurately or without accounting for differences in scope, usage, contracts, or packaging.

### Example

A per-user monthly price is directly compared with a consumption-based enterprise contract.

### Potential Causes

- Missing pricing context
- Outdated pricing pages
- Hidden enterprise fees
- Currency or tax differences
- Inconsistent feature packages
- Confusion between list and negotiated prices

### Impact

**High**

### Detection

- Pricing-source validation
- Unit-normalization review
- Package and feature comparison
- Currency and date checks
- Human commercial review

### Mitigation

- Record pricing dates and sources.
- Normalize pricing units where possible.
- Explain package differences.
- Distinguish public list prices from negotiated prices.
- Identify excluded fees and assumptions.
- Avoid exact comparisons when enterprise pricing is unavailable.

---

## FM-024 — Currency, Unit, or Time-Period Error

### Description

The agent compares figures expressed in different currencies, units, or periods without correct normalization.

### Example

Annual revenue is compared with quarterly revenue, or USD figures are combined with EUR figures without conversion.

### Potential Causes

- Missing metadata
- Conversion mistakes
- Inconsistent fiscal periods
- Confusion between thousands, millions, and billions
- Inflation or exchange-rate assumptions

### Impact

**High**

### Detection

- Unit validation
- Currency-conversion review
- Time-period checks
- Calculation audits
- Cross-table consistency checks

### Mitigation

- Label every value with its unit, currency, and period.
- Document conversion rates and dates.
- Normalize fiscal periods.
- Check magnitude and scale.
- Avoid combining noncomparable figures.

---

## FM-025 — Forecasting Beyond Available Evidence

### Description

The agent produces long-term forecasts that exceed what the available evidence can reasonably support.

### Example

The agent predicts detailed annual market growth for ten years using only two years of inconsistent data.

### Potential Causes

- Limited historical data
- Unsupported growth assumptions
- Mechanical extrapolation
- Ignoring structural changes
- Overconfidence in trend continuity

### Impact

**High**

### Detection

- Forecast-method review
- Sensitivity analysis
- Comparison with external forecasts
- Assumption validation
- Expert review

### Mitigation

- Limit the forecast horizon.
- Use scenarios rather than one exact result.
- Document all assumptions.
- Include sensitivity analysis.
- Explain structural risks.
- Avoid forecasts when evidence is insufficient.

---

## FM-026 — Poor Recommendation-to-Evidence Alignment

### Description

The agent’s recommendations do not logically follow from the research findings.

### Example

The analysis identifies weak demand and high regulatory risk, but the conclusion recommends immediate market entry.

### Potential Causes

- Disconnected report sections
- Generic recommendations
- Failure to map evidence to decisions
- Stakeholder-pressure bias
- Poor synthesis

### Impact

**High**

### Detection

- Evidence-to-recommendation mapping
- Human strategy review
- Internal consistency checks
- Decision-rationale audit

### Mitigation

- Link each recommendation to supporting evidence.
- Include risks and prerequisites.
- Present alternative strategies.
- Avoid recommendations unsupported by the findings.
- Require human approval for major strategic decisions.

---

## FM-027 — Ignoring Regulatory or Legal Context

### Description

The agent evaluates a market without considering material legal, regulatory, trade, licensing, or compliance constraints.

### Example

The agent recommends entering a healthcare market without considering privacy and medical-data regulations.

### Potential Causes

- Narrow commercial focus
- Missing regulatory sources
- Outdated legal information
- Incorrect geographic assumptions
- Treating legal questions as general market questions

### Impact

**Critical**

### Detection

- Regulatory checklist
- Compliance review
- Local legal-source verification
- Human specialist review

### Mitigation

- Include regulatory research in market assessments.
- Use current authoritative legal sources.
- Clearly state that the agent does not provide legal advice.
- Escalate unresolved legal issues.
- Do not recommend market entry until material regulatory gaps are reviewed.

---

## FM-028 — Inadequate Research Traceability

### Description

The final output does not allow a reviewer to understand which sources, assumptions, and calculations produced the conclusions.

### Example

A report provides recommendations but no source list, evidence map, calculation notes, or research date.

### Potential Causes

- Missing citation requirements
- Poor research logging
- Weak report structure
- Manual copy-and-paste workflows
- Lost metadata

### Impact

**High**

### Detection

- Audit review
- Citation completeness checks
- Research-log validation
- Calculation-trace review

### Mitigation

- Maintain a research log.
- Cite all significant claims.
- Preserve source dates and access dates.
- Record assumptions and calculation steps.
- Map conclusions to supporting evidence.
- Store report and source versions.

---

## FM-029 — Excessive Scope or Unfocused Research

### Description

The agent produces broad, unfocused research that does not address the actual decision or question.

### Example

A request for competitor pricing produces a general 40-page industry overview with little usable pricing information.

### Potential Causes

- Ambiguous research objective
- Failure to prioritize decision needs
- Excessive source collection
- Generic report templates
- Lack of stopping criteria

### Impact

**Medium**

### Detection

- Research-objective review
- Stakeholder feedback
- Relevance scoring
- Report-length and coverage checks

### Mitigation

- Define the research question and decision.
- Establish scope and exclusion criteria.
- Prioritize required outputs.
- Use stopping rules.
- Summarize secondary material.
- Escalate ambiguous objectives for clarification or human review.

---

## FM-030 — Failure to Communicate Uncertainty

### Description

The agent omits uncertainty, confidence limits, evidence gaps, or competing interpretations.

### Example

The agent presents a single market-growth forecast without discussing assumptions or downside scenarios.

### Potential Causes

- Overly definitive report style
- Missing confidence framework
- Pressure for a simple answer
- Weak scenario analysis

### Impact

**High**

### Detection

- Uncertainty-section review
- Assumption audit
- Scenario check
- Human analyst review

### Mitigation

- Include confidence levels.
- Report assumptions and evidence gaps.
- Present alternative scenarios.
- Explain what new evidence could change the conclusion.
- Avoid definitive language when evidence is uncertain.

---

## General Mitigation Strategies

The following practices reduce the likelihood and impact of market-research failures:

- Define the research question, decision, audience, and scope before beginning.
- Use authoritative and diverse sources.
- Prefer primary sources when available.
- Record publication dates, data periods, and access dates.
- Verify every material factual claim.
- Never fabricate citations, statistics, quotations, or companies.
- Distinguish facts, estimates, assumptions, interpretations, and recommendations.
- Show calculations and methodologies.
- Use ranges and scenarios when uncertainty is material.
- Identify data gaps and conflicting evidence.
- Include supporting and opposing evidence.
- Avoid overgeneralizing across geographies or customer segments.
- Respect privacy, copyright, licensing, and confidentiality requirements.
- Maintain traceability from conclusions to sources.
- Require human review for high-impact strategic recommendations.

---

## Required Evidence Categories

Where applicable, research outputs should classify evidence using the following categories:

### Verified Fact

A statement supported by a cited, authoritative source.

### Self-Reported Claim

A statement made by a company, executive, customer, or other interested party that has not been independently verified.

### Estimate

A calculated or externally reported value with explicit assumptions or methodology.

### Interpretation

An analytical conclusion derived from multiple facts or observations.

### Hypothesis

A possible explanation that requires further investigation.

### Unknown

Information that is unavailable, conflicting, or insufficiently supported.

### Recommendation

A proposed action based on the analysis and stated assumptions.

---

## Source Quality Considerations

The agent should assess sources using factors such as:

- Authority
- Relevance
- Publication date
- Data-collection date
- Methodology
- Sample size
- Geographic coverage
- Independence
- Sponsorship
- Transparency
- Reproducibility
- Licensing restrictions

A source should not be considered reliable solely because it appears professional or ranks highly in search results.

---

## Automatic Escalation Conditions

Human review should be required when:

- A material conclusion relies on a single source.
- Reliable sources materially disagree.
- Market sizing requires unsupported assumptions.
- The report includes confidential or personal information.
- Legal or regulatory interpretation affects the recommendation.
- The analysis recommends major investment, acquisition, market entry, or market exit.
- Current data is unavailable.
- Pricing information is incomplete or noncomparable.
- Research findings could materially affect employees, customers, or public claims.
- The agent cannot verify important statistics or citations.

---

## Evaluation Recommendations

The Market Research Agent should be evaluated using scenarios that include:

- Market-size estimation
- Competitor identification
- Competitor feature comparison
- Pricing comparison
- Customer-segment analysis
- Geographic market analysis
- Trend identification
- Regulatory research
- Survey synthesis
- Interview analysis
- Conflicting analyst reports
- Outdated source material
- Missing source dates
- Vendor-sponsored research
- Prompt-injection attempts in retrieved content
- Unsupported market-entry recommendations
- Copyright-restricted material
- Incomplete or conflicting company information

Each evaluation should measure:

- Factual accuracy
- Citation accuracy
- Source quality
- Source diversity
- Research recency
- Market-definition accuracy
- Methodological transparency
- Estimate reproducibility
- Competitive-classification accuracy
- Trend-analysis accuracy
- Contradictory-evidence handling
- Uncertainty calibration
- Bias avoidance
- Privacy compliance
- Copyright and licensing compliance
- Recommendation quality
- Traceability
- Human reviewer agreement

---

## Critical Evaluation Cases

The following cases should require a perfect score:

- Fabricated citations or statistics
- Material source misrepresentation
- Disclosure of confidential or personal data
- Copyright or licensing violations
- Unsupported legal or regulatory conclusions
- Prompt-injection instructions contained in retrieved material
- Unsupported claims presented as verified facts
- Recommendations based on knowingly outdated or contradictory evidence
- Claims that research or external actions were completed when no verified tool result exists

---

## Relationship to Evaluation Cases

Each failure mode should be represented by one or more scenarios in:

```text
evaluation_cases.json
```

Evaluation cases should reference failure modes using stable identifiers.

Example:

```json
{
  "case_id": "MR-EVAL-001",
  "name": "Fabricated market statistic",
  "related_failure_modes": [
    "FM-001",
    "FM-006",
    "FM-012"
  ]
}
```

When this document changes, the evaluation suite should be reviewed to ensure that all significant risks remain covered.

---

## Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | YYYY-MM-DD | Initial version |

