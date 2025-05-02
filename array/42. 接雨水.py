# -*- coding: utf-8 -*-
# @Time : 2025/4/30 17:29
# @Author : ddz
from typing import List


# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

class Solution:
    def trap(self, height: List[int]) -> int:

        # 解法一：
        # 每个index位置的储水量等于 min(左边的最大值， 右边的最大值) - height[index]
        # left_max 代表0到left的最大值，right_max 代表right到结尾处的最大值
        # height     =[0,1,0,2,1,0,1,3,2,1,2,1]
        # left_max   =[0,0,1,1,2,2,2,2,3,3,3,3]
        # right_max  =[3,3,3,3,3,3,3,2,2,2,1,0]
        # min        =[0,0,1,1,2,2,2,2,2,2,1,0]
        # 每个位置储水量=[0,0,1,0,1,2,1,0,0,1,0,0] = sum=6

        # 解法二：双指针，木桶原理以最短边为准，如果当前点的left_max<right_max，则肯定以left_max作为Min，再减去height[index]
        left_max = right_max = 0
        # 左右指针
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += (left_max - height[left])
                left += 1
            else:
                ans += (right_max - height[right])
                right -= 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
