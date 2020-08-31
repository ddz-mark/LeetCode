# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:59 下午
# @Author : ddz

import sys


def test(m, n):
    print((n - 1) * pow(m, n - 1) - m)


if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    test(m, n)

    # test(2, 3)
