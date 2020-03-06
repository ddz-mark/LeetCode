
# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        '''矩阵转置'''
        for x in range(n):
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        '''转置后列变换'''
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])//2):
        #         matrix[i][j],matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]