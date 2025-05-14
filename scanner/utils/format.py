def format_wallet_data(wallets):
    return [f"{w['wallet']}: {w['risk']}%" for w in wallets]