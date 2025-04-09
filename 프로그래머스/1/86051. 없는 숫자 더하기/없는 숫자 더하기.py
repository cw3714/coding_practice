def solution(numbers):
    origin = [x for x in range(0,10)]
    set1 = set(origin)
    set2 = set(numbers)
    res = list(set1 - set2)
    return sum(res)
        
    
    