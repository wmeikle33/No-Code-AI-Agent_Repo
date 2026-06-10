from code_modules.routing.lead_router import LeadRouter
from code_modules.scoring.lead_scorer import LeadScorer
from code_modules.output.recommendation import (
    generate_recommendation
)


class SupportToLeadWorkflow:

    def __init__(self):
        self.router = LeadRouter()
        self.scorer = LeadScorer()

    def run(self, ticket: dict) -> dict:

        route = self.router.route(
            ticket["message"]
        )

        score = self.scorer.score(ticket)

        return {
            "workflow": "support_to_lead",
            "route": route,
            "lead_score": score,
            "recommendation":
                generate_recommendation(score)
        }
