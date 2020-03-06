# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 解题思路：
# 只需要关注后一天比前一天多就行了。


class Solution:
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += (prices[i + 1] - prices[i])
            i += 1

        return profit
