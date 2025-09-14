import sys

input = sys.stdin.readline
number = 0


T = int(input())

for _ in range(T):
  number = int(input())
  bin_num = bin(number)[2:][::-1]
  one_idx = [idx for idx, bit in enumerate(bin_num) if bit == '1']
  print(*one_idx)