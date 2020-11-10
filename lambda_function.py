import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import os
   
url = os.environ.get('webhook')
   
def lambda_handler(event, context):
    x = json.dumps(event, sort_keys=True, indent=4)
    payload_list = x.split(",")
    eventType = str(payload_list[3])
    y=5
    if "AssessmentCompletionEvent" in eventType:
        payload = "Dome9 Assessment Completion Event: \n"
        payload += "\n"
        while y != 18:
            payload += payload_list[y]
            payload += "\n"
            y+=1
    elif "ApiKeyCreatedEvent" in eventType:
        payload = "Dome9 Api Key Created Event: \n"
        payload += "\n"
        while y != 10:
            payload += payload_list[y]
            payload += "\n"
            y+=1
    elif "ApiKeyDeletedEvent" in eventType:
        payload = "Dome9 Api Key Deleted Event: \n"
        payload += "\n"
        while y != 10:
            payload += payload_list[y]
            payload += "\n"
            y+=1            
    elif "NewUserCreatedEvent" in eventType:
        payload = "Dome9 New User Created Event: \n"
        payload += "\n"
        while y != 11:
            payload += payload_list[y]
            payload += "\n"
            y+=1   
    elif "UserDeletedEvent" in eventType:
        payload = "Dome9 User Deleted Event: \n"
        payload += "\n"
        while y != 11:
            payload += payload_list[y]
            payload += "\n"
            y+=1         
    else:
        payload = "Dome9 Event: \n"
        payload += "\n"
        while y != 18:
            payload += payload_list[y]
            payload += "\n"
            y+=1
    payload += "\n"
    webhook = DiscordWebhook(url=url, content=payload)
    response = webhook.execute()