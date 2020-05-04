# -*- coding: utf-8 -*-
# @Time : 2020/4/28 3:26 下午
# @Author : ddz

# coding=utf-8
import sys
# str = input()
# print(str)
# print('Hello,World!')
import math


def test(L, R):
    t = L * math.radians(180) / (R * math.pi)
    x1 = math.cos(math.radians(t))
    y1 = math.sin(math.radians(t))

    print(x1, y1, x1, -y1)


if __name__ == '__main__':
    test(1, 2)
