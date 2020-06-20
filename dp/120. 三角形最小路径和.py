# -*- coding: utf-8 -*-
# @Time : 2020/6/16 10:29 下午
# @Author : ddz
# 166
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 思路一：递归超时
        # if triangle == []:
        #     return 0
        #
        # def dfs(i, j):
        #     # 递归：先写结束条件
        #     if i == len(triangle) - 1:
        #         return triangle[i][j]
        #
        #     res = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
        #     return res
        #
        # return dfs(0, 0)

        # 思路二：从下往上，通过空间换时间，在原数组上进行修改
        if triangle == []:
            return 0
        rows = len(triangle)
        for i in range(rows - 2, -1, -1):
            cols = len(triangle[i])
            for j in range(cols):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    ob = Solution()
    print(ob.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
