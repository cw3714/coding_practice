import sys
input = sys.stdin.readline
ase = [1,2,3,4,5,6,7,8]
desc = [8,7,6,5,4,3,2,1]
arr = list(map(int,input().split())) 

if (arr == ase) == True:
    print("ascending")
elif(arr == desc) == True:
    print("descending")
else:
    print("mixed")