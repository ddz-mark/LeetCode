# -*- coding: utf-8 -*-
# @Time : 2021/3/14 上午11:49
# @Author : ddz

import sys


def test03(arr):
    return arr.count(1)



if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    test03(arr)
