def solution(absolutes, signs):
    cal_list = []
    for i in range(0,len(absolutes)):
        if signs[i] == True:
            cal_list.append(absolutes[i])
        elif signs[i] == False:
            cal_list.append(-absolutes[i])
    return sum(cal_list)