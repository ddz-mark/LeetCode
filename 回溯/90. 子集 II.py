# -*- coding: utf-8 -*-
# @Time : 2020/5/30 4:40 下午
# @Author : ddz


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def dfs(combination, k, candidates):
            # 递归：先写判断条件
            if len(combination) == k:
                if combination[:] not in res:
                    res.append(combination[:])
                return
            else:
                for v in candidates:
                    dfs(combination + [v], k, candidates[candidates.index(v) + 1:])

        nums = sorted(nums)
        for i in range(len(nums) + 1):
            dfs([], i, nums)
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.subsetsWithDup([4, 4, 4, 1, 4]))
