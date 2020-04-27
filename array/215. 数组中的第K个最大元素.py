# -*- coding: utf-8 -*-
# @Time : 2020/4/27 1:18 下午
# @Author : ddz

# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4

# 思路一：快排思路
# 思路二：堆排序
import heapq


class Solution(object):
    # 思路一
    # def division(self, left, right, nums):
    #
    #     base = nums[left]
    #     while left < right:
    #
    #         while base <= nums[right] and left < right:
    #             right -= 1
    #         nums[left] = nums[right]
    #
    #         while base >= nums[left] and left < right:
    #             left += 1
    #         nums[right] = nums[left]
    #
    #     nums[left] = base
    #
    #     return left
    #
    # def quickSort(self, left, right, nums, k):
    #     if left < right:
    #         base = self.division(left, right, nums)
    #         if len(nums) - base > k:
    #             return self.quickSort(base + 1, right, nums, k)
    #         elif len(nums) - base < k:
    #             return self.quickSort(left, base - 1, nums, k)
    #         else:
    #             return nums[base]
    #     else:
    #         return nums[left]
    #
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     return self.quickSort(0, len(nums) - 1, nums, k)

    # 思路二：
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    ob = Solution()
    nums = [3, 1, 2, 4, 6, 5]
    print(ob.findKthLargest(nums, 2))
