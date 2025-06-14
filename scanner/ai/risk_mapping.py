from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from .wallet_analysis import analyze_wallet_behavior

def generate_risk_map(wallets):
    def safe_analyze(wallet):
        try:
            return analyze_wallet_behavior(wallet)
        except:
            return {"wallet": wallet, "risk": None}

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(safe_analyze, wallets))

    results = [r for r in results if r["risk"] is not None]
    results.sort(key=lambda x: x["risk"], reverse=True)

    buckets = defaultdict(list)
    for r in results:
        risk = r["risk"]
        if risk >= 90:
            buckets["Critical"].append(r)
        elif risk >= 70:
            buckets["High"].append(r)
        elif risk >= 40:
            buckets["Moderate"].append(r)
        else:
            buckets["Low"].append(r)

    return {
        "summary": {
            "total": len(results),
            "critical": len(buckets["Critical"]),
            "high": len(buckets["High"]),
            "moderate": len(buckets["Moderate"]),
            "low": len(buckets["Low"])
        },
        "map": buckets
    }
