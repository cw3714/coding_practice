str_list = []

while True:
    try:
        str_list.append(input())
    except:
        break

for i in range(len(str_list)):
    print(str_list[i])