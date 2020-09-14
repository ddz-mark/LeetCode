# -*- coding: utf-8 -*-
# @Time : 2020/9/11 9:17 上午
# @Author : ddz


def test(rows, cols, grid):
    def dfs(i, j, rows, cols, grid, temp_list, mask):
        # 递归：先写结束条件
        if grid[i][j] == -1:
            mask[i][j] = True
        # 上下左右递归处理
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == -1 and mask[x][y] == False:
                dfs(x, y, rows, cols, grid, temp_list, mask)
            elif 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1:
                temp_list.append(grid[x][y])

    avg_list = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                mask = [[False] * cols for _ in range(rows)]
                temp_list = []
                dfs(i, j, rows, cols, grid, temp_list, mask)
                avg_list.append(temp_list)

    avg = [sum(v) // len(v) for v in avg_list]

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                grid[i][j] = avg[count]
                count += 1

    # 输出结果
    for row in grid:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    import sys

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    rows, cols = list(map(int, line.split()))
    grid = []
    for _ in range(rows):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        grid.append(list(map(int, line.split())))

    test(rows, cols, grid)
