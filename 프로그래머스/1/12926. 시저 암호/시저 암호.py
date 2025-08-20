import string
def solution(s, n):
    upper_list = [x for x in string.ascii_uppercase]
    lower_list = [x for x in string.ascii_lowercase]
    answer = ""
    for i in s:
        if i.isupper() == True:
            answer += upper_list[(upper_list.index(i) + n) % 26]
        elif i.islower() == True:
            answer += lower_list[(lower_list.index(i) + n) % 26]
        else:
            answer += i
    return answer
