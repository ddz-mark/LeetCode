# -*- coding: utf-8 -*-
# @Time : 2020/9/2 11:41 下午
# @Author : ddz
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 思路：状态转移题型

class Solution:
    def maxProfit(self, prices):

        # 思路：隐藏状态影响
        # f[i][0]:持有一支股票，对应的累计最大收益
        # f[i][1]：不持有，处于冷冻期，累计最大
        # f[i][2]：不持有，不处于冷冻期，累计最大

        n = len(prices)
        if n < 2:
            return 0
        f = [[0] * 3 for _ in range(n)]
        f[0][0] = -prices[0]
        print(f)

        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[-1][1], f[-1][2])


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxProfit([1, 2]))
