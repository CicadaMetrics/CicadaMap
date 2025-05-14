def alert_if_high_risk(transaction):
    if transaction.get("amount", 0) > 50000:
        return "High-risk transaction detected"
    return None