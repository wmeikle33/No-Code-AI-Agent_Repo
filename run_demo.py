import argparse
import json

from workflows.support_to_lead import SupportToLeadWorkflow
from workflows.research import ResearchWorkflow
from workflows.customer_support import CustomerSupportWorkflow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.workflow == "support_to_lead":
        workflow = SupportToLeadWorkflow()
    elif args.workflow == 'customer_support":
        workflow = CustomerSupportWorkflow()
    elif args.workflow == 'market_research':
        workflow = MarketResearchWorkflow()
    else:
        raise ValueError(f"Unknown workflow: {args.workflow}")

    result = workflow.run(data)
    print(json.dumps(result, indent=2))


if __name__ = '__main__':
    main()
