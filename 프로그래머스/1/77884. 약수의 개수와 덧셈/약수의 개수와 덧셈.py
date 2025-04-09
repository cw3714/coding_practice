#약수의 갯수가 홀수인 경우는 제곱수인 경우밖에 없다.
import math
def solution(left, right):   
    answer = 0
    for i in range(left, right + 1):
        if math.sqrt(i).is_integer():
            answer = answer - i
        else:
            answer = answer + i
    return answer
            
            
            