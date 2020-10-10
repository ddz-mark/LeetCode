# -*- coding: utf-8 -*-
# @Time : 2020/10/10 8:53 下午
# @Author : ddz

# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 思路：
        # dp[i]：代表 s 中第 i 个字符结尾的字符串，能不能拆分
        # 转移状态：dp[j] = dp[i] and (s[i:j] in  wordDict)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            for j in range(i + 1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.wordBreak("leetcode", ["leet", "code"]))
