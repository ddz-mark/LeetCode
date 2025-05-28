# -*- coding: utf-8 -*-
# @Time : 2020/10/15 8:25 下午
# @Author : ddz

# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，
# 假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
#
# 示例1:
#  输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
#  输出: 8（元素5在该数组中的索引）
#
# 示例2:
#  输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
#  输出：-1 （没有找到）


class Solution(object):
    def search(self, nums, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 在 A1 数组中
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 在 A2 数组中
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    ob = Solution()
    print(ob.search([4, 5, 6, 7, 0, 1, 2], 0))
