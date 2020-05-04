# -*- coding: utf-8 -*-
# @Time : 2020/4/27 4:31 下午
# @Author : ddz

# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 思路一：双指针 + 滑动窗口
        res = len(nums) + 1
        low = total = 0
        for i, v in enumerate(nums):
            total += v
            while total >= s:
                res = min(res, i - low + 1)
                total -= nums[low]
                low += 1
        return 0 if res == len(nums) + 1 else res


if __name__ == '__main__':
    ob = Solution()
    print(ob.minSubArrayLen(15, [1, 2, 3, 4, 5]))
