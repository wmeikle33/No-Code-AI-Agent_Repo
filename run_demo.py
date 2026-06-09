import json
import sys
from pathlib import Path

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def qualify_lead(input_data):
    message = input_data.get("message", "").lower()

    score = 0
    reasons = []

    if any(word in message for word in ["pricing", "demo", "quote", "sales"]):
        score += 40
        reasons.append("Commercial intent detected")

    if any(word in message for word in ["enterprise", "team", "company", "business"]):
        score += 30
        reasons.append("Business context detected")

    if any(word in message for word in ["urgent", "this week", "soon"]):
        score += 20
        reasons.append("Time sensitivity detected")

    route = "sales" if score >= 50 else "support"

    return {
        "route": route,
        "lead_score": score,
        "reasons": reasons,
        "recommended_next_step": (
            "Send to sales for follow-up"
            if route == "sales"
            else "Handle through support workflow"
        )
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_demo.py demos/lead_qualification_demo/sample_input.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    input_data = load_json(input_path)

    result = qualify_lead(input_data)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
