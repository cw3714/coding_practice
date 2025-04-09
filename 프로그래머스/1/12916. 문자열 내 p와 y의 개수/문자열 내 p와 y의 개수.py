def solution(s):
    s = s.lower()
    count_p = s.count('p')
    count_y = s.count('y')
    if count_p == count_y or 0:
        return True
    elif count_p != count_y:
        return False
    
        
        