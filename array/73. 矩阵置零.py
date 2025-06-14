# -*- coding: utf-8 -*-
# @Time : 2025/6/4 17:13
# @Author : ddz
from typing import List


# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 思路1：O(mn)，使用row和col两个数组进行标记
        # m, n = len(matrix), len(matrix[0])
        # row, col = [False] * m, [False] * n
        #
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row[i] = col[j] = True
        # for i in range(m):
        #     for j in range(n):
        #         if row[i] or col[j]:
        #             matrix[i][j] = 0

        # 思路2:使用两个标记变量
        # 可以用矩阵的第一行和第一列代替方法一中的两个标记数组，以达到 O(1) 的额外空间。
        # 但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 0。因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 0。
        # m, n = len(matrix), len(matrix[0])
        # # 1. 记录第一行和第一列有没有0
        # flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        # flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        #
        # # 2. 使用第一行和第一列记录 0
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = matrix[0][j] = 0
        # # 3. 根据上面的标记设置为0
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        # # 4. 根据第一行和第一列的记录设置相关值
        # if flag_col0:
        #     for i in range(m):
        #         matrix[i][0] = 0
        # if flag_row0:
        #     for j in range(n):
        #         matrix[0][j] = 0

        # 思路3: 思路2的优化，使用1个标记变量
        # 只使用一个标记变量记录第一列是否原本存在 0。这样，第一列的第一个元素即可以标记第一行是否出现 0。
        # 但为了防止每一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素。
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False

        for i in range(m):
            # 1. 记录第一列有没有0
            if matrix[i][0] == 0:
                flag_col0 = True
            # 2. 使用第一行和第一列记录 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 3. 倒序处理
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0


if __name__ == '__main__':
    obj = Solution()
    obj.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
