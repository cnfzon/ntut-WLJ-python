import random as rand

def gen_invoices(n, seed):
    rand.seed(seed)
    invoices = [str(rand.random())[2:2+8] for k in range(n)]
    return invoices

# 生成 1 萬筆發票號碼，seed = 6
invoices = gen_invoices(10000, 6)

# 中獎號碼
winning = "31872067"

# 對獎：由後往前對號碼，只取最高中獎等級
m0 = m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = 0

for inv in invoices:
    matched = 0
    for i in range(1, 9):
        if inv[-i:] == winning[-i:]:
            matched = i
        else:
            break  # 一旦不符就停止（由後往前連續對）

    if matched == 0:
        m0 += 1
    elif matched == 1:
        m1 += 1
    elif matched == 2:
        m2 += 1
    elif matched == 3:
        m3 += 1
    elif matched == 4:
        m4 += 1
    elif matched == 5:
        m5 += 1
    elif matched == 6:
        m6 += 1
    elif matched == 7:
        m7 += 1
    elif matched == 8:
        m8 += 1

print(f"m0 = {m0}")
print(f"m1 = {m1}")
print(f"m2 = {m2}")
print(f"m3 = {m3}")
print(f"m4 = {m4}")
print(f"m5 = {m5}")
print(f"m6 = {m6}")
print(f"m7 = {m7}")
print(f"m8 = {m8}")
print(f"\nm0 = {m0}")
print(f"m1 * m2 ** m3 = {m1 * m2 ** m3}")