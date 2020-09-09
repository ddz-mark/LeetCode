# -*- coding: utf-8 -*-
# @Time : 2020/9/7 2:59 下午
# @Author : ddz
import sys

# 1
# 6
# 3 6 9 66 66 99
# 2
# 1 1 1
# 10 4 2

t = int(sys.stdin.readline().strip())


def bi(arr, l, r, x):
    if l <= r:
        mid = int(l + (r - l) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bi(arr, l, mid - 1, x)
        else:
            return bi(arr, mid + 1, r, x)
    else:
        return r


for _ in range(t):
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    w = list(map(int, line.split()))
    d = {}
    l = []
    for i, wi in enumerate(w):
        l.append(wi)
        if wi in d:
            continue
        d[wi] = i
    l = sorted(l)

    q = int(sys.stdin.readline().strip())
    for _ in range(q):

        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        xyz = list(map(int, line.split()))

        # xyz = list(map(int, input().split()))
        money = xyz[0] * xyz[1] * xyz[2]
        length = len(l)

        p = bi(l, 0, length - 1, money)
        if p == -1:
            print(-1)
        else:
            print(d[l[p]]+1, l[p])
    # 二分法
