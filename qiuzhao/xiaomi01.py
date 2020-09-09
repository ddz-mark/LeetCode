# -*- coding: utf-8 -*-
# @Time : 2020/9/8 5:59 下午
# @Author : ddz
import sys


def test(A, B):
    if len(A[0]) == len(B):
        C = [[0] * len(B[0]) for _ in range(len(A))]

        # 普通算法
        # for i in range(len(A)):
        #     for j in range(len(B[0])):
        #         for k in range(len(B)):
        #             C[i][j] += (A[i][k] * B[k][j])

        # 优化算法
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    for j in range(len(B[0])):
                        C[i][j] += (A[i][k] * B[k][j])
        for rows in C:
            print(" ".join(map(str, rows)))

    # for a in A:
    #     print(" ".join(map(str, [sum(a * b for a, b in zip(a, b)) for b in zip(*B)])))
    # C = [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
    # print(C)
    # for rows in C:
    #     print(" ".join(map(str, rows)))


if __name__ == '__main__':
    A = [[1, 2, 3], [1, 2, 3]]
    B = [[1, 1], [1, 1], [1, 1]]

    # line = sys.stdin.readline().strip()
    # M, K, N = list(map(int, line.split()))
    # A = []
    # B = []
    # for _ in range(M):
    #     line1 = sys.stdin.readline().strip()
    #     temp = list(map(int, line1.split()))
    #     A.append(temp)
    #
    # for _ in range(K):
    #     line2 = sys.stdin.readline().strip()
    #     temp = list(map(int, line2.split()))
    #     B.append(temp)

    test(A, B)
