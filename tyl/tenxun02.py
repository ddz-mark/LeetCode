# -*- coding: utf-8 -*-

import sys
import math


def test02(n, u, v, s, t, m):
    # res = float("inf")
    # for x in range(n):
    #     for y in range(n // 2):
    #         if s * x + t * y * y <= m and x + 2 * y == n:
    #             res = min(res, u * x + v * y)
    #
    # print(res)

    yt1 = (2 * s + (math.sqrt(4 * s * s - 4 * t * (m - s * n)))) // (2 * t)
    yt2 = (2 * s - (math.sqrt(4 * s * s - 4 * t * (m - s * n)))) // (2 * t)

    xt1 = n - 2 * yt1
    xt2 = n - 2 * yt2

    res = float("inf")
    for x in range(min(xt1, xt2), max(xt1, xt2)):
        for y in range(min(yt1, yt2), max(yt1, yt2)):
            if s * x + t * y * y <= m and x + 2 * y == n:
                res = min(res, u * x + v * y)

    print(res)

if __name__ == '__main__':
    n, u, v, s, t, m = list(map(int, sys.stdin.readline().strip().split()))

    test02(n, u, v, s, t, m)
