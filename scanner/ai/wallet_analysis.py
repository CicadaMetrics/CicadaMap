from datetime import datetime
import statistics

def parse_timestamps(transactions):
    times = []
    for tx in transactions:
        try:
            times.append(datetime.fromisoformat(tx['timestamp']))
        except:
            continue
    return sorted(times)

def calculate_intervals(timestamps):
    return [(timestamps[i+1] - timestamps[i]).total_seconds() for i in range(len(timestamps)-1)]

def transaction_frequency(transactions):
    return len(transactions)

def regularity_score(intervals):
    if len(intervals) < 2:
        return 0
    std = statistics.stdev(intervals)
    mean = statistics.mean(intervals) + 1
    return round(min(1.0, std / mean), 4)

def average_amount(transactions):
    amounts = [tx.get('amount', 0) for tx in transactions]
    return sum(amounts) / len(amounts) if amounts else 0

def behavior_trend(transactions):
    if len(transactions) < 2:
        return 0
    deltas = []
    for i in range(1, len(transactions)):
        a1 = transactions[i - 1].get('amount', 0)
        a2 = transactions[i].get('amount', 0)
        if a1 > 0:
            deltas.append((a2 - a1) / a1)
    return round(statistics.mean(deltas), 4) if deltas else 0

def wallet_risk_score(freq, regularity, avg_amt, trend):
    score = 0
    score += min(freq * 2, 25)
    score += min(regularity * 100, 20)
    score += min(avg_amt / 1000, 25)
    if trend > 0.3:
        score += 20
    elif trend < -0.5:
        score += 10
    return min(100, round(score, 2))

def analyze_wallet_behavior(wallet):
    transactions = wallet.get('transactions', [])
    timestamps = parse_timestamps(transactions)
    intervals = calculate_intervals(timestamps)
    freq = transaction_frequency(transactions)
    reg = regularity_score(intervals)
    avg_amt = average_amount(transactions)
    trend = behavior_trend(transactions)
    risk = wallet_risk_score(freq, reg, avg_amt, trend)

    return {
        "wallet": wallet.get('address'),
        "risk_score": risk,
        "factors": {
            "frequency": freq,
            "regularity": reg,
            "average_amount": avg_amt,
            "activity_trend": trend
        }
    }
