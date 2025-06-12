import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd

SOL_MINT = "So11111111111111111111111111111111111111112"
API_URL = "https://quote-api.jup.ag/v1/markets"

st.set_page_config(page_title="Solana Token Listener", layout="wide")

def pretty(n):
    if n is None:
        return "-"
    if abs(n) >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if abs(n) >= 1_000:
        return f"{n/1_000:.2f}K"
    return f"{n:.2f}"

def fetch_jupiter_markets():
    try:
        resp = requests.get(API_URL)
        st.info(f"API状态码: {resp.status_code}")
        st.caption(f"API响应前200字: {resp.text[:200]}")
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception as e:
            st.error(f"无法解析API响应为JSON（可能是限流或服务器异常）: {e}")
            return []
    except Exception as e:
        st.error(f"API 请求失败: {e}")
        return []

st.title("Solana 7日成交额Top30排行榜（SOL配对）")
st.caption("拉取Jupiter所有市场，筛选7天内与SOL配对成交额最高Token。")

col0, col1 = st.columns([1, 4])
with col0:
    run = st.button("刷新排行榜", use_container_width=True)
with col1:
    log = st.empty()

if run:
    log.info("正在拉取 Jupiter 市场数据...")
    markets = fetch_jupiter_markets()
    st.info(f"Jupiter返回市场数量: {len(markets)}")
    results = []
    for m in markets:
        # Jupiter volume字段有多种，优先volume7d，其次base/quoteVolume7d，其次base/quoteVolume
        volume = None
        if m.get("volume7d"):
            volume = m["volume7d"]
        elif m.get("baseVolume7d") or m.get("quoteVolume7d"):
            if m.get("baseMint") == SOL_MINT:
                volume = m.get("baseVolume7d")
            elif m.get("quoteMint") == SOL_MINT:
                volume = m.get("quoteVolume7d")
        elif m.get("baseVolume") or m.get("quoteVolume"):
            if m.get("baseMint") == SOL_MINT:
                volume = m.get("baseVolume")
            elif m.get("quoteMint") == SOL_MINT:
                volume = m.get("quoteVolume")
        else:
            continue
        if not volume or volume == 0:
            continue
        if m.get("baseMint") == SOL_MINT:
            token_symbol = m.get("quoteSymbol") or m.get("quoteMint")[:6]
            token_mint = m.get("quoteMint")
            pair_dir = "SOL/Token"
        elif m.get("quoteMint") == SOL_MINT:
            token_symbol = m.get("baseSymbol") or m.get("baseMint")[:6]
            token_mint = m.get("baseMint")
            pair_dir = "Token/SOL"
        else:
            continue
        results.append({
            "排名": 0,
            "Token": token_symbol,
            "Mint": token_mint,
            "方向": pair_dir,
            "7日SOL成交量": volume,
            "市场ID": m.get("id", "")
        })
    results = sorted(results, key=lambda x: x["7日SOL成交量"], reverse=True)
    top_tokens = []
    token_seen = set()
    for r in results:
        uniq = f"{r['Token']}|{r['Mint']}|{r['方向']}"
        if uniq not in token_seen:
            top_tokens.append(r)
            token_seen.add(uniq)
        if len(top_tokens) >= 30:
            break
    for idx, r in enumerate(top_tokens, 1):
        r["排名"] = idx
    if len(top_tokens) == 0:
        st.warning("⚠️ 未获取到有效的Top30市场数据，请检查API状态、限流、或市场活跃度。")
    else:
        st.success(f"本次共拉取 {len(markets)} 个市场，筛选出成交额前30的Token。")
        st.markdown("#### Top 30 代币（按7日SOL成交量）")
        cols = st.columns(3)
        for i, r in enumerate(top_tokens):
            with cols[i%3]:
                st.markdown(f"**{r['排名']}\\. {r['Token']}**")
                st.markdown(f"`{r['Mint']}`")
                st.markdown(f"方向：{r['方向']}")
                st.markdown(f"7日SOL成交量：:green[{pretty(r['7日SOL成交量'])}]\n")
        st.markdown("---")
        df = pd.DataFrame(top_tokens)
        st.dataframe(df, hide_index=True, use_container_width=True)
    log.success("排行榜刷新完成。")
