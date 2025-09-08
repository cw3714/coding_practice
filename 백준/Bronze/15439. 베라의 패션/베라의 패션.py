import sys
from itertools import combinations,product

input = sys.stdin.readline
N = int(input())
print(N * (N - 1))