# -*- coding: utf-8 -*-
# @Time : 2025/5/30 16:12
# @Author : ddz

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 思路一：f[i][j]代表从(0,0)到(i,j)的路径数，则f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        # f = [[0] * (n + 1) for _ in range(m + 1)]
        # f[0][1] = 1
        # for i in range(m):
        #     for j in range(n):
        #         f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        # return f[m][n]

        # 思路二：思路一的空间优化
        # 举个例子，在计算 f[1][1] 时，会用到 f[0][1]，但是之后就不再用到了。
        # 那么干脆把 f[1][1] 记到 f[0][1] 中，这样对于 f[1][2] 来说，
        # 它需要的数据就在 f[0][1] 和 f[0][2] 中。f[1][2] 算完后也可以同样记到 f[0][2] 中。
        f = [0] * (n + 1)
        f[1] = 1
        for _ in range(m):
            for j in range(n):
                f[j + 1] += f[j]
        return f[n]


if __name__ == '__main__':
    obj = Solution()
    obj.uniquePaths(3, 7)
