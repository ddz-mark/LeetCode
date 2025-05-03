# -*- coding: utf-8 -*-
# @Time : 2025/5/2 23:15
# @Author : ddz
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        # 思路：从左到右遍历上侧元素、从上到下遍历右侧元素
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            # 从左到右遍历上侧元素
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            # 从上到下遍历右侧元素
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            # 防止单列情况，单列只需要上面两步即可
            if left < right and top < bottom:
                # if left<right，则从右到左遍历下侧元素
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                # if top<bottom，从下到上遍历左侧元素
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


if __name__ == '__main__':
    obj = Solution()
    # obj.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(obj.spiralOrder([[3], [2]]))
