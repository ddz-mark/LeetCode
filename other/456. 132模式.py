# -*- coding: utf-8 -*-
# @Time : 2020/10/14 11:00 下午
# @Author : ddz

# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
# 设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
# 注意：n 的值小于15000。
#
# 示例1:
# 输入: [1, 2, 3, 4]
# 输出: False
# 解释: 序列中不存在132模式的子序列。
#
# 示例 2:
# 输入: [3, 1, 4, 2]
# 输出: True
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

# 思路：1、维护一个最小前缀值的数组，即aj对应的最小M1
#      2、因为有了前缀最小值，所以我们可以很快判断aj和M1的关系，接下来的任务就是找M2。
#       首先可以想到暴力解，遍历[j+1]到n的每一个数，时间复杂度是O(n^2)，那么有什么办法可以优化这部分，
#       我们可以从数组尾部开始向前维护一个单调递减栈，对于每一个aj，如果aj>M1，然后在当前栈中找比M1大的最小值，
#       即以M1为最小标准值来维护这个递减栈之后的栈顶元素，如果栈顶元素小于aj，即找到我们所需要的情况


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        le = len(nums)
        if le < 2:
            return False

        mi = [nums[0]]
        for i in range(1, le):
            mi.append(min(nums[i], mi[-1]))

        stack = []
        for i in range(le - 1, -1, -1):
            if nums[i] > mi[i]:
                while stack and mi[i] >= stack[-1]:
                    stack.pop()

                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


if __name__ == '__main__':
    ob = Solution()
    print(ob.find132pattern([3, 1, 4, 2]))
