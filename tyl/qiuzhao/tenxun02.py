# -*- coding: utf-8 -*-
# @Time : 2021/9/5 下午9:46
# @Author : ddz

import sys


def test02(k, b):
    print(k, b)



if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    k, b = list(map(int, line.split()))
    test02(k, b)
