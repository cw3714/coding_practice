def solution(n):
    con = []
    for i in range(1, n+1):
        if n % i == 1:
            con.append(i)
    return min(con)
        