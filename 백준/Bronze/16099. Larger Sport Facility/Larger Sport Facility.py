import sys

input = sys.stdin.readline


for _ in range(int(input())):
  Te_w,Te_l,Eu_w,Eu_l = map(int,input().split(" "))
  if Te_w * Te_l > Eu_w * Eu_l:
    print("TelecomParisTech")
  elif Eu_w * Eu_l > Te_w * Te_l:
    print("Eurecom")
  else:
    print("Tie")