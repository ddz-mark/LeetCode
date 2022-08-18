# -*- coding: utf-8 -*-
# @Time : 2021/8/29 上午9:43
# @Author : ddz

import sys

def test(n, values):
    res = 0
    dict = {}
    for i, v in enumerate(values):
        if dict.get(v):
            dict[v] += 1
        else:
            dict[v] = 1

        res += sorted(dict.keys()).index(v)

    print(res)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    test(n, values)