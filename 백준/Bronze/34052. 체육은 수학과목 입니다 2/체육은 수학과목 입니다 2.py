import sys

input = sys.stdin.readline


time = [int(input()) for _ in range(4)]
checker = sum(time)

print("Yes") if checker + 300 <= 1800 else print("No")