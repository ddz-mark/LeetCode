# -*- coding: utf-8 -*-
# @Time : 2020/9/30 7:01 下午
# @Author : ddz

import sys


def test(grid, m, n):
    left, right, top, bottom = 0, n, 0, m

    matrxi = [[0] * n for _ in range(m)]
    length = 0
    while True:

        # 从左到右
        for i in range(left, right):
            matrxi[top][i] = grid[length]
            length += 1
        top += 1
        if top >= bottom:
            break

        # 从上到下
        for i in range(top, bottom):
            matrxi[i][right - 1] = grid[length]
            length += 1
        right -= 1
        if left >= right:
            break

        # 从右到左
        for i in range(right, left, -1):
            matrxi[bottom - 1][i - 1] = grid[length]
            length += 1
        bottom -= 1
        if top >= bottom:
            break

        # 从下到上
        for i in range(bottom, top, -1):
            matrxi[i - 1][left] = grid[length]
            length += 1
        left += 1
        if left >= right:
            break

    for v in matrxi:
        print(" ".join(map(str, v)))


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    m, n = list(map(int, line.split()))

    grid = []
    for _ in range(m):
        line1 = sys.stdin.readline().strip()
        values = list(map(int, line1.split()))

        grid.extend(values)
    # print(grid)

    test(sorted(grid), m, n)
# 4 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
