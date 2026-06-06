# Gemma-4-Hackathon-Repo

```bash

├── .github/
│   └── workflows/
│       └── validation.yml          # Auto-tests prompt formatting and runs Python unit tests
├── agents/                         # 🤖 AGENT PERSONAS & INSTRUCTIONS
│   ├── customer-support/
│   │   ├── agent.json              # Model configs (e.g., GPT-4o, low temperature)
│   │   └── system_prompt.md        # Guardrails for customer interactions
│   └── financial-analyst/
│       ├── agent.json              # Model configs (e.g., Claude 3.5 Sonnet, high reasoning)
│       └── system_prompt.md        # Compliance instructions (tells agent when to use Python)
├── code_modules/                   # 🐍 MODULAR PYTHON ENGINES (Referenced by Agents)
│   ├── __init__.py
│   ├── requirements.txt            # Shared dependencies (pandas, numpy, scipy, requests)
│   ├── math_engines/               # 🧮 Heavy calculations to prevent LLM math errors
│   │   ├── investment_metrics.py   # IRR, NPV, ROI logic
│   │   └── tax_brackets.py         # Capital gains and tax deduction algorithms
│   ├── data_transformers/          # 📊 Formatting raw data into LLM-readable layouts
│   │   ├── stripe_cleaner.py       # Converts complex billing JSON into clean tables
│   │   └── csv_to_markdown.py      # Shrinks massive bank CSVs to save token costs
        └── inventory_actions.py  
│   └── custom_validators/          # 🛡️ Safety limits and risk rules
│       ├── budget_guardrails.py    # Hard-stops workflow if spend requests exceed $5,000
│       └── anomaly_detector.py     # Checks for duplicate invoices or statistical outliers
├── tools/                          # 🔌 NO-CODE API & WEBHOOK CONNECTIONS
│   ├── core_webhooks.json          # Standard communication links (Zapier, Slack, Make)
│   ├── finance_apis.json           # Secure data feeds (Plaid, Plaid, Polygon.io ticker)
│   └── python_executors.json       # Visual schema telling the agent how to call your Python modules
├── knowledge/                      # 📚 RETRIEVAL-AUGMENTED GENERATION (RAG) CONTEXT
│   ├── internal_finance/
│   │   ├── q3_budget_actuals.csv   # Target spreadsheet data for analysis
│   │   └── expense_policies.md     # Company rules on what items can be reimbursed
│   └── product_catalog.csv         # Support text data for the customer bot
├── workflows/                      # 🔄 MULTI-AGENT ROUTING LOGIC
│   ├── support_to_lead.json        # Directs sales leads from support over to marketing
│   └── invoice_reconciliation.json # Step-by-step routing for financial approvals
├── .env.example                    # Template for your LLM and API keys (Never commit raw keys)
├── AGENTS.md                       # High-level map showing how your agents talk to each other
└── README.md                       # Comprehensive guide on setup and deployment instructions

```
