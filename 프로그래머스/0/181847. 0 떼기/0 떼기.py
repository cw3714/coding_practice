import re
def solution(n_str):
    answer = ''
    return re.sub(r'^0+','',n_str)