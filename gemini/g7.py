from collections import Counter

file_name = "Scores-9384-5.txt"
students = []

# 1. 讀取並精準解析檔案
with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳過空行、網址或來源標籤
        if not line or line.startswith("
            try:
                scores = [int(x) for x in parts[1:]]
                students.append({
                    "name": name,
                    "scores": scores,
                    "total": sum(scores)
                })
            except ValueError:
                # 排除可能包含非數字的雜訊行
                continue

# --- 問題 1 & 2：姓氏與不及格科目數統計 ---
wang_count = 0
wu_count = 0

for s in students:
    # 統計不及格（小於 60 分）的科目數
    fail_count = sum(1 for score in s["scores"] if score < 60)
    
    # 姓王且剛好 2 科不及格
    if s["name"].startswith("王") and fail_count == 2:
        wang_count += 1
        
    # 姓吳且剛好 3 科不及格
    if s["name"].startswith("吳") and fail_count == 3:
        wu_count += 1

print(f"1. 姓 王 的同學，且剛好有 2 個科目不及格，共有 {wang_count} 人。")
print(f"2. 姓 吳 的同學，且剛好有 3 個科目不及格，共有 {wu_count} 人。")

# --- 問題 3：最高分與最低分 high + low ---
totals = [s["total"] for s in students]
high = max(totals)
low = min(totals)
print(f"3. 最高分 (high) = {high}, 最低分 (low) = {low} ➔ high + low = {high + low}")

# --- 問題 4 & 5：同分人數統計與分數加總 ---
score_counts = Counter(totals)
# 找出最高的同分人數是多少人
max_same_count = max(score_counts.values()) 

# 找出所有符合「最高同分人數」的總分分數
most_common_scores = [score for score, count in score_counts.items() if count == max_same_count]
sum_of_scores = sum(most_common_scores)

print(f"4. 在統計總分同分人數時，最多的是幾人: {max_same_count} 人。")
print(f"5. 符合最多同分人數的分數為 {most_common_scores}，將這些分數加總的結果是: {sum_of_scores}")