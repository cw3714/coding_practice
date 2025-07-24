def solution(numLog):
    answer = ''
    con_list = {
        1 : 'w',
        -1 : 's',
        10 : 'd',
        -10 : 'a'
    } 
    cal_list = []
    for i in range(1,len(numLog)):
        cal_list.append(numLog[i] - numLog[i - 1])
    
    for k in cal_list:
        answer += con_list[k]
        
    return answer