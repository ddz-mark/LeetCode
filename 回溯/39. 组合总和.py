# -*- coding: utf-8 -*-
# @Time : 2020/5/30 3:25 下午
# @Author : ddz
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(combination, target):
            # 递归：先写判断条件
            if target == 0:
                res.append(combination[:])
                return
            elif target < 0:
                return
            else:
                for v in candidates:
                    # 由于一定是小的数在前面，
                    if combination and combination[-1] > v:  # 防止重复的方法是,不让其找在当前元素以前的元素
                        continue
                    dfs(combination + [v], target - v)

        dfs([], target)

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.combinationSum([2, 3, 5], 8))
