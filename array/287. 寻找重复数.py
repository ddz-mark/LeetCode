# -*- coding: utf-8 -*-
# @Time : 2020/5/4 11:35 上午
# @Author : ddz

# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 思路一：直接比较
        # if nums == []:
        #     return 0
        #
        # for i, v in enumerate(nums):
        #     if i + 1 < len(nums) and v in nums[i + 1:]:
        #         return v

        # 思路二：二分法，按题目表达，设数组长度为 n，则数组中元素 ∈[1,n−1]，
        # 且只有一个重复元素。一个直观的想法，设一个数字 k∈[1,n−1]，统计数组中小于等于k的数字的个数count：
        # 若count <= k，说明重复数字一定在(k, n - 1]的范围内。
        # 若count > k，说明重复数字一定在[0, k]的范围内。
        left = 0
        right = len(nums) - 1
        while left < right:

            mid = (left + right) // 2
            count = 0
            for v in nums:
                if v <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    ob = Solution()
    print(ob.findDuplicate([3, 1, 3, 4, 2]))