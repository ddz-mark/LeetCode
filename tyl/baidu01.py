# -*- coding: utf-8 -*-

# TODO:记得理解思路代码，思路链接：https://blog.csdn.net/qq_32711799/article/details/111712996

import sys


def test01(matrix):
    # 判空条件
    if matrix == [] or matrix[0] == []:
        return 0

    m, n = len(matrix), len(matrix[0])  # 行 # 列
    res = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
            res = max(res, matrix[i][j])
    return res * res


if __name__ == '__main__':

    # 把每一行的数字分隔后转化成int列表
    m, n = list(map(int, sys.stdin.readline().strip().split()))
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        line = sys.stdin.readline().strip()
        for j, v in enumerate(list(line)):
            if v == 'M':
                matrix[i][j] = 1
    print(test01(matrix))

# matrix = [[1, 1, 1, 1],
#           [1, 1, 0, 0],
#           [0, 1, 1, 1],
#           [1, 1, 1, 1],
#           [1, 0, 1, 1]]
# 5 4
# MMMM
# MMFF
# FMMM
# MMMM
# MFMM
