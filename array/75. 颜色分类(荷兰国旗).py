# -*- coding: utf-8 -*-
# @Time : 2020/4/27 1:01 下午
# @Author : ddz

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]

# 荷兰国旗问题思路：p0，p2 分别是 0 的右边界和 2 的左边界
# 当前值如果为 0,则与 p0 互换，如果为 2，则与 p2 互换

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p0, cur = 0, 0
        p2 = len(nums) - 1

        while cur <= p2:

            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1

        return nums


if __name__ == '__main__':
    ob = Solution()
    print(ob.sortColors([2, 0, 2, 1, 1, 0]))
