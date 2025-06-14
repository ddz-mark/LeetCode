# -*- coding: utf-8 -*-
# @Time : 2025/6/5 11:20
# @Author : ddz
from typing import List


# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
#
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
# 示例 1：
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 思路：最后high的元素进行判断，如果<nums[high]，往左移，否则往右移
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = (high + low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]


if __name__ == '__main__':
    obj = Solution()
    obj.findMin([3, 4, 5, 1, 2])
