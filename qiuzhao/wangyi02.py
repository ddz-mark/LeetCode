# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:52 下午
# @Author : ddz

import sys


def test(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n + 1):
            if j - i > 1 and s[i:j] == s[i:j][::-1]:
                # print(s[i:j], s[i:j][::-1])
                res += 1
    print(res)


if __name__ == '__main__':
    # s = 'abbcbb'

    s = sys.stdin.readline().strip()
    test(s)
