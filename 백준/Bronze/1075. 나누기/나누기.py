import sys

input = sys.stdin.readline

N = int(input())
F = int(input())
number = [f'{x:02d}' for x in range(0,100)]

for i in number: 
  change_num = str(N)
  change_num = change_num[:-2] + i
  change_num = int(change_num )

  if change_num % F == 0:
    print(i)
    break