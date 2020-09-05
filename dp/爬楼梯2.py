# -*- coding: utf-8 -*-
# @Time : 2020/9/4 10:05 下午
# @Author : ddz

# 爬楼梯：每次你可以爬 m 个台阶，且每次上的台阶不相同。你有多少种不同的方法可以爬到楼顶呢？且与前两次上的台阶数不相同

class Solution:
    def climbStairs(self, n, m):
        climb = [[1] * m for _ in range(n)]
        print(climb)
        # climb[0], climb[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(m):
                climb[i][j] = climb[i - 1][j] + climb[i - 2][j]

        return climb[n]


if __name__ == '__main__':
    solution = Solution()
    solution.climbStairs(10, 2)
