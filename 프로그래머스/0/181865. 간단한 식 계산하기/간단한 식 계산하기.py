def solution(binomial):
    expr = binomial.split()
    expr[0] = int(expr[0])
    expr[2] = int(expr[2])
    if expr[1] == "+":
        return expr[0] + expr[2]
    elif expr[1] == "-":
        return expr[0] - expr[2]
    else:
        return expr[0] * expr[2]