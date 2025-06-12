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
HELIUS_METADATA_API = "https://api.helius.xyz/v0/token-metadata?api-key=YOUR_HELIUS_API_KEY"

class SolanaMarketGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Solana 活跃交易对排行榜")

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
        self.log_text = tk.Text(self.root, height=10, state=tk.DISABLED)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)

        # 表格区域
        columns = ("base", "quote", "base_mint", "quote_mint", "launch_time", "liquidityUSD")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 绑定双击显示 token 图标
        self.tree.bind("<Double-1>", self.on_double_click)

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
        self.log("==============================")
        self.log(f"开始刷新 Jupiter 市场数据... {datetime.now().strftime('%H:%M:%S')}")

        def worker():
            try:
                self.log("正在从 Jupiter 拉取市场数据...")
                markets = self.fetch_jupiter_markets()
                self.log(f"获取到原始市场数量: {len(markets)}")

                if len(markets) > 0:
                    self.log(f"样本市场字段: {list(markets[0].keys())}")
                    # 只打印第1条样本全部内容
                    import json
                    self.log(f"样本市场内容: {json.dumps(markets[0], ensure_ascii=False, indent=2)[:600]} ...")
                else:
                    self.log("API返回为空或不是列表。")

                self.log("正在过滤符合条件的市场...\n")
                filtered = self.filter_markets(markets, days=7)
                self.log(f"筛选出最近7天上线且与SOL配对的市场数量: {len(filtered)}")

                if len(filtered) == 0:
                    self.log("⚠️ 警告: 没有符合过滤条件的市场！请检查API结构或过滤规则是否正确。")

                self.log("正在按流动性排序...\n")
                top20 = self.get_top_markets(filtered)
                self.markets = top20

                for m in top20:
                    base = m.get("baseSymbol", "N/A")
                    quote = m.get("quoteSymbol", "N/A")
                    base_mint = m.get("baseMint")
                    quote_mint = m.get("quoteMint")
                    launch_time_str = m.get("launchTime")
                    launch_time_fmt = launch_time_str.split("T")[0] if launch_time_str else "未知"
                    liquidity_usd = round(m.get("liquidityUSD", 0), 2)

                    # 在表格中插入数据
                    self.tree.insert("", tk.END, values=(
                        base, quote, base_mint, quote_mint, launch_time_fmt, liquidity_usd
                    ))

                self.log(f"刷新完成，共显示 {len(top20)} 个市场。\n")
            except Exception as e:
                self.log(f"错误：{e}")
                messagebox.showerror("错误", f"获取数据失败：{e}")
            finally:
                self.refresh_btn.config(state=tk.NORMAL)

        threading.Thread(target=worker).start()

    def fetch_jupiter_markets(self):
        # 使用 lite-api.jup.ag 免费端点
        url = "https://quote-api.jup.ag/v1/markets"
        try:
            response = requests.get(url)
            self.log(f"API 状态码: {response.status_code}")
            self.log(f"API 响应前500字: {response.text[:500]}")
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                sample = data[0]
                self.log(f"API 返回字段示例: {list(sample.keys())}")
            else:
                self.log("API 返回为空或不是列表。")
            return data
        except Exception as e:
            self.log(f"API 请求失败，错误: {e}")
            return []

    def filter_markets(self, markets, days=7):
        # 过滤出最近7天且与SOL配对的市场
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
        self.log(f"过滤统计：无launchTime: {count_no_launch}，太早: {count_time_old}，非SOL配对: {count_not_sol}")
        return filtered

    def get_top_markets(self, filtered_markets, top_n=20):
        # 按流动性 USD 排序，取 Top N
        sorted_markets = sorted(filtered_markets, key=lambda x: x.get("liquidityUSD", 0), reverse=True)
        return sorted_markets[:top_n]

    def on_double_click(self, event):
        item = self.tree.selection()
        if not item:
            return
        item = item[0]
        values = self.tree.item(item, "values")
        base_mint = values[2]
        quote_mint = values[3]
        base_name = values[0]
        quote_name = values[1]

        win = tk.Toplevel(self.root)
        win.title(f"{base_name} / {quote_name} Token 图标")

        def load_and_show():
            base_icon = self.get_token_icon(base_mint)
            quote_icon = self.get_token_icon(quote_mint)

            if base_icon:
                lbl1 = tk.Label(win, image=base_icon)
                lbl1.image = base_icon
                lbl1.pack(side=tk.LEFT, padx=10, pady=10)
                tk.Label(win, text=base_name).pack(side=tk.LEFT, padx=10)
            else:
                tk.Label(win, text=f"{base_name} 图标未找到").pack(side=tk.LEFT, padx=10, pady=10)

            if quote_icon:
                lbl2 = tk.Label(win, image=quote_icon)
                lbl2.image = quote_icon
                lbl2.pack(side=tk.LEFT, padx=10, pady=10)
                tk.Label(win, text=quote_name).pack(side=tk.LEFT, padx=10)
            else:
                tk.Label(win, text=f"{quote_name} 图标未找到").pack(side=tk.LEFT, padx=10, pady=10)

        threading.Thread(target=load_and_show).start()

    def get_token_icon(self, mint):
        if mint in self.token_icon_cache:
            return self.token_icon_cache[mint]

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
