def solution(d, budget):
    d = sorted(d)
    for i in range(0, len(d)):
        budget = budget - d[i]
        if budget <0:
            return i
            break
    return len(d)
    