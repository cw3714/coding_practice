def solution(price,money,count):
    res_price = 0
    for i in range(1, count + 1):
        res_price = res_price + price * i
    if money - res_price >= 0:
        return 0
    else:    
        return abs(money-res_price)