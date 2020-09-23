# -*- coding: utf-8 -*-
# @Time : 2020/9/20 3:07 下午
# @Author : ddz

import sys


def test(line):
    # print(line)
    n = len(line)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if j - i > n - j:
                break
            if line[i:j] == line[j:j + (j - i)]:
                res += 1

    print(res)


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    test(line)
