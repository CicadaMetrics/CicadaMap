def predict_market_risk(volatilities):
    avg_vol = sum(volatilities) / len(volatilities)
    return "Unstable Market" if avg_vol > 50 else "Stable Market"