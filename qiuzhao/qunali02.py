# -*- coding: utf-8 -*-
# @Time : 2020/9/23 8:15 下午
# @Author : ddz

import sys


def test(s1, s2):
    n = len(s1)

    dp = [[0] * (n + 1)] * (n + 1)
    # print(dp)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][n])


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    s1 = sys.stdin.readline().strip().split()
    s2 = sys.stdin.readline().strip().split()

    test(s1, s2)
