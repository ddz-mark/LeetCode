# -*- coding: utf-8 -*-
# @Time : 2020/5/29 9:03 下午
# @Author : ddz

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：用 dp[i][j] 字符串从位置 i 到位置 j(闭区间)是否为回文子串.
        # 动态规划状态转移方程：P（i,j）=P(i+1,j-1) ^ (Si == Sj)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""

        # 外循环：遍历子串长度
        for length in range(n):
            # 内循环：
            for i in range(n):
                j = i + length  # 子串结束点
                if j >= n:
                    break
                # 长度为 0 时，都是回文子串
                if length == 0:
                    dp[i][j] = True
                # 长度为 1 时，判断是否相等
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                # 长度大于 1 时，使用转移方程
                else:
                    dp[i][j] = (dp[i + 1][j - 1]) and (s[i] == s[j])

                # 如果长度超过当前最大，则更新
                if dp[i][j] and length + 1 > len(res):
                    res = s[i:j + 1]
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.longestPalindrome("babad"))
