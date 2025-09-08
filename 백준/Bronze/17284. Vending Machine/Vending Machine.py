import sys

input = sys.stdin.readline
money = 5000
price = {1 : 500,
        2 : 800,
        3 : 1000}

button_list = map(int,input().split(" "))

money -= sum(price[x] for x in button_list)

print(money)

