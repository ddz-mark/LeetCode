# -*- coding: utf-8 -*-
# @Time : 2025/5/11 21:49
# @Author : ddz

# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 解法：多维动态规划
        # 定义dp[i][j]：代表把 word1[0:i] 转化为 word2[0:j] 需要的最少操作数
        # 递推公式为：dp[i][j] = dp[i-1][j-1] 当word1[i-1]==word2[j-1]时
        # 当word1[i-1]!=word2[j-1]时: dp[i][j] = mim(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，分别代表替换、删除、增加
        # 边界：i=0时dp[0][j]=j，j=0时dp[i][0]=i

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # 边界
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        print(dp)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    print(obj.minDistance(word1="horse", word2="ros"))
