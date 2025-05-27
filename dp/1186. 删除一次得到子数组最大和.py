# -*- coding: utf-8 -*-
# @Time : 2025/5/27 17:14
# @Author : ddz
from typing import List


# 给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
#
# 注意，删除一个元素后，子数组 不能为空。
#
#
#
# 示例 1：
#
# 输入：arr = [1,-2,0,3]
# 输出：4
# 解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
# 示例 2：
#
# 输入：arr = [1,-2,-2,3]
# 输出：3
# 解释：我们直接选出 [3]，这就是最大和。
# 示例 3：
#
# 输入：arr = [-1,-1,-1,-1]
# 输出：-1
# 解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
#      我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 思路：定义两个动态规划的数组
        # 第一个no_skip：没有跳过，递推公式为no_skip = max(nums[i], no_skip + nums[i])
        # 第二个skip：有两种情况，一是当前值跳过，则为前面的no_skip，另一个是前面的值跳过，当前值必须加
        #           skip = max(no_skip_prev, skip + nums[i])

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        no_skip = nums[0]
        skip = 0
        max_sum = nums[0]

        for i in range(1, n):
            # 保存前一个 no_skip，因为 skip 的计算需要用到
            no_skip_prev = no_skip
            # 更新 no_skip
            no_skip = max(nums[i], no_skip + nums[i])
            # 更新 skip
            skip = max(no_skip_prev, skip + nums[i])
            # 更新全局最大值
            current_max = max(no_skip, skip)
            if current_max > max_sum:
                max_sum = current_max

        return max_sum
