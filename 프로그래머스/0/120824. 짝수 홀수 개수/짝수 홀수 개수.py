def solution(num_list):
    even = 0
    odd = 0
    for check in num_list:
        if check % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even,odd]