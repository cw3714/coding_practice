import sys

input = sys.stdin.readline


N = int(input())

for i in range(1, N + 1):
  print(" " * (N - i), end = "")
  for star in range(i * 2 - 1):
    print("*", end = "")
  print()
  