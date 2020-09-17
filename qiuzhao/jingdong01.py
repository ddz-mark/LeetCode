# -*- coding: utf-8 -*-
# @Time : 2020/9/17 8:18 下午
# @Author : ddz

import sys


def test(n, p, grid):
    dp = [0 for _ in range(p + 1)]

    for i in range(n):
        for j in range(p, -1, -1):
            k = min(j // grid[i][1], grid[i][0])
            dp[j] = max([dp[j - x * grid[i][1]] + x * grid[i][2] for x in range(k + 1)])
    print(dp[-1])


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, p = list(map(int, line.split()))

    grid = []
    for _ in range(n):
        line1 = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line1.split()))
        grid.append(values)

    test(n, p, grid)
