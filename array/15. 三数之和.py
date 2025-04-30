# -*- coding: utf-8 -*-
# @Time : 2020/5/4 10:11 上午
# @Author : ddz

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 思路：排序 + 双指针，可以看出，一般数组的连续问题，大部分都用双指针解决。
        res = []
        # 数组排序
        nums = sorted(nums)
        n = len(nums)

        for i in range(n):
            # 比 0 大的情况直接返回
            if nums[i] > 0:
                return res
            # 相同数字的情况就跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 双指针
            left = i + 1
            right = n - 1
            while left < right:
                # 判断正好等于0
                if (nums[left] + nums[i] + nums[right]) == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 如果右边重复，往左移
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    # 如果左边重复，往右移
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 往中间移动
                    left += 1
                    right -= 1
                # 大于 0 的时候，右边往左移
                elif (nums[left] + nums[i] + nums[right]) > 0:
                    right -= 1
                # 小于0的时候，左边往右移
                else:
                    left += 1

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.threeSum([-1, 0, 1, 2, -1, -4]))
