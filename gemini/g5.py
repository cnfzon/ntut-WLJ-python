import re

# 讀取檔案內容
with open("Numbers_In_FourKinds-2.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 【已修正】完美移除 標籤，且不會造成引號未關閉錯誤
content = re.sub(r"\", "", content)

# 找出所有被空格、換行分隔開的資料項
tokens = content.split()

# 定義 4 種型態的列表以利後續計算
type1_list = []
type2_list = []
type3_list = []
type4_list = []

for token in tokens:
    # 型態 4: 以 $ 開頭，且包含逗點
    if token.startswith("$") and "," in token:
        type4_list.append(token)
    # 型態 3: 以 $ 開頭，且不含逗點
    elif token.startswith("$") and "," not in token:
        type3_list.append(token)
    # 型態 2: 不以 $ 開頭，但包含逗點
    elif not token.startswith("$") and "," in token:
        type2_list.append(token)
    # 型態 1: 不以 $ 開頭，且不含逗點（純數字組合）
    else:
        type1_list.append(token)

a = len(type1_list)
b = len(type2_list)
c = len(type3_list)
d = len(type4_list)

# ----------------- 第一部分 -----------------
ans1 = a + b + c * d

# ----------------- 第二部分 -----------------
# 型態 2 相加（需先移除逗點轉成整數）
sum_type2 = sum(int(x.replace(",", "")) for x in type2_list)

# 型態 3 相加（需先移除 $ 符號轉成整數）
sum_type3 = sum(int(x.replace("$", "")) for x in type3_list)

# ----------------- 第三部分 -----------------
# 將型態 1 的所有字串直接串接起來
concat_type1 = "".join(type1_list)
ans_length = len(concat_type1)

# 將串接字串中的每個字元數字逐一轉整數相加
ans_digit_sum = sum(int(char) for char in concat_type1)

# ----------------- 印出結果 -----------------
print(f"a + b + c * d = {ans1}")
print(f"將所有 型態2) 的數字相加，其總和是：{sum_type2}")
print(f"將所有 型態3) 的數字相加，其總和是：{sum_type3}")
print(f"將所有 型態1) 的數字先轉換成字串後直接串接，其總文字長度是：{ans_length}")
print(f"如果將上述串接內容的每個數字字號逐一相加，其總和是：{ans_digit_sum}")