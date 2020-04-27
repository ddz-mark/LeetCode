# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:59 下午
# @Author : ddz

import sys

import math


def test(A, B, C):
    x1, y1 = 0, 0

    # 两个交点坐标
    x2 = (2 * A - 2 * B * C + math.sqrt((2 * B * C - 2 * A) * (2 * B * C - 2 * A) - 4 * B * B * C * C)) / (2 * B * B)
    x3 = (2 * A - 2 * B * C - math.sqrt((2 * B * C - 2 * A) * (2 * B * C - 2 * A) - 4 * B * B * C * C)) / (2 * B * B)
    y2 = (2 * A - 2 * B * C + math.sqrt(4 * A * A - 8 * A * B * C)) / (2 * B) + C
    y3 = (2 * A - 2 * B * C - math.sqrt(4 * A * A - 8 * A * B * C)) / (2 * B) + C

    # print(x2, x3, y2, y3)
    # 积分面积
    s = pow(y2, 2) / (2 * B) - C * y2 / B - pow(y2, 3) / (6 * A) - \
        pow(y3, 2) / (2 * B) - C * y3 / B - pow(y3, 3) / (6 * A)
    print(s)

if __name__ == '__main__':
    # n = int(input())
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     A, B, C = list(map(int, line.split()))
    #     test(A, B, C)

    test(1, 1, -6)
