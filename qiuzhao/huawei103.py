# -*- coding: utf-8 -*-
# @Time : 2020/9/30 8:51 下午
# @Author : ddz

import sys


def test(n, m, uv):
    # print(n, m, uv)

    hash_set_1 = set()
    hash_set_2 = set()
    res = 0
    for v in uv:
        if v[0] in hash_set_1 and v[1] in hash_set_2:
            continue
        else:
            res += 1
            hash_set_1.add(v[0])
            hash_set_2.add(v[1])

    print(res)


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))

    uv = []
    for _ in range(m):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        uv.append(values)
    test(n, m, uv)
