# -*- coding: utf-8 -*-
# @Time : 2021/9/5 下午7:54
# @Author : ddz
import itertools
import sys


def pow(x, n):
    if x == 0 and n < 0:
        return

    def inner_pow(N):
        if N == 0:
            return 1.0
        y = inner_pow(N // 2)
        if N % 2 == 0:
            return y * y
        else:
            return y * y * x

    return inner_pow(n) if n >= 0 else 1 / inner_pow(-n)


def test01(n, m, w, A):

    res = [[str(-1)] * 2 for _ in range(m)]
    for v1, v2 in list(itertools.permutations(w, 2)):
        mi = pow(v1, v2)
        if mi in A:
            res[A.index(mi)] = [str(v1), str(v2)]

    for v in res:
        print(" ".join(list(v)))


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, m = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    w = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    A = list(map(int, line3.split()))

    test01(n, m, w, A)
# 3 3
# 2 3 4
# 4 9 16
