# -*- coding: utf-8 -*-
# @Time : 2021/3/27 下午3:54
# @Author : ddz


def test02(s1, s2):
    n = len(s1)
    m = len(s2)

    # 有一个字符串为空串
    if n * m == 0:
        return n + m

    # DP 数组
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 边界状态初始化
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # 计算所有 DP 值
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = dp[i - 1][j] + 1
            down = dp[i][j - 1] + 1
            left_down = dp[i - 1][j - 1]
            if s1[i - 1] != s2[j - 1]:
                left_down += 1
            dp[i][j] = min(left, down, left_down)

    return dp[n][m]


if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'axc'
    print(test02(s1, s2))
    print('%.2f' % ((len(s1) + len(s2) - test02(s1, s2)) / (len(s1) + len(s2))))
