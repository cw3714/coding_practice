import sys

input = sys.stdin.readline



_ = input()

number = [int(x) for x in input().split(" ")]

print(min(number) * max(number))