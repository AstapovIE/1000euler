s, k = 0, 0
for i in range(1,101):
    s += i*i
    k += i
print(k**2 - s)