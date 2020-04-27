# -*- coding: utf-8 -*-
# @Time : 2020/4/27 10:28 上午
# @Author : ddz

# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 你不需要考虑数组中超出新长度后面的元素。


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 思路一：删除数组
        # i = 0
        # while i < len(nums):
        #
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i += 1
        #
        # return len(nums)

        # 思路二：双指针
        j = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[j] = v
                j += 1

        return j


if __name__ == '__main__':
    ob = Solution()
    print(ob.removeElement([3, 2, 2, 3], 2))
