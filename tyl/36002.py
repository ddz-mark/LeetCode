# -*- coding: utf-8 -*-
# @Time : 2021/3/28 下午7:47
# @Author : ddz
import sys


def test02(k, goods):
    res = sum(sorted(list(zip(*goods))[1])[k - 1:])
    return res


if __name__ == '__main__':

    n, m, k = list(map(int, sys.stdin.readline().strip().split()))
    goods = []
    for i in range(n):
        v1, v2 = list(map(int, sys.stdin.readline().strip().split()))
        if v1 <= m * k:
            goods.append([v1, v2])
    print(test02(k, goods[1:]) + goods[0][1])
