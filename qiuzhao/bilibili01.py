# -*- coding: utf-8 -*-
import sys

def test(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = ""

    for length in range(n):

        for i in range(n):
            j = i + length
            if j >= n:
                break
            if length == 0:
                dp[i][j] = True
            elif length == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1]) and (s[i] == s[j])

            if dp[i][j] and length + 1 > len(res):
                res = s[i:j + 1]
    print(res)


if __name__ == '__main__':
    # s = 'yabccbau'
    s = sys.stdin.readline().strip()
    test(s)
