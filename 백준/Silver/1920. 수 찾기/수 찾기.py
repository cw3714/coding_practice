import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
array1 = set(map(int,input().split()))

M = int(input())
array2= list(map(int,input().split()))


for i in array2:
  if i in array1:
    print(1)
  else:
    print(0)