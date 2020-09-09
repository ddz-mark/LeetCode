# -*- coding: utf-8 -*-
# @Time : 2020/9/7 2:59 下午
# @Author : ddz

import sys
import math


def test(n, m, ai, pi):

    total = 0
    i = 0
    j = 1
    shengyu = 0
    while j < n:
        # print('i, j', i, j)
        if pi[i] < pi[j]:
            if j == n-1:
                total += (math.ceil((sum(ai[i:]) / m)) * pi[i])
        else:
            total += (math.ceil((sum(ai[i:j] + shengyu) / m)) * pi[i])
            shengyu = sum(ai[i:j]) - (math.ceil((sum(ai[i:j] + shengyu) / m)) * pi[i])

            i = j

        j += 1


    print(total)


if __name__ == '__main__':
    # n, m = 3, 2
    # ai = [10, 1, 2]
    # pi = [5, 1, 1000]
    # test(n, m, ai, pi)
# 3 2
# 10 1 2
# 5 1 1000

    line1 = sys.stdin.readline().strip()
    n, m = list(map(int, line1.split()))
    line2 = sys.stdin.readline().strip()
    ai = list(map(int, line2.split()))
    line3 = sys.stdin.readline().strip()
    pi = list(map(int, line3.split()))
    test(n, m, ai, pi)