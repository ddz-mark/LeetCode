# -*- coding: utf-8 -*-
# @Time : 2020/5/29 8:42 下午
# @Author : ddz

# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # 思路一：递归
        # res = []
        # def helper(s, tmp):
        #     # 递归：结束条件
        #     if not s:
        #         res.append(tmp)
        #     for i in range(1, len(s) + 1):
        #         if s[:i] == s[:i][::-1]:
        #             tmp.append(s[:i])
        #             helper(s[i:], tmp)
        #             tmp.pop()
        #
        # helper(s, [])
        # return res

        # 思路二：动态规划+回溯，dp[i][j]代表i到j是否是回文串
        # 递推公式：dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])，确认是否为回文串
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        # 倒序：先处理末尾的子串，并逐步向左扩展处理更长的子串
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        ret = list()
        ans = list()

        # 回溯思路：先设置i从0到n遍历，再设置j对i从n进行遍历，保证每个子串都遍历一次
        # 如果是回文串，则添加到ans，然后递归j+1
        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret


if __name__ == '__main__':
    ob = Solution()
    print(ob.partition("aab"))
