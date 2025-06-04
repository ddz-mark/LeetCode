# -*- coding: utf-8 -*-
# @Time : 2020/5/30 4:40 下午
# @Author : ddz

# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
# 示例 1：
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # res = []
        #
        # def dfs(combination, k, candidates):
        #     # 递归：先写判断条件
        #     if len(combination) == k:
        #         if combination[:] not in res:
        #             res.append(combination[:])
        #         return
        #     else:
        #         for v in candidates:
        #             dfs(combination + [v], k, candidates[candidates.index(v) + 1:])
        #
        # nums = sorted(nums)
        # for i in range(len(nums) + 1):
        #     dfs([], i, nums)
        # return res

        res = []

        def recur(index, tmp):
            # 结束条件：避免重复
            if tmp not in res:
                res.append(tmp)
            for i in range(index, len(nums)):
                recur(i + 1, tmp + [nums[i]])

        nums = sorted(nums)
        recur(0, [])
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.subsetsWithDup([4, 4, 4, 1, 4]))
