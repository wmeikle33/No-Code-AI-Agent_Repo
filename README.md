# No-Code-AI-Agent

No-Code-AI-Agent is an image-analysis and machine-learning pipeline for estimating root biomass from plant images.

This public repository is a redacted demonstration of the model used in the workplace

# Repository Scope

This repository is a redacted demonstration of a proprietary no code AI agent. It is intended to showcase project structure, engineering practices, testing, CI/CD, and workflows while protecting confidential intellectual property.

Included

Public-facing project architecture and package organization 

Excluded

Proprietary datasets and annotations Production-trained model weights Internal research code and experimental algorithms Customer-specific workflows and deployment infrastructure Confidential performance benchmarks derived from private data The included code is representative of the overall system design but does not contain all components used in production environments.

# No-Code-AI-Agent-Repo

```bash

├── .github/
│   └── workflows/
│       └── validation.yml          # Auto-tests prompt formatting and runs Python unit tests
├── agents/                         # 🤖 AGENT PERSONAS & INSTRUCTIONS
│   ├── customer-support/
│   │   ├── agent.json              # Model configs (e.g., GPT-4o, low temperature)
│   │   └── system_prompt.md        # Guardrails for customer interactions
│   └── financial-analyst/
│   │   ├── agent.json              # Model configs (e.g., Claude 3.5 Sonnet, high reasoning)
│   │   └── system_prompt.md        # Compliance instructions (tells agent when to use Python)
│   └── employee-support/
│       ├── agent.json
│       └── system_prompt.md    
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
│   │   ├── budget_actuals.csv   # Target spreadsheet data for analysis
│   │   └── expense_policies.md     # Company rules on what items can be reimbursed
│   └── product_catalog.csv         # Support text data for the customer bot
├── workflows/                      # 🔄 MULTI-AGENT ROUTING LOGIC
│   ├── support_to_lead.json        # Directs sales leads from support over to marketing
│   └── invoice_reconciliation.json # Step-by-step routing for financial approvals
├── .env.example                    # Template for your LLM and API keys (Never commit raw keys)
├── AGENTS.md                       # High-level map showing how your agents talk to each other
└── README.md                       # Comprehensive guide on setup and deployment instructions

```
