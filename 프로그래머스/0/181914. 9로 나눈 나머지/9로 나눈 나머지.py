def solution(number):
    li = []
    for i in str(number):
        li.append(i)
    int_list = map(int,li)
    return sum(int_list) % 9
        