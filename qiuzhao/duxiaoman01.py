# -*- coding: utf-8 -*-

import sys


def test(rows, cols, matrix):
    def dfs(i, j, mask):

        # 递归：返回条件
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return 0

        if matrix[i][j] == '#' or mask[i][j] == True:
            return float('inf')

        mask[i][j] = True

        up = dfs(i - 1, j, mask)
        down = dfs(i + 1, j, mask)
        left = dfs(i, j - 1, mask)
        right = dfs(i, j + 1, mask)
        if matrix[i][j] == '*':
            return 1 + min(up, down, left, right)
        else:
            return min(up, down, left, right)

    mask = [[False] * cols for _ in range(rows)]
    i, j = 0, 0
    while i < rows:
        if '@' in matrix[i]:
            j = matrix[i].index('@')
            break
        i += 1

    up = dfs(i - 1, j, mask)
    mask = [[False] * cols for _ in range(rows)]
    down = dfs(i + 1, j, mask)
    mask = [[False] * cols for _ in range(rows)]
    left = dfs(i, j - 1, mask)
    mask = [[False] * cols for _ in range(rows)]
    right = dfs(i, j + 1, mask)
    # print('----------')

    res = min(up, down, left, right)
    if str(res) == 'inf':
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        rows, cols = list(map(int, line.split()))
        matrix = []
        for _ in range(rows):
            line1 = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            matrix.append(list(line1))

        test(rows, cols, matrix)
