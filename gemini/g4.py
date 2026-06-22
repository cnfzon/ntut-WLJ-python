import datetime

# 讀取檔案內的所有日期資料
with open("PartDaysInAYear-4.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 將所有的 4 位數日期（例如 '0914'）提取出來並存入列表
dates = [token for token in content.split() if token.isdigit() and len(token) == 4]

# ----------------- 第一部分：統計月份出現次數 -----------------
month_counts = {}
for d in dates:
    month = d[:2]
    month_counts[month] = month_counts.get(month, 0) + 1

max_days = max(month_counts.values())
min_days = min(month_counts.values())

# ----------------- 第二部分：星期轉換與統計 -----------------
# 民國年對應的西元年
years = {
    116: 2027,
    117: 2028, # 2028是閏年
    118: 2029,
    119: 2030
}

y1, y3, y5, y6 = 0, 0, 0, 0

for d in dates:
    month = int(d[:2])
    day = int(d[2:])
    
    # 檢查並統計民國 116 年 (2027) 的星期一
    # datetime.weekday() 返回 0~6 分別代表 星期一~星期日
    try:
        if datetime.date(years[116], month, day).weekday() == 0:
            y1 += 1
    except ValueError:
        pass # 排除該年不存在的日期（例如非閏年的2月29日）
        
    # 檢查並統計民國 117 年 (2028) 的星期三 (weekday == 2)
    try:
        if datetime.date(years[117], month, day).weekday() == 2:
            y3 += 1
    except ValueError:
        pass

    # 檢查並統計民國 118 年 (2029) 的星期五 (weekday == 4)
    try:
        if datetime.date(years[118], month, day).weekday() == 4:
            y5 += 1
    except ValueError:
        pass

    # 檢查並統計民國 119 年 (2030) 的星期六 (weekday == 5)
    try:
        if datetime.date(years[119], month, day).weekday() == 5:
            y6 += 1
    except ValueError:
        pass

# ----------------- 計算題目要求的填空組合 -----------------
ans_sum1 = y1 + y5
ans_sum2 = y3 + y6
ans_prod = y1 * y3 * y5 * y6

# ----------------- 印出結果 -----------------
print(f"出現最多天的是: {max_days} 天")
print(f"出現最少天的是: {min_days} 天")
print(f"y1 (M116週一) = {y1}, y3 (M117週三) = {y3}, y5 (M118週五) = {y5}, y6 (M119週六) = {y6}")
print(f"y1 + y5 = {ans_sum1}")
print(f"y3 + y6 = {ans_sum2}")
print(f"他們的乘積 y1 * y3 * y5 * y6 = {ans_prod}")