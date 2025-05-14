def evaluate_access(user_context):
    """
    Simple rule-based access decision engine.
    """
    risk = user_context.get("risk", "low")
    geo = user_context.get("geo", "unknown")

    if risk == "high":
        return "DENY"
    if geo in ["CN", "RU"]:
        return "DENY"
    return "ALLOW"
