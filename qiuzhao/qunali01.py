# -*- coding: utf-8 -*-
# @Time : 2020/9/23 8:07 下午
# @Author : ddz

import sys
import math


def test(n, m):
    # 思路一
    # print(math.factorial(n) // (math.factorial(m) * math.factorial(n - m)))

    # 思路二
    if m > n / 2:
        m = n - m
    res = 1
    for _ in range(m):
        res *= n
        n -= 1

    for i in range(m):
        res = res // (i + 1)
    print(res)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    test(n, m)
