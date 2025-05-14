export function analyzeWalletBehavior(transactions: number[]): string {
  const frequency = calculateFrequency(transactions);
  const riskScore = evaluateRisk(frequency);
  return riskScore > 50 ? "High Risk Wallet" : "Low Risk Wallet";
}

function calculateFrequency(txs: number[]): number {
  return txs.length;
}

function evaluateRisk(frequency: number): number {
  return Math.min(100, frequency * 5);
}