def transaction_frequency(transactions):
    return len(transactions)

def wallet_risk_score(frequency):
    return min(100, frequency * 5)

def analyze_wallet_behavior(wallet):
    freq = transaction_frequency(wallet['transactions'])
    risk = wallet_risk_score(freq)
    return {"wallet": wallet['address'], "risk": risk}