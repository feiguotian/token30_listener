import streamlit as st
import pandas as pd
import requests

# 获取钱包交易数据
def get_wallet_transactions(wallet_address):
    url = "https://api.helius.xyz/v0/transactions"
    params = {
        "api-key": "f71ab4f1-900c-43a7-8ea2-9b4a440b008e",  # 直接填入用户的 Helius API 密钥
        "address": wallet_address,
        "limit": 100
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 抛出请求异常
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"无法获取交易数据: {e}")
        return []

# 筛选与WSOL相关的交易
def filter_wsol_transactions(transactions):
    wsol_transactions = []
    
    for tx in transactions:
        # 查找涉及WSOL的交易
        if "WSOL" in [instruction.get("token") for instruction in tx.get("instructions", [])]:
            wsol_transactions.append(tx)
    
    return wsol_transactions

# 提取交易信息（交易类型、币种、金额、余额）
def extract_transaction_details(transactions):
    details = []
    for tx in transactions:
        for instruction in tx.get("instructions", []):
            details.append({
                "交易类型": instruction.get("type", "未知"),
                "币种": "SOL",
                "金额": instruction.get("amount", "未知"),
                "余额": instruction.get("preBalances", [0])[-1]  # 获取余额变化
            })
    return details

# 展示交易表格
def display_transactions_table(wallet_address):
    transactions = get_wallet_transactions(wallet_address)
    if not transactions:
        st.write("无法获取该钱包的交易数据，请检查钱包地址。")
        return

    # 筛选与WSOL相关的交易
    wsol_transactions = filter_wsol_transactions(transactions)
    if not wsol_transactions:
        st.write("未找到与WSOL相关的交易。")
        return

    # 提取交易详细信息
    details = extract_transaction_details(wsol_transactions)

    if details:
        # 使用 pandas 将数据整理成表格
        df = pd.DataFrame(details)
        st.write(df)

        # 导出 CSV 按钮
        st.download_button(
            label="导出CSV",
            data=df.to_csv(index=False),
            file_name=f"{wallet_address}_transactions.csv",
            mime="text/csv"
        )
    else:
        st.write("未能提取交易明细。")

# 主程序界面
st.title("Solana 钱包交易历史分析")

# 用户输入钱包地址
wallet_address = st.text_input("请输入Solana钱包地址")
if wallet_address:
    display_transactions_table(wallet_address)
