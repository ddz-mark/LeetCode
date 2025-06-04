# -*- coding: utf-8 -*-
# @Time : 2025/5/19 16:57
# @Author : ddz

# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
# 示例 1：
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 思路：dp[i][j]代表字符串i到j 是回文序列的长度
        # 递推公式：dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j]，相等的话，长度+2
        #         dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])，不相等的话，判断最大值
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # 倒序：先处理末尾的子串，并逐步向左扩展处理更长的子串
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
