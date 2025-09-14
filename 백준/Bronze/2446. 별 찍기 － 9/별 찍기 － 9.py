import sys

input = sys.stdin.readline


N = int(input())

for line in range(1, N + 1):
  print(" " * (line - 1),end = "")
  print("*" * (2 * N - (2 * line - 1)))

for line1 in range(N - 1, 0, -1):
  print(" " * (line1 - 1), end = "")
  print("*" * ((2 * N) - (2 * line1 - 1)))
  
  # 5 3 
  # 4 5 
  # 3 7 
  # 2 9