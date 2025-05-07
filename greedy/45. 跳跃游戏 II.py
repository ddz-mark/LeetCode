# -*- coding: utf-8 -*-
# @Time : 2025/5/7 20:38
# @Author : ddz
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
from typing import List


# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 思路：贪心算法，每次找到可到达的最远位置记为边界，从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

        n = len(nums)
        end, step = 0, 0
        max_length = 0

        for index in range(n-1):
            # 更新最大长度
            max_length = max(max_length, index + nums[index])
            # 如果到达边界，则进行下一次跳
            if index == end:
                end = max_length
                step += 1
        return step


if __name__ == '__main__':
    obj = Solution()
    print(obj.jump([2, 3, 1, 1, 4]))
