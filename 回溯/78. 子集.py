# -*- coding: utf-8 -*-
# @Time : 2020/5/30 4:24 下午
# @Author : ddz
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # res = []

        # def dfs(combination, k, candidates):
        #     # 递归：先写判断条件
        #     if len(combination) == k:
        #         res.append(combination[:])
        #         return
        #     else:
        #         for v in candidates:
        #             dfs(combination + [v], k, candidates[candidates.index(v) + 1:])

        # for i in range(len(nums) + 1):
        #     dfs([], i, nums)
        # return res

        # 回溯法：
        res = []

        def recur(index, tmp):
            # 结束条件
            res.append(tmp)
            for i in range(index, len(nums)):
                #
                recur(i + 1, tmp + [nums[i]])

        recur(0, [])
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.subsets([1, 2, 3]))
