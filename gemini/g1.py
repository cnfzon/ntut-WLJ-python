# 1. 建立九九乘法表，並依照「由左往右、從上往下」提取所有數字（移除 x, = 和空格）
digit_list = []
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        # 將每一項拆解為單個數字字元，例如 2x5=10 拆成 '2', '5', '1', '0'
        equation_digits = list(str(i) + str(j) + str(product))
        digit_list.extend(equation_digits)

# 將其合併為長字串
long_string = "".join(digit_list)

# ----------------- 第一題 -----------------
# 找出第 125 個數字（人性化第 1 個對應 Python 索引 124）
ans1 = long_string[124]

# ----------------- 第二題 -----------------
# 將拆解出的數字組合（個別數字），先逐一加上 4 後連乘起來
total_product = 1
for d in digit_list:
    num = int(d) + 4
    total_product *= num
# 計算連乘積的總位數
ans2 = len(str(total_product))

# ----------------- 第三題 -----------------
# 統計 0~9 各個數字出現的次數
counts = {}
for char in "0123456789":
    counts[char] = long_string.count(char)

# 計算出現次數最多與最少的差值
max_count = max(counts.values())
min_count = min(counts.values())
ans3 = max_count - min_count

# ----------------- 印出結果 -----------------
print(f"1. 第 125 個數字是: {ans1}")
print(f"2. 連乘積的結果位數為: {ans2}")
print(f"3. 次數最多與次數最少的差為: {ans3}")

# 附帶印出 0-9 的出現次數給您參考
print("\n[參考數據] 各數字出現次數統計：")
for k, v in sorted(counts.items()):
    print(f"數字 {k}: 出現 {v} 次")