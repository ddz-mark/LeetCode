# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        if nums == []:
            return res

        if len(nums) <= k:
            return [max(nums)]

        for i in range(0, len(nums) - k + 1):
            res.append(max(nums[i:i + k]))

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
