# -*- coding: utf-8 -*-
# @Time : 2020/6/6 1:59 下午
# @Author : ddz
# 记录：162

# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
# 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

# 思路：DFS，但是需要注意从边界出发搜索设为B，其余的设为X


class Solution(object):

    def dfs(self, i, j, rows, cols, board):

        board[i][j] = 'B'
        # 递归：先写结束条件
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and board[x][y] == 'O':
                self.dfs(x, y, rows, cols, board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        if rows == 0:
            return []
        cols = len(board[0])

        for j in range(cols):
            # 第一行
            if board[0][j] == 'O':
                self.dfs(0, j, rows, cols, board)
            # 最后一行
            if board[rows - 1][j] == 'O':
                self.dfs(rows - 1, j, rows, cols, board)

        for i in range(rows):
            # 第一列
            if board[i][0] == 'O':
                self.dfs(i, 0, rows, cols, board)
            # 最后一列
            if board[i][cols - 1] == 'O':
                self.dfs(i, cols - 1, rows, cols, board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'
        return board


if __name__ == '__main__':
    ob = Solution()
    print(ob.solve([["X", "O", "X", "O", "X", "O"],
                    ["O", "X", "O", "X", "O", "X"],
                    ["X", "O", "X", "O", "X", "O"],
                    ["O", "X", "O", "X", "O", "X"]]))
