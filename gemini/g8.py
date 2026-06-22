file_name = "Scores-9384-5.txt"
students = []

# 1. 讀取並解析檔案
with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("
                scores = [int(x) for x in parts[1:]]
                students.append({
                    "name": name, 
                    "scores": scores, 
                    "total": sum(scores)
                })
            except ValueError:
                continue

# 2. 分類統計不及格科目數
fail_2_totals = []  # 剛好 2 科不及格的總分清單
fail_3_totals = []  # 剛好 3 科不及格的總分清單

for s in students:
    fail_count = sum(1 for score in s["scores"] if score < 60)
    if fail_count == 2:
        fail_2_totals.append(s["total"])
    elif fail_count == 3:
        fail_3_totals.append(s["total"])

# 3. 計算答案
high2, low2 = max(fail_2_totals), min(fail_2_totals)
high3, low3 = max(fail_3_totals), min(fail_3_totals)
ans3_count = len(fail_3_totals) # 3科不及格 = 2科及格

print(f"--- 第八題 執行結果 ---")
print(f"1. 不及格2科者：high2 = {high2}, low2 = {low2} ➔ high2 - low2 = {high2 - low2}")
print(f"2. 不及格3科者：high3 = {high3}, low3 = {low3} ➔ high3 + low3 = {high3 + low3}")
print(f"3. 剛好有2個科目及格（3科不及格）的人數：共有 {ans3_count} 人")