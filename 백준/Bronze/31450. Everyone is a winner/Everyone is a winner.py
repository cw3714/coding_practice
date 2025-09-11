import sys

input = sys.stdin.readline


M,N = map(int,input().split(" "))

print("Yes" if M % N == 0 else "No")