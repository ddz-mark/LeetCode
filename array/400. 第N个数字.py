# -*- coding: utf-8 -*-
# @Time : 2020/4/27 11:02 上午
# @Author : ddz

# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32位整数范围内 ( n < 231)。
#
# 示例 1:
# 输入:
# 3
# 输出:
# 3

# 思路：1-9 占 9x1 位，10-99 占 90 x2 位，100-999 占 900 x 3 位

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        digit = 1
        base = 1
        while n > 9 * digit * base:
            n = n - 9 * digit * base
            digit += 1
            base *= 10

        current_num = (n-1) // digit + base
        index = (n-1) % digit

        return str(current_num)[index]


if __name__ == '__main__':
    ob = Solution()
    print(ob.findNthDigit(11))
