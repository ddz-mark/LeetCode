# -*- coding: utf-8 -*-
# @Time : 2020/4/23 10:04 下午
# @Author : ddz

# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
#
# 示例:
#
# 输入: a = 1, b = 1
# 输出: 2


class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    ob = Solution()
    print(ob.add(1,2))
