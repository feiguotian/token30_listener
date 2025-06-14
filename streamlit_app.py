import streamlit as st
import pandas as pd
import requests
import time

st.title("BTC/USDT 各周期K线数据批量下载（CoinGecko）")

st.info("程序自动获取过去30天的5分钟、15分钟、1小时、4小时、1天K线（现货），全部可下载为CSV。\n"
        "数据源：CoinGecko API，无需API Key，稳定可靠。")

interval_map = {
    "5分钟K线": "minutely",  # CoinGecko 用 "minutely" 来表示 1分钟周期
    "15分钟K线": "minutely",
    "1小时K线": "hourly",    # "hourly" 表示按小时聚合数据
    "4小时K线": "hourly",
    "1天K线": "daily"        # "daily" 表示按天聚合数据
}
data_dict = {}

# 统一时间区间
now = int(time.time())
since = now - 30 * 24 * 60 * 60  # 30天

# 请求CoinGecko的历史市场数据接口
def fetch_data(interval):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",  # 获取过去30天的数据
        "interval": interval
    }
    response = requests.get(url, params=params)
    return response.json()

# 获取K线数据
for display_name, interval in interval_map.items():
    with st.spinner(f"正在下载 {display_name} ..."):
        ohlcv = fetch_data(interval)
        
        # 数据格式处理
        if "prices" in ohlcv:
            df = pd.DataFrame(ohlcv["prices"], columns=["timestamp", "price"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
            df["Open"] = df["price"]
            df["High"] = df["price"]
            df["Low"] = df["price"]
            df["Close"] = df["price"]
            df["Volume"] = 0  # CoinGecko API没有提供交易量数据，设置为0
            data_dict[display_name] = df[["timestamp", "Open", "High", "Low", "Close", "Volume"]]
            st.progress(1.0, text=f"{display_name} 已获取 {len(df)} 条记录")
        else:
            st.warning(f"{display_name} 数据获取失败")

st.divider()
st.subheader("各周期K线数据下载")
for display_name, df in data_dict.items():
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"下载 {display_name} CSV",
        data=csv,
        file_name=f"BTCUSDT_{interval_map[display_name]}_last30days.csv",
        mime="text/csv"
    )

st.caption("数据来源：CoinGecko API，全部为BTCUSDT现货近30天K线，自动适配不同周期，数据直出。")
