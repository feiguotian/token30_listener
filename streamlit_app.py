import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

st.title("币安BTC/USDT 全周期K线数据批量下载")

st.info(
    "程序自动获取过去30天的5分钟、15分钟、1小时、4小时、1天K线（现货），全部可下载为CSV。\n"
    "如有币安API KEY请填写（可加速并稳定），没有也能用。"
)

api_key = st.text_input("币安API Key（可选，仅行情只读权限）", value="", type="default")
api_secret = st.text_input("币安API Secret（可选，仅行情只读权限）", value="", type="password")

interval_map = {
    "5分钟K线": "5m",
    "15分钟K线": "15m",
    "1小时K线": "1h",
    "4小时K线": "4h",
    "1天K线": "1d"
}
data_dict = {}

# 统一时间区间
now = int(time.time() * 1000)
since = now - 30 * 24 * 60 * 60 * 1000

# 优先用API Key，失败时自动切ccxt
use_binance_api = False
if api_key and api_secret:
    try:
        from binance.client import Client
        client = Client(api_key, api_secret)
        # 检查API Key有效性
        client.ping()
        use_binance_api = True
        st.success("已检测到API Key，优先使用币安官方接口（更快更稳）")
    except Exception as e:
        st.warning(f"API Key验证失败，将自动用公共接口（ccxt）。\n错误信息：{e}")

# 抓K线
for display_name, interval in interval_map.items():
    with st.spinner(f"正在下载 {display_name} ..."):
        all_ohlcv = []
        n = 0
        if use_binance_api:
            # 币安官方API每次最多1000根，循环请求
            from binance.client import Client
            tf_map = {
                "5m": Client.KLINE_INTERVAL_5MINUTE,
                "15m": Client.KLINE_INTERVAL_15MINUTE,
                "1h": Client.KLINE_INTERVAL_1HOUR,
                "4h": Client.KLINE_INTERVAL_4HOUR,
                "1d": Client.KLINE_INTERVAL_1DAY,
            }
            interval_binance = tf_map[interval]
            start_dt = datetime.utcnow() - timedelta(days=30)
            end_dt = datetime.utcnow()
            start_str = start_dt.strftime("%Y-%m-%d %H:%M:%S")
            end_str = end_dt.strftime("%Y-%m-%d %H:%M:%S")
            raw_klines = client.get_historical_klines(
                "BTCUSDT", interval_binance, start_str, end_str
            )
            df = pd.DataFrame(raw_klines, columns=[
                "OpenTime", "Open", "High", "Low", "Close", "Volume",
                "CloseTime", "QuoteAssetVolume", "NumTrades",
                "TakerBuyBaseVol", "TakerBuyQuoteVol", "Ignore"
            ])
            if len(df) > 0:
                df = df[["OpenTime", "Open", "High", "Low", "Close", "Volume"]]
                df['OpenTime'] = pd.to_datetime(df['OpenTime'], unit='ms')
                numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
                df[numeric_cols] = df[numeric_cols].astype(float)
            else:
                df = pd.DataFrame(columns=["OpenTime", "Open", "High", "Low", "Close", "Volume"])
            st.progress(1.0, text=f"{display_name} 已获取 {len(df)} 条记录")
        else:
            import ccxt
            ex = ccxt.binance()
            latest = since
            limit = 1000
            while latest < now:
                ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=latest, limit=limit)
                if not ohlcv:
                    break
                all_ohlcv += ohlcv
                latest = ohlcv[-1][0] + 1
                n += len(ohlcv)
                percent = min((latest-since)/(now-since), 1.0)
                st.progress(percent, text=f"{display_name} 已获取 {n} 条记录")
                if len(ohlcv) < limit:
                    break
            df = pd.DataFrame(all_ohlcv, columns=["OpenTime", "Open", "High", "Low", "Close", "Volume"])
            df["OpenTime"] = pd.to_datetime(df["OpenTime"], unit="ms")
            df = df.drop_duplicates(subset="OpenTime")
        data_dict[display_name] = df
        st.success(f"{display_name} 下载完成，共 {len(df)} 条K线。")

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

st.caption("全部为BTCUSDT现货近30天K线，自动适配API或公共接口，数据原始直出。")
