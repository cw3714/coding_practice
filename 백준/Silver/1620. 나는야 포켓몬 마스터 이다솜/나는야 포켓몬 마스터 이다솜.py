import sys

input = sys.stdin.readline


N, M = map(int,input().split(" "))
pocket_list = [input().strip() for _ in range(N)]
pocket_num_name = {idx : name for idx, name in enumerate(pocket_list, start = 1)}
pocket_name_num = {name : idx for idx, name in enumerate(pocket_list, start = 1) } 

for _ in range(M):
  answer = input().strip()
  if answer.isdigit():
    print(pocket_num_name[int(answer)])
  else:
    print(pocket_name_num[answer])