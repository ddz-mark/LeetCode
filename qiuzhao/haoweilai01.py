# -*- coding: utf-8 -*-
# @Time : 2020/9/12 1:29 下午
# @Author : ddz

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 是否为回文数
# @param num int整型
# @return bool布尔型
#
class Solution:
    def isPalindrome(self , num ):
        # write code here

        if num < 0:
            return False

        temp = 0
        while num > temp:
            temp = temp * 10 + num % 10
            num = num // 10

        return temp == num or temp // 10 == num


if __name__ == '__main__':
    ob = Solution()
    print(ob.isPalindrome(12321))