# 文件名：streamlit_app.py

import streamlit as st
import requests

# 替换成你的 Helius API Key
HELIUS_API_KEY = "f71ab4f1-900c-43a7-8ea2-9b4a440b008e"

# ---- 函数 ----

def fetch_helius_transactions(limit=500):
    url = f"https://api.helius.xyz/v0/transactions?api-key={HELIUS_API_KEY}"
    body = {
        "limit": limit,
        "sortDirection": "DESC",
        "accountType": "token",
        "filters": [
            {
                "type": "swap"
            }
        ]
    }
    try:
        response = requests.post(url, json=body)
        response.raise_for_status()
        data = response.json()

        # Helius 返回的数据是列表，直接返回
        return data if isinstance(data, list) else []
    except Exception as e:
        st.error(f"API 请求失败：{e}")
        return []

def filter_swap_pairs(transactions):
    pairs_counter = {}

    for tx in transactions:
        try:
            swap_event = tx.get("events", {}).get("swap", {})
            source_mint = swap_event.get("sourceTokenMint")
            dest_mint = swap_event.get("destinationTokenMint")
            if source_mint and dest_mint:
                pair = (source_mint, dest_mint)
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

if st.button("\ud83d\udd04 \u5237\u65b0\u5e02\u573a\u6570\u636e"):
    st.info("\u5f00\u59cb\u5237\u65b0 Helius \u4ea4\u6613\u6570\u636e...")

    transactions = fetch_helius_transactions()
    st.success(f"\u83b7\u53d6\u5230\u4ea4\u6613\u8bb0\u5f55\u6570\u91cf: {len(transactions)}")

    st.info("\u5728\u7b5b\u9009\u6d3b\u8dc3\u4ea4\u6613\u5bf9...")
    pairs_counter = filter_swap_pairs(transactions)
    st.success(f"\u7b5b\u9009\u51fa\u6d3b\u8dc3\u4ea4\u6613\u5bf9\u6570\u91cf: {len(pairs_counter)}")

    st.info("\u6392\u5e8f Top 20 \u4ea4\u6613\u5bf9...")
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
