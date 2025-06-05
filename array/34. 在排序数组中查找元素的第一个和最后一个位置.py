# -*- coding: utf-8 -*-
# @Time : 2025/6/5 09:51
# @Author : ddz
from typing import List


# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]


class Solution:
    def lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 思路：使用 target+1 代表大于target的第一位，然后下标-1就可以了
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 先找到这个数的右边相邻数字，也就是 >target 的第一个数，在所有数都是整数的前提下，>target 等价于 ≥target+1
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]


if __name__ == '__main__':
    obj = Solution()
    obj.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
