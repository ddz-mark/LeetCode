import sys
import math


def test(n, m, a, q):
    a = sorted(a)[:q]
    sum_n = 0
    for i in range(1, math.ceil(len(a) / m) + 1):
        if len(a) - m - m * (i - 1) < 0:
            sum_n += i * sum(a[:len(a) - m * (i - 1)])
        else:
            sum_n += i * sum(a[len(a) - m - m * (i - 1):len(a) - m * (i - 1)])
    print(sum_n)
    return sum_n


if __name__ == '__main__':
    # 多行输入
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    Q = int(input())

    res = ''
    for i in range(Q):
        res = res + str(test(n, m, a, int(input()))) + '\n'

    print(res)
    # for i in qes:
    #     test(n, m, a, i)
