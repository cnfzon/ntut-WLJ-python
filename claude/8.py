from math import prod

# 建立 a*b 字串（1 到 316）
a = ''.join(str(i) for i in range(1, 317))   # 1,2,3,...,316
b = ''.join(str(i) for i in range(316, 0, -1))  # 316,315,...,1
ab = a + b

print(f"a 長度: {len(a)}, b 長度: {len(b)}, a*b 總長度: {len(ab)}")

def find_non_overlap(s, start_digit, length):
    """從頭到尾，不重疊地找出以 start_digit 開頭、長度為 length 的數字組合"""
    results = []
    i = 0
    while i < len(s):
        if s[i] == start_digit:
            substr = s[i:i+length]
            if len(substr) == length:
                results.append(substr)
                i += length   # 不重疊：跳過這段
            else:
                i += 1
        else:
            i += 1
    return results

# n1：以 2 開頭，長度為 2 的數字組合個數
matches_len2 = find_non_overlap(ab, '2', 2)
n1 = len(matches_len2)
print(f"\nn1（以2開頭、長度2）= {n1}")

# n2：以 4 開頭，長度為 3 的數字組合個數
matches_len3 = find_non_overlap(ab, '4', 3)
n2 = len(matches_len3)
print(f"n2（以4開頭、長度3）= {n2}")
print(f"n1 + n2 = {n1 + n2}")

# 長度為 2 的前 14 個，連乘積
front14 = [int(v) for v in matches_len2[:14]]
print(f"\n前14個長度2以2開頭的數字: {front14}")
product = prod(front14)
print(f"連乘積 = {product}")

# 長度為 3 以 4 開頭的所有數字，總和
total = sum(int(v) for v in matches_len3)
print(f"\n所有長度3以4開頭的數字總和 = {total}")