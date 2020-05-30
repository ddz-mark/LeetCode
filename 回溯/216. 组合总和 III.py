# -*- coding: utf-8 -*-
# @Time : 2020/5/30 4:14 下午
# @Author : ddz

# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        candidates = [i for i in range(1, 10)]

        def dfs(combination, tartget, candidates):
            # 递归：先写结束条件
            if len(combination) == k and tartget == 0:
                res.append(combination)
                return

            for v in candidates:
                dfs(combination + [v], tartget - v, candidates[candidates.index(v) + 1:])

        dfs([], n, candidates)
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.combinationSum3(3, 9))
