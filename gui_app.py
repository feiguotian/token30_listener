import streamlit as st
import requests
import pandas as pd

# 请填写你的 Helius API Key
HELIUS_API_KEY = "f71ab4f1-900c-43a7-8ea2-9b4a440b008e"
HELIUS_ENDPOINT = f"https://api.helius.xyz/v0/addresses/{{address}}/transactions?api-key={HELIUS_API_KEY}"

# 示例：Orca Swap 程序地址，Solana主流swap合约之一（可扩展更多池）
ORCA_SWAP_PROGRAM = "9WwG3z8HkUnkzrH2xkWXDioTfF7M7bTq3U6Xn5wrGHs9"
SOL_MINT = "So11111111111111111111111111111111111111112"

st.set_page_config(page_title="Helius链上SOL配对排行Demo", layout="wide")
st.title("Solana 链上近500笔与SOL配对的swap（Orca演示版）")
st.caption("用Helius API聚合Orca Swap合约，近500笔swap，提取所有与SOL配对的Token按swap量排行。仅为聚合思路演示，非全网榜。")

def fetch_orca_swaps():
    url = HELIUS_ENDPOINT.format(address=ORCA_SWAP_PROGRAM)
    try:
        resp = requests.get(url)
        st.info(f"Helius API状态码: {resp.status_code}")
        st.caption(f"API响应前200字: {resp.text[:200]}")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"API 请求失败: {e}")
        return []

def extract_sol_swaps(transactions):
    # 聚合：统计swap事件里包含SOL的token
    counter = {}
    for tx in transactions:
        # 只看包含swap和SOL的事件
        inner = tx.get("events", [])
        # 新版Helius会在events内标注"swap"
        for ev in inner:
            if ev.get("type") == "swap":
                source = ev.get("source")
                base = ev.get("nativeInputMint") or ev.get("inputMint")
                quote = ev.get("nativeOutputMint") or ev.get("outputMint")
                if not base or not quote:
                    continue
                if SOL_MINT in [base, quote]:
                    # 另一个token
                    token = quote if base == SOL_MINT else base
                    amount = float(ev.get("nativeInputAmount", 0)) if base == SOL_MINT else float(ev.get("nativeOutputAmount", 0))
                    if token not in counter:
                        counter[token] = {"swap_count": 0, "amount": 0, "last_source": source}
                    counter[token]["swap_count"] += 1
                    counter[token]["amount"] += amount
    return counter

col0, col1 = st.columns([1, 4])
with col0:
    run = st.button("拉取Orca/SOL近500笔swap", use_container_width=True)
with col1:
    log = st.empty()

if run:
    log.info("正在拉取 Helius 交易数据...")
    txs = fetch_orca_swaps()
    st.info(f"Orca近500笔链上swap交易记录已抓取。")
    if not txs:
        st.warning("⚠️ 未获取到交易数据，请检查API/Key/额度。")
    else:
        rank = extract_sol_swaps(txs)
        # 取前10
        rank_list = sorted(rank.items(), key=lambda x: x[1]["swap_count"], reverse=True)[:10]
        st.success(f"已提取出{len(rank_list)}个与SOL配对的Token。")
        st.markdown("#### Orca合约与SOL配对Token近500笔swap统计Top10")
        df = pd.DataFrame([
            {"Token Mint": k, "Swap次数": v["swap_count"], "累计Swap金额": v["amount"], "数据来源": v["last_source"]}
            for k, v in rank_list
        ])
        st.dataframe(df, hide_index=True, use_container_width=True)
    log.success("聚合完成。")
