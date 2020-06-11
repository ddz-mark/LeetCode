# -*- coding: utf-8 -*-
# @Time : 2020/6/6 3:13 下午
# @Author : ddz
# 163


class Solution(object):

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(matrix)
        if rows == 0:
            return []

        cols = len(matrix[0])
        res1 = set()
        res2 = set()

        def dfs(i, j, res):
            res.add((i, j))

            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] >= matrix[i][j] and (x, y) not in res:
                    dfs(x, y, res)

        for j in range(cols):
            # 太平洋 第一行
            dfs(0, j, res1)

            # 大西洋 最后一行
            dfs(rows - 1, j, res2)

        # 太平洋 第一列
        for i in range(rows):
            # 太平洋 第一列
            dfs(i, 0, res1)

            # 大西洋 最后一列
            dfs(i, cols - 1, res2)

        return ([list(i) for i in res1.intersection(res2)])


if __name__ == '__main__':
    ob = Solution()
    matrix = [[1, 2, 2, 3, 5],
              [3, 2, 3, 4, 4],
              [2, 4, 5, 3, 1],
              [6, 7, 1, 4, 5],
              [5, 1, 1, 2, 4]]
    print(ob.pacificAtlantic(matrix))
