with open('Numbers_In_FourKinds-2.txt', 'r') as f:
    content = f.read()

tokens = content.split()

# 分類四種型態
# 型態1: 純數字（無逗號、無$）
# 型態2: 有逗號的貨幣格式（無$）
# 型態3: $開頭 + 純數字（無逗號）
# 型態4: $開頭 + 有逗號的貨幣格式

type1, type2, type3, type4 = [], [], [], []

for t in tokens:
    has_dollar = t.startswith('$')
    body = t[1:] if has_dollar else t
    has_comma = ',' in body

    if not has_dollar and not has_comma:
        type1.append(t)
    elif not has_dollar and has_comma:
        type2.append(t)
    elif has_dollar and not has_comma:
        type3.append(t)
    else:
        type4.append(t)

a, b, c, d = len(type1), len(type2), len(type3), len(type4)
print(f"型態1 共 a = {a} 個")
print(f"型態2 共 b = {b} 個")
print(f"型態3 共 c = {c} 個")
print(f"型態4 共 d = {d} 個")
print(f"\na + b + c*d = {a + b + c*d}")

# 型態2 總和
sum2 = sum(int(t.replace(',', '')) for t in type2)
print(f"\n型態2 所有數字相加總和 = {sum2}")

# 型態3 總和（去掉$）
sum3 = sum(int(t[1:]) for t in type3)
print(f"型態3 所有數字相加總和 = {sum3}")

# 型態1 全部轉字串後串接
str1 = ''.join(type1)
print(f"\n型態1 串接後字元長度 = {len(str1)}")

# 每個字元（數字符號）逐一相加
digit_sum = sum(int(ch) for ch in str1)
print(f"型態1 串接內容每個數字符號加總 = {digit_sum}")