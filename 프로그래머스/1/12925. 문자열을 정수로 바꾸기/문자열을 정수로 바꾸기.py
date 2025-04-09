def solution(s):
    if s[0] != '-':
        return abs(int(s))
    else:
        s.replace('','-')
        return int(s)