# -*- coding: utf-8 -*-
# @Time : 2020/4/23 9:38 下午
# @Author : ddz

# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#
# 示例 1：
#
# 输入: n = 3
# 输出: 6
# 示例 2：
#
# 输入: n = 9
# 输出: 45

# 思路：短路运算符， A and B ，当 A 为 False，则 B 不会执行

class Solution(object):

    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """

        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    ob = Solution()
    print(ob.sumNums(3))
