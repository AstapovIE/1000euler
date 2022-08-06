def is_good(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

x = 20
while True:
    if is_good(x):
        print(x)
        break
    x += 20
