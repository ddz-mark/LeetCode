# -*- coding: utf-8 -*-
# @Time : 2020/9/11 9:30 下午
# @Author : ddz

import sys


def test(n, id, record):
    res = [i for i in range(1, n + 1)]
    i = record.index(0)

    res = list(set(res) - set(id[1:i]) - set(id[i:len(record) - 1]))

    if id[0] != id[-1]:
        if id[0] in res:
            res.pop(res.index(id[0]))
        if id[-1] in res:
            res.pop(res.index(id[-1]))
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    # n =
    # id = [1, 2]
    # record = [1, 0]

    s = sys.stdin.readline().strip()
    n, m = list(map(int, s.split()))
    id = []
    record = []
    for _ in range(m):
        line = sys.stdin.readline().strip()
        v1, v2 = list(map(int, line.split()))
        id.append(v1)
        record.append(v2)

    test(n, id, record)
