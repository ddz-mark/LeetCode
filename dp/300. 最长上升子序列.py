# -*- coding: utf-8 -*-
# @Time : 2020/6/16 11:01 下午
# @Author : ddz
# 167

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 思路一：动态规划
        # dp[i] 是前 i 个元素的最长上升子序列
        # 递推公式是：dp[i] = max(dp[0],dp[1]...dp[j]...dp[i-1]) + 1，并且 nums[j] < nums[i]
        # 最后 max(dp[i])
        if nums == []:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    ob = Solution()
    print(ob.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
