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

        res = []

        def helper(s, tmp):
            # 递归：结束条件
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.partition("aab"))
