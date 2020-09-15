# -*- coding: utf-8 -*-
# @Time : 2020/9/14 8:43 下午
# @Author : ddz
import sys


def test(m_list, cost, t1, t2, t3):

    shengyu = sum(m_list) % cost
    print(shengyu)

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    x, y, z = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    t1, t2, t3 = list(map(int, line2.split()))

    m = int(sys.stdin.readline().strip())

    line3 = sys.stdin.readline().strip()
    m_list = list(map(int, line3.split()))

    cost = x * t1 + y * t2 + z * t3
    # print(sum(m_list) // cost)
    test(m_list, cost, t1, t2, t3)
