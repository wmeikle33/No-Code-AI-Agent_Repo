def send_teams_message(channel, message):
    return {
        "platform": "teams",
        "action": "send_message",
        "channel": channel,
        "message": message
    }
