# 文件名：streamlit_app.py

import streamlit as st
import requests

# Replace with your Helius API Key
HELIUS_API_KEY = "f71ab4f1-900c-43a7-8ea2-9b4a440b008e"

# ---- Functions ----

def fetch_helius_transactions(limit=500):
    url = f"https://api.helius.xyz/v0/transactions?api-key={HELIUS_API_KEY}"
    body = {
        "limit": limit,
        "sortDirection": "DESC",
        "accountType": "token"
        # No filters
    }
    try:
        response = requests.post(url, json=body)
        response.raise_for_status()
        data = response.json()

        # Helius returns a list
        return data if isinstance(data, list) else []
    except Exception as e:
        st.error(f"API request failed: {e}")
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

st.set_page_config(page_title="Solana Active Token Pairs Ranking (Helius-only)", layout="wide")
st.title("Solana Active Token Pairs Ranking")

if st.button("Refresh Market Data"):
    st.info("Start refreshing Helius transaction data...")

    transactions = fetch_helius_transactions()
    st.success(f"Fetched transaction count: {len(transactions)}")

    st.info("Filtering active token pairs...")
    pairs_counter = filter_swap_pairs(transactions)
    st.success(f"Filtered active token pairs count: {len(pairs_counter)}")

    st.info("Sorting Top 20 token pairs...")
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








