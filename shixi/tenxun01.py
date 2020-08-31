# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:59 下午
# @Author : ddz

import sys


def test(m, list_c, list_w):
    sum_num = 0
    temp = 0
    for i, v in enumerate(list_w):
        temp = temp + (v - list_c[i] / m)
        sum_num = max(sum_num, int(temp))

    print(sum_num)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    list_c = list()
    list_w = list()
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        c, w = list(map(int, line.split()))
        list_c.append(c)
        list_w.append(w)
    test(m, list_c, list_w)

    # test(1, 2, [3], [1])
