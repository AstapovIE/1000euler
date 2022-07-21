i = 2
j = 1
sum = 0
while i <= 4000000:
    if i % 2 == 0:
        sum += i
    i, j = i + j, i
print(sum)
