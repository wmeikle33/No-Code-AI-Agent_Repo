# Intent Classification

This module identifies the user's intent before agent selection.

Flow:

1. Receive user request
2. Normalize text
3. Match against intent rules
4. Return intent, confidence, matched terms, and alternatives
5. Pass result to agent selection

Example:

```json
{
  "intent": "lead_qualification",
  "confidence": 0.88,
  "matched_terms": ["pricing", "enterprise plan"]
}
