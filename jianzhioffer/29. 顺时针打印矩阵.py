# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return res

        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        while True:

            for i in range(left, right):  # 从左到右
                res.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break

            for i in range(top, bottom):  # 从上到下
                res.append(matrix[i][right - 1])
            right -= 1
            if left >= right:
                break

            for i in range(right, left, -1):  # 从右到左
                res.append(matrix[bottom - 1][i - 1])
            bottom -= 1
            if top >= bottom:
                break

            for i in range(bottom, top, -1):  # 从下到上
                res.append(matrix[i - 1][left])
            left += 1
            if left >= right:
                break

        return res


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ob = Solution()
    print(ob.spiralOrder(matrix))
