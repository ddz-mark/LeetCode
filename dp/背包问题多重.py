# -*- coding: utf-8 -*-
# @Time : 2020/9/17 11:16 下午
# @Author : ddz

# 多重 背包
# 有N件物品和一个容量为V的背包。
# 第i件物品的体积是vi，价值是wi，数量是si。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包流量，且总价值最大。

def backpack(n, v, goods):
    # 思路一：一维动态规划
    dp = [0 for i in range(v + 1)]

    for i in range(n):
        for j in range(v, -1, -1):
            # 考虑两种情况的最小值
            k = min(j // goods[i][0], goods[i][2])
            dp[j] = max([dp[j - x * goods[i][0]] + x * goods[i][1] for x in range(k + 1)])

    print(dp[-1])
