import random as rand

def gen_lotto(n, seed):
    numbers = [k for k in range(1, 43)]
    guess = []
    same = []

    rand.seed(seed)
    k = 0
    while k < n:
        rand.shuffle(numbers)
        g = list(numbers[:6])   # 抓取六個數字（複製一份）
        g.sort()                # 由小到大排序

        # 如果 g 尚未出現在 guess 中，則加入；否則為重複，丟進 same
        if g in guess:
            same.append(g)      # 記錄重複組，不計入 k
        else:
            guess.append(g)
            k += 1              # 只有新組才讓 k 遞增

    return guess, same

# ── 產生 1 萬組不同的樂透號碼，seed = 8 ──────────────────────────────────────
result, duplicates = gen_lotto(10000, 8)

r = len(duplicates)
print(f"重複出現的組數 r = {r}")

sum_6r = sum(num for group in duplicates for num in group)
print(f"這 r 組的 6*r 個數字相加，總和 = {sum_6r}")

# ── 對獎：中獎號碼 [1, 4, 14, 26, 37, 41] ───────────────────────────────────
winning = [1, 4, 14, 26, 37, 41]
winning_set = set(winning)

m1 = m2 = m3 = m4 = 0
for ticket in result:
    matches = len(set(ticket) & winning_set)
    if matches == 1:
        m1 += 1
    elif matches == 2:
        m2 += 1
    elif matches == 3:
        m3 += 1
    elif matches == 4:
        m4 += 1

print(f"\n對中 1 個號碼的組數 m1 = {m1}")
print(f"對中 2 個號碼的組數 m2 = {m2}")
print(f"對中 3 個號碼的組數 m3 = {m3}")
print(f"對中 4 個號碼的組數 m4 = {m4}")

ans = m1 + m2 + m3**m4
print(f"\nm1 + m2 + m3**m4 = {ans}")