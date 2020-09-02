# -*- coding: utf-8 -*-
import sys


def climb(n):

    if n > 0 and n <= 36:
        climb = dict()
        climb[0], climb[1] = 1, 1
        for i in range(2, n + 1):
            climb[i] = climb[i - 1] + climb[i - 2]
            # print(climb[i], i)

        return climb[n]
    else:
        return 0


if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    if n.isdigit():
        print(str(climb(int(n))))
    else:
        print('0')
    # print(str(climb(n)))
