# -*- coding: utf-8 -*-
# @Time : 2020/5/30 1:56 下午
# @Author : ddz

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = list()

        def dfs(first=1, curr=[]):

            # 递归：先写结束条件
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(first, n+1):
                curr.append(i)
                dfs(i+1, curr)
                curr.pop()

        dfs(1)
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.combine(4, 2))
