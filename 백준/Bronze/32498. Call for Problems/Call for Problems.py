import sys

input = sys.stdin.readline
cnt = 0

for _ in range(int(input())):
  check = int(input())
  if check % 2 != 0:
    cnt += 1
    
print(cnt)
  
  