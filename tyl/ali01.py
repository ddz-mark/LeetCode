# -*- coding: utf-8 -*-
# @Time : 2020/11/25 10:51 上午
# @Author : ddz

# /*
# 问题：
# 给定一个输入字符串，按word进行翻转
# 比如：
# 输入： "the sky is blue"
# 输出:  "blue is sky the"
#
# 说明：
# 1. word子串内部没有空格
# 2. 输入字符串头部和尾部可能包含空格，翻转后输出结果头尾不能包含空格
# 3. 如果word之间包含多个空格，翻转后需变成一个空格
# 4. 请使用O(1)空间复杂度实现
# */

import sys


def test01(line):
    # 思路：对于情况2，结尾开头不包含空格，使用strip()去掉
    # return ' '.join(line.split()[::-1])

    line = line[::-1] + ' '
    n = len(line)
    j = 0
    line_new = ''
    for i in range(n):
        # 判断多种空格情况
        while line[j] == ' ':
            j = j + 1

        # 进行切分
        if line[i] == ' ':
            line_new += line[j:i + 1][::-1]
            j = i + 1

    return line_new.strip()


def asplit(s, scut):
    s = s + (scut)
    N = len(s)
    point1 = 0
    res = []
    for i in range(N):
        if s[i] == scut:
            res.append(s[point1:i])
            point1 = i + 1
    return res


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    print(test01(line))
    # print(asplit(line, ' '))
