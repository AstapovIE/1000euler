# не придумал адекватного(только перебор)
def is_palin(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


x = 100
for i in range(100, 999):
    for j in range(100, 999):
        if is_palin(i * j) and i * j > x:
            x = i * j
print(x)