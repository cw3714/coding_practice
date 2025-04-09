
def solution(arr, divisor):
    
    def sol(n):
        if n % divisor == 0:
            return True
        return False
    
    answer = list((filter(sol,arr)))
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer