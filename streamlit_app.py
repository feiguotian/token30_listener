import streamlit as st
import pandas as pd
import ccxt
import time
from datetime import datetime

st.title("币安BTC/USDT历史K线数据下载")

# 选择K线周期
interval_map = {
    "5分钟": "5m",
    "15分钟": "15m",
    "1小时": "1h",
    "4小时": "4h",
    "1天": "1d"
}
interval = st.selectbox("选择K线周期", list(interval_map.keys()), index=0)
interval_ccxt = interval_map[interval]

# 查询时间范围（近30天）
now = int(time.time() * 1000)
since = now - 30 * 24 * 60 * 60 * 1000  # 30天前

# 查询数据
st.info("数据量大，初次加载需1-2分钟，请耐心等待…")
with st.spinner("正在获取数据..."):
    ex = ccxt.binance()
    all_ohlcv = []
    limit = 1000  # 每次最大1000根
    latest = since
    while latest < now:
        ohlcv = ex.fetch_ohlcv('BTC/USDT', interval_ccxt, since=latest, limit=limit)
        if not ohlcv:
            break
        all_ohlcv += ohlcv
        latest = ohlcv[-1][0] + 1  # 避免重复
        if len(ohlcv) < limit:
            break

    df = pd.DataFrame(all_ohlcv, columns=["OpenTime", "Open", "High", "Low", "Close", "Volume"])
    df["OpenTime"] = pd.to_datetime(df["OpenTime"], unit="ms")
    # 可选：去重
    df = df.drop_duplicates(subset="OpenTime")

if len(df) > 0:
    st.success(f"获取成功，共 {len(df)} 条K线数据！")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="下载CSV文件",
        data=csv,
        file_name=f"BTCUSDT_{interval}_last30days.csv",
        mime="text/csv"
    )
else:
    st.warning("未获取到任何数据。")

st.caption("技术支持：ChatGPT/ccxt/Streamlit")
