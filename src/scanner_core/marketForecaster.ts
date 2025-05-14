export function predictMarketRisk(data: any[]): string {
  const risk = data.reduce((acc, d) => acc + d.volatility, 0) / data.length;
  return risk > 50 ? "Unstable Market" : "Stable Market";
}