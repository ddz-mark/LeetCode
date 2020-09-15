# -*- coding: utf-8 -*-
# @Time : 2020/9/15 7:05 下午
# @Author : ddz

import sys


def test(n, k, s):
    flag = '1'
    cnt = 1
    for i, c in enumerate(s):

        if c == flag:
            continue
        else:
            cnt += 1
            if flag == '0':
                flag = '1'
            else:
                flag = '0'



if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, k = list(map(int, line.split()))

    s = list(sys.stdin.readline().strip())
    test(n, k, s)
