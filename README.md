# No-Code-AI-Agent

No-Code-AI-Agent is a LLM based agent that allows users to write and execute code automatically according to user requests.

This public repository is a redacted demonstration of the model used in the workplace.

## Repository Scope

This repository is a redacted demonstration of a proprietary no code AI agent. It is intended to showcase project structure, engineering practices, testing, CI/CD, and workflows while protecting confidential intellectual property.

### Included

- Public-facing project architecture
- Agent personas and instructions
- Example workflow routing logic
- Example tool schemas
- Sample retrieval/context files
- CI validation and basic testing structure

### Excluded

- Proprietary datasets and annotations
- Production-trained model weights
- Internal research code
- Customer-specific workflows
- Deployment infrastructure
- Confidential performance benchmarks


The included code is representative of the overall system design but does not contain all components used in production environments.

## Example Use Cases

- Route customer-support requests to sales or finance workflows
- Reconcile invoices against expense policies
- Use retrieval context to answer employee or product-support questions

## Repo Structure

```text
├── .github/workflows/        # CI validation
├── agents/                   # Agent personas and instructions
├── code_modules/             # Python modules used by agents
├── knowledge/                # Retrieval/context files
├── tools/                    # Tool and API schemas
├── workflows/                # Multi-agent routing logic
├── .env.example              # Environment variable template
├── AGENTS.md                 # Agent interaction guide
└── README.md
````
