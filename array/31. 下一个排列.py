# -*- coding: utf-8 -*-
# @Time : 2025/4/30 14:04
# @Author : ddz
from typing import List


# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [4, 5, 2, 6, 3, 1] 找出较小数2（靠右），再找出比2的较大数3（靠右），变成[4,5,3,6,2,1]，再把[6,2,1]升序为[1,2,6]即可
        # 思路：1. 找出较小数2，判断nums[i]<nums[i+1]，从后往前，则nums[i]为较小数
        # 2. 找出较大数3，从后往前>nums[i]的第一个数为较大数nums[j]
        # 3. 交换i,j位置，对i+1到len的数组升序即可

        # 找出较小数
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 避免排列已经为最大值情况
        if i >= 0:
            j = len(nums) - 1
            # 找出较大数
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 原地排序 i+1 之后的数组
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    obj = Solution()
    # obj.nextPermutation(nums=[4, 5, 2, 6, 3, 1])
    obj.nextPermutation(nums=[5, 1, 1])
