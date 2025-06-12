import streamlit as st
import requests
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
            st.error(f"无法解析API响应为JSON: {e}")
            return []
    except Exception as e:
        st.error(f"API 请求失败: {e}")
        return []

st.title("Solana 最新30个SOL配对市场（按交易额排序）")
st.caption("拉取Jupiter所有市场，筛选最新30个与SOL配对市场，并按成交额排序。")

col0, col1 = st.columns([1, 4])
with col0:
    run = st.button("刷新排行榜", use_container_width=True)
with col1:
    log = st.empty()

if run:
    log.info("正在拉取 Jupiter 市场数据...")
    markets = fetch_jupiter_markets()
    st.info(f"Jupiter返回市场数量: {len(markets)}")
    # 过滤出与SOL配对的市场，按API顺序取最新30个
    sol_markets = []
    for m in markets:
        if m.get("baseMint") == SOL_MINT or m.get("quoteMint") == SOL_MINT:
            # Jupiter volume字段多种，优先volume7d，其次base/quoteVolume7d，其次base/quoteVolume，其次volume
            volume = m.get("volume7d")
            if not volume:
                if m.get("baseMint") == SOL_MINT:
                    volume = m.get("baseVolume7d") or m.get("baseVolume") or m.get("volume")
                elif m.get("quoteMint") == SOL_MINT:
                    volume = m.get("quoteVolume7d") or m.get("quoteVolume") or m.get("volume")
            # 方向判断
            if m.get("baseMint") == SOL_MINT:
                token_symbol = m.get("quoteSymbol") or m.get("quoteMint")[:6]
                token_mint = m.get("quoteMint")
                pair_dir = "SOL/Token"
            else:
                token_symbol = m.get("baseSymbol") or m.get("baseMint")[:6]
                token_mint = m.get("baseMint")
                pair_dir = "Token/SOL"
            sol_markets.append({
                "Token": token_symbol,
                "Mint": token_mint,
                "方向": pair_dir,
                "成交额": volume or 0,
                "市场ID": m.get("id", "")
            })
        if len(sol_markets) >= 30:
            break
    # 按成交额排序
    sol_markets = sorted(sol_markets, key=lambda x: x["成交额"], reverse=True)
    for idx, r in enumerate(sol_markets, 1):
        r["排名"] = idx
    if len(sol_markets) == 0:
        st.warning("⚠️ 未获取到有效的SOL配对市场数据，请检查API状态。")
    else:
        st.success(f"共拉取 {len(markets)} 个市场，已筛选并显示最新30个SOL配对市场，现按成交额排序。")
        st.markdown("#### 最新30个与SOL配对市场（成交额降序）")
        cols = st.columns(3)
        for i, r in enumerate(sol_markets):
            with cols[i%3]:
                st.markdown(f"**{r['排名']}\. {r['Token']}**")
                st.markdown(f"`{r['Mint']}`")
                st.markdown(f"方向：{r['方向']}")
                st.markdown(f"成交额：:green[{pretty(r['成交额'])}]\n")
        st.markdown("---")
        df = pd.DataFrame(sol_markets)
        st.dataframe(df, hide_index=True, use_container_width=True)
    log.success("排行榜刷新完成。")
