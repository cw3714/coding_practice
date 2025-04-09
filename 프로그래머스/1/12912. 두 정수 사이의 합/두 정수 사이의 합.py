def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b):
            for k in range(i, b+1):
                answer = answer + k
            return answer
    elif a > b:
        for i in range(b, a):
            for k in range(i, a+1):
                answer = answer + k
            return answer
    else:
        return a or b
            