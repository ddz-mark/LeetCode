# -*- coding: utf-8 -*-
# @Time : 2020/9/16 7:01 下午
# @Author : ddz

import sys

def test(n, values):
    print(n, values)



if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    test(n, values)