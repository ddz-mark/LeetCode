# -*- coding: utf-8 -*-
# @Time : 2020/4/22 1:53 下午
# @Author : ddz

# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#
# 示例 1:
#
# 输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
# 示例 2:
#
# 输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """

        if n < 1:
            return
        total = 6 ** n
        dp = [[0 for i in range(6 * n + 1)] for j in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(2, 6 * n + 1):
                sum = 0

                for m in range(1, j):
                    if m <= 6:
                        sum += dp[i - 1][j - m]
                dp[i][j] = sum

        res = []
        for k in range(n, 6 * n + 1):
            res.append(float(dp[n][k] / total))
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.twoSum(1))
