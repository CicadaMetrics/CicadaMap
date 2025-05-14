import { generateRiskMap } from "./core/generateMap";
import { renderMap } from "./ui/renderer";

const wallets = [
  { address: "0xABC", transactions: [1, 2, 3] },
  { address: "0xDEF", transactions: [1, 2, 3, 4, 5, 6] },
];

const riskMap = generateRiskMap(wallets);
renderMap(riskMap);