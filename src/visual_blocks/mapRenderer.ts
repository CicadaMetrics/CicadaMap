export function renderMap(riskMap: any[]): void {
  const container = document.getElementById("mapContainer");
  if (!container) return;
  container.innerHTML = riskMap.map(w =>
    `<div>${w.walletAddress}: ${w.risk} Risk</div>`
  ).join('');
}