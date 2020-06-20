# -*- coding: utf-8 -*-
# @Time : 2020/6/6 9:32 下午
# @Author : ddz
# 165

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # 思路一：运用动态规划
        # F 表示所需要的最少硬币数
        # F(1) = min(F(1 - 1), F(1 - 2), F(1 - 5)) + 1
        # F(2) = min(F(2 - 1), F(2 - 2), F(2 - 5)) + 1
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0
        # # print(dp)
        #
        # for i in range(1, amount + 1):
        #     for j in range(len(coins)):
        #
        #         if i >= coins[j]:
        #             dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        #
        # if dp[amount] == amount +1:
        #     return -1
        # else:
        #     return dp[amount]

        #  思路二：优化思路一，避免不必要的计算
        f = [amount + 1] * (amount + 1)
        f[0] = 0
        for c in coins:  # 枚举硬币种数
            for j in range(c, amount + 1):  # 从小到大枚举金额，确保j-c >= 0.
                f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount] != (amount + 1) else -1  # 如果为inf说明状态不可达，返回-1即可。

        # 变体：硬币只能使用一次
        # f = [float('inf')] * (amount + 1)
        # f[0] = 0
        # for c in coins:  # 枚举硬币总数
        #     for j in range(amount, c - 1, -1):  # 从大到小枚举金额，确保j-c >= 0.
        #         f[j] = min(f[j], f[j - c] + 1)
        # return f[amount] if f[amount] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

        # 变体：每个硬币选择的次数有限制为 s
        # f = [float('inf')] * (amount + 1)
        # f[0] = 0
        # for i in range(len(coins)):
        #     for j in range(amount, coins[i] - 1, -1):
        #         for k in range(1, s[i] + 1):  # 枚举每个硬币的个数 [1, s[i]]
        #             if j >= k * coins[i]:  # 确保不超过金额 j
        #                 f[j] = min(f[j], f[j - k * coins[i]] + k)
        # print(f)
        # return -1 if f[amount] > amount else f[amount]




if __name__ == '__main__':
    ob = Solution()
    print(ob.coinChange([2], 3))
