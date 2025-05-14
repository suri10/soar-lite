import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ✅ Correctly get the SLACK_WEBHOOK_URL from .env
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def score_log(log_text: str) -> float:
    if "unauthorized" in log_text.lower():
        return 0.9
    return 0.2

def send_alert_to_slack(log_text: str, score: float):
    if not SLACK_WEBHOOK_URL:
        print("❌ Slack webhook not set.")
        return

    payload = {
        "text": f"""🚨 *Threat Detected!*\n*Log:* `{log_text}`\n*Score:* {score}"""
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("✅ Slack alert sent")
    except Exception as e:
        print(f"❌ Failed to send Slack alert: {e}")
