def solution(s):
    cal = int(len(s) / 2)
    if len(s) % 2 != 0:  
        return s[cal]
    else:
        return s[cal-1] + s[cal]