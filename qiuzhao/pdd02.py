# -*- coding: utf-8 -*-

import sys


def test(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = flag = 0

    def dfs(i, j, rows, cols, mask):
        count = 0
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1' and mask[i][j] == False:
            mask[i][j] = True
            count = 1 + dfs(i - 1, j, rows, cols, mask) + dfs(i + 1, j, rows, cols, mask) \
                    + dfs(i, j - 1, rows, cols, mask) + dfs(i, j + 1, rows, cols, mask)

        return count

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                mask = [[False] * cols for _ in range(rows)]
                grid[i][j] = '1'
                res = max(res, dfs(i, j, rows, cols, mask))
                grid[i][j] = '0'
            else:
                flag += 1

    if res >= flag:
        print(res - 1)
    else:
        print(res)


if __name__ == '__main__':
    # line1 = sys.stdin.readline().strip()
    # n, m = list(map(int, line1.split()))
    # ans = []
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = line.split()
    #     ans.append(values)

    # print(ans)
    ans = [['1', '0', '1', '1'],
           ['1', '1', '0', '1'],
           ['0', '0', '0', '0'],
           ['1', '1', '1', '1']]
    test(ans)
