# -*- coding: utf-8 -*-
# @Time : 2020/5/13 7:11 下午
# @Author : ddz

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

# 使用递归完成

def isReserveSame(s, left, right):
    # s = "xueersiisreeux"
    # 1. 思路一
    # return 1 if s[::-1] == s else 0

    # 2. 思路二：
    # 递归的结束条件
    if left >= right:
        return 1

    if s[left] != s[right]:
        return 0

    return isReserveSame(s, left + 1, right - 1)


# ******************************结束写代码******************************

if __name__ == '__main__':
    s = input()
    print(isReserveSame(s, 0, len(s)-1))
