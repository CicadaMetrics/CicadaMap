def calculate_anomaly_score(amount, avg_amount):
    score = abs(amount - avg_amount) / (avg_amount + 1)
    return round(score, 2)

def detect_scam(transaction):
    score = calculate_anomaly_score(transaction['amount'], transaction['avg_amount'])
    return "Possible Scam" if score > 0.75 else "Normal"