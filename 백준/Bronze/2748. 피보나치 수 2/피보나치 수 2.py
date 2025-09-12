import sys
from functools import lru_cache

input = sys.stdin.readline
n = int(input())

@lru_cache(maxsize=None)
def fibo(n):
  if n <= 1:
    return n
  else:
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n))
  