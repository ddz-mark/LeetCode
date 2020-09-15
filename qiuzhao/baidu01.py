# -*- coding: utf-8 -*-
# @Time : 2020/9/14 8:11 下午
# @Author : ddz

import sys

def solve(board):

    rows = len(board)
    if rows == 0:
        return []
    cols = len(board[0])

    def dfs(i, j, rows, cols, board):
        board[i][j] = '2'
        # 递归：先写结束条件
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and board[x][y] == '0':
                dfs(x, y, rows, cols, board)

    for j in range(cols):
        # 第一行
        if board[0][j] == '0':
            dfs(0, j, rows, cols, board)
        # 最后一行
        if board[rows - 1][j] == '0':
            dfs(rows - 1, j, rows, cols, board)

    for i in range(rows):
        # 第一列
        if board[i][0] == '0':
            dfs(i, 0, rows, cols, board)
        # 最后一列
        if board[i][cols - 1] == '0':
            dfs(i, cols - 1, rows, cols, board)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '0':
                board[i][j] = '1'
            elif board[i][j] == '2':
                board[i][j] = '0'
    for v in board:
        print("".join(v))


if __name__ == '__main__':
    # n = 4
    # board = [['1', '1', '1', '1'], ['0', '1', '0', '1'], ['1', '1', '0', '1'], ['0', '0', '1', '0']]

    # # 多行输入
    n = int(sys.stdin.readline().strip())
    board = []
    for _ in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        if line != "":
            board.append(list(line))

    # print(ans)
    solve(board)
# 4
# 1111
# 0101
# 1101
# 0010