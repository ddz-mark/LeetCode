# -*- coding: utf-8 -*-
# @Time : 2020/6/1 10:34 下午
# @Author : ddz

# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false


class Solution(object):
    def judge(self, matrix, rows, cols, i, j, word, mask_matirx):

        if not word:
            return True
        # 判断条件，如果越界或者不相等或者已经走过了
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != word[0] or mask_matirx[i][j] == True:
            return False

        mask_matirx[i][j] = True

        # 检查上下左右是否存在路径
        if (self.judge(matrix, rows, cols, i - 1, j, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i + 1, j, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i, j - 1, word[1:], mask_matirx) or
                self.judge(matrix, rows, cols, i, j + 1, word[1:], mask_matirx)):
            return True

        # 第一个是，但是上下左右不是，则设置未走过
        mask_matirx[i][j] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)  # 行数
        cols = len(board[0])  # 列数
        # memo = [[1] * m for i in range(n)]
        mask_matirx = [[False] * cols for _ in range(rows)]
        # print(mask_matirx)
        for i in range(rows):
            for j in range(cols):
                if self.judge(board, rows, cols, i, j, word, mask_matirx):
                    return True
        return False


if __name__ == '__main__':
    ob = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(ob.exist(board, "ABCB"))
