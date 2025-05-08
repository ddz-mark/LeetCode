# -*- coding: utf-8 -*-
# @Time : 2025/5/8 20:23
# @Author : ddz
from typing import List


# 给你一个整数数组 nums 和一个 正整数 k 。
#
# 请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
#
# 子数组是数组中的一个连续元素序列。
# 示例 1：
#
# 输入：nums = [1,3,2,3,3], k = 2
# 输出：6
# 解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
# 示例 2：
#
# 输入：nums = [1,4,2,1], k = 3
# 输出：0
# 解释：没有子数组包含元素 4 至少 3 次。

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 思路：滑动窗口，使用left和right两个指针，使用cnt计数最大值数量
        # 首先，不断移动 right，直到 cnt == k，然后向右移动left，
        # 在左指针移动过程中，滑动窗口的所有子数组，即右端点为 right 且左端点小于 left 的子数组，都包含至少 k 个 mx，因此我们可以把答案增加 left

        max_num = max(nums)
        res = 0
        cnt = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                cnt += 1

            # 满足 cnt == k时，开始右移left
            while cnt == k:
                if nums[left] == max_num:
                    cnt -= 1
                left += 1
            print("left", left)
            # 这里关注下：后面的left是包含前面的left内容的，因为后续满足大于K,再加上前面部分也一定大于K
            res += left

        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.countSubarrays([1, 3, 2, 3, 3], k=2))
    # print(obj.countSubarrays([1, 4, 2, 1], k=3))
