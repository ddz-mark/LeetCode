# -*- coding: utf-8 -*-
import sys


def test(m, values):
    dx = [0] * (m - 1)
    for i in range(0, m - 1):

        if values[i] == -1:
            dx[i] = None
        else:
            if values[i + 1] != -1:
                dx[i] = (values[i + 1] - values[i])
            else:
                dx[i] = (dx[i - 1])
    # print(dx)

    res = 1
    for i in range(0, len(dx) - 1):
        if dx[i] is None:
            continue
        else:

            if dx[i+1] is not None and dx[i] != dx[i + 1]:
                res += 1
    print(res)


if __name__ == '__main__':
    m = 0
    i = 0
    while True:
        if i % 2 == 0:
            # 读取每一行
            m = int(sys.stdin.readline().strip())
        else:
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split()))
            test(m, values)
        i += 1
    # m = 7
    # values = [-1, -1, -1, 4, 5, 1, 2]
    # test(m, values)
