# -*- coding: utf-8 -*-
# @Time : 2020/6/17 11:29 下午
# @Author : ddz
# 168
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 回溯超时
        # rows, cols = len(grid), len(grid[0])
        #
        # def dfs(i, j):
        #
        #     # 递归：先写结束条件
        #     if i == rows - 1 and j == cols - 1:
        #         return grid[i][j]
        #
        #     if 0 <= i < rows and 0 <= j < cols:
        #         return grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
        #     else:
        #         return float('inf')
        #
        # return dfs(0, 0)

        # 动态规划：思路跟三角形最小路径和一样，通过空间换时间
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                # 最后一行
                elif i == rows - 1:
                    grid[i][j] += grid[i][j + 1]
                # 最后一列
                elif j == cols - 1:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]


if __name__ == '__main__':
    ob = Solution()
    print(ob.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
