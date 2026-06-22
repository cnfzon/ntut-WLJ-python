from collections import Counter

# 讀取檔案（與此程式放在同一層）
with open('Scores-9384-5.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 解析：姓名 + 5 科成績
students = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 6:
        name = parts[0]
        scores = list(map(int, parts[1:]))
        students.append((name, scores))

print(f"共 {len(students)} 位學生")

# 不及格 = 分數 < 60

# 姓王，剛好有 2 科不及格
wang_exact2 = sum(1 for name, scores in students
                  if name[0] == '王' and sum(1 for s in scores if s < 60) == 2)
print(f"\n姓王且剛好 2 科不及格: {wang_exact2} 人")

# 姓吳，剛好有 3 科不及格
wu_exact3 = sum(1 for name, scores in students
                if name[0] == '吳' and sum(1 for s in scores if s < 60) == 3)
print(f"姓吳且剛好 3 科不及格: {wu_exact3} 人")

# 所有人的總分
totals = [sum(scores) for name, scores in students]
high = max(totals)
low = min(totals)
print(f"\n最高總分 high = {high}")
print(f"最低總分 low  = {low}")
print(f"high + low = {high + low}")

# 統計總分人數，找出最多人的人數
total_counter = Counter(totals)
max_count = max(total_counter.values())
print(f"\n總分同分人數最多的是: {max_count} 人")

# 哪些總分的人數等於最多人數
most_common_totals = sorted(t for t, cnt in total_counter.items() if cnt == max_count)
print(f"這些總分值: {most_common_totals}")
print(f"將這些分數加總: {sum(most_common_totals)}")