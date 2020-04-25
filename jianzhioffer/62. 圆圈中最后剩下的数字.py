# -*- coding: utf-8 -*-
# @Time : 2020/4/22 10:52 下午
# @Author : ddz

# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
#
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
#
# 示例 1：
#
# 输入: n = 5, m = 3
# 输出: 3
# 示例 2：
#
# 输入: n = 10, m = 17
# 输出: 2


class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        if n < 1 or m < 1:
            return -1
        index = 0
        for i in range(2, n+1):
            index = (index + m) % i

            print(index)
        return index

if __name__ == '__main__':
    ob = Solution()
    print(ob.lastRemaining(5,3))


