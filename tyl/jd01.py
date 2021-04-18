# -*- coding: utf-8 -*-
# @Time : 2021/3/27 下午7:43
# @Author : ddz

def test01(board):
    def dfs(i, j, rows, cols, board, blood, mask):

        # 递归：先写结束条件
        if 0 <= i < rows and 0 <= j < cols and blood > 0 and mask[i][j] == False:
            mask[i][j] = True
            print(i, j, board[i][j])
            if board[i][j] == '#':
                mask[i][j] = False
                return float('inf')
            elif board[i][j] == '*':
                blood -= 1
            elif board[i][j] == 'E':
                mask[i][j] = False
                return 0

            tmp_1 = dfs(i - 1, j, rows, cols, board, blood, mask)
            tmp_2 = dfs(i + 1, j, rows, cols, board, blood, mask)
            tmp_3 = dfs(i, j - 1, rows, cols, board, blood, mask)
            tmp_4 = dfs(i, j + 1, rows, cols, board, blood, mask)
            print("sss:", i, j, blood, tmp_1, tmp_2, tmp_3, tmp_4)
            mask[i][j] = False
            return 1 + min(tmp_1, tmp_2, tmp_3, tmp_4)
        else:
            return float('inf')

    rows = len(board)  # 行数
    cols = len(board[0])  # 列数
    mask = [[False] * cols for _ in range(rows)]
    # print(mask)
    i, j, n = 0, 2, 2

    return dfs(i, j, rows, cols, board, n, mask)


if __name__ == '__main__':
    board = [['.', '.', 'S'],
             ['*', '.', '.'],
             ['E', '#', '.'],
             ['.', '.', '.']]

    print(board[0][2])
    print(test01(board))
