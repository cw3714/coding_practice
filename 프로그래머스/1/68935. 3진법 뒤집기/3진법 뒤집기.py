def solution(n):
    answer = 0
    third = ''
    while n > 0:
        third += str(n % 3)
        n //= 3
    
    for i in range(len(third)):
        answer += int(third[i]) * (3 ** (len(third) - i - 1))
    return answer
  