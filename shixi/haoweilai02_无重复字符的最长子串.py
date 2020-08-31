# -*- coding: utf-8 -*-
# @Time : 2020/5/13 7:51 下午
# @Author : ddz

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def engthOfLongestSubstr(s):
    if len(s) < 2:
        return len(s)

    head = tail = 0
    res = 1
    while tail < len(s) - 1:
        tail += 1
        if s[tail] not in s[head:tail]:
            res = max(res, tail - head + 1)
        else:
            while s[tail] in s[head:tail]:
                head += 1
    return res


# ******************************结束写代码******************************

if __name__ == '__main__':

    try:
        _s = input()
    except:
        _s = None

    res = engthOfLongestSubstr(_s)

    print(str(res) + "\n")