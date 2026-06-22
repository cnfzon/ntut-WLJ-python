import re

# 1. 讀取並清洗檔案內容
with open("names-10000.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 移除檔案內類似 的標籤行
# content = re.sub(r"\", "", content)

# 2. 抓取所有乾淨的姓名列表
all_full_names = [name for name in content.split() if name.strip()]

# 3. 提取出所有人名的「姓氏」（中文姓名取第一個字）
all_last_names = [name[0] for name in all_full_names if len(name) > 0]

# 4. 統計每個姓氏出現的次數
lastname_counts = {}
for ln in all_last_names:
    lastname_counts[ln] = lastname_counts.get(ln, 0) + 1

# 5. 找出有重複的姓氏（出現次數大於 1）
# 依據題目定義：只要已經有這個姓氏，出現第二次以上就算重複。
r_groups = [ln for ln, count in lastname_counts.items() if count > 1]
r = len(r_groups)

# 6. 計算這 r 組重複姓氏的「姓氏字數」總和
total_lastname_chars = sum(len(ln) for ln in r_groups)

# ----------------- 印出最終答案 -----------------
print(f"總共成功讀取到: {len(all_full_names)} 個姓氏")
print(f"1. 重複狀況共有 r = {r} 組")
print(f"2. 這 r 組的姓氏字數相加總和為 = {total_lastname_chars}")

# 附帶印出前 10 個重複出現的姓氏供您參考
print(f"\n[參考數據] 前 10 個重複出現的姓氏：{r_groups[:10]}")