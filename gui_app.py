import streamlit as st
import requests
from datetime import datetime, timedelta
import json

SOL_MINT = "So11111111111111111111111111111111111111112"
HELIUS_METADATA_API = "https://api.helius.xyz/v0/token-metadata?api-key=YOUR_HELIUS_API_KEY"

def fetch_jupiter_markets():
    url = "https://quote-api.jup.ag/v1/markets"
    try:
        response = requests.get(url)
        st.write(f"API 状态码: {response.status_code}")
        st.write(f"API 响应前500字: {response.text[:500]}")
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        st.error(f"API 请求失败，错误: {e}")
        return []

def filter_markets(markets, days=7):
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
    st.write(f"过滤统计：无launchTime: {count_no_launch}，太早: {count_time_old}，非SOL配对: {count_not_sol}")
    return filtered

def get_top_markets(filtered_markets, top_n=20):
    sorted_markets = sorted(filtered_markets, key=lambda x: x.get("liquidityUSD", 0), reverse=True)
    return sorted_markets[:top_n]

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

st.title("Solana 活跃交易对排行榜")

if 'top20' not in st.session_state:
    st.session_state['top20'] = []

if st.button("刷新市场数据"):
    st.write("==============================")
    st.write(f"开始刷新 Jupiter 市场数据... {datetime.now().strftime('%H:%M:%S')}")
    markets = fetch_jupiter_markets()
    st.write(f"获取到原始市场数量: {len(markets)}")
    if len(markets) > 0:
        st.write(f"样本市场字段: {list(markets[0].keys())}")
        st.write(f"样本市场内容: {json.dumps(markets[0], ensure_ascii=False, indent=2)[:600]} ...")
    else:
        st.warning("API返回为空或不是列表。")
    st.write("正在过滤符合条件的市场...")
    filtered = filter_markets(markets, days=7)
    st.write(f"筛选出最近7天上线且与SOL配对的市场数量: {len(filtered)}")
    if len(filtered) == 0:
        st.warning("⚠️ 警告: 没有符合过滤条件的市场！请检查API结构或过滤规则是否正确。")
    st.write("正在按流动性排序...")
    top20 = get_top_markets(filtered)
    st.session_state['top20'] = top20
    st.write("Top 20 结果如下：")
    st.dataframe(top20)
    st.success(f"刷新完成，共显示 {len(top20)} 个市场。")

if st.button("显示Top 20 Token图标"):
    top20 = st.session_state.get('top20', [])
    for i, m in enumerate(top20):
        base_name = m.get("baseSymbol", "N/A")
        base_mint = m.get("baseMint")
        quote_name = m.get("quoteSymbol", "N/A")
        quote_mint = m.get("quoteMint")

        base_icon_url = get_token_icon_url(base_mint)
        quote_icon_url = get_token_icon_url(quote_mint)

        cols = st.columns(4)
        cols[0].write(f"{i+1}. {base_name}")
        if base_icon_url:
            cols[1].image(base_icon_url, width=40)
        else:
            cols[1].write("无图标")
        cols[2].write(f"{quote_name}")
        if quote_icon_url:
            cols[3].image(quote_icon_url, width=40)
        else:
            cols[3].write("无图标")
