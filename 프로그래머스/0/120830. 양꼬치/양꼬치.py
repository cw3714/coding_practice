def solution(n, k):
    sale = (n // 10) * 2000
    total = n * 12000 + k * 2000 - sale

    return total
        
    