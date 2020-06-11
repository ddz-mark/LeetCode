# -*- coding: utf-8 -*-
# @Time : 2020/6/7 3:25 下午
# @Author : ddz

import sys


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def test(res):
    res = sorted(res)

    if res != []:
        head = Node(res[0])  # 头节点
        cur = head
        # print(cur.val)
        for i in range(1, len(res)):
            node = Node(str(res[i]))
            cur.next = node
            cur = cur.next
            # print(cur.val)
    # print(res)
    print(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    # 当输入是单个整数时：
    #
    n = int(input())
    res = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        # 把每一行的数字分隔后转化成int列表
        res.extend(values)
    # res = [2, 4, 8, 3, 6, 9]
    test(res)
