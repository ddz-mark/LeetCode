# -*- coding: utf-8 -*-
# @Time : 2025/5/22 14:05
# @Author : ddz
from typing import List


# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
# 二、示例
# 2.1> 示例 1：
#
# 【输入】nums = [1,1,1], k = 2
# 【输出】2
#
# 2.2> 示例 2：
#
# 【输入】nums = [1,2,3], k = 3
# 【输出】2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 思路：使用前缀和+hash表优化， 前缀和mp[i]代表i之前的数字之和，则mp[j]-mp[i]代表i到j之间的数字子和
        # 添加mp[pre-k]是担心有负数
        count = 0
        pre = 0
        # 前缀和，初始化哈希表，前缀和为0出现过1次
        mp = {0: 1}
        for i in range(len(nums)):
            pre += nums[i]
            # 检查是否存在 pre - k 的前缀和
            if pre - k in mp.keys():
                count += mp[pre - k]
            # 更新当前前缀和的出现次数
            mp[pre] = mp.get(pre, 0) + 1
        return count
