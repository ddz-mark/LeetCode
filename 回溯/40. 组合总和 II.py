# -*- coding: utf-8 -*-
# @Time : 2020/5/30 4:01 下午
# @Author : ddz
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
#
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(combination, target, candidates):
            # 递归：先写判断条件
            if target == 0:
                if combination not in res:
                    res.append(combination[:])
                return
            elif target < 0:
                return
            else:
                for v in candidates:
                    dfs(combination + [v], target - v, candidates[candidates.index(v) + 1:])

        dfs([], target, sorted(candidates))

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.combinationSum2([2, 5, 2, 1, 2], 5))
