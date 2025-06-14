import math
import statistics

def exponential_moving_average(data, alpha=0.3):
    ema = data[0]
    for value in data[1:]:
        ema = alpha * value + (1 - alpha) * ema
    return ema

def rolling_std(data, window=5):
    if len(data) < window:
        return 0
    return statistics.stdev(data[-window:])

def spike_index(data, threshold=1.5):
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    return sum(1 for v in data if v > mean + threshold * std)

def regime_class(vol):
    if vol < 30:
        return "low"
    if vol < 60:
        return "mid"
    return "high"

def predict_market_risk(volatilities):
    if len(volatilities) < 5:
        return "Insufficient Data"

    avg_vol = statistics.mean(volatilities)
    ema_vol = exponential_moving_average(volatilities)
    std_recent = rolling_std(volatilities)
    spike_count = spike_index(volatilities)
    trend = volatilities[-1] - volatilities[0]
    max_drawup = max(volatilities) - min(volatilities)
    latest_regime = regime_class(volatilities[-1])

    score = 0

    if ema_vol > 50:
        score += 1.5
    if std_recent > 10:
        score += 1
    if spike_count >= 3:
        score += 1.5
    if trend > 20:
        score += 1
    if max_drawup > 70:
        score += 1
    if latest_regime == "high":
        score += 1

    if score >= 5:
        return "🔥 Critical Market Risk"
    elif score >= 3:
        return "⚠️ Unstable Market"
    elif score >= 1.5:
        return "⚖️ Moderate Volatility"
    else:
        return "✅ Stable Market"
