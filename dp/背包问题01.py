# -*- coding: utf-8 -*-
# @Time : 2020/9/17 11:16 下午
# @Author : ddz

# 01 背包
# 描述：
# 有N件物品和一个容量为V的背包。
# 第i件物品的体积是vi，价值是wi。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包流量，且总价值最大。

def backpack01(n, v, goods):
    # 思路一：二维动态规划
    # f[i][j] 前 i 个物品，体积为 j 的情况下，总价值最大
    # 递推公式：
    # 1. 不选第 i 个物品 f[i][j] = f[i-1][j]
    # 2. 选第 i 个物品 f[i][j] = f[i-1][j-v[i]] + w[i]

    # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求
    # dp = [[0 for i in range(v + 1)] for j in range(n + 1)]
    #
    # for i in range(1, n + 1):
    #     for j in range(1, v + 1):
    #         dp[i][j] = dp[i - 1][j]  # 第i个物品不选
    #         if j >= goods[i - 1][0]:  # 判断背包容量是不是大于第i件物品的体积
    #             # 在选和不选的情况中选出最大值
    #             dp[i][j] = max(dp[i][j], dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1])
    #
    # print(dp[-1][-1])

    # 优化思路一：一维动态规划
    # 根据二维动态规划可以看出，f[i] 只与f[i-1]相关。
    # 因此状态转移方程为：dp[i] = max(dp[i] , dp[i-v[i]]+w[i])
    # 注意：这个必须要从后面遍历，不然状态 dp[i-v[i]] 就会改变，就不是dp[i-1][i-v[i]] 了
    dp = [0 for i in range(v + 1)]

    # dp[j] 代表体积为 j 的情况下，总价值最大
    for i in range(n):
        for j in range(v, -1, -1):  # 从后往前
            if j >= goods[i][0]:
                dp[j] = max(dp[j], dp[j - goods[i][0]] + goods[i][1])

    print(dp[-1])


