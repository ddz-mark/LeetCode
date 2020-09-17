# -*- coding: utf-8 -*-
# @Time : 2020/9/17 7:43 下午
# @Author : ddz
import sys


def test(rows, cols, matrix):

    def dfs(i, j, mask):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == '#' or mask[i][j] == True:
            return False
        if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 'E' and mask[i][j] == False:
            return True
        mask[i][j] = True
        # 检查上下左右是否存在路径
        if (dfs(i - 1, j, mask) or dfs(i + 1, j, mask) or dfs(i, j - 1, mask) or dfs(i, j + 1, mask)):
            return True
        return False
    mask = [[False] * cols for _ in range(rows)]
    i, j = 0, 0
    while i < rows:
        if 'S' in matrix[i]:
            j = matrix[i].index('S')
            break
        i += 1
    if dfs(i, j, mask):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        rows, cols = list(map(int, line.split()))
        matrix = []
        for _ in range(rows):
            line1 = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            matrix.append(list(line1))

        test(rows, cols, matrix)
