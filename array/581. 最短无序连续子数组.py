# -*- coding: utf-8 -*-
# @Time : 2020/4/27 11:38 上午
# @Author : ddz

# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i < j and nums[i] <= min(nums[i + 1:]):
            i += 1
        while j > i and nums[j] >= max(nums[i:j]):
            j -= 1

        if i == j:
            return 0

        return j - i + 1


if __name__ == '__main__':
    ob = Solution()
    print(ob.findUnsortedSubarray([1, 2,3,4]))
