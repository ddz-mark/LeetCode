# -*- coding: utf-8 -*-
# @Time : 2020/9/12 1:49 下午
# @Author : ddz

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算买卖股票可获得的最大利润
# @param prices int整型一维数组 每天的股票价格
# @return int整型
#
class Solution:
    def maxProfit(self, prices):
        # 思路：dp
        if len(prices) < 2:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        # print(dp)

        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxProfit([1, 2, 3, 0, 2]))
