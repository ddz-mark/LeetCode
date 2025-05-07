# -*- coding: utf-8 -*-
# @Time : 2025/5/7 17:15
# @Author : ddz

# 给定两个字符串text1和text2，返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列 ，返回0 。
#
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace"是"abcde"的子序列，但"aec"不是"abcde"的子序列。两个字符串的公共子序列是这两个字符串所共同拥有的子序列。
#
# 示例1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是"ace" ，它的长度为3 。
#
# 示例2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是"abc" ，它的长度为3 。
#
# 示例3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回0 。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # 思路：dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列的长度。
        # 递推公式：dp[i][j] = dp[i-1][j-1] + 1，当text1[i-1]==text2[j-1]的时候
        #         dp[i][j] = max(dp[i-1][j], dp[i][j-1])，当text1[i-1]!=text[j-1]时，取两项中最大值
        # 边界：i=0时,dp[0][j]=0，j=0时，dp[i][0]=0，第一位无公共子序列
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestCommonSubsequence("abcde", "ace"))
