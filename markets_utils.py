# 文件名：markets_utils.py

import requests
from datetime import datetime, timedelta

# REST API 数据源
JUPITER_API_MARKETS = "https://quote-api.jup.ag/v1/markets"

# Solana 原生代币
SOL_MINT = "So11111111111111111111111111111111111111112"

def fetch_jupiter_markets():
    """
    拉取 Jupiter 市场数据
    """
    resp = requests.get(JUPITER_API_MARKETS)
    resp.raise_for_status()
    return resp.json()

def filter_markets(markets, days=7):
    """
    筛选出最近 N 天内上线，且和 SOL 配对的市场
    """
    cutoff_time = datetime.utcnow() - timedelta(days=days)
    filtered = []

    for m in markets:
        launch_time_str = m.get("launchTime")
        if not launch_time_str:
            continue

        try:
            dt = datetime.fromisoformat(launch_time_str.replace("Z", "+00:00"))
        except Exception:
            continue

        if dt < cutoff_time:
            continue

        if m.get("baseMint") == SOL_MINT or m.get("quoteMint") == SOL_MINT:
            filtered.append(m)

    return filtered

def get_top_markets(filtered_markets, top_n=20):
    """
    按流动性 USD 排序，取 Top N
    """
    sorted_markets = sorted(filtered_markets, key=lambda x: x.get("liquidityUSD", 0), reverse=True)
    return sorted_markets[:top_n]
