# -*- coding: utf-8 -*-
# @Time : 2025/5/30 16:02
# @Author : ddz
from typing import List


# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路：由于矩阵的每一行是递增的，且每行的第一个数大于前一行的最后一个数，如果把矩阵每一行拼在一起，我们可以得到一个递增数组。
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            # 关键点，对当前值求横纵坐标
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False


if __name__ == '__main__':
    obj = Solution()
    obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
