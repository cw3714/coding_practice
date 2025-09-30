import sys

input = sys.stdin.readline

while True:
  word = input().rstrip()
  if word == "END":
    break
  else:
    print(word[::-1])