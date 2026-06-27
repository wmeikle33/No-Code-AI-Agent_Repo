from code_modules.routing.router import route_request

def test_routes_support_question_to_support_agent():
    result = route_request("I need help with my account")

    assert result["selected_agent"] == "customer_support_agent"


def test_routes_sales_interest_to_lead_agent():
    result = route_request("I want pricing for an AI assistant")

    assert result["selected_agent"] == "lead_qualification_agent"


def test_unknown_request_uses_fallback_agent():
    result = route_request("Tell me a random joke about clouds")

    assert result["selected_agent"] == "fallback_agent"
