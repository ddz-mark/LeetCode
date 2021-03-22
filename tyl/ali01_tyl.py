# -*- coding: utf-8 -*-
# @Time : 2021/3/12 下午6:46
# @Author : ddz

import collections
import sys
def test(connections, x, y):

    edges = collections.defaultdict(list)
    for i, j in connections:
        edges[i].append(j)
        # edges[j].append(i)


    def dfs(x, y, res):
        # 递归：先写结束条件
        if x == y:
            return res

        if x not in edges.keys():
            return -1

        for v in edges[x]:
            res += 1
            return dfs(v, y, res)

    print(dfs(x, y, 0))


if __name__ == '__main__':
    # 读取每一行
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))
    connections = []
    for i in range(1, m+1):
        line1 = sys.stdin.readline().strip()
        connections.append(list(map(int, line1.split())))

    q = int(sys.stdin.readline().strip())
    for i in range(q):
        line2 = sys.stdin.readline().strip()
        x, y = list(map(int, line2.split()))
        test(connections, x, y)

