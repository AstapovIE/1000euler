def is_simple(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = 10001
k = 0
i = 2
while k != n:
    if is_simple(i):
        k += 1
    i+=1
print(i-1)
