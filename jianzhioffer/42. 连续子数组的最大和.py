# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        max_num, current_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i] + current_sum, nums[i])
            max_num = max(max_num, current_sum)

        return max_num


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
