import streamlit as st
import pandas as pd
from binance.client import Client
import datetime

st.title("币安BTC/USDT历史K线数据下载工具")

# 选择K线周期
interval_map = {
    "5分钟": Client.KLINE_INTERVAL_5MINUTE,
    "15分钟": Client.KLINE_INTERVAL_15MINUTE,
    "1小时": Client.KLINE_INTERVAL_1HOUR,
    "4小时": Client.KLINE_INTERVAL_4HOUR,
    "1天": Client.KLINE_INTERVAL_1DAY
}
interval = st.selectbox("选择K线周期", list(interval_map.keys()), index=0)

# 配置API（只查行情数据不用填API KEY）
api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

symbol = "BTCUSDT"
interval_binance = interval_map[interval]

# 默认拉取最近30天
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(days=30)

with st.spinner("正在获取数据..."):
    klines = client.get_historical_klines(
        symbol,
        interval_binance,
        start_str=start_time.strftime("%Y-%m-%d %H:%M:%S"),
        end_str=end_time.strftime("%Y-%m-%d %H:%M:%S")
    )
    df = pd.DataFrame(klines, columns=[
        "OpenTime", "Open", "High", "Low", "Close", "Volume",
        "CloseTime", "QuoteAssetVolume", "NumTrades",
        "TakerBuyBaseVol", "TakerBuyQuoteVol", "Ignore"
    ])
    if len(df) > 0:
        df['OpenTime'] = pd.to_datetime(df['OpenTime'], unit='ms')
        df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='ms')
        numeric_cols = ["Open", "High", "Low", "Close", "Volume", "QuoteAssetVolume", "TakerBuyBaseVol", "TakerBuyQuoteVol"]
        df[numeric_cols] = df[numeric_cols].astype(float)

if len(df) > 0:
    st.success(f"获取成功，共 {len(df)} 条K线数据！")
    st.dataframe(df[["OpenTime", "Open", "High", "Low", "Close", "Volume"]])
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="下载CSV文件",
        data=csv,
        file_name=f"{symbol}_{interval}_last30days.csv",
        mime="text/csv"
    )
else:
    st.warning("未获取到任何数据，请检查网络或稍后重试。")
