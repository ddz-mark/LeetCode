# 统计一个数字在排序数组中出现的次数。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0


# 思路一：正常循环
# 思路二：二分查找

import collections


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 思路一：
        # return collections.Counter(nums).get(target) if collections.Counter(nums).get(target) else 0

        # 思路二：
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        right_final = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left_final = right

        return right_final - left_final - 1



if __name__ == '__main__':
    ob = Solution()
    print(ob.search([5, 7, 7, 8, 8, 10], 8))
