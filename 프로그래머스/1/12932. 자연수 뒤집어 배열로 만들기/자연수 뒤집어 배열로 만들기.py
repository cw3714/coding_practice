def solution(n):
    li = []
    new_li = []
    for x in str(n):
        li.append(x)
    
    li = li[::-1]
    return list(map(int,li))
        