import httpx
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("https://hooks.slack.com/services/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")

async def send_slack_alert(log_text: str, score: float):
    if SLACK_WEBHOOK_URL is None:
        print("❌ Slack webhook is not configured.")
        return

    message = {
        "text": f"🚨 *Threat Detected!*\n*Log:* `{log_text}`\n*Score:* {score}"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(SLACK_WEBHOOK_URL, json=message)
            response.raise_for_status()
            print("✅ Slack alert sent successfully")
    except Exception as e:
        print(f"❌ Failed to send Slack alert: {e}")


    
