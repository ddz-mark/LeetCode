# -*- coding: utf-8 -*-
# @Time : 2025/5/21 12:00
# @Author : ddz
from typing import List


# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
#
# 输入：nums = [1,0,1,2]
# 输出：3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 思路：先对每个数都判断一次这个数是不是连续序列的开头那个数，用set实现
        # 如果是开头的数，则通过while遍历
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # 判断是不是开头的数字，不存在则表达是开头
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # while循环：直到连续数字结束
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))
