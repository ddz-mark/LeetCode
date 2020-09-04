# -*- coding: utf-8 -*-
import sys

def test(l):
    n = len(l)
    if n == 0:
        return 0
    dp = [l[0]] * n
    for i in range(1, n):
        dp[i] = max(dp[i-1] + l[i], l[i])

    print(max(dp))


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split(',')))
    # values = [1, 2, -5, 3, 4]
    test(values)