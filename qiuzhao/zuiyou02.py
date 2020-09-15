# -*- coding: utf-8 -*-
import sys


def test(s):
    n = len(s)
    res = []

    def dfs(x):
        # 递归：先写结束条件
        if x == n - 1:
            res.append("".join(s[:]))
            return

        for i in range(x, n):
            if s[i] in s[x:i]:
                continue

            s[i], s[x] = s[x], s[i]
            dfs(x + 1)
            s[i], s[x] = s[x], s[i]

    dfs(0)
    # print(" ".join(res))
    print(" ".join(sorted(res, reverse=False)))


if __name__ == '__main__':
    s = list(sys.stdin.readline().strip())
    test(s)
