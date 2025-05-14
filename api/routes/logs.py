from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from engine.analyzer import score_log, send_alert_to_slack

router = APIRouter()

class LogRequest(BaseModel):
    log: str

@router.post("/analyze")
async def analyze_log(req: LogRequest):
    score = score_log(req.log)
    action = "⚠️ Alert" if score > 0.5 else "✅ Safe"

    if score > 0.5:
        alert_msg = f"[ALERT] 🚨 Log flagged with score {score}: {req.log}"
        send_alert_to_slack(alert_msg, score)


    return {
        "log": req.log,
        "score": score,
        "action": action
    }

