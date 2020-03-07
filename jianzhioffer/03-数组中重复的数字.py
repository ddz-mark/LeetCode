# 找出数组中重复的数字。
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
# 但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # hash 表法
        d = {}
        for i in nums:
            if d.get(i):
                return i
            d[i] = 1

        return -1

if __name__ == '__main__':
    ob = Solution()
    print(ob.findRepeatNumber([1, 0, 2, 5, 3]))