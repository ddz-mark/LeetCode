# -*- coding: utf-8 -*-
# @Time : 2020/5/4 12:32 下午
# @Author : ddz
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 思路一：库函数
        # res = []
        # for i in range(0, num + 1):
        #     res.append(bin(i).count('1'))
        # return res

        # 动态规划，规律为：
        # 1. dp[i] = dp[i - 1] + 1 # i 是奇数
        # 2. dp[i] = dp[i // 2] # i 是偶数

        dp = [0] * (num + 1)
        for i in range(0, num + 1):

            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1

        return dp


if __name__ == '__main__':
    ob = Solution()
    print(ob.countBits(2))
