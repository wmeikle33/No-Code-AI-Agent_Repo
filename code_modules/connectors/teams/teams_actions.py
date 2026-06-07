import pymsteams

# Initialize the connector with your Teams Webhook URL
teams_msg = pymsteams.connectorcard("<YOUR_MICROSOFT_WEBHOOK_URL>")

# Add message payload
teams_msg.text("Hello Team! This automated alert was sent from a Python script.")

# Execute the POST request
teams_msg.send()
