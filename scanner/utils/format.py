def format_wallet_data(wallets, top_n=None):
    def risk_bar(score):
        filled = int(score / 10)
        empty = 10 - filled
        return "[" + "█" * filled + "░" * empty + f"] {score}%"

    def label(score):
        if score >= 90: return "🟥 Critical"
        if score >= 70: return "🟧 High"
        if score >= 40: return "🟨 Moderate"
        return "🟩 Low"

    sorted_wallets = sorted(wallets, key=lambda w: w.get("risk", 0), reverse=True)
    if top_n:
        sorted_wallets = sorted_wallets[:top_n]

    blocks = []
    for w in sorted_wallets:
        addr = w.get("wallet", "unknown")
        score = w.get("risk", 0)
        block = f"""Wallet: {addr}
Risk Score: {label(score)} {risk_bar(score)}
------------------------"""
        blocks.append(block)

    return "\n".join(blocks)
