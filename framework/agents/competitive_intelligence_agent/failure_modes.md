# Competitive Intelligence Agent — Failure Modes

## Purpose

This document identifies common ways the Competitive Intelligence Agent can fail, explains why those failures happen, and provides mitigation strategies.

The goal is to make the agent more reliable, transparent, and safe when analyzing competitors, markets, products, positioning, pricing, and strategic signals.

---

## 1. Outdated Information

### Description
The agent may rely on old competitor information, expired pricing, outdated product pages, old funding data, or previous market positioning.

### Example
The agent says a competitor does not offer an AI feature, but the competitor launched that feature last month.

### Causes
- Stale knowledge base
- Cached research
- Missing source dates
- No live web verification
- Overreliance on old reports

### Mitigation
- Require source dates for all competitor claims
- Prefer official company pages, recent press releases, and current documentation
- Flag uncertain or time-sensitive claims
- Add a freshness check before producing final recommendations

---

## 2. Unsupported Competitive Claims

### Description
The agent may make strong claims without enough evidence.

### Example
“Competitor A is clearly losing market share.”

### Causes
- Weak sourcing
- Overinterpretation of limited signals
- Confusing marketing language with actual performance
- Lack of quantitative evidence

### Mitigation
- Require citations or source references for major claims
- Separate confirmed facts from inferred analysis
- Use confidence levels: high, medium, low
- Avoid definitive language unless evidence is strong

---

## 3. Confusing Marketing Claims with Product Reality

### Description
The agent may treat competitor marketing language as proof that a feature or capability exists.

### Example
A competitor says they offer “enterprise-grade AI automation,” and the agent assumes they support advanced workflow orchestration.

### Causes
- Overtrusting homepage copy
- Lack of feature validation
- No comparison against docs, demos, or user reviews

### Mitigation
- Distinguish between advertised claims and verified capabilities
- Check product documentation when available
- Mark marketing-only claims as unverified
- Look for screenshots, changelogs, docs, or customer examples

---

## 4. Incorrect Competitor Identification

### Description
The agent may analyze the wrong company, product, or market category.

### Example
The user asks about “Claude,” and the agent confuses Anthropic Claude with another product or unrelated brand.

### Causes
- Ambiguous company names
- Similar product names
- Poor entity resolution
- Missing domain or market context

### Mitigation
- Confirm the target competitor when ambiguity exists
- Use company websites, product names, and market categories
- Store competitor aliases and known domains
- Ask for clarification when multiple matches are plausible

---

## 5. Biased Competitive Framing

### Description
The agent may favor the user’s company too strongly or frame competitors unfairly.

### Example
The agent describes the user’s product as “more innovative” without objective evidence.

### Causes
- User-provided bias
- One-sided internal documents
- Lack of balanced source review
- Overly promotional tone

### Mitigation
- Compare strengths and weaknesses objectively
- Include competitor advantages as well as disadvantages
- Use neutral business language
- Separate strategy recommendations from factual findings

---

## 6. Overconfidence in Strategic Recommendations

### Description
The agent may recommend aggressive business actions based on incomplete research.

### Example
“Lower prices immediately to beat Competitor B.”

### Causes
- Missing financial context
- No customer segmentation
- Limited market data
- Weak understanding of company constraints

### Mitigation
- Present recommendations as options, not commands
- Include assumptions and risks
- Identify what additional data is needed
- Use confidence levels for strategic suggestions

---

## 7. Missing Smaller or Emerging Competitors

### Description
The agent may focus only on obvious major competitors and ignore startups, niche tools, or regional competitors.

### Causes
- Search bias toward large companies
- Limited source diversity
- Overreliance on known market leaders
- Weak long-tail discovery

### Mitigation
- Include direct, indirect, and emerging competitors
- Search by use case, not just company name
- Review marketplaces, review sites, directories, and communities
- Add an “emerging threats” section to reports

---

## 8. Poor Source Quality

### Description
The agent may rely on low-quality blogs, outdated comparison pages, SEO content, or affiliate reviews.

### Causes
- Weak source ranking
- No source credibility checks
- Lack of distinction between primary and secondary sources

### Mitigation
- Prefer primary sources where possible
- Label source types clearly
- Treat SEO comparison articles cautiously
- Cross-check important claims across multiple sources

---

## 9. Misinterpreting Pricing

### Description
The agent may misunderstand competitor pricing tiers, hidden fees, enterprise pricing, usage-based billing, or discounts.

### Causes
- Complex pricing models
- Missing pricing pages
- Outdated pricing screenshots
- Region-specific pricing differences

### Mitigation
- Record pricing source and access date
- Separate public pricing from inferred pricing
- Flag enterprise pricing as unknown unless verified
- Avoid direct cost comparisons when pricing models differ

---

## 10. Incomplete Feature Comparison

### Description
The agent may compare features at too shallow a level.

### Example
Both products are marked as having “automation,” even though one supports only simple triggers and the other supports complex multi-step workflows.

### Causes
- Oversimplified feature matrix
- Lack of capability depth scoring
- No validation from documentation or demos

### Mitigation
- Use feature maturity levels:
  - Not available
  - Basic
  - Intermediate
  - Advanced
  - Unknown
- Add notes explaining feature depth
- Validate important features against documentation

---

## 11. Hallucinated Market Data

### Description
The agent may invent market share, revenue, customer counts, growth rates, or adoption metrics.

### Causes
- Missing reliable data
- Pressure to provide complete reports
- Weak uncertainty handling

### Mitigation
- Never invent quantitative metrics
- Use “unknown” when data is unavailable
- Label estimates clearly
- Provide source-backed numbers only

---

## 12. Legal or Ethical Boundary Issues

### Description
The agent may suggest inappropriate intelligence-gathering methods.

### Example
Scraping private systems, impersonating customers, or bypassing access controls.

### Causes
- Poorly constrained research instructions
- Overly aggressive competitive research goals
- Missing ethics policy

### Mitigation
- Use only public, lawful, and ethical sources
- Do not recommend deception, credential misuse, or private data collection
- Escalate questionable requests to human review
- Include an ethical research policy in the agent prompt

---

## 13. Confidential Information Leakage

### Description
The agent may expose internal company strategy, private customer data, or sensitive competitive plans in generated reports.

### Causes
- Mixing internal and external-facing outputs
- Missing sensitivity labels
- Poor access control
- Lack of output review

### Mitigation
- Classify outputs as internal or external
- Redact sensitive data before sharing
- Require human approval for strategic reports
- Avoid including confidential assumptions in customer-facing materials

---

## 14. Weak Differentiation Analysis

### Description
The agent may list differences without explaining why they matter strategically.

### Example
“Competitor A has integrations with Slack and HubSpot. We do not.”

### Causes
- Feature checklist thinking
- No customer impact analysis
- No prioritization framework

### Mitigation
- Tie differences to customer pain points
- Rank differences by strategic importance
- Explain impact on sales, retention, positioning, and roadmap
- Distinguish between table-stakes features and true differentiators

---

## 15. Poor Regional or Market Context

### Description
The agent may assume all competitors operate in the same geography, regulatory environment, or customer segment.

### Causes
- Missing market scope
- US-centric assumptions
- No segmentation by region, industry, or customer size

### Mitigation
- Define target market before analysis
- Segment findings by region, industry, and customer type
- Flag when data may not apply to the user’s market
- Include local competitors where relevant

---

## 16. Inaccurate SWOT Analysis

### Description
The agent may produce generic SWOT sections that do not reflect real competitive dynamics.

### Causes
- Template-driven analysis
- Weak evidence
- No connection to user’s company strategy

### Mitigation
- Ground each SWOT point in evidence
- Avoid generic statements
- Tie SWOT items to actual business implications
- Include uncertainty where evidence is limited

---

## 17. Failure to Distinguish Direct and Indirect Competitors

### Description
The agent may treat all alternatives as equally competitive.

### Example
A spreadsheet, an automation platform, and a dedicated AI agent product are grouped together without explanation.

### Causes
- Weak category definitions
- Missing customer use-case analysis
- No buyer journey context

### Mitigation
- Categorize competitors as:
  - Direct competitors
  - Indirect competitors
  - Substitute solutions
  - Emerging threats
  - Adjacent platforms
- Explain why each competitor matters

---

## 18. Overly Long or Unusable Reports

### Description
The agent may produce reports that are too long, unfocused, or difficult for stakeholders to use.

### Causes
- No output structure
- Excessive detail
- Missing executive summary
- No prioritization

### Mitigation
- Use a consistent report format
- Start with key takeaways
- Include action items
- Separate appendix-level detail from executive insights

---

## 19. Failure to Escalate Uncertainty

### Description
The agent may continue producing analysis even when the available evidence is weak.

### Causes
- No confidence threshold
- No escalation rules
- User pressure for a complete answer

### Mitigation
- Add confidence scoring
- Escalate low-confidence findings
- Clearly state missing information
- Recommend follow-up research steps

---

## 20. Recommendations Not Aligned With Business Goals

### Description
The agent may recommend actions that do not fit the company’s strategy, resources, or positioning.

### Example
Suggesting enterprise expansion when the company is focused on small businesses.

### Causes
- Missing internal strategy context
- No ICP definition
- No product roadmap awareness

### Mitigation
- Require company strategy, ICP, and positioning inputs
- Connect recommendations to business goals
- Flag recommendations that require executive review
- Avoid roadmap suggestions without internal validation

---

# Severity Levels

| Severity | Description |
|---|---|
| Low | Minor issue; does not materially affect the analysis |
| Medium | Could mislead users or reduce usefulness |
| High | Could cause poor strategic decisions |
| Critical | Could create legal, ethical, financial, or reputational risk |

---

# Escalation Rules

The agent should escalate to human review when:

- A claim could affect pricing, positioning, investment, or roadmap decisions
- Evidence is weak or contradictory
- The report includes confidential internal information
- Legal, ethical, or compliance risks are present
- A competitor claim cannot be verified
- The output will be shared externally
- The analysis involves private companies with limited public data

---

# Output Quality Checklist

Before finalizing a competitive intelligence report, verify:

- Sources are recent and credible
- Important claims are supported by evidence
- Facts are separated from assumptions
- Competitors are correctly identified
- Pricing information is dated and qualified
- Feature comparisons include depth, not just availability
- Strategic recommendations include risks
- Unknowns are clearly marked
- No confidential information is exposed
- The report is useful for a specific business decision

---

# Preferred Agent Behavior

The Competitive Intelligence Agent should:

- Be evidence-driven
- Use neutral language
- Avoid overconfidence
- Clearly label uncertainty
- Prefer recent primary sources
- Distinguish facts from interpretation
- Highlight strategic implications
- Escalate risky or low-confidence findings
- Avoid unethical research methods
- Produce decision-ready outputs
