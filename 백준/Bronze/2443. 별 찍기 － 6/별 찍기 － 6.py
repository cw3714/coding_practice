import sys

input = sys.stdin.readline

N = int(input())
star = 2 * N

for line in range(1, N + 1):
  print(" " * (line - 1), end = "")
  for stars in range(star - (2 * line - 1)):
    print("*", end = "")
  print()