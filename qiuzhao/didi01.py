# -*- coding: utf-8 -*-
# @Time : 2020/9/13 7:41 下午
# @Author : ddz

import sys


def test(n, list1):
    # print(list1)
    if list1 == []:
        print('No')
        return
    res = set(list1[0])
    # print(res)
    flag = True
    for i in range(1, len(list1)):
        # for j in range(0, len(list1)):
        if len(res) != n and res.intersection(set(list1[i])):
            res = res.union(set(list1[i]))

        if len(res) == n:
            print('Yes')
            flag = False
            return

    for i in range(1, len(list1)):
        # for j in range(0, len(list1)):
        if len(res) != n and res.intersection(set(list1[i])):
            res = res.union(set(list1[i]))

        if len(res) == n:
            print('Yes')
            flag = False
            return

    for i in range(1, len(list1)):
        # for j in range(0, len(list1)):
        if len(res) != n and res.intersection(set(list1[i])):
            res = res.union(set(list1[i]))

        if len(res) == n:
            print('Yes')
            flag = False
            break


    if flag:
        print('No')

if __name__ == '__main__':
    # # 多行输入
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        line = sys.stdin.readline().strip()
        n, m, k = list(map(int, line.split()))

        list1 = []
        for _ in range(m):
            line1 = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            a1, a2, cost = list(map(int, line1.split()))
            if cost <= k:
                list1.append([a1, a2])

        test(n, list1)

# 2
# 3 3 400
# 1 2 200
# 1 3 300
# 2 3 500
# 3 3 400
# 1 2 500
# 1 3 600
# 2 3 700
