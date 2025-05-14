def generate_risk_map(wallets):
    from .wallet_analysis import analyze_wallet_behavior
    return [analyze_wallet_behavior(wallet) for wallet in wallets]