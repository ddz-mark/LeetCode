# -*- coding: utf-8 -*-
# @Time : 2025/6/3 12:28
# @Author : ddz
from typing import List


# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 思路：广度优先遍历
        rows, cols, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, time))

        # bfs：使用队列实现
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < rows and 0 <= j + dj < cols and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))
        for row in grid:
            if 1 in row:
                return -1
        return time


if __name__ == '__main__':
    obj = Solution()
    print(obj.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
