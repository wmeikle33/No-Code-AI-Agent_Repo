import pytest

from code_modules.workflows.support_to_lead import SupportToLeadWorkflow


def test_workflow_handles_failed_lead_creation(monkeypatch):
    def broken_create_lead(*args, **kwargs):
        raise RuntimeError("CRM unavailable")

    monkeypatch.setattr(
        "code_modules.workflows.support_to_lead.create_lead",
        broken_create_lead,
    )

    workflow = SupportToLeadWorkflow()

    result = workflow.run({
        "name": "Jane Doe",
        "email": "jane@example.com",
        "message": "I am interested in support automation",
    })

    assert result["status"] == "error"
    assert "CRM unavailable" in result["error"]
