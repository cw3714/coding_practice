import math
N = str(math.factorial(int(input())))[::-1]
cnt = 0
for i in N:
    if i == '0':
        cnt += 1
    if i != '0':
        break
print(cnt)
    