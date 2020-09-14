# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:52 下午
# @Author : ddz

import sys

def test(dic):
    res = 0
    for i in dict(dic).keys():

        if len(dic[i]) != 2:
            continue

        if dic[i][0] not in dic.keys() and dic[i][1] not in dic.keys():
            res += 1
        # print(i)
    print(res)


if __name__ == '__main__':
    # dic = {1: [2, 3], 2: [4, 5], 3: [6], 6: [7, 8], 7: [9, 10]}

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    m, n = list(map(int, line.split()))
    dic = {}
    for _ in range(n):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        index, _, value = line.split()
        index = int(index)
        value = int(value)

        if dic.get(index):
            dic[index].append(value)
        else:
            dic[index] = [value]
    # print(dic)
    test(dic)
# 10 9
# 1 left 2
# 1 right 3
# 2 left 4
# 2 right 5
# 3 right 6
# 6 left 7
# 6 right 8
# 7 left 9
# 7 right 10