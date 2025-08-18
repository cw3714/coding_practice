import sys
input = sys.stdin.readline
write= sys.stdout.write

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()

for num in array:
    write(f"{num}\n")