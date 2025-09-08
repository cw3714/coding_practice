import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

answer = []
member = deque([x for x in range(1, N + 1)])


while member:
  member.rotate(-(K-1))
  die_person = member.popleft()
  answer.append(str(die_person))

print("<" + ", ".join(answer) + ">")