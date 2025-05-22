# -*- coding: utf-8 -*-
# @Time : 2025/5/22 15:15
# @Author : ddz
from typing import List


# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
# 示例 1:
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 思路：一维动态规划，保留之前的最大值，与当前值相乘，因为有负数，则把最小值也保留下
        # 对比：最大、最小值 与 当前值的乘积
        if not nums:
            return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]

        for num in nums[1:]:
            # 对比：最大、最小值 与 当前值的乘积
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            # 对比结果res
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProduct([2, 3, -2, 4]))
