# 文件名：gui_app.py

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import io
import threading
from datetime import datetime, timedelta

# Solana 原生代币
SOL_MINT = "So11111111111111111111111111111111111111112"

# 替换成你的 Helius API Key
HELIUS_API_KEY = "f71ab4f1-900c-43a7-8ea2-9b4a440b008e"
HELIUS_TRANSACTIONS_API = f"https://api.helius.xyz/v0/addresses/{SOL_MINT}/transactions?api-key={HELIUS_API_KEY}"

class SolanaMarketGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Solana 活跃交易对排行榜 (Helius-only)")

        self.token_icon_cache = {}
        self.tk_images = {}

        self.create_widgets()
        self.markets = []

    def create_widgets(self):
        # 控制面板
        ctrl_frame = ttk.Frame(self.root)
        ctrl_frame.pack(fill=tk.X, padx=5, pady=5)

        self.refresh_btn = ttk.Button(ctrl_frame, text="刷新市场数据", command=self.refresh_data)
        self.refresh_btn.pack(side=tk.LEFT)

        # 日志文本框
        self.log_text = tk.Text(self.root, height=6, state=tk.DISABLED)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)

        # 表格区域
        columns = ("base_mint", "quote_mint", "tx_count")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def log(self, msg):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def refresh_data(self):
        self.refresh_btn.config(state=tk.DISABLED)
        self.tree.delete(*self.tree.get_children())  # 清空表格
        self.token_icon_cache.clear()
        self.tk_images.clear()
        self.log("开始刷新 Helius 交易数据...")

        def worker():
            try:
                self.log("正在从 Helius 获取交易数据...")
                transactions = self.fetch_helius_transactions()
                self.log(f"获取到交易记录数量: {len(transactions)}")

                self.log("正在筛选活跃交易对...")
                pairs = self.filter_swap_pairs(transactions)
                self.log(f"筛选出活跃交易对数量: {len(pairs)}")

                self.log("正在按交易次数排序...")
                top_pairs = self.get_top_pairs(pairs)

                for pair in top_pairs:
                    base_mint, quote_mint = pair[0]
                    tx_count = pair[1]

                    self.tree.insert("", tk.END, values=(base_mint, quote_mint, tx_count))

                self.log("刷新完成。")
            except Exception as e:
                self.log(f"错误：{e}")
                messagebox.showerror("错误", f"获取数据失败：{e}")
            finally:
                self.refresh_btn.config(state=tk.NORMAL)

        threading.Thread(target=worker).start()

    def fetch_helius_transactions(self, limit=500):
        url = HELIUS_TRANSACTIONS_API + f"&limit={limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("transactions", [])
        except Exception as e:
            self.log(f"API 请求失败，错误: {e}")
            return []

    def filter_swap_pairs(self, transactions):
        pairs_counter = {}

        for tx in transactions:
            try:
                token_transfers = tx.get("tokenTransfers", [])
                if len(token_transfers) >= 2:
                    base_mint = token_transfers[0].get("mint")
                    quote_mint = token_transfers[1].get("mint")
                    if not base_mint or not quote_mint:
                        continue
                    pair = (base_mint, quote_mint)
                    pairs_counter[pair] = pairs_counter.get(pair, 0) + 1
            except Exception:
                continue

        return pairs_counter

    def get_top_pairs(self, pairs_counter, top_n=20):
        sorted_pairs = sorted(pairs_counter.items(), key=lambda x: x[1], reverse=True)
        return sorted_pairs[:top_n]


# 保留原来的 get_token_icon 函数 (如果你还需要显示 Token 图标，可以保留)
def get_token_icon(self, mint):
    if mint in self.token_icon_cache:
        return self.token_icon_cache[mint]

    try:
        url = f"https://api.helius.xyz/v0/token-metadata?api-key={HELIUS_API_KEY}&mint={mint}"
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
        if not image_url:
            return None
        img_resp = requests.get(image_url)
        img_resp.raise_for_status()
        img_data = img_resp.content
        from PIL import Image
        image = Image.open(io.BytesIO(img_data)).convert("RGBA")
        image = image.resize((64, 64), Image.ANTIALIAS)
        tk_img = ImageTk.PhotoImage(image)
        self.token_icon_cache[mint] = tk_img
        return tk_img
    except Exception:
        return None
