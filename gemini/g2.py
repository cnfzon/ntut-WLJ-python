import random

def gen_lotto(n, seed):
    numbers = [k for k in range(1, 43)]
    guess = []
    
    # 用來記錄在生成過程中被捨棄（重複）的組別
    duplicated_groups = []
    
    # 建立獨立的隨機產生器以確保 seed 作用精確
    rand = random.Random()
    rand.seed(seed)
    
    k = 0
    while k < n:
        rand.shuffle(numbers)
        g = numbers[:6]  # 抓取六個數字
        g.sort()         # 由小到大排序
        
        # 題目邏輯補全：如果 g 已經在 guess 中，代表重複了
        if g in guess:
            duplicated_groups.append(g)  # 記錄重複的組別
            # 注意：此處不遞增 k，代表捨棄並重新生成
            pass
        else:
            guess.append(g)
            k += 1  # 成功生成一組不重複的，k 才加 1
            
    return guess, duplicated_groups

# 執行題目要求：生成一萬組（n=10000），隨機種子帶入 8
n = 10000
seed = 8
lotto_tickets, r_groups = gen_lotto(n, seed)

# ----------------- 第一題 & 第二題 -----------------
r = len(r_groups)
# 將重複組別中的所有數字相加
r_sum = sum(sum(group) for group in r_groups)

# ----------------- 第三題（對獎統計） -----------------
winning_numbers = {1, 4, 14, 26, 37, 41}
m1, m2, m3, m4 = 0, 0, 0, 0

for ticket in lotto_tickets:
    # 計算每張彩券與中獎號碼重疊的個數
    match_count = len(set(ticket) & winning_numbers)
    if match_count == 1:
        m1 += 1
    elif match_count == 2:
        m2 += 1
    elif match_count == 3:
        m3 += 1
    elif match_count == 4:
        m4 += 1

# 計算 m1 + m2 + m3**m4 的結果
ans3 = m1 + m2 + (m3 ** m4)

# ----------------- 印出結果 -----------------
print(f"1. 重複狀況組數 r = {r}")
print(f"   重複組別的內容為: {r_groups}")
print(f"2. 這 {r} 組的 6*{r} 個數字相加總和為 = {r_sum}")
print(f"--- 對獎數據統計 ---")
print(f"   對中 1 個號碼的組數 m1 = {m1}")
print(f"   對中 2 個號碼的組數 m2 = {m2}")
print(f"   對中 3 個號碼的組數 m3 = {m3}")
print(f"   對中 4 個號碼的組數 m4 = {m4}")
print(f"3. 最終計算 m1 + m2 + m3**m4 = {ans3}")