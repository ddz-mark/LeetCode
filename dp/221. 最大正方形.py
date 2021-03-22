# -*- coding: utf-8 -*-

# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # 思路：使用dp方式，设dp[i][j]为以（i，j）为右下角的正方形最大边长
        # 转移方程为：
        # 1. matrix[i][j]=1时，dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
        # 2. matrix[i][j]=0时，dp[i][j]=0
        # 3. 边界条件 i=0 或者 j=0 时，dp[i][j] = matrix[i][j]

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare
