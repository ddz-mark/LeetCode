# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import sys


def test(l):

    if l == [] or len(l) == 1:
        return 0
    count = 0
    while True:
        length = len(l)
        for i in range(len(l) - 1, 0, -1):
            if l[i - 1] > l[i]:
                l.pop(i)
        print(l)
        if length == len(l):
            break
        count += 1

    print(count)


if __name__ == '__main__':
    # n = int(sys.stdin.readline().strip())
    # # # 把每一行的数字分隔后转化成int列表
    # line = sys.stdin.readline().strip()
    # # 把每一行的数字分隔后转化成int列表
    # values = list(map(int, line.split()))
    # n = 6
    values = [4, 3, 2, 3, 2, 1, 7]
    # n = 3
    # values = [1, 2, 3]
    test(values)
