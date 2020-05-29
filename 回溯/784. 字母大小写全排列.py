# -*- coding: utf-8 -*-
# @Time : 2020/5/27 10:52 下午
# @Author : ddz

# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
import itertools


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        # 思路一：递归，单个字母往后加入，每个新字母都是在结果数组的复制下，再加入大小写
        res = [[]]
        for c in S:
            n = len(res)  # 结果长度
            if c.isalpha():  # 是英文单词
                # 对结果进行复制，然后依次加入大小写
                for i in range(n):
                    res.append(res[i][:])  # 复制原值
                    res[i].append(c.lower())  # 加入小写
                    res[n+i].append(c.upper())  # 加入大写
            else:
                for i in range(n):
                    res[i].append(c)

        return list(map("".join, res))


        # 思路二：内置函数

        # f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        # return list(map("".join, itertools.product(*map(f, S))))


if __name__ == '__main__':
    ob = Solution()
    print((ob.letterCasePermutation('abc')))








