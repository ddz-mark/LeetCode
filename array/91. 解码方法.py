# -*- coding: utf-8 -*-
# @Time : 2020/5/3 1:48 下午
# @Author : ddz

# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        # 特判
        if size == 0:
            return 0
        dp = [0] * (size + 1)
        dp[0] = 1
        for i in range(1, size + 1):
            print(i)
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]  # 最后一个数字解密成一个字母
            if i >= 2:  # 下面这种情况至少要有两个字符
                if '10' <= s[i - 2:i] <= '26':
                    dp[i] += dp[i - 2]  # 最后两个数字解密成一个一个字母
        return dp[-1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.numDecodings("110"))
