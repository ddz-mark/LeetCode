# -*- coding: utf-8 -*-
# @Time : 2025/5/30 14:41
# @Author : ddz
from typing import List


# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路一：直接查找
        # for row in matrix:
        #     for element in row:
        #         if element == target:
        #             return True
        # return False

        # 思路二：二分法
        # 由于矩阵 matrix 中每一行的元素都是升序排列的，因此我们可以对每一行都使用一次二分查找，判断 target 是否在该行中，从而判断 target 是否出现。
        # 时间复杂度：O(mlogn)，每一行O(logn)
        # for row in matrix:
        #     l, r = 0, len(row) - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return False

        # 思路三：Z字形查找
        # 先从右上角(0, n-1)开始查找，当前值>target值时，列向量-1；当<target时，行向量+1
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


if __name__ == '__main__':
    obj = Solution()
    obj.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target=5)
