import requests
from typing import Any, Dict
from Loaders.image_loader import fetch_image_from_url
from Loaders.quote_loader import fetch_quote

teams_webhook_url = "https://quantorillc.webhook.office.com/webhookb2/986a3528-9d9c-43aa-a313-28f621c59260@124ccfbd-07ea-44e3-8794-af8986d63809/IncomingWebhook/c314d4a9c25a47db931489749aa7d788/dfc6f754-1356-49de-9d68-a09d53f86f85"

def send_to_teams(webhook_url: str, quote: str = None, author: str = None, image_url: str = None) -> None:
    headers = {"Content-Type": "application/json",}
    if quote and author and image_url:
        message_data = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "contentUrl": None,
                    "content": {
                        "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.2",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "a crumb of inspiration by nini bendianishvili, have a good day<3",
                            },
                            {
                                "type": "TextBlock",
                                "text": quote,
                            },
                            {
                                "type": "Image",
                                "url": image_url,
                            },
                        ],
                    },
                },
            ],
        }

        try:
            response = requests.post(webhook_url, headers=headers, json=message_data)
            response.raise_for_status()
            print("Message sent successfully to Microsoft Teams!")
        except requests.RequestException as e:
            print(f"Failed to send message to Microsoft Teams: {str(e)}")
    else:
        print("Incomplete data. Quote, author, and image URL are required for sending.")

def main():
    image_url = "https://picsum.photos/200/300" 
    image_data = fetch_image_from_url(image_url)
    if image_data:
        quote = fetch_quote()
        if quote:
            send_to_teams(teams_webhook_url, quote=quote, author="Anonymous", image_url=image_url)

if __name__ == "__main__":
    main()
