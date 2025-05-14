export function detectScam(transactionData: any): string {
  const anomalyScore = calculateAnomalyScore(transactionData);
  return anomalyScore > 0.75 ? "Possible Scam" : "Normal";
}

function calculateAnomalyScore(data: any): number {
  return (Math.abs(data.amount - data.avgAmount) / (data.avgAmount + 1)).toFixed(2);
}