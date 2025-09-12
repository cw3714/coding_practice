import sys

input = sys.stdin.readline

T = int(input())

def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

for _ in range(T):
  a,b = map(int,input().split(" "))
  print(a * b // gcd(a,b))