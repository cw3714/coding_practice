def solution(emergency):
    answer = []
    new_list = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(new_list.index(i) + 1)
    return answer
    