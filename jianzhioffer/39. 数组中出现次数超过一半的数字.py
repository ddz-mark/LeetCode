# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2


import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(collections.Counter(nums))
        # print(dic)
        for i, v in dic.items():
            if v == max(dic.values()):
                return i

if __name__ == '__main__':
    ob = Solution()
    print(ob.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
