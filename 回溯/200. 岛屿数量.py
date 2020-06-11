# -*- coding: utf-8 -*-
# @Time : 2020/6/1 10:45 下午
# @Author : ddz

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1


class Solution(object):

    def dfs(self, i, j, rows, cols, grid):

        # 递归：先写结束条件
        grid[i][j] = 0

        # 上下左右递归处理
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                self.dfs(x, y, rows, cols, grid)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        # print(rows, cols)

        res_num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res_num += 1
                    self.dfs(i, j, rows, cols, grid)
        return res_num


if __name__ == '__main__':
    ob = Solution()
    data = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(ob.numIslands(data))
