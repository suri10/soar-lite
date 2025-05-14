def score_log(log):
    # Basic scoring logic (can be extended later)
    score = 0
    description = "Normal activity"

    if "ssh" in log.get("event", "").lower():
        if "0.0.0.0" in log.get("source_ip", "") or log.get("source_ip", "").startswith("13."):
            score = 8
            description = "Potential unauthorized SSH access"

    elif "login failed" in log.get("event", "").lower():
        score = 5
        description = "Failed login attempt"

    return {
        "score": score,
        "description": description,
        "log": log
    }
