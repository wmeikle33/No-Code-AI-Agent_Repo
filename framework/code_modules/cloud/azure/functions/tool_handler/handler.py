def lambda_handler(event, context):
    """
    Example Lambda entry point for AI-agent workflows.
    """

    return {
        "statusCode": 200,
        "workflow": "lead_qualification",
        "message": "Workflow triggered successfully."
    }
