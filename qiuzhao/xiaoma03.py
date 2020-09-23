# -*- coding: utf-8 -*-
# @Time : 2020/9/20 3:25 下午
# @Author : ddz

import sys


def test(n, values):
    # print(n, values)

    res = 0
    i = 0
    while i < n - 1:
        while i < n - 1 and values[i + 1] > values[i]:
            i += 1
        if values[i] - min(values[:i + 1]) > 0:
            res += (values[i] - min(values[:i + 1]))
            values[i] = float('inf')
            values[values.index(min(values[:i + 1]))] = float('inf')

        i += 1

    print(res)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    test(n, values)
