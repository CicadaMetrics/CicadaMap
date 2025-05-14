export function generateRiskMap(wallets: any[]): any[] {
  return wallets.map(wallet => ({
    walletAddress: wallet.address,
    risk: evaluateWalletRisk(wallet.transactions)
  }));
}

function evaluateWalletRisk(transactions: number[]): number {
  return Math.min(100, transactions.length * 3);
}