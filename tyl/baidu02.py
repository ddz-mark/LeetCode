# -*- coding: utf-8 -*-
# @Time : 2021/3/21 下午6:02
# @Author : ddz
import sys


def test02(n, a, b):

    # 差集
    maxL = list(set(a).difference(set(b)))
    minL = list(set(b).difference(set(a)))


    # 并集
    if len(set(a).union(set(b))) < n:
        print(-1, -1)
        return
    else:
        resMax, resMin = -1, -1
        if len(maxL) == 1:
            resMax = maxL[0]

        if len(minL) == 1:
            resMin = minL[0]

        print(resMax, resMin)


if __name__ == '__main__':
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    a, b = [], []
    for i in range(m):
        ai, bi = list(map(int, sys.stdin.readline().strip().split()))
        a.append(ai)
        b.append(bi)
    test02(n, a, b)

# 5 5
# 2 1
# 2 3
# 1 3
# 3 4
# 4 5

# 4 4
# 1 2
# 2 3
# 3 1
# 4 2
