__version__ = "1.3"
__author__ = "Cicadamap"
__description__ = "AI-powered blockchain risk and wallet behavior analysis suite"

from .alerts import alert_if_high_risk
from .market_predictor import predict_market_risk
from .risk_mapping import generate_risk_map
from .scam_detection import detect_scam, calculate_anomaly_score
from .wallet_analysis import analyze_wallet_behavior, wallet_risk_score, transaction_frequency

__all__ = [
    "alert_if_high_risk",
    "predict_market_risk",
    "generate_risk_map",
    "detect_scam",
    "calculate_anomaly_score",
    "analyze_wallet_behavior",
    "wallet_risk_score",
    "transaction_frequency"
]
