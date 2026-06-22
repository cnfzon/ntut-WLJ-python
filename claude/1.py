from collections import Counter

# ── 建立 9x9 乘法表（字串格式）──────────────────────────────────────────────
rows = []
for i in range(1, 10):
    row_parts = []
    for j in range(1, 10):
        row_parts.append(f"{i}x{j}={i*j}")
    rows.append(' '.join(row_parts))

full_table = '\n'.join(rows)
print("=== 乘法表 ===")
print(full_table)
print()

# ── 由左→右、上→下，取出所有數字字元 ─────────────────────────────────────
all_chars = full_table.replace('\n', '').replace(' ', '')
digits_seq = [c for c in all_chars if c.isdigit()]   # 移除 x 和 = 後的數字字元序列

# ── Q1：第 125 個數字 ────────────────────────────────────────────────────────
ans1 = digits_seq[124]   # index 從 0 開始
print(f"Q1 第 125 個數字是：{ans1}")
print()

# ── 拆解每個格子為三個數（i, j, i*j）────────────────────────────────────────
number_list = []
for i in range(1, 10):
    for j in range(1, 10):
        number_list.extend([i, j, i * j])   # 移除 x, = 後的三個數字組合

# ── Q2：每個數加 4 後連乘，結果是幾位數 ──────────────────────────────────────
product = 1
for n in number_list:
    product *= (n + 4)

digit_count = len(str(product))
print(f"Q2 各數字加 4 後連乘的結果共 {digit_count} 位數")
print()

# ── Q3：合併成長字串，統計各數字出現次數，最多與最少的差 ─────────────────────
long_str = ''.join(str(n) for n in number_list)
counter = Counter(long_str)

print("Q3 各數字出現次數：")
for digit in sorted(counter.keys()):
    print(f"  '{digit}' 出現 {counter[digit]} 次")

max_count = max(counter.values())
min_count = min(counter.values())
diff = max_count - min_count
print(f"\nQ3 次數最多={max_count}，次數最少={min_count}，差為：{diff}")