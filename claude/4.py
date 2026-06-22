from collections import Counter
import datetime

# 讀取檔案（與此程式放在同一層）
with open("PartDaysInAYear-4.txt", "r") as f:
    data = f.read()

dates = data.split()
print(f"共 {len(dates)} 筆日期")

# ── Q1：同月份中出現最多/最少天數 ─────────────────────────────────────────────
month_counter = Counter(d[:2] for d in dates)
max_days = max(month_counter.values())
min_days = min(month_counter.values())
print(f"\n同月份中出現最多天的是 {max_days} 天，出現最少天的是 {min_days} 天")

# ── Q2：在民國 116~119 年中，找符合指定星期幾的日期數量 ─────────────────────
# 民國年 = 西元年 - 1911
# 116 → 2027, 星期一 (weekday=0)
# 117 → 2028, 星期三 (weekday=2)
# 118 → 2029, 星期五 (weekday=4)
# 119 → 2030, 星期六 (weekday=5)

year_config = {
    116: (2027, 0),   # 星期一
    117: (2028, 2),   # 星期三
    118: (2029, 4),   # 星期五
    119: (2030, 5),   # 星期六
}

results = {}
for roc_year, (western_year, target_weekday) in year_config.items():
    count = 0
    for d in dates:
        month = int(d[:2])
        day = int(d[2:])
        try:
            dt = datetime.date(western_year, month, day)
            if dt.weekday() == target_weekday:
                count += 1
        except ValueError:
            pass  # 無效日期（如閏年的 0229 在非閏年）
    results[roc_year] = count

y1 = results[116]   # 民國116，星期一
y3 = results[117]   # 民國117，星期三
y5 = results[118]   # 民國118，星期五
y6 = results[119]   # 民國119，星期六

print(f"\ny1 = {y1}（民國116年，星期一）")
print(f"y3 = {y3}（民國117年，星期三）")
print(f"y5 = {y5}（民國118年，星期五）")
print(f"y6 = {y6}（民國119年，星期六）")

print(f"\ny1 + y5 = {y1 + y5}")
print(f"y3 + y6 = {y3 + y6}")
print(f"y1 * y3 * y5 * y6 = {y1 * y3 * y5 * y6}")