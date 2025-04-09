def solution(n):
    answer = 0
    n = list(str(n))
    n.sort(reverse = True)
    n = int(''.join(n))
    return n
    