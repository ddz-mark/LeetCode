# -*- coding: utf-8 -*-
# @Time : 2021/3/13 下午4:03
# @Author : ddz

import sys

def test01(matrix):
    row, col = len(matrix), len(matrix[0])

    if row != col:
        for v in [[row[i] for row in matrix] for i in range(len(matrix[0]))]:
            print(' '.join(map(str,v)))
    else:
        '''矩阵转置'''
        for x in range(row):
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        for l in matrix:
            print(' '.join(map(str, l)))


if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))
    matrix = []
    for i in range(n):
        # 读取每一行
        line1 = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line1.split()))

        matrix.append(values)
    test01(matrix)
