def solution(a, b):
    #answer = []
    #for i in range(len(a)):
        #answer.append(a[i] * b[i])
    #return sum(answer)

    return sum([a[x] * b[x] for x in range(len(a))])