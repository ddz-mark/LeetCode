# -*- coding: utf-8 -*-
# @Time : 2020/9/12 4:02 下午
# @Author : ddz

import sys


def test(matrix):
    # 匈牙利算法
    rows, cols = len(matrix), len(matrix[0])
    grils = [-1] * cols
    res = 0

    def dfs(i, mask):

        for j in range(cols):
            if matrix[i][j] == 1 and mask[i][j] == False:
                mask[i][j] = True

                if grils[j] == -1 or dfs(grils[j], mask):
                    grils[j] = i
                    return True
        return False

    for i in range(rows):
        mask = [[False] * cols for _ in range(rows)]
        if dfs(i, mask):
            res += 1
    print(res)


if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    boys_id = list(map(int, line.split()))

    line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    grils_id = list(map(int, line1.split()))

    n = int(sys.stdin.readline().strip())

    matrix = [[0] * len(grils_id) for _ in range(len(boys_id))]
    for _ in range(n):

        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        i, j = list(map(int, line.split()))

        matrix[boys_id.index(i)][grils_id.index(j)] = 1

    test(matrix)
# 0 1 2
# 3 4 5
# 6
# 0 4
# 0 3
# 1 3
# 1 4
# 2 5
# 2 4