# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:59 下午
# @Author : ddz

import sys


def test(n, k, list_k):
    count = 0
    if n == 0:
        return 0

    for i in range(n):
        for j in range(i + 1, n):
            temp = []
            for q in range(0, k):
                temp.append(list_k[i][q] + list_k[j][q])

            if len(list(set(temp))) == 1:
                count += 1

    print(count)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    list_k = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        list_k.append(list(map(int, line.split())))

    # n = 5
    # k = 3
    # list_k = [[2, 11, 21],
    #           [19, 10, 1],
    #           [20, 11, 1],
    #           [6, 15, 24],
    #           [18, 27, 36]]
    test(n, k, list_k)

    # print([1, 2, 2] + [2, 3, 4])
