export function sendAlertIfRiskDetected(transaction: any): void {
  const level = analyzeRisk(transaction);
  if (level === "High") notifyUser("High-risk transaction detected!");
}

function analyzeRisk(tx: any): string {
  return tx.amount > 50000 ? "High" : "Low";
}

function notifyUser(msg: string): void {
  alert(msg);
}