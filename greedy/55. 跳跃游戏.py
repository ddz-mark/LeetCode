# -*- coding: utf-8 -*-
# @Time : 2025/5/7 19:58
# @Author : ddz
from typing import List


# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

# 示例 2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 思路：只要存在一个位置 x，它本身可以到达，并且它跳跃的最大长度为 x+nums[x]，这个值大于等于 y，即 x+nums[x]≥y
        n = len(nums)
        max_length = 0
        for index in range(n):
            # 在当前最大长度里面
            if index <= max_length:
                # 更新最大长度
                max_length = max(max_length, index + nums[index])
                if max_length >= n-1:
                    return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.canJump([2, 3, 1, 1, 4]))
