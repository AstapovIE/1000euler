def is_p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


d = 2
x = 600851475143
while d * d != x:
    if x % d == 0 and is_p(x // d):
        print(x // d)
        break
    d += 1

