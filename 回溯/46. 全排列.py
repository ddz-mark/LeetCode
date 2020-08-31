# -*- coding: utf-8 -*-
# @Time : 2020/5/30 11:37 上午
# @Author : ddz

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 思路：回溯法
        n = len(nums)
        res = []

        def dfs(x):
            # 递归：先写结束条件
            if x == n - 1:
                res.append(nums[:])
            # dic = set()
            for i in range(x, n):

                # 去重
                # if nums[i] in dic:
                #     continue
                # dic.add(nums[i])

                nums[x], nums[i] = nums[i], nums[x]
                dfs(x + 1)
                # 还原数组，重新进行替换
                nums[x], nums[i] = nums[i], nums[x]

        dfs(0)
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.permute([1, 2, 2]))
