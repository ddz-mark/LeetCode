# -*- coding: utf-8 -*-
# @Time : 2020/9/9 2:56 下午
# @Author : ddz

import sys

def test(n):
    count = 0
    while n:
        count += n // 5
        n = n // 5
    return count


if __name__ == '__main__':
    # n = 5
    n = int(sys.stdin.readline().strip())
    print(test(n))