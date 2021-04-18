# -*- coding: utf-8 -*-
# @Time : 2021/3/27 下午3:21
# @Author : ddz

# 01背包问题的衍生，下去把背包问题可以都看看，包括01背包、多重背包、完全背包
# 思路：一般的01背包是求解不超过容量x，并且最接近x的价值，这里是求解超过x并且超过的最小的价值。
# 只需要对它的对立面求01背包就行了。就是求背包容量为sum-x的01背包，最后sum-价值-优惠，就是答案，就是sum(goods) - dp[-1] - y

import sys


def test03(n, v, y, goods, sums):
    # 优化思路一：一维动态规划
    # 根据二维动态规划可以看出，f[i] 只与f[i-1]相关。
    # 因此状态转移方程为：dp[i] = max(dp[i] , dp[i-v[i]]+w[i])
    # 注意：这个必须要从后面遍历，不然状态 dp[i-v[i]] 就会改变，就不是dp[i-1][i-v[i]] 了
    dp = [0 for _ in range(v + 1)]
    # dp[j] 代表体积为 j 的情况下，总价值最大
    for i in range(n):
        for j in range(v, -1, -1):  # 从后往前
            if j >= goods[i]:
                dp[j] = max(dp[j], dp[j - goods[i]] + goods[i])

    print(sums - dp[-1] - y)


if __name__ == '__main__':
    v = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())
    goods = list(map(int, sys.stdin.readline().strip().split()))
    n = len(goods)
    sums = sum(goods)
    test03(n, sums - v, y, goods, sums)
