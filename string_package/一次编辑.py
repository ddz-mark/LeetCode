# -*- coding: utf-8 -*-
# @Time : 2020/7/15 11:09 下午
# @Author : ddz

"""字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
示例 1:
输入:
first = "pale"
second = "ple"
输出: True
示例 2:
输入:
first = "pales"
second = "pal"
输出: False
"""

# 思路：如果当前点不一致，则通过比对后一位之后


class Solution(object):

    def test(self, s1, s2):

        if abs(len(s1) - len(s2)) > 1:
            return False
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                continue
            else:
                return s1[i + 1:] == s2[i + 1:] or s1[i + 1:] == s2[i:] or s1[i:] == s2[i + 1:]
        return True


if __name__ == '__main__':
    ob = Solution()
    print(ob.test("pale", "ple1"))
