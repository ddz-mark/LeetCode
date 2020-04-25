# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
#
# 示例:
#
# s = "abaccdeff"
# 返回 "b"
#
# s = ""
# 返回 " "

import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 思路一：
        dic = collections.Counter(s)
        for i, v in dic.items():
            if v == 1:
                return i
        return " "


if __name__ == '__main__':
    ob = Solution()
    print(ob.firstUniqChar("leetcode"))
