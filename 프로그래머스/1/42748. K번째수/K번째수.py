def solution(array, commands):    
    answer = []
    for a,b,c in commands:
        source = sorted(array[a-1:b])[c-1]
        answer.append(source)
    return answer