# -*- coding: utf-8 -*-
# @Time : 2020/9/11 8:54 上午
# @Author : ddz

import sys


def test(s):
    qinxu_list = ['63231323', '53231323', '43231323']

    res = 0
    for v in qinxu_list:
        res += s.count(v)

    print(res)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        test(line)

    # s = '165432313236432313236'
    # s = '632313225323'
    # s = '666653231323'
    # test(s)
