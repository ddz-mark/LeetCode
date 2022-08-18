# -*- coding: utf-8 -*-
# @Time : 2021/9/5 下午8:37
# @Author : ddz

import sys


def judge(n, m, i, j, mask, matrix, label):
    if 0 <= i < n and 0 <= j < m and mask[i][j] == False and matrix[i][j] != label:
        mask[i][j] = True
        return 1 + judge(n, m, i - 2, j - 1, mask, matrix, matrix[i][j]) + \
               judge(n, m, i - 2, j + 1, mask, matrix, matrix[i][j]) + \
               judge(n, m, i - 1, j - 2, mask, matrix, matrix[i][j]) + \
               judge(n, m, i + 1, j - 2, mask, matrix, matrix[i][j]) + \
               judge(n, m, i + 2, j - 1, mask, matrix, matrix[i][j]) + \
               judge(n, m, i + 2, j + 1, mask, matrix, matrix[i][j]) + \
               judge(n, m, i - 1, j + 2, mask, matrix, matrix[i][j]) + \
               judge(n, m, i + 1, j + 2, mask, matrix, matrix[i][j])
    else:
        return 0


def movingCount(n, m, matrix, x, y):
    mask = [[False] * m for _ in range(n)]
    init_label = 'b' if matrix[x][y] == 'r' else 'r'
    res = judge(n, m, x, y, mask, matrix, init_label)
    print(res)


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, m = list(map(int, line1.split()))

    matrix = []
    for _ in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = [v for v in line]
        matrix.append(values)

    line3 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    x, y = list(map(int, line3.split()))

    movingCount(n, m, matrix, x, y)
# 3 3
# bbb
# bbb
# rbr
# 1 2
