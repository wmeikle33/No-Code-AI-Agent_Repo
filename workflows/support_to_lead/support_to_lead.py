from code_modules.tools.lead_capture import create_lead

class SupportToLeadWorkflow:
    def run(self, data: dict) -> dict:
        customer_message = data.get("message", "")

        lead = create_lead({
            "name": data.get("name", "Unknown"),
            "email": data.get("email"),
            "message": customer_message,
            "source": "support_to_lead_workflow",
        })

        return {
            "status": "success",
            "workflow": "support_to_lead",
            "lead": lead,
