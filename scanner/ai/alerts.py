from datetime import datetime

blacklisted_addresses = {"", "", ""}

transaction_count = {}

def alert_if_high_risk(transaction):
    sender = transaction.get("from")
    amount = transaction.get("amount", 0)
    timestamp = transaction.get("timestamp")  
    risk_score = 0
    alerts = []

    if amount > 50000:
        risk_score += 2
        alerts.append("⚠️ Large transaction amount")

    if sender in blacklisted_addresses:
        risk_score += 3
        alerts.append("🚨 Blacklisted sender")

    if timestamp:
        try:
            tx_time = datetime.fromisoformat(timestamp)
            if 0 <= tx_time.hour <= 4:
                risk_score += 1
                alerts.append("🌙 Night-time activity")
        except Exception:
            alerts.append("⏰ Invalid timestamp format")

    if sender:
        transaction_count[sender] = transaction_count.get(sender, 0) + 1
        if transaction_count[sender] > 5:
            risk_score += 1
            alerts.append("🔁 High transaction frequency")

    if risk_score >= 3:
        return f"High-risk transaction detected: {'; '.join(alerts)}"

    return None
