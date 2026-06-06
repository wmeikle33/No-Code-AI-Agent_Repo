# Gemma-4-Hackathon-Repo

```bash

├── .github/
│   └── workflows/              # GitHub Action scripts to auto-test your agent profiles
│       └── validation.yml
├── agents/                     # Configuration definitions for distinct agents
│   ├── customer-support/
│   │   ├── agent.json          # Agent metadata, selected model, & baseline parameters
│   │   └── system_prompt.md    # Persona, behavioral guardrails, and explicit rules
│   └── lead-generator/
│   │    ├── agent.json
│   │    └── system_prompt.md
│   └── financial-analysis/
│          ├── agent.json
│          └── system_prompt.md
├── tools/                      # No-code tool schemas and webhook maps
│   ├── webhooks.json           # Definitions for REST APIs and third-party webhook links
│   └── schemas/
│       ├── google_sheets.json  # Input/output validation arrays for external data sync
│       └── slack_notify.json
├── knowledge/                  # RAG (Retrieval-Augmented Generation) static context files
│   ├── company_policy.md
│   └── product_catalog.csv
├── workflows/                  # Sequential routing and multi-agent interaction logic
│   └── support_to_lead.json
├── AGENTS.md                   # Direct map of available agents and how they collaborate
├── config.env.example          # Sample environment credentials file for your API tokens
└── README.md                   # Core technical manual explaining how to initialize the system

```
