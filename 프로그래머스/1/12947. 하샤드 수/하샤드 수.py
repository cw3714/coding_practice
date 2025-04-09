def solution(x):
    li = []
    for i in str(x):
        li.append(i)
    li = list(map(int,li))
    if x % sum(li) ==0 :
        return True
    else:
        return False
        