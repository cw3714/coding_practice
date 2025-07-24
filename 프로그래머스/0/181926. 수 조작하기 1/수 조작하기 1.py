def solution(n, control):
    con_list = {
        'w' : 1,
        's' : -1,
        'd' : 10,
        'a' : -10
    }
    
    for i in control:
        n += con_list[i]
    return n