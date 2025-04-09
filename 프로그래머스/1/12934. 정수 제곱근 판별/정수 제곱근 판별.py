import math
def solution(n):
    n = n ** (1/2)
    if n % 1 == 0:
        return pow(n+1,2)
    else:
        return -1