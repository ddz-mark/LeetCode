# -*- coding: utf-8 -*-
# @Time : 2020/10/12 11:21 上午
# @Author : ddz

def backpack(n, v, goods):
    # a 代表大小
    # w 代表价值
    # n 代表物品数
    # v 代表背包体积

    # 思路：动态规划，dp[i][j]代表前 i 个物品，体积为 j，总价值最大
    # 转移方式：1. 不装第 i 个物品：dp[i][j] = dp[i - 1][j]
    #  2. 装入第 i 个物品：dp[i][j] = dp[i - 1][j - a[i - 1]] + w[i - 1]

    dp = [[0 for i in range(v + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, v + 1):
            dp[i][j] = dp[i - 1][j]  # 第i个物品不选
            if j >= goods[i - 1][0]:  # 判断背包容量是不是大于第i件物品的体积
                # 在选和不选的情况中选出最大值
                dp[i][j] = max(dp[i][j], dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1])

    print(dp[-1][-1])


if __name__ == '__main__':
    n = 4
    a = [2, 3, 5, 7] # 体积
    w = [1, 5, 2, 4] # 价值
    v = 10
    goods = [[2, 1], [3, 5], [5, 2], [7, 4]]
    backpack(n, v, goods)
