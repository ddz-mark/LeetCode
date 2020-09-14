# -*- coding: utf-8 -*-

import sys

def test(n):
    res = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                res.append(i)

                break
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    test(n)