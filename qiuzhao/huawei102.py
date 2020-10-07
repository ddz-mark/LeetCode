# -*- coding: utf-8 -*-
# @Time : 2020/9/30 7:48 下午
# @Author : ddz

import sys


def test(last_time, n, number, profit, start_time, time):

    temp = []
    for i, v in enumerate(start_time):
        if v + time[i] >= last_time:
            continue
        temp.append([number[i], profit[i], v, v + time[i]])

    temp = sorted(temp, key=lambda x: x[2])

    res = []
    i = 0
    # for i in range(1, len(temp)):
    while i <= len(temp) - 1:
        if i == len(temp) - 1:
            res.append(temp[i])
            i += 1
        else:
            if temp[i][3] > temp[i + 1][2]:
                if temp[i][1] > temp[i + 1][1]:
                    res.append(temp[i])
                else:
                    res.append(temp[i + 1])
                i += 2
            else:
                res.append(temp[i])
                i += 1


    res_profit = 0
    res_n = len(res)
    res_number = []
    for v in res:
        res_profit += v[1]
        res_number.append(v[0])
    print(res_profit)
    print(res_n)
    for v in res_number:
        print(v)



if __name__ == '__main__':
    last_time = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    number, profit, start_time, time = [], [], [], []

    for _ in range(n):
        line1 = sys.stdin.readline().strip()
        values = list(map(int, line1.split()))
        number.append(values[0])
        profit.append(values[1])
        start_time.append(values[2])
        time.append(values[3])

    test(last_time, n, number, profit, start_time, time)
