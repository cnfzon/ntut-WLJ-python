from collections import Counter

# 讀取檔案（與此程式放在同一層）
with open('names-10000.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 以逗號分隔，去除空白
names = [n.strip() for n in content.split(',') if n.strip()]
print(f"共 {len(names)} 筆姓名")

counter = Counter(names)

# 「重複」= 同一全名第二次及之後出現的次數
dup_count = sum(cnt - 1 for cnt in counter.values() if cnt >= 2)
print(f"\n全名有重複的共有 {dup_count} 人")

# 其中姓王的
wang_dup = sum(cnt - 1 for name, cnt in counter.items() if name[0] == '王' and cnt >= 2)
print(f"這些重複中，姓王的共有 {wang_dup} 人")