
from code_modules.tools.catalog import search_catalog
from code_modules.tools.lead_capture import create_lead

def test_customer_support_to_lead_flow():
    results = search_catalog("support")

    assert len(results) >= 1
    assert results[0]["name"] == "AI Support Agent"

    lead = create_lead(
        name="Jane Doe",
        email="jane@example.com",
        interest=results[0]["name"]
    )

    assert lead["status"] == "created"
    assert lead["lead"]["source"] == "customer_support_agent"
    assert lead["lead"]["interest"] == "AI Support Agent"
