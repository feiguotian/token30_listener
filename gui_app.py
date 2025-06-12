import streamlit as st
import requests
import pandas as pd

DEX_API_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"
SOL_SYMBOL = "SOL"

st.set_page_config(page_title="Solana Token Listener (DexScreener)", layout="wide")

def pretty(n):
    if n is None:
        return "-"
    try:
        n = float(n)
    except:
        return str(n)
    if abs(n) >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if abs(n) >= 1_000:
        return f"{n/1_000:.2f}K"
    return f"{n:.2f}"

def fetch_dexscreener_markets():
    try:
        resp = requests.get(DEX_API_URL)
        st.info(f"DexScreener API状态码: {resp.status_code}")
        st.caption(f"API响应前200字: {resp.text[:200]}")
        resp.raise_for_status()
        data = resp.json()
        return data.get('pairs', data)
    except Exception as e:
        st.error(f"API 请求失败: {e}")
        return []

st.title("Solana 最新30个SOL配对市场（DexScreener·按24h美元成交额排序）")
st.caption("拉取DexScreener全市场，筛选最新30个与SOL配对市场，并按24小时USD成交额排序。无需API Key，数据来自主流Solana DEX聚合。")

col0, col1 = st.columns([1, 4])
with col0:
    run = st.button("刷新排行榜", use_container_width=True)
with col1:
    log = st.empty()

if run:
    log.info("正在拉取 DexScreener 市场数据...")
    markets = fetch_dexscreener_markets()
    st.info(f"DexScreener返回市场数量: {len(markets)}")
    sol_markets = []
    for m in markets:
        base = m.get("baseToken", {})
        quote = m.get("quoteToken", {})
        base_sym = base.get("symbol", "-")
        quote_sym = quote.get("symbol", "-")
        base_addr = base.get("address", "")
        quote_addr = quote.get("address", "")
        # 必须有一侧为SOL
        if base_sym == SOL_SYMBOL or quote_sym == SOL_SYMBOL:
            if base_sym == SOL_SYMBOL:
                token_symbol = quote_sym
                token_addr = quote_addr
                pair_dir = "SOL/Token"
                vol = m.get("volume24hUsd", 0)
            else:
                token_symbol = base_sym
                token_addr = base_addr
                pair_dir = "Token/SOL"
                vol = m.get("volume24hUsd", 0)
            sol_markets.append({
                "Token": token_symbol,
                "地址": token_addr,
                "方向": pair_dir,
                "24h美元成交额": vol,
                "DEX": m.get("dexId", "")
            })
        if len(sol_markets) >= 30:
            break
    # 按24h成交额USD排序
    sol_markets = sorted(sol_markets, key=lambda x: float(x["24h美元成交额"] or 0), reverse=True)
    for idx, r in enumerate(sol_markets, 1):
        r["排名"] = idx
    if len(sol_markets) == 0:
        st.warning("⚠️ 未获取到有效的SOL配对市场数据，请检查API状态。")
    else:
        st.success(f"共拉取 {len(markets)} 个市场，已筛选并显示最新30个SOL配对市场，现按24小时USD成交额排序。")
        st.markdown("#### 最新30个与SOL配对市场（24h美元成交额降序）")
        cols = st.columns(3)
        for i, r in enumerate(sol_markets):
            with cols[i%3]:
                st.markdown(f"**{r['排名']}\. {r['Token']}**")
                st.markdown(f"`{r['地址']}`")
                st.markdown(f"方向：{r['方向']}")
                st.markdown(f"24h美元成交额：:green[{pretty(r['24h美元成交额'])}]\n")
                st.markdown(f"DEX来源: `{r['DEX']}`")
        st.markdown("---")
        df = pd.DataFrame(sol_markets)
        st.dataframe(df, hide_index=True, use_container_width=True)
    log.success("排行榜刷新完成。")
