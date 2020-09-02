# -*- coding: utf-8 -*-

import sys


def test(n):
    matrixs = [["0"] * n for _ in range(n)]
    print(matrixs)
    for i in range(n):
        for j in range(n):
            if n % 2 != 0:
                if i == (n-1) // 2 or j == (n-1) // 2:
                    continue

            if i == j or i == n - j - 1:
                continue
            if i < n // 2 and j >= n // 2:
                if j / (n - 1 - i) > 1:
                    matrixs[i][j] = "8"
                    print('8-', i, j)
                else:
                    print('1-', i, j)
                    matrixs[i][j] = "1"
            elif i < n // 2 and j < n // 2:
                if (n - 1 - j) / (n - 1 - i) < 1:
                    print('2-', i, j, (n - 1 - j) / (n - 1 - i))
                    matrixs[i][j] = "2"
                else:
                    print('3-', i, j, (n - 1 - j) / (n - 1 - i))
                    matrixs[i][j] = "3"
            elif i >= n // 2 and j < n // 2:
                if (n - 1 - i) != 0 and j / (n - 1 - i) < 1:
                    print('4-', i, j, j / (n - 1 - i))
                    matrixs[i][j] = "4"
                else:
                    print('5-', i, j)
                    matrixs[i][j] = "5"
            elif i >= n // 2 and j >= n // 2:  # 4
                if (n - 1 - i) != 0 and (n - 1 - j) / (n - 1 - i) < 1:
                    print('7-', i, j)
                    matrixs[i][j] = "7"
                else:
                    print('6-', i, j)
                    matrixs[i][j] = "6"

    for i in range(n):
        print(" ".join(matrixs[i]))


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    test(n)
