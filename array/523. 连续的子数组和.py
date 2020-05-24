# -*- coding: utf-8 -*-
# @Time : 2020/5/23 8:49 下午
# @Author : ddz

# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，
# 即总和为 n*k，其中 n 也是一个整数。
#
# 示例 1:
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
#
# 示例 2:
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 思路一：暴力解法优化，通过 动态规划 dp: dp[i]=dp[i-1]+nums[i]
        # 所以暴力解法中：sum = dp[j]-dp[i]+nums[i]
        # 然后优化暴力解法
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = dp[j] - dp[i] + nums[i]
                if k == 0:
                    if sum == 0:
                        return True
                else:
                    if sum % k == 0:
                        return True
        return False


if __name__ == '__main__':
    ob = Solution()
    print(ob.checkSubarraySum([23, 2, 6, 4, 7], 0))
