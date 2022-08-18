# -*- coding: utf-8 -*-
# @Time : 2021/8/29 上午10:49
# @Author : ddz


import sys


def test03(s, a):
    front = 0
    flag = 0
    for i, v in enumerate(a):
        if v not in s:
            print(-1)
            return

        index = s.index(v)
        if index > flag:
            front += (index - flag)
        else:
            front += (index + len(s) - flag)
        flag = index

    print(front - len(a) + 1)


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    a = sys.stdin.readline().strip()
    test03(s, a)
