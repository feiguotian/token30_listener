import streamlit as st
import requests
import pandas as pd

# 你的 Birdeye API Key
BIRDEYE_API_KEY = "c1bbf5f9be294136857f6f089c93591b"
BIRDEYE_API_URL = "https://public-api.birdeye.so/defi/markets"
SOL_MINT = "So11111111111111111111111111111111111111112"

st.set_page_config(page_title="Solana Token Listener", layout="wide")

def pretty(n):
    if n is None:
        return "-"
    if abs(n) >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if abs(n) >= 1_000:
        return f"{n/1_000:.2f}K"
    return f"{n:.2f}"

def fetch_birdeye_markets():
    headers = {"X-API-KEY": BIRDEYE_API_KEY}
    try:
        resp = requests.get(BIRDEYE_API_URL, headers=headers)
        st.info(f"Birdeye API状态码: {resp.status_code}")
        st.caption(f"API响应前200字: {resp.text[:200]}")
        resp.raise_for_status()
        try:
            data = resp.json()
            # 有些API包在data字段里
            return data.get('data', data)
        except Exception as e:
            st.error(f"无法解析API响应为JSON: {e}")
            return []
    except Exception as e:
        st.error(f"API 请求失败: {e}")
        return []

st.title("Solana 最新30个SOL配对市场（Birdeye·按24h成交额排序）")
st.caption("拉取Birdeye全市场，筛选最新30个与SOL配对市场，并按24小时成交额排序。")

col0, col1 = st.columns([1, 4])
with col0:
    run = st.button("刷新排行榜", use_container_width=True)
with col1:
    log = st.empty()

if run:
    log.info("正在拉取 Birdeye 市场数据...")
    markets = fetch_birdeye_markets()
    st.info(f"Birdeye返回市场数量: {len(markets)}")
    # 过滤出与SOL配对的市场，按返回顺序取前30
    sol_markets = []
    for m in markets:
        # birdeye字段：baseToken/quoteToken、baseTokenMint/quoteTokenMint、volume_24h_base_token、volume_24h_quote_token
        base_mint = m.get("baseTokenMint")
        quote_mint = m.get("quoteTokenMint")
        if base_mint == SOL_MINT or quote_mint == SOL_MINT:
            # volume字段，取与SOL相关的那一侧24h成交额
            if base_mint == SOL_MINT:
                volume = m.get("volume_24h_base_token", 0)
                token_symbol = m.get("quoteTokenSymbol", "-")
                token_mint = quote_mint
                pair_dir = "SOL/Token"
            else:
                volume = m.get("volume_24h_quote_token", 0)
                token_symbol = m.get("baseTokenSymbol", "-")
                token_mint = base_mint
                pair_dir = "Token/SOL"
            sol_markets.append({
                "Token": token_symbol,
                "Mint": token_mint,
                "方向": pair_dir,
                "24h成交额": volume or 0,
                "市场ID": m.get("id", "")
            })
        if len(sol_markets) >= 30:
            break
    # 按24h成交额排序
    sol_markets = sorted(sol_markets, key=lambda x: x["24h成交额"], reverse=True)
    for idx, r in enumerate(sol_markets, 1):
        r["排名"] = idx
    if len(sol_markets) == 0:
        st.warning("⚠️ 未获取到有效的SOL配对市场数据，请检查API状态。")
    else:
        st.success(f"共拉取 {len(markets)} 个市场，已筛选并显示最新30个SOL配对市场，现按24小时成交额排序。")
        st.markdown("#### 最新30个与SOL配对市场（24h成交额降序）")
        cols = st.columns(3)
        for i, r in enumerate(sol_markets):
            with cols[i%3]:
                st.markdown(f"**{r['排名']}\. {r['Token']}**")
                st.markdown(f"`{r['Mint']}`")
                st.markdown(f"方向：{r['方向']}")
                st.markdown(f"24h成交额：:green[{pretty(r['24h成交额'])}]\n")
        st.markdown("---")
        df = pd.DataFrame(sol_markets)
        st.dataframe(df, hide_index=True, use_container_width=True)
    log.success("排行榜刷新完成。")
