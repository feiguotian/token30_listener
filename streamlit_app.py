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

        # Helius 返回的数据是一个列表，而不是 dict，直接返回 list
        return data if isinstance(data, list) else []
    except Exception as e:
        st.error(f"API 请求失败：{e}")
        return []

def filter_swap_pairs(transactions):
    pairs_counter = {}

    for tx in transactions:
        try:
            inner_instructions = tx.get("innerInstructions", [])

            token_transfers = []
            for inner in inner_instructions:
                instructions = inner.get("instructions", [])
                for inst in instructions:
                    parsed = inst.get("parsed", {})
                    if parsed.get("type") == "transfer":
                        info = parsed.get("info", {})
                        mint = info.get("mint")
                        if mint:
                            token_transfers.append(mint)

            if len(token_transfers) >= 2:
                base_mint = token_transfers[0]
                quote_mint = token_transfers[1]
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
