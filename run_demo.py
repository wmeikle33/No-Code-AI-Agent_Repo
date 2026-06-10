import argparse
import json

from code_modules.workflows.support_to_lead import SupportToLeadWorkflow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.workflow == "support_to_lead":
        workflow = SupportToLeadWorkflow()
    else:
        raise ValueError(f"Unknown workflow: {args.workflow}")

    result = workflow.run(data)
    print(json.dumps(result, indent=2))


if __name__ =
