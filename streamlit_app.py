# 文件名：streamlit_app.py

import streamlit as st
import requests
from datetime import datetime, timedelta

# Solana 原生代币
SOL_MINT = "So11111111111111111111111111111111111111112"

# 替换成你的 Helius API Key
HELIUS_API_KEY = "f71ab4f1-900c-43a7-8ea2-9b4a440b008e"
HELIUS_TRANSACTIONS_API = f"https://api.helius.xyz/v0/addresses/{SOL_MINT}/transactions?api-key={HELIUS_API_KEY}"

# ---- 函数 ----

def fetch_helius_transactions(limit=500):
    url = HELIUS_TRANSACTIONS_API + f"&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("transactions", [])
    except Exception as e:
        st.error(f"API 请求失败：{e}")
        return []

def filter_swap_pairs(transactions):
    pairs_counter = {}

    for tx in transactions:
        try:
            token_transfers = tx.get("tokenTransfers", [])
            if len(token_transfers) >= 2:
                base_mint = token_transfers[0].get("mint")
                quote_mint = token_transfers[1].get("mint")
                if not base_mint or not quote_mint:
                    continue
                pair = (base_mint, quote_mint)
                pairs_counter[pair] = pairs_counter.get(pair, 0) + 1
        except Exception:
            continue

    return pairs_counter

def get_top_pairs(pairs_counter, top_n=20):
    sorted_pairs = sorted(pairs_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_pairs[:top_n]

# ---- Streamlit UI ----

st.set_page_config(page_title="Solana 活跃交易对排行榜 (Helius-only)", layout="wide")
st.title("Solana 活跃交易对排行榜")

if st.button("🔄 刷新市场数据"):
    st.info("开始刷新 Helius 交易数据...")

    transactions = fetch_helius_transactions()
    st.success(f"获取到交易记录数量: {len(transactions)}")

    st.info("在筛选活跃交易对...")
    pairs_counter = filter_swap_pairs(transactions)
    st.success(f"筛选出活跃交易对数量: {len(pairs_counter)}")

    st.info("排序 Top 20 交易对...")
    top_pairs = get_top_pairs(pairs_counter)

    table_data = []
    for pair, tx_count in top_pairs:
        base_mint, quote_mint = pair
        table_data.append({
            "base_mint": base_mint,
            "quote_mint": quote_mint,
            "tx_count": tx_count
        })

    st.table(table_data)
