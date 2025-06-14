import math
from datetime import datetime

def calculate_anomaly_score(value, baseline):
    if baseline <= 0:
        return 1.0
    deviation = abs(value - baseline) / (baseline + 1)
    return round(min(1.0, math.log1p(deviation)), 4)

def time_risk(timestamp):
    try:
        dt = datetime.fromisoformat(timestamp)
        if dt.hour < 4 or dt.hour > 22:
            return 0.6
        if 4 <= dt.hour <= 6 or 20 <= dt.hour <= 22:
            return 0.3
        return 0.0
    except:
        return 0.2

def wallet_behavior_class(tx_count, wallet_age):
    if tx_count < 3 and wallet_age < 7:
        return "Flash Wallet"
    if tx_count > 100 and wallet_age > 365:
        return "Established"
    if tx_count > 50:
        return "Accumulation"
    return "Regular"

def detect_scam(transaction):
    amount = transaction.get("amount", 0)
    avg_amount = transaction.get("avg_amount", 1)
    tx_count = transaction.get("tx_count", 1)
    avg_tx_count = transaction.get("avg_tx_count", 10)
    wallet_age = transaction.get("wallet_age_days", 1)
    avg_wallet_age = transaction.get("avg_wallet_age_days", 180)
    timestamp = transaction.get("timestamp", "")

    s_amount = calculate_anomaly_score(amount, avg_amount)
    s_tx = calculate_anomaly_score(tx_count, avg_tx_count)
    s_age = calculate_anomaly_score(wallet_age, avg_wallet_age)
    s_time = time_risk(timestamp)

    risk_raw = (0.4 * s_amount) + (0.25 * s_tx) + (0.2 * s_age) + (0.15 * s_time)
    risk_score = round(min(1.0, risk_raw), 3)

    if risk_score > 0.9:
        label = "🚨 Likely Scam"
    elif risk_score > 0.65:
        label = "⚠️ Suspicious Activity"
    elif risk_score > 0.35:
        label = "🧐 Slight Anomaly"
    else:
        label = "✅ Normal"

    return {
        "wallet_class": wallet_behavior_class(tx_count, wallet_age),
        "risk_score": risk_score,
        "label": label,
        "components": {
            "amount_score": s_amount,
            "tx_score": s_tx,
            "age_score": s_age,
            "time_risk": s_time
        }
    }
