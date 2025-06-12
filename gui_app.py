import streamlit as st
import requests
from datetime import datetime, timedelta
import json

SOL_MINT = "So11111111111111111111111111111111111111112"
HELIUS_METADATA_API = "https://api.helius.xyz/v0/token-metadata?api-key=YOUR_HELIUS_API_KEY"

st.set_page_config(page_title="Solana Token Listener", layout="wide")

def fetch_jupiter_markets(progress):
    url = "https://quote-api.jup.ag/v1/markets"
    progress.progress(0.1, "开始请求 Jupiter API...")
    try:
        response = requests.get(url)
        progress.progress(0.3, "收到响应，正在解析数据...")
        data = response.json()
        progress.progress(0.4, f"API 状态码: {response.status_code}")
        progress.progress(0.5, f"API 响应预览: {response.text[:200]}")
        return data
    except Exception as e:
        progress.progress(1.0, f"API 请求失败: {e}")
        st.error(f"API 请求失败，错误: {e}")
        return []

def filter_markets(markets, days=7, progress=None):
    cutoff_time = datetime.utcnow() - timedelta(days=days)
    filtered = []
    count_no_launch = 0
    count_time_old = 0
    count_not_sol = 0

    for m in markets:
        launch_time_str = m.get("launchTime")
        if not launch_time_str:
            count_no_launch += 1
            continue
        try:
            dt = datetime.fromisoformat(launch_time_str.replace("Z", "+00:00"))
        except Exception:
            count_no_launch += 1
            continue
        if dt < cutoff_time:
            count_time_old += 1
            continue
        if m.get("baseMint") == SOL_MINT or m.get("quoteMint") == SOL_MINT:
            filtered.append(m)
        else:
            count_not_sol += 1
    if progress:
        progress.progress(0.7, f"过滤完成：无launchTime: {count_no_launch}，太早: {count_time_old}，非SOL配对: {count_not_sol}")
    return filtered

def get_top_markets(filtered_markets, top_n=20, progress=None):
    sorted_markets = sorted(filtered_markets, key=lambda x: x.get("liquidityUSD", 0), reverse=True)
    if progress:
        progress.progress(0.85, "流动性排序完成。")
    return sorted_markets[:top_n]

@st.cache_data(ttl=60*5)
def get_token_icon_url(mint):
    try:
        url = f"{HELIUS_METADATA_API}&mint={mint}"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            return None
        meta = data[0]
        offchain = meta.get("offChainMetadata")
        if not offchain:
            offchain_uri = meta.get("offChainUri")
            if not offchain_uri:
                return None
            r = requests.get(offchain_uri)
            r.raise_for_status()
            offchain = r.json()
        image_url = offchain.get("image")
        return image_url
    except Exception:
        return None

st.markdown(
    "<h1 style='text-align: left; color: #3c3c3c; margin-bottom: 12px;'>Solana 活跃交易对排行榜</h1>",
    unsafe_allow_html=True,
)

st.markdown("点击下方按钮，刷新Solana链最新活跃Token市场。")
progress = st.empty()
cols = st.columns([1, 3])

with cols[0]:
    if st.button("刷新市场数据", use_container_width=True):
        st.session_state['refresh'] = True

# 用于进度区
with cols[0]:
    if st.session_state.get('refresh'):
        progress_bar = st.progress(0.0, "初始化...")
        markets = fetch_jupiter_markets(progress_bar)
        progress_bar.progress(0.2, f"原始市场数量: {len(markets)}")
        if len(markets) > 0:
            st.write(f"字段示例: {list(markets[0].keys())}")
        else:
            st.warning("API返回为空或不是列表。")
        filtered = filter_markets(markets, days=7, progress=progress_bar)
        progress_bar.progress(0.8, f"符合条件市场数量: {len(filtered)}")
        top20 = get_top_markets(filtered, progress=progress_bar)
        progress_bar.progress(1.0, f"完成，Top 20共{len(top20)}条。")
        st.session_state['top20'] = top20
        st.session_state['refresh'] = False

with cols[1]:
    top20 = st.session_state.get('top20', [])
    if top20:
        st.markdown("#### Top 20 交易对（按流动性USD）")
        # 生成固定表格风格
        import pandas as pd
        show_data = []
        base_icons = []
        quote_icons = []
        for m in top20:
            base = m.get("baseSymbol", "N/A")
            quote = m.get("quoteSymbol", "N/A")
            base_icon_url = get_token_icon_url(m.get("baseMint"))
            quote_icon_url = get_token_icon_url(m.get("quoteMint"))
            base_icons.append(base_icon_url)
            quote_icons.append(quote_icon_url)
            show_data.append({
                "Base": base,
                "Quote": quote,
                "Base Mint": m.get("baseMint"),
                "Quote Mint": m.get("quoteMint"),
                "Launch": m.get("launchTime", "")[:10],
                "LiquidityUSD": round(m.get("liquidityUSD", 0), 2)
            })
        df = pd.DataFrame(show_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("##### Token 图标一览")
        for i, m in enumerate(top20):
            row = st.columns([1, 1, 1, 1])
            row[0].write(f"{i+1}. {m.get('baseSymbol', 'N/A')}")
            if base_icons[i]:
                row[1].image(base_icons[i], width=36)
            else:
                row[1].write("无图标")
            row[2].write(f"{m.get('quoteSymbol', 'N/A')}")
            if quote_icons[i]:
                row[3].image(quote_icons[i], width=36)
            else:
                row[3].write("无图标")
